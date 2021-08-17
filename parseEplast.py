import time
import openpyxl
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

# navigating to TA
time.sleep(2)
baseButton = browser.find_element_by_class_name('handbook')
baseButton.click()
usersButton = browser.find_element_by_link_text('Користувачі')
usersButton.click()
maleCheck = browser.find_element_by_name('sex-male')
maleCheck.click()
stanucjaField = browser.find_element_by_name('stanucja')
stanucjaField.send_keys('Львів')
time.sleep(1)
lvivButton = browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[4]/div/div[5]/div[2]/div[4]/span[1]')
lvivButton.click()
searchButton = browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[4]/div/div[8]/input')
searchButton.click()

# scrapping TA data
users_ids_list = []
usersList = browser.find_elements_by_class_name('user')
for user in usersList:
    user_id = user.get_attribute('joinobjid')
    users_ids_list.append(user_id)

names_list = []
for x in range(5):
    user_link = 'https://plast.sitegist.net/?pageid=500&userid=' + users_ids_list[x]
    browser.get(user_link)
    user_name = browser.find_element_by_class_name('profileName').text
    user_social = browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[5]/div[2]/a').get_attribute('href')
    user_kurin = browser.find_elements_by_class_name('simpleunit').text

print(names_list)













