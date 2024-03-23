from user.Server import LocalSQL
from library.connect_sql import CallMySQL, CallSQL


class SQL():
    def __init__(self, database, num):
        """
        :param database:  数据库连接数据
        """
        self.type = database['type'][num]
        self.user = database['username'][num]
        self.password = str(database['password'][num])
        self.ip = database['IP'][num] + ':' + database['port'][num]
        self.database = database['db'][num]


def connect_to_database(id):
    """
    连接到指定类型的数据库，并返回数据库连接对象。
    :param id: 需要查询的数据的ID标识符。
    :return: 数据库连接对象，根据数据库类型（SQL Server或MySQL）返回不同类型的连接对象。
    """
    server = CallSQL(LocalSQL)
    command = """select * from sql_db;"""
    # 从数据库获取数据
    df = server.get_data(command)
    df.index = df.id  # 重置索引为id
    database = SQL(df, id)
    # 判断数据库类型并连接
    if database.type == 'sqlserver':
        data_server = CallSQL(database)
        print('已连接至SQL数据库')
        return data_server
    elif database.type == 'MySQL':
        data_server = CallMySQL(database)
        print('已连接至MySQL数据库')
        return data_server
    else:
        print('未连接至数据库或未找到数据')
        return None


if __name__ == '__main__':
    a = connect_to_database(11)
    sql_command = """select * from test;"""
    print(a.get_data(sql_command))
