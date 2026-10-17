class Observatory:
    def __init__(self, name):
        self.name = name
        self.observation_log = []

    def observe(self, body_name, telescope, result):
        details = {
            "body": body_name,
            "telescope": telescope,
            "result": result
        }
        self.observation_log.append(details)

    def values(self): # This is for the filter values in show_log
        pass


    def show_log(self, fields = None):

        if fields is None:
            fields = []
            for observation in self.observation_log:
                fields.append(observation.values())

        for field in fields:
            if field.lower() not in ['body', 'telescope', 'result']:
                return 'Your filter is not valid. Please pick from body/telescope/result in list only.'
        
        showrequest = []
        for observation in self.observation_log:
            group = {}
            for field in fields:
                group[field.lower()] = observation[field.lower()]
            showrequest.append(group)

        return showrequest


observatory = Observatory("Manila Observatory")

observations = [
    {
        "body": "Mars",
        "telescope": "Hubble",
        "result": "Possible dust storm detected"
    },
    {
        "body": "Jupiter",
        "telescope": "James Webb",
        "result": "Atmospheric composition analyzed"
    },
    {
        "body": "Saturn",
        "telescope": "Cassini",
        "result": "Ring structure observed"
    },
    {
        "body": "Moon",
        "telescope": "Lunar Reconnaissance Orbiter",
        "result": "Surface crater mapped"
    },
    {
        "body": "Venus",
        "telescope": "Magellan",
        "result": "Volcanic terrain mapped"
    }
]

for observation in observations:
    observatory.observe(observation['body'], observation['telescope'], observation['result'])

print(observatory.show_log(['Hubble']))
