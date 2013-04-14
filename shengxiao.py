#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def isInt(function):
    def validation(year):
        if isinstance(year, int):
            return function(year)
        else:
            return "The number of year must be an int."

    return validation


@isInt
def yearToAnimal(year):
    """根据年份计算属相"""
    animals = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    order = (year - 1984) % 12
    return animals[order]


@isInt
def yearToGanZhi(year):
    """根据年份计算干支"""
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', ]
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥', ]

    step = year - 1911      # 纪念辛亥革命发生于1911年
    year_name = tiangan[(7 + step) % 10] + dizhi[(11 + step) % 12]
    return year_name

if __name__ == "__main__":
    year = datetime.datetime.now().year
    print "This year is %s, it should be dominated by %s" % (yearToGanZhi(year), yearToAnimal(year))