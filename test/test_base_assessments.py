import unittest
from meuh.assessments.base import Assessment


class TestBaseAssessments(unittest.TestCase):
    def test_cannot_instanciate_assessment(self):
        """Ensure Assessment is an abstract base class that cannot be instanciated."""
        with self.assertRaises(TypeError):
            Assessment()

