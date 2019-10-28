from xml.dom import minidom

xmldoc = minidom.parse('parse.xml')
itemlist = xmldoc.getElementsByTagName('feed')
print(str(len(itemlist)))

print(itemlist[1].attributes['entry'].value)