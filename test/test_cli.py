import unittest
from StringIO import StringIO
from tempfile import NamedTemporaryFile

from meuh.cli import main


class TestCLI(unittest.TestCase):
    def test_usage_on_stderr(self):
        """Assert usage information is displayed to stderr and not stdout(reserved for results)."""

        err_stream = StringIO()
        out_stream = StringIO()

        try:
            args = str_to_args("./meuh")
            main(args, out=out_stream, err=err_stream)
        except SystemExit:  # Because arparse will call sys.exit
            self.assertEqual("", out_stream.getvalue())
            self.assertEqual("usage: nosetests [-h] config_file data_file\nnosetests: error: too few arguments\n", err_stream.getvalue())

    def test_minimal_args_incorrect(self):
        """Check that it argument parsing fail if one providing one (config) readable file."""

        err_stream = StringIO()
        out_stream = StringIO()

        config_file = NamedTemporaryFile()

        try:
            # Provide config file, but no DwC-A
            args = str_to_args("./meuh {config_file}".format(config_file=config_file.name))
            main(args, out=out_stream, err=err_stream)
        except SystemExit as err:  # Because arparse will call sys.exit
            self.assertTrue("error: too few arguments" in err_stream.getvalue())
            self.assertNotEqual(0, err.code)

    def test_minimal_args_correct(self):
        """Check that it argument parsing pass if we get two readable files."""

        err_stream = StringIO()
        out_stream = StringIO()

        config_file = NamedTemporaryFile()
        dwca_file = NamedTemporaryFile()

        # Provide both
        args = str_to_args("./meuh {config} {dwca}".format(config=config_file.name,
                                                               dwca=dwca_file.name))
        rc = main(args, out=out_stream, err=err_stream)
        
        self.assertEqual("", err_stream.getvalue())
        self.assertEqual(0, rc)


    # Ensure output is by default on stdout

    # Ensure output can be set to an arbitrary file

def str_to_args(str):
    return str.split()