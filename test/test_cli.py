import unittest
from StringIO import StringIO
from tempfile import NamedTemporaryFile

from meuh.cli import main, BadConfigFileException
from meuh.test.helpers import sample_data_path, sample_config_path


def _str_to_args(str):
    return str.split()


class TestCLI(unittest.TestCase):
    SAMPLE_ARCHIVE_PATH = sample_data_path('dwca-simple-test-archive.zip')

    def test_usage_on_stderr(self):
        """Assert usage information is displayed to stderr and not stdout(reserved for results)."""

        err_stream = StringIO()
        out_stream = StringIO()

        try:
            args = _str_to_args("./meuh")
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
            args = _str_to_args("./meuh {config_file}".format(config_file=config_file.name))
            main(args, out=out_stream, err=err_stream)
        except SystemExit as err:  # Because arparse will call sys.exit
            self.assertTrue("error: too few arguments" in err_stream.getvalue())
            self.assertNotEqual(0, err.code)

    def test_invalid_config_file(self):
        config_path = sample_config_path('missing_meuhconfig_var.py')
        args = _str_to_args("./meuh {config} {dwca}".format(config=config_path,
                                                            dwca=self.SAMPLE_ARCHIVE_PATH))
        err_stream = StringIO()
        out_stream = StringIO()

        with self.assertRaises(BadConfigFileException):
            main(args, out=out_stream, err=err_stream)

        # TODO: Implement more checks for invalid config ?

    def test_minimal_args_correct(self):
        """Check that argument parsing succeed if we get two readable files."""

        err_stream = StringIO()
        out_stream = StringIO()

        config_file = sample_config_path('valid.py')

        # Provide both
        args = _str_to_args("./meuh {config} {dwca}".format(config=config_file,
                                                            dwca=self.SAMPLE_ARCHIVE_PATH))
        rc = main(args, out=out_stream, err=err_stream)
        
        self.assertEqual("", err_stream.getvalue())
        self.assertEqual(0, rc)


    # Ensure output is by default on stdout

    # Ensure output can be set to an arbitrary file


