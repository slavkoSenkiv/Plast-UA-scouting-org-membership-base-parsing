import requests, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
"""
url = 'https://plast.sitegist.net/?pageid=500&userid=324'
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
userName = soup.select('div .profileName')
if not userName:
    print('no user name found')
else:
    print(userName[0].getText())
"""
s = 1
mainUrl = 'https://plast.sitegist.net/'
browser = webdriver.Chrome(executable_path=r'/Users/ysenkiv/Code/chromedriver')
browser.get(mainUrl)
print(s)
s += 1
# loginButton = browser.find_element_by_link_text('Увійти')
loginButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'loginLink')))
print(s)
s += 1
loginButton.click()
print(s)
s += 1
# loginField = browser.find_element_by_name('f_login_email')
loginField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'f_login_email')))
print(s)
s += 1
browser.implicitly_wait(10)
print(s)
s += 1
ActionChains(browser).move_to_element(loginField).click(loginField).perform()
print(s)
s += 1
loginField.send_keys('slavko.senkiv@gmail.com')
print(s)
s += 1
# loginPass = browser.find_element_by_name('f_login_password')
loginPass = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'f_login_password')))
print(s)
s += 1
loginPass.send_keys('makeself')
print(s)
s += 1



# browser.get('https://plast.sitegist.net/?pageid=500&userid=324')


# try:
# userName = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'profileName')))
# userName = browser.find_element_by_class_name('profileName').text
# finally:
# browser.quit()

"""if not userName:
    print('found nothing')
else:
    print(userName)"""

