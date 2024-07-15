# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 792)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignRight)

        self.locationInput = QLineEdit(self.centralwidget)
        self.locationInput.setObjectName(u"locationInput")
        self.locationInput.setMaximumSize(QSize(293, 16777215))

        self.horizontalLayout.addWidget(self.locationInput)

        self.locationSubmit = QPushButton(self.centralwidget)
        self.locationSubmit.setObjectName(u"locationSubmit")

        self.horizontalLayout.addWidget(self.locationSubmit, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.location = QLabel(self.centralwidget)
        self.location.setObjectName(u"location")
        self.location.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.location)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(25)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.sunrise = QLabel(self.centralwidget)
        self.sunrise.setObjectName(u"sunrise")

        self.gridLayout_2.addWidget(self.sunrise, 2, 1, 1, 1)

        self.latitude = QLabel(self.centralwidget)
        self.latitude.setObjectName(u"latitude")

        self.gridLayout_2.addWidget(self.latitude, 0, 1, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.sunset = QLabel(self.centralwidget)
        self.sunset.setObjectName(u"sunset")

        self.gridLayout_2.addWidget(self.sunset, 3, 1, 1, 1)

        self.longitude = QLabel(self.centralwidget)
        self.longitude.setObjectName(u"longitude")

        self.gridLayout_2.addWidget(self.longitude, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.description)

        self.dayornight = QLabel(self.centralwidget)
        self.dayornight.setObjectName(u"dayornight")
        self.dayornight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.dayornight)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(25)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.humidity = QLabel(self.centralwidget)
        self.humidity.setObjectName(u"humidity")

        self.gridLayout.addWidget(self.humidity, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.windspeed = QLabel(self.centralwidget)
        self.windspeed.setObjectName(u"windspeed")

        self.gridLayout.addWidget(self.windspeed, 8, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.feelslike = QLabel(self.centralwidget)
        self.feelslike.setObjectName(u"feelslike")

        self.gridLayout.addWidget(self.feelslike, 5, 1, 1, 1)

        self.temp = QLabel(self.centralwidget)
        self.temp.setObjectName(u"temp")

        self.gridLayout.addWidget(self.temp, 0, 1, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.maxtemp = QLabel(self.centralwidget)
        self.maxtemp.setObjectName(u"maxtemp")

        self.gridLayout.addWidget(self.maxtemp, 1, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.precip = QLabel(self.centralwidget)
        self.precip.setObjectName(u"precip")

        self.gridLayout.addWidget(self.precip, 6, 1, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.uvmax = QLabel(self.centralwidget)
        self.uvmax.setObjectName(u"uvmax")

        self.gridLayout.addWidget(self.uvmax, 3, 1, 1, 1)

        self.pressure = QLabel(self.centralwidget)
        self.pressure.setObjectName(u"pressure")

        self.gridLayout.addWidget(self.pressure, 7, 1, 1, 1)

        self.mintemp = QLabel(self.centralwidget)
        self.mintemp.setObjectName(u"mintemp")

        self.gridLayout.addWidget(self.mintemp, 2, 1, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 743, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.locationInput)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.locationInput.returnPressed.connect(self.locationSubmit.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Weather App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter a city:", None))
        self.locationSubmit.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.location.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Longitude:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Latitude:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sunrise:", None))
        self.sunrise.setText("")
        self.latitude.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sunset:", None))
        self.sunset.setText("")
        self.longitude.setText("")
        self.description.setText("")
        self.dayornight.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.humidity.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Feels like:", None))
        self.windspeed.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Temperature:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Maximum UV Index:", None))
        self.feelslike.setText("")
        self.temp.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.maxtemp.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Precipitation:", None))
        self.precip.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Wind Speed:", None))
        self.uvmax.setText("")
        self.pressure.setText("")
        self.mintemp.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Minimum Temperature:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Maximum Temperature:", None))
    # retranslateUi

