import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome(executable_path=r'/Users/ysenkiv/Code/chromedriver')

# entering main page
mainUrl = 'https://plast.sitegist.net/'
browser.get(mainUrl)
loginButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'loginLink')))
loginButton.click()
browser.implicitly_wait(10)
loginField = browser.find_element_by_name('f_login_email')
loginField.send_keys('slavko.senkiv@gmail.com')
loginPass = browser.find_element_by_name('f_login_password')
loginPass.send_keys('makeself')
enterButton = browser.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div[3]/input')
enterButton.click()
baseButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Довідники')))
# baseButton = browser.find_element_by_link_text('Довідники')
baseButton.click()








