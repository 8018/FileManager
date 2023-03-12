# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -*- coding: UTF-8 -*-

import os
import shutil

garbage = ["更多精彩套图视频下载尽在",
           "更多精彩套图与视频尽在",
           '关于资源二次加压',
           '会员站,美图触手可及',
           '精选优惠券低至一折',
           '美图控',
           '游戏设置成中文方法-看一下',
           '套图吧说明',
           '套图吧网址发布页',
           "资源来自于美图阁",
           "logo.png",
           '重要必须看',
           '务必收藏',
           '聚 合 全 網 H 直 播',
           '社 區 最 新 情 報',
           '最 新 位 址 獲 取',
           'x u u 6 2 . c o m',
           '欢迎添加我为好友',
           '好用代理',
           '好用的梯子',
           '写真图库',
           '资源目录',
           '更多优质资源',
           '来了就能下载和观看！纯免费！',
           '论坛介绍',
           '永久地址',
           'Thumbs.db',
           '最新地址',
           '更多的免费资源',
           '空的.txt',
           '游戏动漫资源网站',
           '地址发布页',
           '欢迎关注我的公众号']


def is_garbage(file_name):
    for garbage_name in garbage:
        if file_name.count(garbage_name) > 0:
            return True
    return False


def is_empty_folder(path):
    if not os.path.isdir(path):
        return False

    count = 0
    files = os.listdir(path)
    for file in files:
        if str(file) != '.DS_Store':
            count += 1

    if count == 0:
        return True

    return False


def delete_garbage_if_indeed(file_name):
    if not os.path.exists(file_name):
        return

    if is_garbage(file_name):
        print("Delete garbage file " + file_name)
        try:
            os.remove(file_name)
        except Exception as e:
            print("The except is %s" % e)

    if is_empty_folder(file_name):
        print("Delete garbage folder " + file_name)
        try:
            shutil.rmtree(file_name)
        except Exception as e:
            print("The except is %s" % e)
