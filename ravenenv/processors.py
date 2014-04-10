from raven import processors
from raven.conf import defaults
import os


class AddEnviromentContext(processors.Processor):

    def get_env_info(self):
        """return environment variables as dict"""
        data = {}
        data.update(os.environ)
        return data

    def process(self, data, **kwargs):
        """add to message data environment variables"""
        if 'extra' in data:
            data['extra'].update(self.get_env_info())
        else:
            data['extra'] = self.get_env_info()
        return data
