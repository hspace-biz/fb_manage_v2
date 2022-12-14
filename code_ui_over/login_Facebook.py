from code_ui_raw.login_Facebook import Ui_Login_Facebook
from main_utils.api import call_api
from main_utils.driver import init_Chrome_Driver
from PyQt6.QtWidgets import  QMessageBox
from PyQt6.QtGui import QAction
import pyperclip
from PyQt6.QtCore import QThread

class Thr(QThread):
    def __init__(self, fun):
        super().__init__()
        self.fun = fun
    def run(self):
        self.fun()
        
class Ui_Login_Facebook_Over(Ui_Login_Facebook):
    
    def set_info_login(self,proxy,cookies,name,uid,ip):
        self.proxy = proxy
        self.cookies = cookies
        self.name = name
        self.uid = uid
        self.ip = ip
        
    def setupUi(self, widget):
        super().setupUi(widget)
        self.widget = widget
        
        self.driver = None    
        self.label_ip.setText(self.ip)
        self.label_name.setText(self.name)
        self.label_uid.setText(self.uid)
        
        copy_ip_action = QAction(self.widget)
        copy_ip_action.setStatusTip("This is your button")
        copy_ip_action.triggered.connect(self.copy_ip)
        
        self.label_ip.mousePressEvent =self.copy_ip
        self.label_uid.mousePressEvent =self.copy_uid
        self.label_name.mousePressEvent =self.copy_name
        
        self.pushButton_login.clicked.connect(lambda x: self.login())
        self.pushButton_update.clicked.connect(lambda x: self.update_cookie())
    
    def copy_ip(self,*arg, **kwargs):
        pyperclip.copy(self.label_ip.text())
        
        font = self.label_uid.font()
        font.setBold(False)
        self.label_uid.setFont(font)
        
        font = self.label_ip.font()
        font.setBold(True)
        self.label_ip.setFont(font)
        
        
        font = self.label_name.font()
        font.setBold(False)
        self.label_name.setFont(font)
        
    
    def copy_uid(self,*arg, **kwargs):
        pyperclip.copy(self.label_uid.text())
        
        font = self.label_uid.font()
        font.setBold(True)
        self.label_uid.setFont(font)
        
        font = self.label_ip.font()
        font.setBold(False)
        self.label_ip.setFont(font)
        
        
        font = self.label_name.font()
        font.setBold(False)
        self.label_name.setFont(font)
        
        
    def copy_name(self,*arg, **kwargs):
        pyperclip.copy(self.label_name.text())
        font = self.label_uid.font()
        font.setBold(False)
        self.label_uid.setFont(font)
        
        font = self.label_ip.font()
        font.setBold(False)
        self.label_ip.setFont(font)
        
        
        font = self.label_name.font()
        font.setBold(True)
        self.label_name.setFont(font)
        
        
    def update_cookie(self):
        if self.driver is None or len(self.driver.window_handles)<=0:
            return
        
        cookies = self.driver.get_cookies()
        cookie = {}
        for _cookie in cookies:
            if _cookie['name']=="xs":
                cookie["xs"] =  _cookie['value']
                
            if _cookie['name']=="sb":
                cookie["sb"] =  _cookie['value']
                
            if _cookie['name']=="c_user":
                cookie["c_user"] =  _cookie['value']
                
        if not all([cookie.get("xs"),cookie.get("sb"),cookie.get("c_user")]) :
            dialog = QMessageBox(parent=self.widget, text=f"Cookie not correct.")
            dialog.setWindowTitle("Proxy")
            ret = dialog.exec() 
            return
        
        
        res = call_api(method="put",api="insert_cookie_for_master_user",
            data={
                "cookies":cookie,
                "proxy":self.proxy,
                "is_update":True,
                "upsert":True
            }
        )
        if res.status_code == 200:
            dialog = QMessageBox(parent=self.widget, text=f"Update cookie successfull.")
            dialog.setWindowTitle("Cookies")
            ret = dialog.exec() 
            for _cookie in self.cookies:
                if _cookie['name']=="xs":
                    _cookie["value"] =  cookie['xs']
                
                if _cookie['name']=="sb":
                    _cookie["value"] =  cookie['sb']
                
                if _cookie['name']=="c_user":
                    _cookie["value"] =  cookie['c_user']
                    
            return
        
        dialog = QMessageBox(parent=self.widget, text=f"Update cookie failed: {res.status_code}-{res.text}.")
        dialog.setWindowTitle("Cookies")
        ret = dialog.exec() 
        
    
    def login(self):
        self.thr_login = Thr(self._login)
        self.thr_login.start()
    def _login(self):
        self.driver,msg = init_Chrome_Driver(proxy_user_name=self.proxy["user_name"],proxy_password=self.proxy["password"],proxy_ip=self.proxy["ip"],proxy_port=self.proxy["port"])
        if self.driver is None:
            dialog = QMessageBox(parent=self.widget, text=msg)
            dialog.setWindowTitle("Error")
            ret = dialog.exec() 
            return
        
        self.driver.get("https://www.facebook.com")
        
        for cookie in self.cookies:
            self.driver.add_cookie(
                {"name": cookie.get("name"), "value": cookie.get("value"), "domain": ".facebook.com"})
            
        self.driver.get("https://www.facebook.com")
    
        