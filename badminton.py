import time

from captcha import captcha_extract
from config import user_text, passwd_text

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By


def login(driver, path):
    driver.get(path)
    login_button = driver.find_element(By.CLASS_NAME, 'el-button.el-button--primary')
    login_button.click()

    user = driver.find_element(By.ID, 'user')
    user.click()
    user.send_keys(user_text)

    passwd = driver.find_element(By.ID, 'pass')
    passwd.click()
    passwd.send_keys(passwd_text)

    captcha = driver.find_element(By.ID, 'captcha')
    captcha_img = driver.find_element(By.ID, 'captcha-img')
    captcha_res = captcha_extract(captcha_img.screenshot_as_base64)
    captcha_text = ''
    for r in captcha_res['words_result']:
        for i in r['words']:
            captcha_text = captcha_text + i

    captcha.click()
    captcha.send_keys(captcha_text)

    submit = driver.find_element(By.ID, 'submit-button')
    submit.click()
    
    try:
        submit = driver.find_element(By.ID, 'submit-button')
    except:
        return True
    
    return False

def order(driver):
    # 体育馆选择
    time.sleep(1)
    huoyingdong = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[4]/ul/li[6]/div/div/div[1]/img')
    huoyingdong.click()

    time.sleep(1)
    # 运动类型（羽毛球，篮球）
    # sport_type = driver.find_element(By.ID, 'tab-561d43a3-338e-4834-b35f-747bdc578366')
    # sport_type.click()

    # 运动时间
    time_now = datetime.now()
    current_time = (time_now + timedelta(days=7)).strftime("%Y-%m-%d")

    try:
        select_date = driver.find_element(By.ID, f'tab-{current_time}')
        select_date.click()
    except:
        return False
    time.sleep(1)

    # 场地选择   //*[@id="apointmentDetails"]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[10]/div[1]/div/div/img
    t = [10, 11]
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for x in p:
        for y in t:  
            ele_xpath = f'//*[@id="apointmentDetails"]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[{y}]/div[{x}]/div/div/img'
            place = driver.find_element(By.XPATH, ele_xpath)
            place.click()

        order = driver.find_element(By.XPATH, '//*[@id="apointmentDetails"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/button')
        order.click()
        time.sleep(1)

        try:
            agree = driver.find_element(By.XPATH, '//*[@id="apointmentDetails"]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/label/span[2]')
            agree.click()
            time.sleep(1)

            confirm = driver.find_element(By.XPATH, '//*[@id="apointmentDetails"]/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/button[2]')
            confirm.click()
            time.sleep(1)
        except:
            continue

        try:
            order = driver.find_element(By.XPATH, '//*[@id="apointmentDetails"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/button')
        except:
            return True
    
    return False