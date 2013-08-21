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
        self.asked_assessments = config['assessments']
        self.applicable_assessments = []  # Will be filled at the beginning of execution

    def _select_applicable_tests(self, asked_assessments, dwca):
        """Returns a subset of asked_assessments that are applicable to the archive.

        Each entry in asked_assessment will log info in its own logger.
        """
        return [a for a in asked_assessments if a.applicable_to_archive(dwca)]

    def run(self, log_stream):
        """Executes all the tests on the target DwC-A, according to the configuration.

        Progress is logged on log_stream so the user isn't left in the dark in case it's long.
        """
        log_stream.write('Engine running...\n')
        self.applicable_assessments = self._select_applicable_tests(self.asked_assessments, self.dwca)
        log_stream.write('Engine finished execution.\n')

    def cleanup(self):
        self.dwca.close()

#TODO: Test that the engine properly calls and reacts to applicable_to_archive 