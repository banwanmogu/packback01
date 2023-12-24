import pyautogui
import time
import cv2
import os
import config
import pytesseract
from PIL import Image
import calu

def testmouse():
    time.sleep(2)
    x, y = pyautogui.position()
    print('鼠标当前位置：', x, y)
    return x,y

def delete_temp_png_files(directory):
    # 确保目录路径是有效的
    if not os.path.exists(directory):
        print(f"目录 '{directory}' 不存在。")
        return
        # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否是临时PNG文件（以.png结尾，并且名称中包含'temp'）
        if filename.endswith('.png'):
            # 构造完整的文件路径
            file_path = os.path.join(directory, filename)
            # 删除文件
            try:
                os.remove(file_path)
                print(f"已删除文件：{file_path}")
            except OSError as e:
                print(f"无法删除文件 {file_path}：{str(e)}")

def teststop():
    local_image = cv2.imread('source/machwhite.png')
    local_image2 = cv2.imread('source/machwhite2.png')
    current_screenshot = pyautogui.screenshot()
    current_region = current_screenshot.crop(
        (config.comparex, config.comparey, config.comparex + 50, config.comparey + 25))  # 查询config。py
    current_region.save('tempfile/machwhitetemp.png')
    now_image=cv2.imread('tempfile/machwhitetemp.png')
    #similarity = cv2.compareStructuralSimilarity(local_image, current_region, win_size=3)
    similarity_threshold = 0.9
    similarity =cv2.matchTemplate(local_image, now_image, cv2.TM_CCOEFF_NORMED)
    similarity2 = cv2.matchTemplate(local_image2, now_image, cv2.TM_CCOEFF_NORMED)
    if similarity < similarity_threshold and similarity2 < similarity_threshold:
        print('not mach,sim=',similarity,'sim2=',similarity2)
    else:
        print('mach,sim=',similarity,'sim2=',similarity2)



def grayscale(image_path):


    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    grayscale_image.save('comparefile/gray.png')

    bw_image = grayscale_image.point(lambda x: 0 if x < 90 else 255, '1')
    bw_image.save('comparefile/two.png')

def getji():
    time.sleep(1)
    b = pyautogui.locateOnScreen('source/ji.png')
    if b:
        print("查找到app坐标:", b)
    else:
        print("屏幕上并没有找到app，你是不是没打开")
    return b

#uni.gettext('tempfile/技能截图1_20231014_173944.png')

    # image = cv2.imread()
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度化
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # 二值化


# jipoint=getji()
# x,y=testmouse()
# print('dec=',x-jipoint.left, y-jipoint.top)




# 1628 538 1634 681    1633 721 2048 765  2119 804
# teststop()
# tempfile_directory = 'tempfile/'
# delete_temp_png_files(tempfile_directory)
# current_screenshot = pyautogui.screenshot()
# current_region = current_screenshot.crop((2100, 1000, 2100+50, 1000+25))#查找到app坐标: Box(left=1552, top=64, width=25, height=27)
# current_region.save('source/machwhite2.png')

# zuoshang 1473 598 youjia 1590 616
#jineng 1366 103
# 107   495            117  18



#1392 624  1394 797
#warp: 1 1353 563  2  1354 1118  =555

#mouse :2169 1014右下角灰色位置  1555 68 左上角技位置

# skilllist = ['胜利的鼓动', '中山赛场○', '良场地○', '阴天○', '彻底盯紧○', '弯道加速○', '圆孤弧艺术家', '弯道恢复○', '钢铁意志', '隐身衣', '加快步伐', '准备突围', '逼近', '加快速度', '大胃王', '营养补给', '重振旗鼓']
# costlist = ['BRE', '81', '54', '90', '72', 'BRE', '323', '170', '304', '160', 'BRE', '162', '104', '160', 'CRE', 'BRE', 'BRE']
# weightlist = [0.0, 1.43, 1.43, 1.43, 1.43, 1.21, 1.49, 1.28, 1.59, 1.36, 1.28, 1.21, 1.36, 1.36, 1.41, 1.21, 1.81]
#
# new_costlist = []
# new_weightlist = []
# new_skilllist = []
#
# new_costlist = [cost for cost in costlist if cost.isdigit()]
# new_weightlist = [weight for cost, weight in zip(costlist, weightlist) if cost.isdigit()]
# new_skilllist = [skill for cost, skill in zip(costlist, skilllist) if cost.isdigit()]
# new_costlist = [int(cost) for cost in new_costlist]
#
# print("New costlist:", new_costlist)
# print("New weightlist:", new_weightlist)
# print("New skilllist:", new_skilllist)
# skillpoint=1000
# calu.calu(new_skilllist,new_costlist,new_weightlist,skillpoint)

