"""import bs4
import requests
from selenium import webdriver
url = 'http://3proba.sitegist.net/uk/profile/?userid='
# user_id = 2000 # +++ пустий
# user_id = 7500 # +++ неТретьопробник / настя сурма
user_id = 1000 # +++ тількиСтупінь / Папірник
# user_id = 7304 # вПроцесі / садовий
# user_id = 7416 # +++ завершений / кубик


def get_check_write(object, selector):
    try:
        value = soup.select(selector)[0].getText()
        print(f'{object} = {value}')
    except IndexError:
        print(f'нема {object}')


page = requests.get(url + str(user_id))
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')

try:
    name = soup.select('div.profileBox > h3')[0].getText()
    print(user_id)
    print(name)

    get_check_write('датаВступу', 'div.panel-body > p:nth-child(1)')
    get_check_write('датаПрисяги', 'div.panel-body > p:nth-child(2)')
    get_check_write('датаІменуванняРозвідувачем', 'div.panel-body > p:nth-child(3)')
    get_check_write('часНаПробу', 'div.alert.alert-success')
    get_check_write('діловедення', 'div:nth-child(3) > div.panel-body')
    get_check_write('табори', 'div:nth-child(4) > div.panel-body')
    get_check_write('пересторогиТаВідзначення', 'div:nth-child(5) > div.panel-body')
    get_check_write('неТретьопробник', 'div.well > b')
    get_check_write('номерПроби', 'div.well > div > div.num')
    get_check_write('датаПроби', 'div.well > div > div.date')
    get_check_write('курінь', 'div.descriptionCol > h4')
    # get_check_write('станиця', '___')
    # get_check_write('округа', '___')

    vmilosti_string = ''
    vmilosti_element = soup.select('div.uservmilist > div')
    for x in vmilosti_element:
        vmilosti_string += x.getText() + ', '
    print(vmilosti_string.replace('\n', ''))


except IndexError:
    print(user_id)
    print('пуста сторінка')"""
"""
for x in range(5, 10):
    print(x)"""
"""id_list = []
id_file = open('id boys.txt', 'r')
for user_id in id_file:
    user_id = user_id.replace('\n', '')
    id_list.append(user_id)

id_file.close()

print(id_list)"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome(executable_path='/Users/ysenkiv/Code/chromedriver')
actions = ActionChains(browser)
browser.maximize_window()
browser.get('https://xkcd.com/')
actions.send_keys(Keys.COMMAND + 't')
actions.perform()
browser.get('https://ua.sinoptik.ua/')

