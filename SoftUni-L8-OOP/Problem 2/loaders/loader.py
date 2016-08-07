import json
import yaml

from loaders.base_loader import Loader


class JSONLoader(Loader):
    def __init__(self, filename):
        super().__init__(filename)

    def load(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data


class YAMLLoader(Loader):
    def __init__(self, filename):
        super().__init__(filename)

    def load(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            return input_data
