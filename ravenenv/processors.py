from raven import processors

class AddEnviromentContext(processors.Processor):

    def get_env_info(self):
        """return environment variables as dict"""
        import os
        return os.environ

    def process(self, data, **kwargs):
        """add to massage date environment variables"""
        if 'extra' in data:
            data['extra'].update(self.get_env_info())
        else:
            data['extra'] = self.get_env_info()
        return data
