from utils import *
from datetime import datetime

json = {"name": "the matrix", "age": 20, "metadata": {"dateWatched": str(datetime.now())}}
xml = JsonXml(json, 'movie')



xmlContent = """<details class="4b" count="1" gender="boy">
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
<details class="4a" count="2" gender="girl">
    <name type="firstname">Samantha</name>
    <age>13</age>
    <hobby>Fishing</hobby>
    <hobby>Chess</hobby>
    <address current="no">
        <country>Australia</country>
        <state>NSW</state>
    </address>
</details>"""

# print(xml, end='\n\n')
print(XmlJson(xmlContent))
print(XmlJsonv2(xmlContent))
# print(XmlJsonWithAttribs(xmlContent))
# print(JsonMessagePack(json))
print(JsonCSV(json))
# print(XmlJson(xmlContent))