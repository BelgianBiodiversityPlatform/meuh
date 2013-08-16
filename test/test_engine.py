import unittest
import os

from meuh.test.helpers import sample_data_path, sample_config_path
from meuh.engine import MeuhEngine


class TestEngine(unittest.TestCase):
    SAMPLE_ARCHIVE_PATH = sample_data_path('dwca-simple-test-archive.zip')

    def test_auto_cleanup(self):
        """Ensure that when used with the 'with' statement, no temporary files are left after use."""

        num_files_before = len(os.listdir('.'))

        meuh_config = {
        'tests': []
        }

        with MeuhEngine(config=meuh_config, dwca=self.SAMPLE_ARCHIVE_PATH):
            # After instanciating, DwCAReader should have created a temporary dir.
            num_files_during = len(os.listdir('.'))

        # After with statement, temporary files should have disappeared
        num_files_after = len(os.listdir('.'))

        self.assertEqual(num_files_before, num_files_after)
        self.assertEqual(num_files_before, (num_files_during - 1))

    def test_invalid_archive(self):
        """Test various invalid archives are rejected."""
        
        # Test with invalid zip file

        # Other tests: to define what should be refused and how, and implement them

        # TODO: Implement 
