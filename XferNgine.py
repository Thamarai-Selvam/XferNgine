'''
Utility APIs for XferNgine
Currently Supports the following Conversions
__________________________________________________________
|   From        | To             |  APIName               |\n
----------------| ----------------------------------------
| JSON          | XML Document   |  JsonXML               |\n
| XML Document  | JSON           |  XMLJson               |\n
| Protobuf      | XML            |  NotYetImplemented     |\n
| XML           | Protobuf       |  NotYetImplemented     |\n
| ProtoBuf      | JSON           |  ProtoBuftoJson        |\n
| JSON          | Protobuf       |  JsonProtoBuf          |\n
| CSV           | JSON           |  NotYetImplemented     |\n
| JSON          | CSV            |  JsonCSV               |\n
| XML           | CSV            |  XmlCSV                |\n
| MessagePack   | JSON           |  NotYetImplemented     |\n
| MessagePack   | XML            |  NotYetImplemented     |\n
| YAML          | JSON           |  YamlJson              |\n
| JSON          | YAML           |  JsonYaml              |\n
| YAML          | XML            |  YamlXml               |\n
| XML           | YAML           |  XmlYaml               |\n
| JSON          | MessagePack    |  JsonMessagePack       |\n
| XML           | MessagePack    |  NotYetImplemented     |\n
----------------------------------------------------------
'''

#region---------------Imports-------------------------------
from utils import *
from typing import Union
import re
import json
from xml.etree import ElementTree as ET
from xml.dom import minidom
import msgpack
import pandas
import ast
import xmltodict
import yaml
import ruamel.yaml
import xmlplain
from google.protobuf.json_format import Parse, MessageToDict, MessageToJson

#endregion---------------Imports-----------------------------

#region---------------FromJsonAPIs-------------------------------
def JsonXml(data: Union[dict, bool], rootElement='root'):
    '''
    Converts from Json to XML\n
    @param data : json as dictionary or json key value pair\n
    @param rootElement : Tag name to be added as xml root Element\n
                         Default is "root"\n
    Returns XML as string
    '''
    node = f'<{rootElement} type="{type(data).__name__}">'
    if isinstance(data, dict):
        for key, value in data.items():
            node += JsonXml(value, key)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            node += JsonXml(item, 'item')

    else:
        node += f'{str(data)}'

    node += f'</{rootElement}>'
    return node

def JsonMessagePack(data):
    """
        Converts Json to MessagePack.\n
        @param data: json as dictionary/json.\n
        Returns MessagePack
    """
    return msgpack.packb(data)

def JsonCSV(jsonContent):
    """
        Converts Json to CSV.\n
        @param jsonContent: json as dictionary/json.\n
        Returns CSV
    """
    return pandas.DataFrame(flatten_json(jsonContent))

def JsonYaml(jsonContent):
    """
        Converts Json to Yaml.\n
        @param jsonContent: json as dictionary/json.\n
        Returns Yaml
    """
    return yaml.safe_dump(jsonContent, allow_unicode=True)

def JsonProtoBuf(jsonContent):
    """
        Converts Json to ProtoBuf.\n
        @param jsonContent: json as dictionary/json.\n
        Returns ProtoBuf
    """
    pass
    # return Parse(
    #    json.dumps(jsonContent),
        #descriptor automation ideas on process
        # Thing(),
        # ignore_unknown_fields=False)

#endregion---------------FromJsonAPIs-----------------------------

#region---------------FromXMLAPIs-------------------------------

def XmlJsonWithAttribs(xml):
    """
        Converts XMl to Json.\n
        @param xml: xml as string.\n
        @param flag: defaulted to 0 for internal puposes only, don't pass one.\n
        Returns Json with it's included Attributes 
            Eg : <name type="firstname">Jonh</name> as {'name': [{'@attributes': [{'type': 'firstname'}]}, {'$values': 'John'}]}
    """
    singleQuotedJson = XmlJsonWithAttribsHelper(xml)
    return json.dumps(singleQuotedJson)

def XmlCSV(xml):
    """
        Converts XML to CSV.\n
        @param xmlContent: xmlContent as string .\n
        Returns CSV
    """
    jsonXML = xmltodict.parse(xml)
    return JsonCSV(jsonXML)

def XmlJson(xmlContent):
    """
        Converts XML to JSON.\n
        @param xmlContent: xmlContent as string .\n
        Returns JSON
    """
    return json.dumps(parse_element(minidom.parseString(xmlContent.replace('\n',''))))

def XmlYaml(xmlContent):
    """
        Converts XML to Yaml.\n
        @param xmlContent: xmlContent as string .\n
        Returns Yaml
    """
    return yaml.safe_dump(parse_element(minidom.parseString(xmlContent.replace('\n',''))), allow_unicode=True)

def XmlMessagePack(xmlContent):
    """
        Converts XML to MessagePack.\n
        @param xmlContent: xmlContent as string .\n
        Returns MessagePack
    """
    return msgpack.packb(xmlContent)
#endregion---------------FromXMLAPIs-------------------------------

#region---------------FromYAMLAPIs-------------------------------

def YamlJson(yamlContent):
    """
        Converts Yaml to Json.\n
        @param yamlContent: yamlContent as string .\n
        Returns Json
    """
    yaml = ruamel.yaml.YAML(typ='safe')
    return json.dumps(yaml.load(yamlContent))

def YamlXml(yamlContent):
    """
        Converts Yaml to XML.\n
        @param yamlContent: yamlContent as string .\n
        Returns XML
    """
    yamlObject = xmlplain.obj_from_yaml(yamlContent)
    return str(xmlplain.xml_from_obj(yamlObject, pretty=True).decode("utf-8") )

#endregion---------------FromYAMLAPIs-------------------------------

#region---------------FromProtoBufAPIs-------------------------------

def ProtoBuftoJson(protoMessage):
    """
        Converts ProtoBuf to Json.\n
        @param protoMessage: protoMessage as proto Message Type/ '.proto' contents .\n
        Returns Json
    """
    return MessageToJson(protoMessage)

#endregion---------------FromProtoBufAPIs-------------------------------
