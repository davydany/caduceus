LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'caduceus': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

class Configuration():

    def __init__(self, debug):

        self.debug = bool(debug)

    def get_logging_config(self):

        return LOGGING_CONFIG

    def get_caduceus_remote_url(self, project_id):


        host = 'localhost' if self.debug else 'caduceus.herokuapp.com'
        port = '9000' if self.debug else '80'
        params = {
            'host': host,
            'port': port,
            'project_id': project_id
        }

        return 'http://%(host)s:%(port)s/api/project/%(project_id)s/request/' % (
            params
        )

    