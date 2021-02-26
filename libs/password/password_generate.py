# @Time : 2021/2/4 9:32 

# @Author : Upgrade(570492547@qq.com)
import random


def password_generate(password_length=12, if_number=True, if_letter=True, if_symbol=True, chars_excludes=None):
    """ 密码生成器

    生成一个随机密码，通过参数指定密码长度，设置是否需要数字，是否需要字母，是否需要符号，是否有排除字符

    Args:
        length int: 生成的密码长度，默认为12
        if_number bool: 是否包含数字，默认包含
        if_letter bool: 是否包含字母，默认包含
        if_symbol bool: 是否包含符号，默认包含
        chars_excludes list: 需要排除的字符，默认为空
    Return:
        password str: 返回生成的密码
    """
    available_chars = []
    password_list = []

    # 根据参数生成可用字符列表
    if if_number:
        available_chars += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if if_letter:
        available_chars += ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if if_symbol:
        available_chars += ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    # 排除不用的字符
    if chars_excludes:
        for char in chars_excludes:
            if char in available_chars:
                available_chars.remove(char)

    random_range = len(available_chars)

    for _ in range(password_length):

        password_list.append(available_chars[random.randint(0, random_range-1)])

    password = ''.join(password_list)

    return password


if __name__ == '__main__':
    print(password_generate())
