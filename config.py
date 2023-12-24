#在此进行配置
#source/machwhite 用于判断循环比较的文件
import pyautogui


zeropoint = pyautogui.locateOnScreen('source/ji.png')
czpoint=pyautogui.locateOnScreen('source/zhi.png')


nowx=(czpoint.left-zeropoint.left)/596  #实际分辨率下的x方向长度
nowy=(czpoint.top-zeropoint.top ) /1054    #实际分辨率下的y方向长度

#Size(width=2560, height=1440) 的分辨率下，-596 -1054，所以获取当前分辨率，乘上
warp=550*nowy #技能栏上下偏移高度
jiwarpx=107*nowx
jiwarpy=488*nowy #技字到截图初始点的warp
jilengx=400*nowx
jilengy=40*nowy   #技能截图的长和宽
ji3leng=178*nowy   #三个技能之间偏移量

comparex=531*nowx
comparey=945*nowy   #bijiao

bottomwarp=130*nowy   #底段多出的距离


value_warpx=522*nowx
value_warpy=532*nowy

value_lex=71*nowx+6
value_ley=39*nowy

skill_x=500*nowx
skill_y=390*nowy

