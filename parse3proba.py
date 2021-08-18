import bs4
import requests
import openpyxl

wb = openpyxl.open('3 проба.xlsx')
sheet = wb.active
url = 'http://3proba.sitegist.net/uk/profile/?userid='
id = 7430
for x in range(2, sheet.max_row):
    while id < 7450:
        page = requests.get(url + str(id))
        page.raise_for_status()
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        name = soup.select('#main > div.padding > div > div > div.col-sm-5 > div.panel.panel-default.profileBox > h3')

        if not name:
            name_text = 'cant find name'
            print('cant find name')
            sheet.cell(row=x, column=1).value = name_text
        else:
            name_text = name[0].getText()
            print(name_text)
            sheet.cell(row=x, column=1).value = name_text

        id += 1

wb.save('3 проба.xlsx')


