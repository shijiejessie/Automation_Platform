import os
import yaml
class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf=yamlf
        else:
            raise  FileNotFoundError("yaml文件不存在")
        self._data = None
        self._data_all = None
    def  data(self):
        if not  self._data:
            with open(self.yamlf,"rb") as f:
                 self._data = yaml.safe_load(f)
        return self._data
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all
