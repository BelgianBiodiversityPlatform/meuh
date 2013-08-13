import unittest
from StringIO import StringIO 

from meuh.cli import main 


class TestCLI(unittest.TestCase):
    def test_usage_on_stderr(self):
        """Assert usage information is displayed to stderr (stdout is reserved for results)"""

        err_stream = StringIO()
        out_stream = StringIO()

        try:
            main("", out=out_stream, err=err_stream)
        except SystemExit: # Because arparse will call sys.exit
            self.assertEqual("", out_stream.getvalue())
            self.assertEqual("usage: nosetests [-h] config_file data_file\nnosetests: error: too few arguments\n", err_stream.getvalue())

    # Ensure it requires a config file

    # Ensure it requires a DwC-A

    # Ensure output is by default on stdout

    # Ensure output can be set to an arbitrary file
