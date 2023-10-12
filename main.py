# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup 
from bs4.diagnose import diagnose

file_name = 'test.html'
new_file_name = "new.html"
input_text = "Hello there"
HTML_PATH = "HTML/{}"

HTMLFile = open(HTML_PATH.format(file_name), "r", encoding="utf8") 
index = HTMLFile.read() 

S = BeautifulSoup(index, 'lxml') 

Tag = S.find(id="hw")

Tag.clear()
Tag.insert(1, input_text)

new_file = open(HTML_PATH.format(new_file_name), 'w')
new_file.write(S.prettify())