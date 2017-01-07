# -*- coding: utf-8 -*-
########------------ 线性测试------------------
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.126.com")
# 登录
driver.find_element_by_css_selector("#idinput").clear()
driver.find_element_by_css_selector("#idinput").send_keys("username")
driver.find_element_by_css_selector("#pwdinput").clear()
driver.find_element_by_css_selector("#pwdinput").send_keys("password")
driver.find_element_by_css_selector("#loginBtn").click()

###收信、写信、删信等操作……
pass

#退出
driver.find_element_by_link_text("退出").click()
driver.quit()
########------------ 模块化测试------------------
##将登录登出，封装成类，组合成模块
from selenium import webdriver
class Log()
    def login(self, driver):
        driver.find_element_by_css_selector("#idinput").clear()
        driver.find_element_by_css_selector("#idinput").send_keys("user")
        driver.find_element_by_css_selector("#pwdinput").clear()
        driver.find_element_by_css_selector("#pwdinput").send_keys("pwd")
        driver.find_element_by_css_selector("#loginBtn").click()
    def logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()

## 在测试模块调用
from selenium import webdriver
from public_data import Login
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.126.com")
# 调用类和登录函数
Log().login(driver)
###收信、写信、删信等操作……
pass
# 调用类和登出函数
Log().logout(driver)


########------------ 参数化测试------------------
## 公共模块放置参数的入口
class Log()
    def login(self, driver,user,pwd):
        driver.find_element_by_css_selector("#idinput").clear()
        driver.find_element_by_css_selector("#idinput").send_keys(user)
        driver.find_element_by_css_selector("#pwdinput").clear()
        driver.find_element_by_css_selector("#pwdinput").send_keys(pwd)
        driver.find_element_by_css_selector("#loginBtn").click()
    def logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()
## 测试的模块，传入参数
from selenium import webdriver
from public_module import Login
class Test_log():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.126.com")
    def test_admin_login(self):  # admin登录测试
        username = "admin"
        passwprd = "123456"
        Log.login(self.driver,username,passwprd)
        Log.logout(self.driver)
    def test_guest_login(self):  # admin登录测试
        username = "guest"
        passwprd = "654321"
        Log.login(self.driver,username,passwprd)
        Log.logout(self.driver)
#实例化测试类，运行测试用例
Test_log.test_admin_login()
Test_log.test_guest_login()
