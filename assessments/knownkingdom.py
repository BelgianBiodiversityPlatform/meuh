from dwca.darwincore.utils import qualname as qn

from meuh.assessments.base import IndividualRowAssessment
from meuh.assessments.logging import MessageLevels, MessageTypes


class KnownKingdomAssessment(IndividualRowAssessment):
    ACCEPTED = {'cavalier-smith': set(['animalia', 'fungi', 'plantae', 'chromista', 'protozoa',
                                       'bacteria']),
                'whose_1977': set(['eubacteria', 'archaebacteria', 'protista', 'plantae', 'fungi',
                                   'animalia']),
                'whittaker': set(['monera', 'protista', 'plantae', 'fungi', 'animalia']),
                'copeland': set(['mychota', 'protoctista', 'plantae', 'animalia']),
                'haeckel': set(['protista', 'plantae', 'animalia']),
                'linnaeus': set(['vegetabilia', 'animalia'])}

    def __init__(self, testoptions):
        super(KnownKingdomAssessment, self).__init__()
        
        asked_classification = testoptions['classification']

        if asked_classification == 'all':
            # We have to built a set doing the union of specific classifications
            self._currently_accepted = set()
            for k, v in self.ACCEPTED.items():
                self._currently_accepted = self._currently_accepted.union(v)
        else:
            self._currently_accepted = self.ACCEPTED[asked_classification]

        msg = "Configured to use {cla} classification".format(cla=asked_classification)
        self.logger.log(msg, MessageTypes.INIT, MessageLevels.INFO)

    def applicable_to_archive(self, archive):
        if archive.core_rowtype == qn('Occurrence'):
            if archive.core_contains_term(qn('kingdom')):
                return True
            else:
                self.logger.log("Core should contain the 'kingdom' term", MessageTypes.APPLICABILITY, MessageLevels.ERROR)
                return False
        else:
            self.logger.log("Archive core should be of Occurrence type.", MessageTypes.APPLICABILITY, MessageLevels.ERROR)
            return False
