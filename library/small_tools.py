
def retrieval_text(text,characteristic):
    """
    获取文本特征字符位置
    :param text: 输入的文本，格式位str
    :param characteristic: 要寻找的特征字符，格式位str
    :return: list，标记特征字符所在位置
    """
    # 初始化参数
    star = 0
    index = []
    max_text = len(text)  # 终止条件
    while star <= max_text:
        star = text.find(characteristic, star)
        index.append(star)
        if star == -1:  # 处理找不到的情况
            break
        star += star  # 下次初始位置
    return index




if __name__ == '__main__':
    a = ''