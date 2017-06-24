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