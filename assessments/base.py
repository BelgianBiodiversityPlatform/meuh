from abc import ABCMeta, abstractmethod


class IndividualRowAssessment():
    # TODO: find a mechanism so assessment are easily testable autonomously

    __metaclass__ = ABCMeta

    @abstractmethod
    def applicable_to_archive(self, archive):
        """Check that the assessment, in its current config. is applicable to the given archive.

        Returns a tuple:
        - In not applicable: (False, 'Descriptive error message')
        - If applicatble: (True, True) # Second value will be discarded
        """
        pass