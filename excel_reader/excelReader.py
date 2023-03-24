import openpyxl
import allure
from httpmodel.httpModel import HttpModel
from VAR.VAR import *

class ExcelReader1:

    def excelReader(self):
        book = openpyxl.load_workbook(EXCEL_PATH)
        all_sheets = book.sheetnames
        # print(all_sheets)

        # 这个列表就是为了存放所有已经赋完值的实例化对象
        models = []

        for s in all_sheets:
            sheet = book[s]
            for i in sheet.values:
                if type(i[19]) == int:
                    # print(i)
                    # 实例化对象
                    model = HttpModel()
                    # 给传入的参数赋值
                    model.url = i[0]
                    # print(model.url)
                    model.case_desc = i[1]
                    model.method = i[2]
                    model.para_type = i[3]
                    model.headers = i[4]
                    model.data = i[5]
                    model.assert_data = i[6]
                    model.assert_options = i[7]
                    model.assert_value = i[8]
                    model.assert_result = i[9]
                    model.extract = i[10]
                    model.case_feature = i[11]
                    model.case_story = i[12]
                    model.backup = i[13]
                    model.case_level = i[14]
                    model.sql = i[15]
                    model.sql_var = i[16]
                    model.sql_value = i[17]
                    model.is_run = i[18]
                    model.num = i[19]

                    models.append(model)
        # print(model.url)
        return models


# if __name__ == '__main__':
#     ER = ExcelReader1()
#     print(ER.excelReader())