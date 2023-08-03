# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 11:03
# @Author  : shaocanfan
# @File    : numberTqUtils.py


import re
# 汉字数字转阿拉伯
def chinese_to_arabic(chinese_number):
    chinese_numerals = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
    arabic_number = 0
    temp_num = 0
    total_num = 0
    for char in chinese_number:
        if char in chinese_numerals:
            temp_num = chinese_numerals[char]
            if temp_num < 10:  # 当前字符是'十'之前的数字
                arabic_number += temp_num
            else:
                if arabic_number == 0:  # 第一个字符是'十'及以后的数字
                    arabic_number = 1
                if temp_num < 10000:  # 处理万以下单位
                    arabic_number = arabic_number * temp_num
                else:  # 处理万及以上单位
                    total_num += arabic_number * temp_num
                    arabic_number = 0
        else:
            break

    total_num += arabic_number
    return total_num
# 提取汉字数字
def extract_chinese_numerals(text):
    pattern = r'[零一二三四五六七八九十百千万亿]+'
    # 使用正则表达式进行匹配
    matches = re.findall(pattern, text)
    return matches
# 提取数字
def extract_arabic_numerals(text):
    pattern = r'-?\d+\.?\d*'
    arabic_numerals = re.findall(pattern, text)
    return [float(num) for num in arabic_numerals if num]

# 提取数字加汉字（支持没有汉字）
def extract_number_with_units(text):

    #提取中文，要不是单位，要不是完整数字
    unit = extract_chinese_numerals(text)
    main = extract_arabic_numerals(text)
    if len(unit)!=0:
        if (unit[0] == "千" or unit[0] == "万" or unit[0] == "亿" \
                or unit[0] == "十" or unit[0] == "百万" \
                or unit[0] == "千万") and len(main)==0:
            return 0
        unit1 = unit[0]
        if(len(unit)):
            unit = chinese_unit_to_arabic(unit[0])
            if unit==None:
                #不是单位，直接转为阿拉伯数字
                return chinese_to_arabic(unit1)
        else:
            unit=1
    else:
        unit=1
    if(len(main)):
        main = main[0]
    else:
        main=1

    return str(main*unit)
#//////////////////////////////////////////////
# 获得中文单位
def chinese_unit_to_arabic(chinese_unit):
    chinese_units = {'千': 1000, '万': 10000,'十万': 100000,'百万': 1000000,'千万': 10000000, '亿': 100000000}
    return chinese_units.get(chinese_unit)
# 判断全是数字和有中文数字

if __name__ == '__main__':
    r = extract_number_with_units("线上受众超9.6万人次。")
    print(r)













