import requests, bs4

mainUrl = 'https://plast.sitegist.net/?pageid=500&userid=324'

mainRes = requests.get(mainUrl)
mainRes.raise_for_status()
mainSoup = bs4.BeautifulSoup(mainRes.text, 'html.parser')
userName = mainSoup.select('div.descriptionCol > div.profileName')
print(userName[0])
