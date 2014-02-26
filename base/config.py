'''config.py -- Manages the retrieval and validatio nof configuration
   settings.'''

__author__ = 'Michael Montero <mcmontero@gmail.com>'

# ----- Imports ---------------------------------------------------------------

from .exception import ConfigurationException
import tinyAPI_config

# ----- Public Classes --------------------------------------------------------

class ConfigManager(object):
    '''Handles retrieval and validation of configuration settings.'''

    def value(key):
        if key in tinyAPI_config.values:
            return tinyAPI_config.values[key]
        else:
            raise ConfigurationException(
                '"' + key + '" is not configured in tinyAPI_config')

__all__ = ['ConfigManager']
