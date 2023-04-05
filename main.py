import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSlider, QPushButton\
,QGroupBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt



class musicplayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 窗体
        self.icon_size = 60
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Music Player')
        self.setWindowIcon(QIcon('musicplayer.png'))

        # 整体布局
        alllayout = QVBoxLayout()
        self.setLayout(alllayout)

        #上布局
        uplayout = QHBoxLayout()
        self.setLayout(uplayout)

        label = QLabel(self)
        pixmap = QPixmap('播放.png')
        pixmap = pixmap.scaled(320, 240)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        uplayout.addWidget(label)

        # 中间布局
        middlelayout = QHBoxLayout()
        self.setLayout(middlelayout)
        self.timebar = QSlider(self)
        self.timebar.setOrientation(Qt.Orientation.Horizontal)
        middlelayout.addWidget(self.timebar)

        # 下布局
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # 按钮
        self.play_button = QPushButton(self.centralWidget)
        self.play_button.resize(self.icon_size, self.icon_size)
        self.play_button.setIcon(QIcon('播放.png'))
        self.play_button.setIconSize(QSize(self.icon_size, self.icon_size))


        self.pause_button = QPushButton(self.centralWidget)
        self.pause_button.resize(self.icon_size, self.icon_size)
        self.pause_button.setIcon(QIcon('暂停.png'))
        self.pause_button.setIconSize(QSize(self.icon_size, self.icon_size))


        self.stop_button = QPushButton(self.centralWidget)
        self.stop_button.resize(self.icon_size, self.icon_size)
        self.stop_button.setIcon(QIcon('停止.png'))
        self.stop_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.pre_button = QPushButton(self.centralWidget)
        self.pre_button.resize(self.icon_size, self.icon_size)
        self.pre_button.setIcon(QIcon('上一首.png'))
        self.pre_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.next_button = QPushButton(self.centralWidget)
        self.next_button.resize(self.icon_size, self.icon_size)
        self.next_button.setIcon(QIcon('下一首.png'))
        self.next_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.volume_button = QPushButton(self.centralWidget)
        self.volume_button.resize(30, 30)
        self.volume_button.setIcon(QIcon('音量.png'))
        self.volume_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.volume_bar = QSlider(self.centralWidget)
        # self.volume_bar.setOrientation(1)  # 设置为垂直方向
        self.volume_bar.setOrientation(Qt.Orientation.Vertical)
        self.volume_bar.setGeometry(10, 10, 20, 200)
        self.volume_bar.setRange(0, 100)  # 设置最大最小值
        self.volume_bar.setSliderPosition(50)  # 设置初始值 50
        self.volume_bar.setTickPosition(QSlider.TicksBothSides)  # 设置刻度位置在两侧


        self.shuffle_button = QPushButton(self.centralWidget)
        self.shuffle_button.resize(self.icon_size, self.icon_size)
        self.shuffle_button.setIcon(QIcon('随机.png'))
        self.shuffle_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.repeat_button = QPushButton(self.centralWidget)
        self.repeat_button.resize(self.icon_size, self.icon_size)
        self.repeat_button.setIcon(QIcon('重复.png'))
        self.repeat_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.songlist_play_button = QPushButton(self.centralWidget)
        self.songlist_play_button.resize(self.icon_size, self.icon_size)
        self.songlist_play_button.setIcon(QIcon('列表循环.png'))
        self.songlist_play_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.songlist_button = QPushButton(self.centralWidget)
        self.songlist_button.resize(self.icon_size, self.icon_size)
        self.songlist_button.setIcon(QIcon('歌单.png'))
        self.songlist_button.setIconSize(QSize(self.icon_size, self.icon_size))

        self.repeat_button.hide()
        self.songlist_play_button.hide()
        self.pause_button.hide()
        self.stop_button.hide()

        # 按钮分为左中右区域
        self.left_group_box = QGroupBox()
        left_button_area = QHBoxLayout()
        self.right_group_box = QGroupBox()
        right_button_area = QHBoxLayout()
        self.middle_group_box = QGroupBox()
        middle_button_area = QHBoxLayout()

        # 左侧添加按钮
        left_button_area.addWidget(self.songlist_button)
        left_button_area.addWidget(self.shuffle_button)
        left_button_area.addWidget(self.repeat_button)
        left_button_area.addWidget(self.songlist_play_button)
        self.left_group_box.setLayout(left_button_area)

        # 中间添加按钮
        middle_button_area.addWidget(self.pre_button)
        middle_button_area.addWidget(self.play_button)
        middle_button_area.addWidget(self.pause_button)
        middle_button_area.addWidget(self.stop_button)
        middle_button_area.addWidget(self.next_button)
        self.middle_group_box.setLayout(middle_button_area)

        # 右侧添加按钮
        right_button_area.addWidget(self.volume_button)
        right_button_area.addWidget(self.volume_bar)
        self.right_group_box.setLayout(right_button_area)

        # # 将左中右区域添加到主界面
        # main_layout = QVBoxLayout()
        downlayout = QHBoxLayout(self.centralWidget)
        downlayout.addWidget(self.left_group_box)
        downlayout.addWidget(self.middle_group_box)
        downlayout.addWidget(self.right_group_box)
        self.setLayout(downlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = musicplayer()
    mp.show()
    sys.exit(app.exec_())
