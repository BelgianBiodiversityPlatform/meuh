# TODO: document what is expected from the config file

from assessments import knownkingdom

MeuhConfig = {
    'assessments': [knownkingdom.KnownKingdomAssessment({'classification': 'all'}),
                    #coordinatesform.CoordinatesFormTest(),
                    ]
}
