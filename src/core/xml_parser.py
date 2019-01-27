import xml.etree.ElementTree as ET

tree = ET.parse("../configuration/config.xml")
root = ET.fromstring("config")
print(root.tag)
