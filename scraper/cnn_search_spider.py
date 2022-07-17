from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

search_term = 'covid'
url = f'https://www.cnn.com/search?q={search_term}&size=50'

#gets us path to anchor with href to article
x_path = "//div[contains(@class, 'cnn-search')]//a"

options = Options()
options.add_argument("--headless")
print("setting webdriver")
driver = webdriver.Firefox(options=options)
print("getting url")
driver.get(url)

print("getting page content")
els = driver.find_elements(By.XPATH, x_path)

print("writing elements found")

url_list = []
for el in set(els):
	href_att = el.get_attribute('href')
	if href_att.endswith('index.html'):
		url_list.append(href_att)

with open('urls.txt', 'w') as file:
	for url in url_list:
		file.write(f'{url}\n')

driver.close()

