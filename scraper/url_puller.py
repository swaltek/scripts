import re
import requests

regex = r'[a-z0-9\-]*(?=\/index.html)'

url_count = sum(1 for _ in open('urls.txt'))
cur_count = 1
with open('urls.txt', 'r') as file:
	for url in file:
		url = url.rstrip('\n')
		print(url)
		file_name = re.search(regex, url, flags=re.I).group()
		print(f"getting {cur_count} of {url_count} article '{file_name}'")
		page = requests.get(url)
		print(page)
		with open(f'html_files/{file_name}.html','w') as file:
			file.write(page.text)
		cur_count += 1

