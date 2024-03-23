import os
import pandas as pd


def name_path(file_path, suffix=-5):
    """
    根据文件夹路径，获取其中文件名及文件路径
    :param file_path: 文件夹路径
    :parameter suffix: 需要去除的文件后缀的字符数，默认为-5
    :return: 文件名，文件绝对路径
    """
    file_name = os.listdir(file_path)  # 获取文件路径下的文件列表
    name = [i[:suffix] for i in file_name]  # 将文件后缀去掉
    path_list = list()
    # 将文件路径与文件全名组合成绝对路径，并加入到list
    for i in file_name:
        path_list.append(os.path.join(file_path, i))
    return name, path_list


def table_consolidation(path_list, table_name='Sheet1'):
    """
    将列表中的DataFrame合并成一个DataFrame
    :param path_list: 文件绝对路径列表
    :parameter table_name: excel中子表名称，默认为(Sheet1)
    :return: 合并后的文件
    """
    df_sum = list()
    for i in path_list:
        df = pd.read_excel(i, sheet_name=table_name)
        df_sum.append(df)
    result = pd.concat(df_sum)  # 纵向按照columns相同字段合并
    result = result.iloc[:, 1:]  # 去掉原先表格中的序号
    return result


def table_split(input_path, split_num, out_path, out_name='拆分表', table_name='Sheet1'):
    """
    根据导入的表格，生成指定数量的表格，并保存到指定目录下
    :param input_path: 数据表格所在路径。
    :param split_num: 拆分数量，因为除不尽的原因，所输出的表会比此数字大1。
    :param out_path: 所要保存的文件目录路径。
    :parameter out_name: 索要保存的文件名称。默认为(拆分表)
    :parameter table_name: excel中子表名称，默认为(Sheet1)
    :return:
    """
    df = pd.read_excel(input_path, sheet_name=table_name)
    rows = len(df.iloc[:, 0]) // split_num  # 每一组数据的行数
    b = 0  # 文件计数
    a = 0  # 确定行位置
    while a < len(df.iloc[:, 0]):
        data = df.iloc[a:(a + rows)]
        b += 1
        # 将获取到的路径转换为绝对路径（os.path.abspath），并与目录名称组合成文件路径(os.path.join)
        data.to_excel(os.path.join(os.path.abspath(out_path), f'{out_name}{b}.xlsx'))
        a = a + rows
    print(f"已完成任务，共拆分{b}张表.")
