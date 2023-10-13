# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup 
from html2image import Html2Image

file_name = 'sarcasm.html'
new_file_name = "new.html"
input_text = "Hello there"
HTML_PATH = "HTML/{}"
IMG_PATH = 'img/{}'
dimensions = (900, 500)

line_count = 5
lines = []
contacts = []
line_prompt_text = 'Input text for line number {}: '
contact_prompt_text = 'Input contact information\n enter empty line to finish: '
new_contacts = True

for line in range(line_count):
    lines.append(input(line_prompt_text.format(line + 1)))

print(contact_prompt_text)
while new_contacts:
    new_contact = input()
    if new_contact == '':
        new_contacts = False
    else:
        contacts.append(new_contact)

# lines = ['Nunu and Willump', 'the boy and his yeti', 'adventurer', 'The Freljord is a harsh and unforgiving place', '\"This way to... adventure!" (Willump noises)\"']
# contacts = ['nunu@willump.lol', '9999AP', 'snowball.gg']
print(lines, contacts)
        
HTMLFile = open(HTML_PATH.format(file_name), "r", encoding="utf8") 
contact_tamplate_file = open(HTML_PATH.format('contact.html'))
contact_arrow_file = open(HTML_PATH.format('arrow.html'))
index = HTMLFile.read() 
contact_template = contact_tamplate_file.read()
contact_arrow = contact_arrow_file.read()

S = BeautifulSoup(index, 'lxml') 

line_string = 'line_{}'
for line_index in range(len(lines)):
    element = S.find(id=line_string.format(line_index + 1))
    element.clear()
    element.insert(1, lines[line_index])
    
parent_element = S.find(id='contact_parent')
green_text = S.find(id='contact_text')
for contact in contacts:
    S_contact = BeautifulSoup(contact_template, 'lxml')
    contact_element = S_contact.find(id='contact')
    contact_element.clear()
    contact_element.insert(1, contact)
    parent_element.append(S_contact)
X = BeautifulSoup(contact_arrow, 'lxml')
parent_element.append(X)

main_div = S.find(id='main')
zoom_text = 'zoom: {};'
zoom = 2.6
main_div['style'] = zoom_text.format(zoom)

new_file = open(HTML_PATH.format(new_file_name), 'w')
new_file.write(S.prettify())


Html2Image(output_path='img', size=dimensions).screenshot(html_file=HTML_PATH.format(new_file_name), save_as='out.png')
