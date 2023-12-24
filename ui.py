
from PySide2.QtWidgets import QApplication, QPushButton,QWidget, QPushButton, QVBoxLayout
import detect

# def say_hello():
#  print("Button clicked, Hello!")
#
# # Create the Qt Application
# app = QApplication(sys.argv)
# # Create a button, connect it and show it
# button = QPushButton("Click me")
# button.clicked.connect(say_hello)
# button.show()
# # Run the main Qt loop
# detect.start()
# app.exec_()


class MyApp(QWidget):
 def __init__(self):
  super().__init__()
  self.initUI()

 def initUI(self):
  # 创建布局和按钮
  layout = QVBoxLayout()
  self.button = QPushButton('Start', self)
  self.button.clicked.connect(self.start_function)  # 连接按钮点击信号到start_function方法
  layout.addWidget(self.button)
  self.setLayout(layout)
  self.resize(800, 600)

 def start_function(self):
   detect.start()  # 调用detect模块中的start()函数


app = QApplication([])
ex = MyApp()
ex.show()
app.exec_()