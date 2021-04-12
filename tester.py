from XferNgine import *
from datetime import datetime
from fileIO import *


xmlContent = """<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
<calories>650</calories>
</food>
<food>
<name>Strawberry Belgian Waffles</name>
<price>$7.95</price>
<description>Light Belgian waffles covered with strawberries and whipped cream</description>
<calories>900</calories>
</food>
<food>
<name>Berry-Berry Belgian Waffles</name>
<price>$8.95</price>
<description>Light Belgian waffles covered with an assortment of fresh berries and whipped cream</description>
<calories>900</calories>
</food>
<food>
<name>French Toast</name>
<price>$4.50</price>
<description>Thick slices made from our homemade sourdough bread</description>
<calories>600</calories>
</food>
<food>
<name>Homestyle Breakfast</name>
<price>$6.95</price>
<description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description>
<calories>950</calories>
</food>
</breakfast_menu>"""

jsonContentDF = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
} 

yamlContent = """
glossary:
  GlossDiv:
    GlossList:
      GlossEntry:
        Abbrev: ISO 8879:1986
        Acronym: SGML
        GlossDef:
          GlossSeeAlso:
          - GML
          - XML
          para: A meta-markup language, used to create markup languages such as DocBook.
        GlossSee: markup
        GlossTerm: Standard Generalized Markup Language
        ID: SGML
        SortAs: SGML
    title: S
  title: example glossary
  """
protoMessage = """
message Thing {
    string first = 1;
    bool second = 2;
    int32 third = 3;
}
"""
jsonContent = XmlJson(xmlContent)
print(xmlContent, end='\n\n')

createJson(XmlJson(xmlContent), 'testFiles\\test')

createJson(XmlJsonWithAttribs(xmlContent), 'testFiles\\test')

createCSV(JsonCSV(jsonContentDF), 'testFiles\\test')
createCSV(XmlCSV(xmlContent), 'testFiles\\test')
createXML(JsonXml(jsonContentDF), 'testFiles\\test')

createMessagePack(JsonMessagePack(jsonContent), 'testFiles\\test')

createYaml(JsonYaml(jsonContentDF), 'testFiles\\test')
createJson(YamlJson(yamlContent), 'testFiles\\test')
# createProtoBuf(JsonProtoBuf(jsonContentDF), 'testFiles\\test')
# createJson(ProtoBuftoJson(protoMessage), 'testFiles\\test')

createYaml(XmlYaml(xmlContent), 'testFiles\\test')

createXML(YamlXml(yamlContent), 'testFiles\\test')
createMessagePack(XmlMessagePack(xmlContent), 'testFiles\\test')
createXML(readMessagePack('testFiles\\test.msgpack'), 'testFiles\\test')