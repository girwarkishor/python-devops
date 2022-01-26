import xml.etree.ElementTree as ET

tree = ET.parse("sample_data.xml")
root = tree.getroot()

for each_country in root:
    print(each_country.tag, each_country.attrib)