from utils import *
from datetime import datetime

xml = JsonXml({"name": "the matrix", "age": 20, "metadata": {"dateWatched": datetime.now()}}, 'movie')

print(xml, end='\n\n')
# print(XmlJsonv3(xml), end='\n\n')
xmlContent = """<movie type="dict">
    <name type="str">the matrix</name>
    <age type="int">20</age>
    <metadata type="dict">
        <dateWatched type="datetime">2021-03-29 20:34:46.495150</dateWatched>
    </metadata>
</movie>"""

print(XmlJsonv3(xmlContent))
# print(XmlJsonv2(xmlContent))

xmlContent = """<details class="4b" count=1 boy>
    <name type="firstname">John</name>/
    <age>13</age>
    <hobby>Coin collection</hobby>
    <hobby>Stamp collection</hobby>
    <address>
        <country>USA</country>
        <state>CA</state>
    </address>
</details>
<details empty="True"/>
<details/>
<details class="4a" count=2 girl>
    <name type="firstname">Samantha</name>
    <age>13</age>
    <hobby>Fishing</hobby>
    <hobby>Chess</hobby>
    <address current="no">
        <country>Australia</country>
        <state>NSW</state>
    </address>
</details>"""

# print(XmlJsonv3(xmlContent))