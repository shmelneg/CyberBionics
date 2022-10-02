import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "name").text = "Andrii"
ET.SubElement(doc, "surname").text = "Melnyk"

tree = ET.ElementTree(root)
tree.write("test_xml.xml")
