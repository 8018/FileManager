# coding:utf-8
import os
import shutil
import re
import garbage
import platform

# private_dsts = dict([('鱼子酱', '%s私拍/鱼子酱/' % photo_folder),
#                      ('阿朱', '%s私拍/阿朱/' % photo_folder),
#                      ('利世', '%s私拍/利世/' % photo_folder)])

# def move_private_dir(src, dir_name):
#     for key in private_dsts:
#         if key in src:
#             target_file = os.path.join('%s%s' % (base_path, private_dsts[key]), dir_name)
#             if os.path.exists(target_file):
#                 remove_file(target_file)
#             shutil.move(src, target_file)
#             return True
#     return False

xiuren_rex = '^[0-9]{4}.(((0[13578]|(10|12)).(0[1-9]|[1-2][0-9]|3[0-1]))|(02.(0[1-9]|[1-2][0-9]))|((0[469]|11).(0[1-9]|[1-2][0-9]|30))) (No|NO|Vol|VOL).[0-9]\d* [\u4e00-\u9fa5]{1,}'
beautyleg_rex = '^[0-9]{4}.(((0[13578]|(10|12)).(0[1-9]|[1-2][0-9]|3[0-1]))|(02.(0[1-9]|[1-2][0-9]))|((0[469]|11).(0[1-9]|[1-2][0-9]|30))) No.[1-9]\d* [a-zA-Z]{1,}'

base_path = '/Users/michaelliu/Downloads'
base_favor_path = '/Users/michaelliu/Downloads/favor'
readed_folder = '/Users/michaelliu/Downloads/readed/'
photo_folder = '/写真/'
# xiuren_folder = '/写真/秀人/秀人'
beautyleg_folder = '/写真/Beautyleg'
av_folder = '/你懂的'

dsts = dict([('Yeeun', '%sothers/Son Ye-Eun/' % photo_folder),
             ('Ye-Eun', '%sothers/Son Ye-Eun/' % photo_folder),
             ('ArtGravia', '%sArtGravia/' % photo_folder),
             ('JVID', '%sJVID/' % photo_folder),
             ('X-City', '%s日本/' % photo_folder),
             ('尤果网', '%sUgirls/' % photo_folder),
             ('Ugirls', '%sUgirls/' % photo_folder),
             ('李娇', '%sLIJIAO李娇/' % photo_folder),
             ('LIJIAO', '%sLIJIAO李娇/' % photo_folder),
             ('beautyleg', '%sBeautyleg/' % photo_folder),
             ('[Be]', '%sBeautyleg/' % photo_folder),
             ('AI', '%sAI/' % photo_folder),

             ('年年', '%sModel/年年/' % photo_folder),
             ('阿朱', '%sModel/阿朱/' % photo_folder),
             ('艺轩', '%sModel/艺轩/' % photo_folder),
             ('奶瓶', '%sModel/奶瓶/' % photo_folder),
             ('利世', '%sModel/利世/' % photo_folder),
             ('凯竹', '%sModel/凯竹/' % photo_folder),
             ('廿十', '%sModel/凯竹/' % photo_folder),
             ('安然', '%sModel/安然/' % photo_folder),
             ('王馨瑶', '%sModel/王馨瑶/' % photo_folder),
             ('冯木木', '%sModel/冯木木/' % photo_folder),
             ('林星阑', '%sModel/林星阑/' % photo_folder),
             ('夏诗诗', '%sModel/夏诗诗/' % photo_folder),
             ('夏诗雯', '%sModel/夏诗诗/' % photo_folder),
             ('夏羲瑶', '%sModel/夏羲瑶/' % photo_folder),

             ('小热巴', '%sModel/小热巴/' % photo_folder),
             ('喜欢猫', '%sModel/小热巴/' % photo_folder),
             ('杨晨晨', '%sModel/杨晨晨/' % photo_folder),
             ('小狐狸', '%sModel/小狐狸/' % photo_folder),
             ('鱼子酱', '%sModel/鱼子酱/' % photo_folder),
             ('何嘉颖', '%sModel/何嘉颖/' % photo_folder),
             ('程程程', '%sModel/程程程/' % photo_folder),
             ('顾乔楠', '%sModel/顾乔楠/' % photo_folder),
             ('萌琪琪', '%sModel/萌琪琪/' % photo_folder),
             ('唐安琪', '%sModel/唐安琪/' % photo_folder),
             ('陆萱萱', '%sModel/陆萱萱/' % photo_folder),
             ('苏苏阿', '%sModel/苏苏阿/' % photo_folder),
             ('梦心玥', '%sModel/梦心玥/' % photo_folder),
             ('刘奕宁', '%sModel/刘奕宁/' % photo_folder),
             ('黄楽然', '%sModel/黄楽然/' % photo_folder),
             ('林子欣', '%sModel/林子欣/' % photo_folder),
             ('梦心月', '%sModel/梦心玥/' % photo_folder),
             ('刘飞儿', '%sModel/刘飞儿/' % photo_folder),
             ('朱可儿', '%sModel/朱可儿/' % photo_folder),
             ('小子怡', '%sModel/杨紫嫣/' % photo_folder),
             ('杨紫嫣', '%sModel/杨紫嫣/' % photo_folder),
             ('尹甜甜', '%sModel/尹甜甜/' % photo_folder),
             ('王雨纯', '%sModel/王雨纯/' % photo_folder),
             ('谢小蒽', '%sModel/谢小蒽/' % photo_folder),
             ('王心怡', '%sModel/王心怡/' % photo_folder),
             ('77qiq', '%sModel/77qiq/' % photo_folder),
             ('小甜心CC', '%sModel/杨晨晨/' % photo_folder),
             ('NianNian', '%sModel/年年/' % photo_folder),
             ('小夕juju', '%sModel/王心怡/' % photo_folder),
             ('Angela00', '%sModel/小热巴/' % photo_folder),
             ('安琪Yee', '%sModel/安琪 Yee/' % photo_folder),
             ('Miko酱吖', '%sModel/Miko酱吖/' % photo_folder),
             ('安琪 Yee', '%sModel/安琪 Yee/' % photo_folder),
             ('一颗甜蛋黄', '%sModel/一颗甜蛋黄/' % photo_folder),

             ('阿姣', '%s秀人/阿姣/' % photo_folder),
             ('可乐', '%s秀人/可乐/' % photo_folder),
             ('曉慧', '%s秀人/筱慧/' % photo_folder),
             ('筱慧', '%s秀人/筱慧/' % photo_folder),
             ('菲儿', '%s秀人/菲儿/' % photo_folder),
             ('米娜', '%s秀人/米娜/' % photo_folder),
             ('美七', '%s秀人/美七/' % photo_folder),
             ('娜比', '%s秀人/娜比/' % photo_folder),
             ('猩一', '%s秀人/猩一/' % photo_folder),
             ('甜仔', '%s秀人/甜仔/' % photo_folder),
             ('诗诗', '%s秀人/诗诗/' % photo_folder),
             ('大熙', '%s秀人/大熙/' % photo_folder),
             ('大蜜', '%s秀人/大蜜/' % photo_folder),
             ('沐夕', '%s秀人/沐夕/' % photo_folder),
             ('芝芝', '%s秀人/徐莉芝/' % photo_folder),
             ('林子遥', '%s秀人/林子遥/' % photo_folder),
             ('慕羽茜', '%s秀人/慕羽茜/' % photo_folder),
             ('薇薇酱', '%s秀人/薇薇酱/' % photo_folder),
             ('媛媛酱', '%s秀人/媛媛酱/' % photo_folder),
             ('周妍希', '%s秀人/周妍希/' % photo_folder),
             ('夏沫沫', '%s秀人/夏沫沫/' % photo_folder),
             ('星子柒', '%s秀人/星子柒/' % photo_folder),
             ('韩静安', '%s秀人/韩静安/' % photo_folder),
             ('绮里嘉', '%s秀人/绮里嘉/' % photo_folder),
             ('乔一一', '%s秀人/乔一一/' % photo_folder),
             ('白茹雪', '%s秀人/白茹雪/' % photo_folder),
             ('小海臀', '%s秀人/小海臀/' % photo_folder),
             ('桃桃子', '%s秀人/桃桃子/' % photo_folder),
             ('熊小诺', '%s秀人/熊小诺/' % photo_folder),
             ('月音瞳', '%s秀人/月音瞳/' % photo_folder),
             ('佘贝拉', '%s秀人/佘贝拉/' % photo_folder),
             ('玥儿玥', '%s秀人/玥儿玥/' % photo_folder),
             ('潘娇娇', '%s秀人/潘娇娇/' % photo_folder),
             ('徐莉芝', '%s秀人/徐莉芝/' % photo_folder),
             ('张欣欣', '%s秀人/张欣欣/' % photo_folder),
             ('豆瓣酱', '%s秀人/豆瓣酱/' % photo_folder),
             ('萌汉药', '%s秀人/萌汉药/' % photo_folder),
             ('婠婠么', '%s秀人/婠婠么/' % photo_folder),
             ('沈梦瑶', '%s秀人/沈梦瑶/' % photo_folder),
             ('林乐一', '%s秀人/林乐一/' % photo_folder),
             ('吴雪瑶', '%s秀人/吴雪瑶/' % photo_folder),
             ('薛琪琪', '%s秀人/薛琪琪/' % photo_folder),
             ('周慕汐', '%s秀人/周慕汐/' % photo_folder),
             ('周于希', '%s秀人/周于希/' % photo_folder),
             ('方子萱', '%s秀人/方子萱/' % photo_folder),
             ('尤妮丝', '%s秀人/尤妮丝/' % photo_folder),
             ('圆圆酱', '%s秀人/圆圆酱/' % photo_folder),
             ('小九月', '%s秀人/小九月/' % photo_folder),
             ('金静熙', '%s秀人/金静熙/' % photo_folder),
             ('蜜桃酱', '%s秀人/蜜桃酱/' % photo_folder),
             ('文静儿', '%s秀人/文静儿/' % photo_folder),
             ('糯米NM', '%s秀人/糯米NM/' % photo_folder),
             ('Miki兔', '%s秀人/Miki兔/' % photo_folder),
             ('孙梦瑶V', '%s秀人/孙梦瑶V/' % photo_folder),
             ('蜜桃酱o', '%s秀人/蜜桃酱o/' % photo_folder),
             ('Savina', '%s秀人/Savina/' % photo_folder),
             ('仓井优香', '%s秀人/仓井优香/' % photo_folder),
             ('人间荒糖', '%s秀人/人间荒糖/' % photo_folder),
             ('是小逗逗', '%s秀人/是小逗逗/' % photo_folder),
             ('模特合集', '%s秀人/模特合集/' % photo_folder),
             ('小果冻儿', '%s秀人/小果冻儿/' % photo_folder),
             ('大美媚京', '%s秀人/大美媚京/' % photo_folder),
             ('宋-KiKi', '%s秀人/宋-KiKi/' % photo_folder),
             ('夏西CiCi', '%s秀人/夏西CiCi/' % photo_folder),
             ('Vanessa', '%s秀人/Vanessa/' % photo_folder),
             ('郑颖姗Bev', '%s秀人/郑颖姗Bev/' % photo_folder),
             ('晗大大Via', '%s秀人/晗大大Via/' % photo_folder),
             ('心妍小公主', '%s秀人/心妍小公主/' % photo_folder),
             ('瑶啊摇的瑶', '%s秀人/瑶啊摇的瑶/' % photo_folder),
             ('良人非爱人', '%s秀人/良人非爱人/' % photo_folder),
             ('绯月樱', '%s秀人/绯月樱-Cherry/' % photo_folder),
             ('luna张静燕', '%s秀人/luna张静燕/' % photo_folder),
             ('娜露Selena', '%s秀人/娜露Selena/' % photo_folder),
             ('楚恬Olivia', '%s秀人/楚恬Olivia/' % photo_folder),
             ('蓝夏Akasha', '%s秀人/蓝夏Akasha/' % photo_folder),
             ('Emily顾奈奈', '%s秀人/Emily顾奈奈/' % photo_folder),
             ('周jojobaby', '%s秀人/周jojobaby/' % photo_folder),
             ('谢芷馨Sindy', '%s秀人/谢芷馨Sindy/' % photo_folder),
             ('林文文yooki', '%s秀人/林文文yooki/' % photo_folder),
             ('许诺Sabrina', '%s秀人/许诺Sabrina/' % photo_folder),
             ('果儿Victoria', '%s秀人/果儿Victoria/' % photo_folder),

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
             ('森日菜子', '%s/日本/' % av_folder),
             ('希岛爱理', '%s/日本/' % av_folder),
             ('七森莉莉', '%s/日本/' % av_folder),
             ('岬奈奈美', '%s/日本/' % av_folder),
             ('武藤绫香', '%s/日本/' % av_folder),
             ('神菜美舞', '%s/日本/' % av_folder),
             ('葵司', '%s/日本/' % av_folder),
             ('九色', '%s/中国/91/' % av_folder),
             ('91', '%s/中国/91/' % av_folder),
             ('中国', '%s/中国/' % av_folder),
             ('[3D]', '%s情色/彩漫/' % photo_folder),
             ('脸红Dearie', '%s情色/脸红Dearie/' % photo_folder),
             ('果哥', '%s/中国/果哥/' % av_folder)
             ])


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
    # if str(src_file).__contains__("私拍"):
    #     if move_private_dir(src_file, target_name):
    #         return

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


def filing():
    cal_base_path()

    for root, dirs, files in os.walk(readed_folder):
        if root != readed_folder:
            continue

        for file in files:
            try_move_file(os.path.join(root, file), file)
            garbage.delete_garbage_if_indeed(os.path.join(root, file))

        for folder in dirs:
            print(folder)
            try_move_file(os.path.join(root, folder), folder)

            # if re.match(xiuren_rex, remove_prefix(folder)):
            #     move_file(os.path.join(root, folder),
            #               xiuren_folder, folder)

            if re.match(beautyleg_rex, remove_prefix(folder)):
                move_file(os.path.join(root, folder),
                          beautyleg_folder, folder)

            garbage.delete_garbage_if_indeed(os.path.join(root, folder))


filing()
