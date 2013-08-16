from dwca import DwCAReader


class MeuhEngine(object):
    # Preferably, use 'with' to ensure proper cleanup at the end
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.cleanup()

    def __init__(self, config, dwca):
        # config: object
        # dwca: open file
        self.dwca = DwCAReader(dwca)

        # Parse config
        self.assessment_instances = config['tests']

    def run(self, output_stream):
        pass

    def cleanup(self):
        self.dwca.close()
