from xml.etree import ElementTree as ET

tree = ET.parse('test_xml.xml')
root = tree.getroot()

name = root.find('.//doc/name').text
print(name)
