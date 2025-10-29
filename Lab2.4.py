import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()
values=[]
for child in root.findall('.//Valute'):
    number_text=child.find("Value").text
    number=float(number_text.replace(',','.'))
    values.append(number)
average=sum(values)/len(values)
print(average)
