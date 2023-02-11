from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com")


ButtonElement = driver.find_element(By.XPATH, "(//*[@class='style-scope yt-chip-cloud-chip-renderer'])[3]")
ButtonElement.click()
serchFildElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME ,"search_query")))
serchFildElement.clear()
serchFildElement.send_keys("Emminem")
serchFildElement.send_keys(Keys.ENTER)
pleiButtonElement = driver.find_element(By.XPATH, "(//*[@class='yt-simple-endpoint style-scope ytd-video-renderer']) [1]")
pleiButtonElement.click()
time.sleep(5)


driver.close()
