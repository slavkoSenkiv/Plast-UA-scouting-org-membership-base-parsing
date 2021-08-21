import bs4
import requests
import openpyxl

# <editor-fold desc="start code">


def get_check_write(selector, column):
    try:
        value = soup.select(selector)[0].getText()
        sheet.cell(row=row, column=column).value = value
    except IndexError:
        sheet.cell(row=row, column=column).value = 'нема'


wb = openpyxl.open('3 проба.xlsx')
sheet = wb.active
url = 'http://3proba.sitegist.net/uk/profile/?userid='

# </editor-fold>

user_id = 7430
while user_id <= 7440:
    for row in range(2, sheet.max_row):
        for x in range(1, 7440):

            page = requests.get(url + str(user_id))
            page.raise_for_status()
            soup = bs4.BeautifulSoup(page.text, 'html.parser')
            try:
                name = soup.select('div.profileBox > h3')[0].getText()

                # <editor-fold desc="не 3пробник">
                try:
                    if soup.select('div.well > b')[0].getText().startswith('Ти ще не третьопробник'):
                        sheet.cell(row=row, column=1).value = user_id
                        sheet.cell(row=row, column=2).value = name
                        sheet.cell(row=row, column=3).value = 'не 3пробник'
                except IndexError:
                    print('нема блоку "ще не третьопробник"')
                # </editor-fold>

                else:
                    name_text = name[0].getText()
                    print(name_text)
                    sheet.cell(row=x, column=1).value = str(user_id)
                    sheet.cell(row=x, column=2).value = name_text

            except IndexError:
                sheet.cell(row=row, column=1).value = user_id
                sheet.cell(row=row, column=2).value = 'пуста сторінка'

        user_id += 1

wb.save('3 проба.xlsx')


