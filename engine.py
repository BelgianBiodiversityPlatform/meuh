from dwca import DwCAReader


class MeuhEngine(object):
    # Preferably, use 'with' to ensure proper cleanup at the end
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.cleanup()

    def __init__(self, config, dwca):
        """Initialize Meuh engine for a given config object and DwC-A

        config: object
        dwca: open file
        """
        
        self.dwca = DwCAReader(dwca)

        # Parse config
        self.assessments = AssessmentList(config['assessments'], self.dwca)

    def run(self, log_stream):
        """Executes all the tests on the target DwC-A, according to the configuration.

        Progress is logged on log_stream so the user isn't left in the dark in case it's long.
        """
        log_stream.write('Engine running...\n')

        log_stream.write('Applicable assessments:\n')

        log_stream.write("Applicable: {ass}\n".format(ass=self.assessments.applicable))
        log_stream.write("Non-applicable: {ass}\n".format(ass=self.assessments.non_applicable))

        log_stream.write('1. Testing metadata\n')
        # TODO: Implement

        log_stream.write('2. Testing each line of archive')
        lines_assessments = self.assessments.applicable_for_each_line
        log_stream.write("The following assessments will be executed for each line: {ass}\n".format(ass=lines_assessments))

        for line in self.dwca.each_line():
            log_stream.write('.')
            for a in lines_assessments:
                a.assess_line(line)


        log_stream.write('Engine finished execution.\n')

    def cleanup(self):
        self.dwca.close()

#TODO: Test that the engine properly calls and reacts to applicable_to_archive


class AssessmentList(object):
    def __init__(self, asked_assessments, dwca):
        self.asked = asked_assessments
        self.applicable = [a for a in self.asked if a.applicable_to_archive(dwca)]

    @property
    def applicable_for_each_line(self):
        return [a for a in self.applicable if a.assess_each_line]

    @property
    def non_applicable(self):
        """Returns a lsit of assessments that have delcared themselves unable to operate on this archive.

        self.asked_assessments and self.applicable_assessments should be set prior to call me.
        """
        return [a for a in self.asked if a not in self.applicable]


