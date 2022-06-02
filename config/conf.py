import os
from utils.YamlUtil import YamlReader
current = os.path.abspath(__file__)

#print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)
_config_path = BASE_DIR + os.sep + "config"
_data_path = BASE_DIR + os.sep + "data"

_config_file = _config_path + os.sep + "conf.yml"
_log_path = BASE_DIR + os.sep + "logs"
_db_config_file = _config_path + os.sep + "db_conf.yml"


def get_config_path():
    return  _config_path
def get_config_file():
    return  _config_file
def get_log_path():
    return  _log_path
def get_db_config_file():
    return _db_config_file
def get_data_path():
    return _data_path



class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]
    def get_conf_log(self):
        return  self.config["BASE"]["log_level"]
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]
    def get_db_conf_info(self,db_alias):
        return self.db_config[db_alias]
    def get_excel_file(self):
        return self.config["BASE"]["test"]["case_file"]
    def get_excel_sheet(self):
        return self.config["BASE"]["test"]["case_sheet"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    print(conf_read.get_excel_file())
    print(conf_read.get_excel_sheet())


