from selenium import webdriver
import time

username = "11710913"
pwd = "133617"

course = dict()
course['MAE203B'] = '//*[@id="div_201820193000006"]/a'
course['ME103'] =  '//*[@id="div_201820193000075"]/a'


bs = webdriver.Chrome()
# log in
url = 'https://jwxt.sustech.edu.cn/jsxsd/framework/xsMain.jsp'
bs.get(url)
account = bs.find_element_by_xpath('//*[@id="username"]')
account.send_keys(username)
password = bs.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd)
btn_login = bs.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]')
btn_login.click()
# 点击选课中心

btn1 = bs.find_element_by_xpath('/html/body/div[5]/a[1]/div')
btn1.click()
# 刷新进入选课
already = False
while not already:
    time.sleep(0.5)
    try:
        already = True
        btn2 = bs.find_element_by_xpath('//*[@id="tbKxkc"]/tbody/tr[2]/td[4]/a')
        btn2.click()

    except Exception:
        already = False
        bs.refresh()

btn3 = bs.find_element_by_xpath('/html/body/div[3]/div[2]/center/input')
btn3.click()

# course selecting
all = bs.window_handles
bs.switch_to.window(all[1])
btn4 = bs.find_element_by_xpath('//*[@id="topmenu"]/li[6]/a')
btn4.click()


bs.switch_to.frame("mainFrame")

for courseName in course.keys():
    # 切换iframe
    text_board = bs.find_element_by_xpath('//*[@id="kcxx"]')
    text_board.clear()
    text_board.send_keys(courseName)
    bs.find_element_by_xpath('/html/body/div[2]/input[5]').click()
    try:
        bs.implicitly_wait(20)
        btn = bs.find_element_by_xpath(course[courseName])
        btn.click()
        dig_alert = bs.switch_to.alert
        time.sleep(0.5)
        dig_alert.accept()
        dig_alert = bs.switch_to.alert
        time.sleep(0.5)
        dig_alert.accept()


    except Exception:
        print('error')
        print(Exception)

