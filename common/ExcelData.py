from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
class Data:
    def __init__(self,testcase_file,sheet_name):
        #获取list
        #self.reader = ExcelReader("../data/testdata.xlsx","Sheet1")
        self.reader = ExcelReader(testcase_file,sheet_name)
        #print(reader.data())
    #列的内容是否要运行
    def get_run_data(self):
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig.is_run]).lower() == "y":
                run_list.append(line)
        print(run_list)
        return run_list

    def get_case_list(self):
         #获取全部用例
         # run_list = list()
         # for line in self.reader.data():
         #         run_list.append(line)
         run_list = [line for line in self.reader.data()]
         return run_list
    #获取执行用例方法
    def get_case_pre(self,pre):
        #根据前置条件，获取全部用例
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None


#保存要执行结果，放到新的列表