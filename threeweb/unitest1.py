import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr



class Testcase(unittest.TestCase):
    def test_01_login(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://10.18.11.113:8000/")
        element = driver.find_element(By.ID, "username")
        element.click()
        #driver.find_element(By.ID, "username").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("kS123456")
        driver.find_element(By.XPATH, "//form/button/span[1]").click()
        img = driver.find_element(By.XPATH, "//img[@data-inspector-line='237']")

        data = img.screenshot_as_png
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxx",data)

        ocr = ddddocr.DdddOcr()
        # 进行验证码识别
        text = ocr.classification(data)  # img_bytes=data 这是bytes数据传入时,但在pycharm 会冒黄，我也不清楚为啥
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxx",text)

    # if __name__ == '__main__':
#     print("###################################")
#     unittest.main()