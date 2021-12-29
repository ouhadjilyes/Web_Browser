import sys
from PyQt5.QtCore import QUrl , QRect
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import QApplication, QDialog , QGridLayout , QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from demobrowser import *

class MyBrowser(QDialog):
    def __init__(self):
        super(MyBrowser, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Zed-Browser")

        # setup of the web browser
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(QRect(-1, 59, 881, 481))
        self.web_view.setUrl(QUrl("http://google.com"))
        self.web_view.setObjectName("web_browser")
        
        # back and forward buttons 
        self.forwardbutton = QtWidgets.QPushButton("forward")
        self.backbutton = QtWidgets.QPushButton("back")

        
    
    def initUi(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # setting up a layout
        lay = QGridLayout(central_widget)
        lay.addWidget(self.backbutton, 0, 0)
        lay.addWidget(self.forwardbutton, 0, 1)
        lay.addWidget(self.ui.lineEditURL, 0, 2)
        lay.addWidget(self.ui.pushButtonSearch, 0, 3)
        lay.addWidget(self.web_view, 1, 0, 1, 4)

        # actions 
        self.ui.pushButtonSearch.clicked.connect(self.browse)
        self.show()

    def browse(self):
        url = self.ui.lineEditURL.text()
        if not url.startswith("http"): url = "http://" + url
        self.ui.lineEditURL.setText(url)
        self.web_view.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyBrowser()
    w.show()
    sys.exit(app.exec_())