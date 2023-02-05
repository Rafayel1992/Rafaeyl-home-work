from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class mayTestYourube(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.youtube.com")

    def test_testYoutube(self):
        ButtonElement = self.driver.find_element(By.XPATH, "(//*[@class='style-scope yt-chip-cloud-chip-renderer'])[3]")
        ButtonElement.click()
        serchFildElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME ,"search_query")))
        serchFildElement.clear()
        serchFildElement.send_keys("Emminem")
        serchFildElement.send_keys(Keys.ENTER)
        pleiButtonElement = self.driver.find_element(By.XPATH, "(//*[@class='yt-simple-endpoint style-scope ytd-video-renderer']) [1]")
        pleiButtonElement.click()
        time.sleep(5)
        
    

if __name__ == "__main__":
    unittest.main()
