import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MessagePeopleCardWidget(QWidget):
    clickedValue = pyqtSignal(int)  # special signal, str will be returned

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        self.clickedValue.emit(self.objectName())
        super().mousePressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Menu Widget Example")
        self.setGeometry(100, 100, 400, 300)

        # QToolButton oluşturma
        self.button = QToolButton(self)
        self.button.setText("Show Menu")

        # QMenu oluşturma
        self.peopleCardMenu = QMenu(self)

        self.peopleCardMenu.setStyleSheet("""
QMenu {background-color: #555555;}""")

        # Menü butona bağlama ve butonun altına açılmasını sağlama
        self.button.setMenu(self.peopleCardMenu)
        self.button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        # Butona tıklandığında menüyü belirli bir konumda açma
        self.button.clicked.connect(self.showMenu)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.getPeopleCard()


    def showMenu(self):
        # Menü, butonun altında açılacak şekilde konumlandırılır
        self.peopleCardMenu.exec(self.button.mapToGlobal(self.button.rect().bottomLeft()))
    
    def createPeopleCardWidget(self):
        self.widget_people_card_instance = MessagePeopleCardWidget()
        # self.widget_people_card_instance.setObjectName(u"widget_people_card_instance")
        self.widget_people_card_instance.setGeometry(QRect(80, 60, 226, 50))
        self.widget_people_card_instance.setMinimumSize(QSize(220, 50))
        self.widget_people_card_instance.setMaximumSize(QSize(16777215, 50))
        self.widget_people_card_instance.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: transparent;\n"
"	color: #f0f0f0;\n"
"}\n"
"\n"
"QWidget::hover {\n"
"	background-color: #808080;\n"
"	color: #f0f0f0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_people_card_instance)
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_people_card_profile_image_container = QWidget(self.widget_people_card_instance)
        # self.widget_people_card_profile_image_container.setObjectName(u"widget_people_card_profile_image_container")
        self.widget_people_card_profile_image_container.setMinimumSize(QSize(32, 32))
        self.widget_people_card_profile_image_container.setMaximumSize(QSize(32, 32))
        self.gridLayout = QGridLayout(self.widget_people_card_profile_image_container)
        # self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_people_card_profile_image = QLabel(self.widget_people_card_profile_image_container)
        # self.lbl_people_card_profile_image.setObjectName(u"lbl_people_card_profile_image")
        self.lbl_people_card_profile_image.setMinimumSize(QSize(30, 30))
        self.lbl_people_card_profile_image.setMaximumSize(QSize(30, 30))
        self.lbl_people_card_profile_image.setPixmap(QPixmap(u"C:/Users/Fevzi/Downloads/profile_3.png"))
        self.lbl_people_card_profile_image.setScaledContents(True)

        self.gridLayout.addWidget(self.lbl_people_card_profile_image, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_people_card_profile_image_container)

        self.widget_people_card_text_container = QWidget(self.widget_people_card_instance)
        # self.widget_people_card_text_container.setObjectName(u"widget_people_card_text_container")
        self.widget_people_card_text_container.setMinimumSize(QSize(170, 40))
        self.widget_people_card_text_container.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout = QVBoxLayout(self.widget_people_card_text_container)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_people_card_top_text = QLabel(self.widget_people_card_text_container)
        # self.lbl_people_card_top_text.setObjectName(u"lbl_people_card_top_text")
        self.lbl_people_card_top_text.setMinimumSize(QSize(150, 20))
        self.lbl_people_card_top_text.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lbl_people_card_top_text)

        self.lbl_people_card_bottom_text = QLabel(self.widget_people_card_text_container)
        # self.lbl_people_card_bottom_text.setObjectName(u"lbl_people_card_bottom_text")
        self.lbl_people_card_bottom_text.setMinimumSize(QSize(150, 20))
        self.lbl_people_card_bottom_text.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.lbl_people_card_bottom_text)


        self.horizontalLayout.addWidget(self.widget_people_card_text_container)

        return self.widget_people_card_instance
    
    def getPeopleCard(self):
        self.peopleCardMenu.clear()

        liste = [["Fevzi FİDAN", "111111 - Engineering Department - Embedded Systems"],
                 ["Hikmet ÇATAK", "222222 - Engineering Department - Data Science"],
                 ["Ömer Faruk AZİLİ", "333333 - Engineering Department - Web Development"]]

        # Dinamik olarak eklemek istediğiniz özel widget
        for i in range(3):  # Örnek olarak üç özel widget ekliyoruz
            custom_widget = self.createPeopleCardWidget()

            self.lbl_people_card_top_text.setText(liste[i][0])
            self.lbl_people_card_bottom_text.setText(liste[i][1])

            # QWidgetAction ile widget'ı menüye ekleme
            widget_action = QWidgetAction(self.peopleCardMenu)

            widget_action.setDefaultWidget(custom_widget)
            
            self.peopleCardMenu.addAction(widget_action)
            widget_action.setObjectName(liste[i][1][:liste[i][1].find(" ")])
            widget_action.triggered.connect(self.handleMessagePeopleCardClick)
            for i in widget_action.findChildren(QLabel):
                print(i.objectName())
    
    def handleMessagePeopleCardClick(self, value):
        print(self.sender().objectName())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
