# 使用 requests/Selenium 模拟登录石墨文档 https://shimo.im

'''
    1. 通过webdriver唤起浏览器
    2. 进入石墨文档主页
    3. 模拟登陆
    4. 关闭浏览器
'''

# 导入相关包
from selenium import webdriver
import time

try:
    # 1.通过webdriver唤起浏览器
    browser = webdriver.Chrome()
    
    # 2.进入石墨文档主页
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    # 3.模拟登陆
    #键入账号和密码
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('13325666101')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('smwdhello521')
    time.sleep(1)
    browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
# 4.关闭浏览器
finally:
    pass