from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")

    def test_act(self):
        serchFildElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        serchFildElement.clear()
        serchFildElement.send_keys("BMW  ")
        serchFildElement.send_keys(Keys.ENTER)
        imgButtonElement = self.driver.find_element(By.XPATH, "(//*[@class='hdtb-mitem'])[1]")
        imgButtonElement.click()
        time.sleep(2)
        ButtonElement = self.driver.find_element(By.XPATH, "((//*[@class=' bRMDJf islir'])[1])")
        ButtonElement.click()
        time.sleep(5)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='tvh9oe BIB1wf']")
        except:
            print("Errors 5: Iamge not opened")
            exit(5)

    def tearDown(self):

        self.driver.close()

if __name__ == "__main__":
    unittest.main()
