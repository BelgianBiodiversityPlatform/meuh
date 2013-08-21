import types
from abc import ABCMeta, abstractmethod

from .logging import AssessmentLog


def _hasmethod(obj, name):
    return hasattr(obj, name) and type(getattr(obj, name)) == types.MethodType


class Assessment():
    # TODO: find a mechanism so assessment are easily testable autonomously

    __metaclass__ = ABCMeta

    @abstractmethod
    def applicable_to_archive(self, archive):
        """Check that the assessment, in its current config. is applicable to the given archive.

        Returns True or False
        - In case of non-applicability, should log (MessageLevels.ERROR and MessageLevels.ERROR)
        - In case of applicability, best practice is to not log
        - If deemed necessary, you may log a warning
        """
        pass

    # Subclasses should call this contstructor. They'll get a logger
    def __init__(self):
        self.logger = AssessmentLog()

    # Document adn test this mechanism
    @property
    def assess_each_line(self):
        return _hasmethod(self, 'assess_line')

# TODO: Document ho to create new tests
# TODO: Test that subclasses properly act (i.e., they have a logger, ...)
