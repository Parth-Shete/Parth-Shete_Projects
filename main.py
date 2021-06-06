import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  #* means import everything
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))  #This will appear in the center of the browser
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)  #This is a functionality of a back button
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)  #This is a functionality of a forward button
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)  #This is a functionality of a reload button
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)  #This will take us to the home page
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()  #Here we are editing in line line
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)  #Here we are changing the url in the search box too

    def navigate_home(self):  #This is for the reload button
        self.browser.setUrl(QUrl('http://google.com'))  #Here default home page is set up to google

    def navigate_to_url(self):
        url = self.url_bar.text()  #Here we are adding text in the search space
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):  #q is some parameter
        self.url_bar.setText(q.toString())  #Here we are converting the url in string format


app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
window = MainWindow()
app.exec_()