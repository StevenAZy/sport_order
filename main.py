from selenium import webdriver

from badminton import login, order, time


if __name__ == '__main__':
    path = 'https://sports.sjtu.edu.cn/pc/#/'

    while True:
        driver = webdriver.Chrome()
        res = login(driver, path)
        while res:
            order_res = order(driver)
            if order_res:
                break
            else:
                time.sleep(1)
