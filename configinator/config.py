"""
Simple library to load a config file and make config items available via
dot-notation. I find it easier to read that way.
"""
import json
import base64


class Config(dict):
    """ The class I mentioned above """

    def __init__(self, config):

        def _translate_config_items(config):
            for key, _ in config.items():
                if ":" not in key:
                    continue
                fmt, new_key = key.split(":", 1)

                if fmt == "b64":
                    config[new_key] = base64.b64decode(
                        config.pop(key)).decode('utf-8')
            return config

        super(Config, self).__init__(_translate_config_items(config))

    def __getattr__(self, key):
        if key not in self:
            raise AttributeError("No such attribute '{}'".format(key))
        attr = super(Config, self).get(key)
        if isinstance(attr, dict):
            return Config(attr)
        return attr

    def __repr__(self):
        return str(self.__class__)

    @staticmethod
    def _not_a_dict(*_):
        raise TypeError("Config object is not subscriptable")

    get = __getitem__ = __setitem__ = _not_a_dict

    @staticmethod
    def load_from_file(filename, fmt='json'):
        """ Factory to create Config object from a config file """
        if fmt == 'json':
            # If there are issues opening the file or parsing the json, an
            # exception will be raised for us. We'll let that bubble up
            with open(filename, 'r') as handle:
                config = json.load(handle)

        return Config(config)
