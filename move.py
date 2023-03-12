# coding:utf-8
import os
import shutil
import re
import garbage
import platform

# mygirl_path = '/Users/michaelliu/Downloads/写真/秀人/美媛馆新特刊/'
# mygirl = '美媛馆新特刊'
#
# huayan_path = '/Users/michaelliu/Downloads/写真/秀人/花の颜/'
# huayan = '花の颜'
#
# miitao_path = '/Users/michaelliu/Downloads/写真/秀人/蜜桃社/'
# miitao = '蜜桃社'
#
# mtmeng_path = '/Users/michaelliu/Downloads/写真/秀人/模特联盟/'
# mtmeng = '模特联盟'
#
# candy_path = '/Users/michaelliu/Downloads/写真/秀人/网红馆/'
# candy = '网红馆'
#
# xingyan_path = '/Users/michaelliu/Downloads/写真/秀人/星颜社/'
# xingyan = '星颜社'
#
# youwu_path = '/Users/michaelliu/Downloads/写真/秀人/尤物馆/'
# youwu = '尤物馆'
#
# youmei_path = '/Users/michaelliu/Downloads/写真/尤美/'
# youmei = '尤美'

xiuren_rex = '^[0-9]{4}.(((0[13578]|(10|12)).(0[1-9]|[1-2][0-9]|3[0-1]))|(02.(0[1-9]|[1-2][0-9]))|((0[469]|11).(0[1-9]|[1-2][0-9]|30))) (No|NO|Vol|VOL).[0-9]\d* [\u4e00-\u9fa5]{1,}'
beautyleg_rex = '^[0-9]{4}.(((0[13578]|(10|12)).(0[1-9]|[1-2][0-9]|3[0-1]))|(02.(0[1-9]|[1-2][0-9]))|((0[469]|11).(0[1-9]|[1-2][0-9]|30))) No.[1-9]\d* [a-zA-Z]{1,}'

base_path = '/Users/michaelliu/Downloads'
base_favor_path = '/Users/michaelliu/Downloads/favor'
readed_folder = '/Users/michaelliu/Downloads/readed/'
photo_folder = '/写真/'
xiuren_folder = '/写真/秀人/秀人'
beautyleg_folder = '/写真/Beautyleg'
av_folder = '/你懂的'

dsts = dict([('XINGYAN', '%s秀人/星颜社/' % photo_folder),
             ('Yeeun', '%sothers/Son Ye-Eun/' % photo_folder),
             ('Ye-Eun', '%sothers/Son Ye-Eun/' % photo_folder),
             ('ArtGravia', '%sArtGravia/' % photo_folder),
             ('X-City', '%s日本/' % photo_folder),
             ('尤果网', '%sUgirls/' % photo_folder),
             ('Ugirls', '%sUgirls/' % photo_folder),
             ('李娇', '%sLIJIAO李娇/' % photo_folder),
             ('LIJIAO', '%sLIJIAO李娇/' % photo_folder),
             ('beautyleg', '%sBeautyleg/' % photo_folder),
             ('[Be]', '%sBeautyleg/' % photo_folder),
             ('FEILIN', '%s秀人/嗲囡囡/' % photo_folder),
             ('DKGirl', '%s秀人/御风行者/' % photo_folder),
             ('MFStar', '%s秀人/模范学院/' % photo_folder),
             ('AI', '%sAI/' % photo_folder),
             ('IMiss', '%s秀人/爱蜜社/' % photo_folder),
             ('HuaYang', '%s秀人/花漾/' % photo_folder),
             ('MiStar', '%s秀人/魅妍社/' % photo_folder),
             ('YOUMI', '%s秀人/尤蜜荟/' % photo_folder),
             ('XIAOYU', '%s秀人/语画界/' % photo_folder),
             ('JVID', '%sJVID/' % photo_folder),
             ('语画界', '%s秀人/语画界/' % photo_folder),
             ('blacked', '%s步兵/欧美/' % av_folder),
             ('河北彩花', '%s/日本/' % av_folder),
             ('糖心', '%s/中国/' % av_folder),
             ('星空传媒', '%s/中国/' % av_folder),
             ('三上悠亚', '%s/日本/' % av_folder),
             ('桥本有菜', '%s/日本/' % av_folder),
             ('天使萌', '%s/日本/' % av_folder),
             ('青空光', '%s/日本/' % av_folder),
             ('樱空桃', '%s/日本/' % av_folder),
             ('筱田优', '%s/日本/' % av_folder),
             ('明理绸', '%s/日本/' % av_folder),
             ('相泽楠', '%s/日本/' % av_folder),
             ('吉泽明步', '%s/日本/' % av_folder),
             ('小凑四叶', '%s/日本/' % av_folder),
             ('坂井成羽', '%s/日本/' % av_folder),
             ('深田咏美', '%s/日本/' % av_folder),
             ('濑亚美莉', '%s/日本/' % av_folder),
             ('明里绸', '%s/日本/' % av_folder),
             ('桃谷绘里香', '%s/日本/' % av_folder),
             ('桃乃木香奈', '%s/日本/' % av_folder),
             ('明日花绮罗', '%s/日本/' % av_folder),
             ('前田香织', '%s/日本/' % av_folder),
             ('京香JULIA', '%s/日本/' % av_folder),
             ('山岸逢花', '%s/日本/' % av_folder),
             ('星宫一花', '%s/日本/' % av_folder),
             ('小宵虎南', '%s/日本/' % av_folder),
             ('希岛爱理', '%s/日本/' % av_folder),
             ('七森莉莉', '%s/日本/' % av_folder),
             ('岬奈奈美', '%s/日本/' % av_folder),
             ('武藤绫香', '%s/日本/' % av_folder),
             ('神菜美舞', '%s/日本/' % av_folder),
             ('葵司', '%s/日本/' % av_folder),
             ('九色', '%s/中国/91/' % av_folder),
             ('中国', '%s/中国/' % av_folder),
             ('[3D]', '%s情色/彩漫/' % photo_folder),
             ('脸红Dearie', '%s情色/脸红Dearie/' % photo_folder),
             ('年年', '%s私拍/年年/' % photo_folder),
             ('NianNian', '%s私拍/年年/' % photo_folder),
             ('果哥', '%s/中国/果哥/' % av_folder)
             ])

private_dsts = dict([('鱼子酱', '%s私拍/鱼子酱/' % photo_folder),
                     ('阿朱', '%s私拍/阿朱/' % photo_folder),
                     ('利世', '%s私拍/利世/' % photo_folder)])


def cal_base_path():
    global base_path
    global base_favor_path
    global readed_folder
    system = platform.platform()
    if system.lower().__contains__('macos'):
        base_path = '/Users/michaelliu/Downloads'
        base_favor_path = '/Users/michaelliu/Downloads/favor'
        readed_folder = '/Users/michaelliu/Downloads/readed/'
    if system.lower().__contains__('windows'):
        base_path = 'e://'
        base_favor_path = 'e://favor'
        readed_folder = 'e://readed/'


def is_favor(path):
    if 'f-' in path:
        return True
    if 'favor' in path:
        return True
    return False


def remove_file(file):
    if os.path.isfile(file):
        os.remove(file)
    if os.path.isdir(file):
        shutil.rmtree(file)


def move_private_dir(src, dir_name):
    for key in private_dsts:
        if key in src:
            target_file = os.path.join('%s%s' % (base_path, private_dsts[key]), dir_name)
            if os.path.exists(target_file):
                remove_file(target_file)
            shutil.move(src, target_file)
            return True
    return False


def move_file(src_file, dst_folder, dst_file):
    if not os.path.exists(src_file):
        return

    target_file = os.path.join('%s%s' % (base_path, dst_folder), dst_file)
    if is_favor(src_file):
        target_file = os.path.join('%s%s' % (base_favor_path, dst_folder), dst_file)

    # print(target_file)
    if os.path.exists(target_file):
        remove_file(target_file)
    shutil.move(src_file, target_file)


def try_move_file(src_file, target_name):
    if not os.path.exists(src_file):
        return
    if str(src_file).__contains__("私拍"):
        if move_private_dir(src_file, target_name):
            return

    for key in dsts:
        if str(key).lower() in src_file.lower():
            move_file(src_file, dsts[key], target_name)


def remove_prefix(src):
    return str(src).replace('favor-', '') \
        .replace('f-1-', '') \
        .replace('f-2-', '') \
        .replace('f-3-', '') \
        .replace('f-4-', '') \
        .replace('f-5-', '')


def filing(src_folder):

    cal_base_path()

    for root, dirs, files in os.walk(src_folder):
        if root != src_folder:
            continue

        for file in files:
            try_move_file(os.path.join(root, file), file)
            garbage.delete_garbage_if_indeed(os.path.join(root, file))

        for folder in dirs:
            try_move_file(os.path.join(root, folder), folder)

            if re.match(xiuren_rex, remove_prefix(folder)):
                move_file(os.path.join(root, folder),
                          xiuren_folder, folder)

            if re.match(beautyleg_rex, remove_prefix(folder)):
                move_file(os.path.join(root, folder),
                          beautyleg_folder, folder)

            garbage.delete_garbage_if_indeed(os.path.join(root, folder))


filing(readed_folder)
