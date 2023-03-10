# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -*- coding: UTF-8 -*-

import os
import subprocess
import filetype
import py7zr
import shutil
from unrar import rarfile
import time
import garbage

# b
compressed_suffix = ["mtg", "mtuge", "DRT", "rar", "zip"]

passwords = [
    'meituge',
    'mtuge',
    'taotu8',
    '5188',
    'qwer',
    'qwerty',
    'lc123456@163.com',
    '996acg.com',
    '777acg.com',
    '668acg.com',
    'TMBiwM》rG0WV3Sf7hDgOGE00',
    '555',
    'cunhua',
    'http://www.itokoo.com/',
    '上老王论坛当老王',
    '第一街拍',
    'qingyu',
    'asianpink.net',
    'fgRZ#kF$IdhDO8c@fV',
    'btbtt',
    None]
root_path = "/Users/michaelliu/downloads/Download"


# 判断是否是压缩文件¬
# 需要增加 pdf，txt 后缀文件判断
def file_type(file):
    kind = filetype.guess(file)
    if kind is None:
        return "None"

    return kind.extension


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def is_compressed(file):
    if str(file_type(file)) == 'rar':
        return True
    if str(file_type(file)) == 'zip':
        return True
    if str(file_type(file)) == '7z':
        return True
    return False


def extract_7z(src_file, dst_folder, password):
    try:
        print("7z 正在解压 %s 当前密码是 %s" % (src_file.replace(dst_folder, ''), password))
        start_time = time.time()
        if password is None or len(password) == 0:
            with py7zr.SevenZipFile(src_file, mode='r') as z:
                z.extractall(dst_folder)
        else:
            with py7zr.SevenZipFile(src_file, mode='r', password=password) as z:
                z.extractall(dst_folder)

        now_time = time.time()
        print("spend time is {}".format(now_time - start_time))
        return True
    except Exception as e:
        print("The except is %s" % e)
        return False


def extract_zip(src_file, dst_folder, password):
    try:
        print("zip 正在解压 %s 当前密码是 %s" % (src_file.replace(dst_folder, ''), password))
        start_time = time.time()
        if (password is not None) and len(password) > 0:
            print("with password")
            command = 'unar -f -o %s -p %s %s' % (dst_folder, password, src_file)
        else:
            print("with no password")
            command = 'unar -o %s %s' % (dst_folder, src_file)

        proc = subprocess.Popen(command, shell=True)
        _ = proc.communicate()

        now_time = time.time()
        print("spend time is {}".format(now_time - start_time))
        if proc.returncode == 0:
            print(1)
            return True
        else:
            print(2)
            return False

    except Exception as e:
        print("The except is %s" % e)


def extract_rar(src_file, dst_folder, password=None):
    is_rar = rarfile.is_rarfile(src_file)
    if not is_rar:
        return False

    try:
        print("rar 正在解压 %s 当前密码是 %s" % (src_file.replace(dst_folder, ''), password))
        start_time = time.time()
        if password is None or len(password) == 0:
            with rarfile.RarFile(src_file) as rar_file:
                rar_file.extractall(dst_folder)
        else:
            if is_contains_chinese(password):
                with rarfile.RarFile(src_file,
                                     pwd=password.encode('utf-8').decode('cp437')) as rar_file:
                    rar_file.extractall(dst_folder)

            else:
                with rarfile.RarFile(src_file, pwd=password) as rar_file:
                    rar_file.extractall(dst_folder)

        now_time = time.time()
        print("spend time is {}".format(now_time - start_time))

        return True

    except Exception as e:
        print("The except is %s" % e)
        return False


def extract(src_file, dst_folder):
    for password in passwords:

        if file_type(src_file) == '7z':
            if extract_7z(src_file, dst_folder, password):
                os.remove(src_file)
                return

        if file_type(src_file) == 'zip':
            if extract_zip(src_file, dst_folder, password):
                os.remove(src_file)
                return

        if file_type(src_file) == 'rar':
            if extract_rar(src_file, dst_folder, password):
                os.remove(src_file)
                return


def is_empty_folder(path):
    if not os.path.isdir(path):
        return False

    count = 0
    files = os.listdir(path)
    for _ in files:
        count += 1

    if count == 0:
        return True

    return False


def filing(path):
    for i in range(3):
        for root, dirs, files in os.walk(path):

            for file in files:
                if not os.path.exists(os.path.join(root, file)):
                    continue

                if file == '.DS_Store':
                    continue

                if is_compressed(os.path.join(root, file)) and not str(file).endswith('downloading'):
                    # if root != path:
                    src = os.path.join(root, file)
                    dst = os.path.join(path, "n_" + file)
                    shutil.move(src, dst)
                    if not str(dst).endswith('downloading'):
                        extract(dst, root_path)

                garbage.delete_garbage_if_indeed(os.path.join(root, file))

            for folder in dirs:
                garbage.delete_garbage_if_indeed(os.path.join(root, folder))


filing(root_path)
