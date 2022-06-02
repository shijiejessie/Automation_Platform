import os.path
import xlrd

class SheetTypeError:
    pass
#验证文件是否存在
class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在")
#读取sheet
    def data(self):
        workbook = xlrd.open_workbook(self.excel_file)
        if not self._data:
            if type(self.sheet_by) not in [str,int]:
                raise SheetTypeError("请输入Int或Str")
            elif type(self.sheet_by) == int:
                #int类型
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                #string类型
                sheet = workbook.sheet_by_name(self.sheet_by)
            #格式[{"a":"a1","b":"b1"},{{"a":"a2","b":"b2"}]
            title = sheet.row_values(0)
            #遍历，与首行组成dict放在list里面
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                self._data.append(dict(zip(title,col_value)))
        #返回结果
        return self._data


# head =  ["a","b"]
# value1 = ["a1","b1"]
# value2 = ["a2","b2"]
# print(dict(zip(head,value1)))
# print(dict(zip(head,value2)))
# data_list = list()
# data_list.append(dict(zip(head,value1)))
# data_list.append(dict(zip(head,value2)))
# print(data_list)
if __name__ == "__main__":
    reader = ExcelReader("../data/testdata.xlsx","Sheet1")
    print(reader.data())
