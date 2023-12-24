import pyautogui
import time
import cv2
import os
from PIL import Image
import concurrent.futures
import pytesseract
import threading
import find
import config
import numpy
import img2txt
import calu

def findapp():
    b = pyautogui.locateOnScreen('source/ji.png')
    if b:
        print("查找到app坐标:",b)
    else:
        print("屏幕上并没有找到app，你是不是没打开")
    return b

def drag(location):
    if location:
        # 获取该区域的左上角坐标和宽度、高度
        warp=config.warp
        left, top, width, height = location
        pyautogui.moveTo(left + 400, top + 950, duration=0.0)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(left + 400, top + 950-warp, duration=0.8)
        time.sleep(0.5)
        pyautogui.mouseUp(button='left')
    else:
        print("error")


def dec(location):
        j = 0 #三个技能之间的偏移量
        for i in range(3):

            screenshot = pyautogui.screenshot(region=(location.left+config.jiwarpx, location.top+config.jiwarpy+j, config.jilengx, config.jilengy))# 107   495            117  18
            # 获取当前时间戳
            value_screenshot = pyautogui.screenshot(region=(location.left + config.value_warpx, location.top + config.value_warpy + j, config.value_lex, config.value_ley))
            timestamp = int(time.time())

            # 生成临时文件夹路径 我为了让时间戳格式好看点写了这没屁用的东西 临时文件名谁看啊= =
            time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(timestamp))
            # 生成临时文件夹路径
            temp_folder = 'tempfile/'
            vale_folder='values/'
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
            file_name = f'技能截图{i+1}_{time_str}.png'
            file_path = os.path.join(temp_folder, file_name)
            # 截取屏幕并保存为临时文件
            screenshot.save(file_path)
            value_path=os.path.join(vale_folder,file_name)
            value_screenshot.save(value_path)

            j=j+config.ji3leng
#这里是保存到result中用于查看结果的示例文件
            # result_folder2 = 'result/'
            # if not os.path.exists(result_folder2):
            #     os.makedirs(result_folder2)
            # file_path2 = os.path.join(result_folder2, file_name)
            # screenshot.save(file_path2)




#这里是2023.10.11使用的多线程方式，为了加快识别速度并行，但是无法控制列表顺序。。。就改单线程了
# def recognize_text_from_image(image_path, result_queue):
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文语言模型
#     result_queue.put(text)
#
#
# def recognize_text_from_images(directory):
#     result_queue = queue.Queue()
#     threads = []
#     for filename in sorted(os.listdir(directory)):
#         if filename.endswith('.png') or filename.endswith('.jpg'):
#             image_path = os.path.join(directory, filename)
#             thread = threading.Thread(target=recognize_text_from_image, args=(image_path, result_queue))
#             thread.start()
#             threads.append(thread)
#     for thread in threads:
#         thread.join()
#     text_list = []
#     while not result_queue.empty():
#         text_list.append(result_queue.get())
#     return text_list

# 107   495            117  20
# 识别文字
def recognize_text_from_images(directory):
    text_list = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            grayscale_image = image.convert('L')
          #  bw_image = grayscale_image.point(lambda x: 0 if x < 110 else 255, '1')

          #  bw_image.save('result/rbw_image.png')#=======================================================

          #  text = pytesseract.image_to_string(bw_image, lang='chi_sim')  # 使用简体中文语言模型
            text = pytesseract.image_to_string(grayscale_image)
            text_list.append(text)
    cleaned_list = [text.strip() for text in text_list]
    return cleaned_list

def recognize_eng_from_images(directory):
    text_list = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
         #   grayscale_image = image.convert('L')
          #  bw_image = grayscale_image.point(lambda x: 0 if x < 127 else 255, '1')

           # bw_image.save('result/rbw_image.png')#=======================================================

            text = pytesseract.image_to_string(image)
           # text = pytesseract.image_to_string(grayscale_image)
            text_list.append(text)
    cleaned_list = [text.strip() for text in text_list]
    return cleaned_list

def get_text_from_pngs(path):
    text_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.png'):
                text = img2txt.get_text(os.path.join(root, file))
                text_list.append(text)
    return text_list




# 删除临时文件函数
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
               # print(f"已删除文件：{file_path}")
            except OSError as e:
                print(f"无法删除文件 {file_path}：{str(e)}")

def compare_to_stop(location):  #判断drag（）后技能栏是否到底的函数
    local_image = cv2.imread('source/machwhite.png')
    local_image2 = cv2.imread('source/machwhite2.png')
    current_region = pyautogui.screenshot(region=(location.left+config.comparex, location.top+config.comparey, 50, 25))  #查询config。py
    current_region.save('comparefile/machwhitetemp.png')   #临时文件
    now_image = cv2.imread('comparefile/machwhitetemp.png')
    # similarity = cv2.compareStructuralSimilarity(local_image, current_region, win_size=3)
    similarity_threshold = 0.5
    similarity = cv2.matchTemplate(local_image, now_image, cv2.TM_CCOEFF_NORMED)
    similarity2 = cv2.matchTemplate(local_image2, now_image, cv2.TM_CCOEFF_NORMED)
    if similarity < similarity_threshold and similarity2 < similarity_threshold:
        print('技能栏到底，停止识别', similarity,'sim2=',similarity2)
        return True
    else:
        print('技能栏没有到底，继续识别，sim=', similarity,'sim2=',similarity2)
        return False
    os.remove('comparefile/machwhitetemp.png')

def dec_bottom(location):
    j = 0  # 三个技能之间的偏移量
    if True:
        for i in range(2):

            screenshot = pyautogui.screenshot(region=(location.left + config.jiwarpx, location.top + config.jiwarpy +j+config.bottomwarp, config.jilengx,  config.jilengy))  # 107   495            117  18
            value_screenshot = pyautogui.screenshot(region=(location.left + config.value_warpx, location.top + config.value_warpy + j+config.bottomwarp, config.value_lex,config.value_ley))
            # 获取当前时间戳
            timestamp = int(time.time())

            # 生成临时文件夹路径 我为了让时间戳格式好看点写了这没屁用的东西 临时文件名谁看啊= =
            time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(timestamp))
            # 生成临时文件夹路径
            temp_folder = 'tempfile/'
            value_folder='values/'
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
            file_name = f'技能截图{i + 1}_{time_str}.png'
            file_path = os.path.join(temp_folder, file_name)
            # 截取屏幕并保存为临时文件
            screenshot.save(file_path)
            value_path = os.path.join(value_folder, file_name)
            value_screenshot.save(value_path)

            j = j + config.ji3leng

            # result_folder2 = 'result/'
            # if not os.path.exists(result_folder2):
            #     os.makedirs(result_folder2)
            # file_path2 = os.path.join(result_folder2, file_name)
            # screenshot.save(file_path2)


def getskillpoint(location):
    screenshot = pyautogui.screenshot(region=(location.left+config.skill_x, location.top+config.skill_y, config.jilengx/3.5,config.jilengy))  # 107   495            117  18
    skill_folder = 'skill/'
    if not os.path.exists(skill_folder):
        os.makedirs(skill_folder)
    screenshot.save('skill/skillpoint.png')
    point=recognize_eng_from_images('skill/')
    print(point)

    try:
        # 尝试将识别结果转换为整数
        int_result = int(point[0])
        print("识别技能点数:", int_result)
    except ValueError:
        # 如果转换失败（例如，识别结果不是数字字符串），则打印错误消息
        print("无法将识别结果转换为整数")
    return int_result






def start():
    tempfile_directory = 'tempfile/'
    tempvalue_directory = 'values/'
    tempskill_directory = 'skill/'
    tempcompare_directory = 'comparefile/'
    location = findapp()
    skilllist = []
    weightlist = []

    costlist = []
    delete_temp_png_files(tempfile_directory)  # 清除临时
    delete_temp_png_files(tempvalue_directory)
    delete_temp_png_files(tempskill_directory)
    delete_temp_png_files(tempcompare_directory)

    skillpoint = getskillpoint(location)  # 技能点识别

    for i in range(10):
        dec(location)
        text_list = get_text_from_pngs(tempfile_directory)
        cost = recognize_text_from_images(tempvalue_directory)

        print(text_list)
        print(cost)

        skilllist.extend(text_list)
        costlist.extend(cost)  #
        weight = find.find(text_list)
        weightlist.extend(weight)
        delete_temp_png_files(tempfile_directory)
        delete_temp_png_files(tempvalue_directory)
        drag(location)
        time.sleep(0.5)
        if compare_to_stop(location):
            dec_bottom(location)
            bottest_list = get_text_from_pngs(tempfile_directory)
            botvalue_list = recognize_text_from_images(tempvalue_directory)

            bottom_elements = bottest_list[:2]
            last_two_elements = text_list[-2:]
            setelem = []
            setvalue = []
            for element in bottom_elements:
                if element not in last_two_elements:
                    setelem.append(element)
            if len(setelem) == 1:
                costlist.extend(botvalue_list[:1])
            if len(setelem) == 2:
                costlist.extend(botvalue_list[:2])

            skilllist.extend(setelem)
            weightbot = find.find(setelem)
            weightlist.extend(weightbot)
            delete_temp_png_files(tempfile_directory)
            delete_temp_png_files(tempvalue_directory)
            break
        time.sleep(0.5)

    # 接下来要清洗识别数据，对三个列表的costlist中非数据的值进行去除

    new_costlist = [cost for cost in costlist if cost.isdigit()]
    new_weightlist = [weight * 100 for cost, weight in zip(costlist, weightlist) if cost.isdigit()]
    new_skilllist = [skill for cost, skill in zip(costlist, skilllist) if cost.isdigit()]
    new_costlist = [int(cost) for cost in new_costlist]

    # 最后使用背包算法进行计算
    calu.calu(new_skilllist, new_costlist, new_weightlist, skillpoint)

