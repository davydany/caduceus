import logging
import logging.config as log_config

from caduceus.config import LOGGING_CONFIG

log_config.dictConfig(LOGGING_CONFIG)

class BaseClass(object):

    def __init__(self):
        """
        Initializes with a configured logger.
        """
        self.logger = logging.getLogger('caduceus')
