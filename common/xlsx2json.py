# -*- coding: utf-8 -*-

import xlrd
import json
import codecs

def Excel2Json(file_path):

    if get_data(file_path) is not None:
        book = get_data(file_path)
        sheets = book.sheet_names()
        for sheetName in sheets:
            if sheetName == 'AIM':
                sheet = book.sheet_by_name('AIM')
                row_0 = sheet.row_values(0)  # 第一行是表单标题
                nrows = sheet.nrows
                ncols = sheet.ncols
                result = []
                final = {}
                proj = []
                for i in range(1, nrows):
                    row = {}
                    data = sheet.row_values(i)
                    for j in range(0, ncols):
                        row[row_0[j]] = data[j]
                    result.append(row)
                    proj.append(row['project'])
                final['children'] = result
                final['title'] = sheetName
                final['cols'] = row_0
                final['project'] = proj
                json_data_temp = json.dumps(final, indent=4, sort_keys=True)
                saveFile(sheetName, json_data_temp)
                print()
            elif sheetName == '爱贷网理财_PC' or sheetName == '爱贷网-PC':
                sheet = book.sheet_by_name(sheetName)
                row_0 = sheet.row_values(0)  # 第一行是表单标题
                nrows = sheet.nrows
                ncols = sheet.ncols

                result = {}
                final = {}
                for i in range(1, nrows):
                    row = {}
                    data = sheet.row_values(i)

                    for j in range(1, ncols):
                        row[row_0[j]] = data[j]

                    if not row["模块"] in result:
                        result[row["模块"]] = []

                    result[row["模块"]].append(row)

                final['children'] = result
                final['title'] = sheetName
                final['cols'] = row_0
                json_data_temp = json.dumps(final, indent=4, sort_keys=True)
                saveFile(sheetName, json_data_temp)
                print()
    else:
        final = {}
        result = {'title': 'NULL', 'cols': 'NULL', 'children': 'NULL'}
        final['children'] = result
        final['title'] = 'NULL'
        final['cols'] = 'NULL'
        print(final)
        return final

def get_data(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(u'excel表格读取失败：%s' % e)
        return None

def saveFile(file_name, data):
    output = codecs.open('../Data/' + file_name + '.json', 'w', 'utf-8')
    output.write(data)
    output.close()

if __name__ == '__main__':
    Excel2Json('../DATA/testData.xlsx')
