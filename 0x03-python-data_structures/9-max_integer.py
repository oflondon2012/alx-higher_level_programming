#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    m_num = my_list[0]
    for num in my_list:
        if num > m_num:
            m_num = num
    return m_num
