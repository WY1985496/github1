import xlrd
import allure
from httpmodel.httpModel import HttpModel
from VAR.VAR import *


class ExcelReader2:
    # excel_path = '../data/aishi2.xls'

    def excelReader(self, excel_path=EXCEL_PATH):
        book = xlrd.open_workbook('../data/aishi2.xls')
        all_sheets = book.sheet_names()
        # print(all_sheets)

        # 这个列表就是为了存放所有已经赋完值的实例化对象
        models = []

        for s in all_sheets:
            sheet = book[s]
            for r in range(1, sheet.nrows):  # 跳过第一行
                # 每行添加完成后，列表做一次清空，保证每次最终列表的添加数据都未同一行数据
                list1 = []
                for c in range(sheet.ncols):
                    list1.append(sheet.cell(r, c).value)
                # 实例化对象
                model = HttpModel()
                # 给传入的参数赋值
                model.url = list1[0]
                # print(model.url)
                model.case_desc = list1[1]
                model.method = list1[2]
                model.para_type = list1[3]
                model.headers = list1[4]
                model.data = list1[5]
                model.assert_data = list1[6]
                model.assert_options = list1[7]
                model.assert_value = list1[8]
                model.assert_result = list1[9]
                model.extract = list1[10]
                model.case_feature = list1[11]
                model.case_story = list1[12]
                model.backup = list1[13]
                model.case_level = list1[14]
                model.sql = list1[15]
                model.sql_var = list1[16]
                model.sql_value = list1[17]
                model.is_run = list1[18]
                model.num = list1[19]

                models.append(model)
        # print(model.url)
        return models


if __name__ == '__main__':
    ER = ExcelReader2()
    ER.excelReader()
