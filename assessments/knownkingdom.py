from dwca.darwincore.utils import qualname as qn

from meuh.assessments.base import IndividualRowAssessment


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
        # init_msg = "Configured to use " + asked_classification + ' classification.'
        # self.log_init_message(init_msg, LogLevels.INFO)

        if asked_classification == 'all':
            # We have to built a set doing the union of specific classifications
            self._currently_accepted = set()
            for k, v in self.ACCEPTED.items():
                self._currently_accepted = self._currently_accepted.union(v)
        else:
            self._currently_accepted = self.ACCEPTED[asked_classification]

    def applicable_to_archive(self, archive):
        # Applicable only for occurrence_based archives
        if archive.core_rowtype == qn('Occurrence'):
            if archive.core_contains_term(qn('Kingdom')):
                return (True, True)  # Second true is ignored, just here to avoid an error
            else:
                return (False, "Core should contain the 'Kingdom' term")
        else:
            return (False, 'Archive core should be of Occurrence type.')
