# @Time : 2021/2/24 15:53 

# @Author : Upgrade(570492547@qq.com)


def is_date(string: str, separator: str = '-') -> bool:
    """ judge whether the string is a date format

    Args:
        string: The string which needs to be judged
        separator: string`s separator, default is '-'

    Returns:
        bool: True or False
    """
    year, month, day = [int(x) for x in string.split(separator)]

    # basic judge
    if not len(str(year)) == 4 and 1 <= month <= 12 and year > 0:
        return False

    # day judge
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True if 1 <= day <= 31 else False
    elif month in [4, 6, 9, 11]:
        return True if 1 <= day <= 30 else False
    else:
        if year % 4 == 0:
            return True if 1 <= day <= 29 else False
        else:
            return True if 1 <= day <= 28 else False


def is_time(time_: str, separator: str = ':') -> bool:
    """ judge whether the string is time format

    Args:
        time_: The string which needs to be judged
        separator: string`s separator, default is ':'

    Returns:
        bool: True or False
    """
    hour, minute, second = (int(x) for x in time_.split(separator))

    return True if 0 <= hour <= 24 and 0 <= minute <= 60 and 0 <= second < 60 else False
