# @Time : 2021/2/24 15:53 

# @Author : Upgrade(jicisala@126.com)

# @File : string_type_validate.py 

# @Software: PyCharm


def is_date(string: str, separator: str = '-'):
    year, month, day = (int(x) for x in string.split(separator))

    # 基础判断
    if not len(str(year)) == 4 and 1 <= month <= 12 and year > 0:
        return False

    # 天数判断
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            return False
    if month in [4, 6, 9, 11]:
        if not 1 <= day <= 30:
            return False
    else:
        if year % 4 == 0:
            if not 1 <= day <= 29:
                return False
        else:
            if not 1 <= day <= 28:
                return False

    return True


def is_time(time_: str, separator: str = ':'):
    hour, minute, second = (int(x) for x in time_.split(separator))

    if not 0 <= hour <= 24 or not 0 <= minute <= 60 or not 0 <= second < 60:
        return False

    return True


if __name__ == '__main__':
    print(is_date('13-12-3'))
