# -*- coding: utf8 -*-
import itchat
import math
import PIL.Image as Image
import os

# 扫码登录微信
itchat.auto_login()
# 好友列表
friends = itchat.get_friends(update=True)[0:]
# 本人
user = friends[0]["UserName"]

num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])   # 获取头像图片
    fileImage = open("D:/PycharmProjects/WeChat/pic" + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

ls = os.listdir("D:/PycharmProjects/WeChat/pic")
each_size = int(math.sqrt(float(640*640)/len(ls)))   # 每幅图片的边长像素大小
lines = int(640/each_size)      # 每一行图片的数量
image = Image.new('RGB', (640, 640))
x = 0
y = 0

for i in range(0,len(ls)+1):
    try:
        img = Image.open("D:/PycharmProjects/WeChat/pic" + "/" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        # 将每张图片大小变更为 each_size * each_size 像素
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        # 以(x * each_size, y * each_size)为起点粘贴图片
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        # 换行
        if x == lines:
            x = 0
            y += 1

image.save("D:/PycharmProjects/WeChat/pic" + "/" + "all.jpg")
itchat.send_image("D:/PycharmProjects/WeChat/pic" + "/" + "all.jpg", 'filehelper')
