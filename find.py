
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def read_excel_file(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path, engine='openpyxl')
    return df


def fuzzy_match(strings, choices):
    # 使用模糊匹配找到最符合的字符串
    result = process.extract(strings, choices, limit=1)
    return result[0][0] if result else None


def get_data_from_excel(file_path, strings):
    df = read_excel_file(file_path)
    column_1 = df.iloc[:, 14].tolist()  # 获取第一列的数据
    column_14 = df.iloc[:, 13].tolist()  # 获取第14列的数据
    matched_strings = []
    matched_data = []
    for string in strings:
        best_match = fuzzy_match(string, column_1)
        if best_match:
            index = column_1.index(best_match)
            matched_strings.append(best_match)
            matched_data.append(column_14[index])
    return matched_strings, matched_data


def find(given_strings):
    # 给定的中文字符串列表
    #given_strings = ["女帝的傲", "擅长内道", "非标准距离"]

    # Excel文件路径
    file_path = "weight/output.xlsx"

    # 从Excel文件中获取最符合的行中的第14列数据
    matched_strings, matched_data = get_data_from_excel(file_path, given_strings)
    print("模糊匹配到的字符串:", matched_strings)
    print("评分估值为:", matched_data)
    return matched_data

