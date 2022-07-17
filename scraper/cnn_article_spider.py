import sys
import os

from lxml import html, etree

# Get file from argv
if len(sys.argv) <= 1:
    raise Exception('Insuffecint arguments add a file path')
file_path = sys.argv[1]
#make sure file is an html
if os.path.exists(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext != '.html':
        raise Exception('Argument not an html file')
else: raise Exception('File does not exist!')



#strip all html except tags and hrefs
def strip_w_children(el):
	for key in el.keys():
		if key == 'class':
			if 'read-more' in el.attrib['class']:
				el.attrib.pop(key)
		else:
			el.attrib.pop(key)
	for child in el.getchildren():
		strip_w_children(child)

# xpath_body = "//div[@class='zn-body__paragraph']"

# xpath_body = "//div[contains(@class,'zn-body')]"
# xpath_meta = "//article[contains(@class, 'pg-rail-tall')]/meta"

xpath_body = "//div[contains(@class,'article')]"
xpath_meta = "//article[contains(@class, 'article_data')]"


author_class = 'metadata__byline__author'


print(f'parsing html file {file_path}')
page = html.parse(file_path)

meta_els = page.xpath(xpath_meta)
print(f'found {len(meta_els)} metadata for xpath {xpath_meta}')
els = page.xpath(xpath_body)
print(f'found {len(els)} for xpath {xpath_body}')

print('stripping elements')
for el in els:
	strip_w_children(el)

print('writing elements to file.html')
with open('file.html','w') as file:
	for el in els:
		file.write(etree.tostring(el, encoding='unicode', pretty_print=True))

