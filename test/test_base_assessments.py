import unittest
from meuh.assessments.base import IndividualRowAssessment


class TestBaseAssessments(unittest.TestCase):
    def test_cannot_instanciate_individualrow(self):
        """Ensure IndividualRowAssessment is an abstract base class that cannot be instanciated."""
        with self.assertRaises(TypeError):
            IndividualRowAssessment()

