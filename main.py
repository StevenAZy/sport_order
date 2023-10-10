from selenium import webdriver

from badminton import login, order, time


if __name__ == '__main__':
    path = 'https://sports.sjtu.edu.cn/pc/#/'
    driver = webdriver.Chrome()

    while True:
        res = login(driver, path)
        if res:
            order_res = order(driver)
            if order_res:
                break
            else:
                time.sleep(1)
        else:
            time.sleep(1)
