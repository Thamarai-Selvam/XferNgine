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
| ProtoBuf      | JSON           |  NotYetImplemented     |\n
| JSON          | Protobuf       |  NotYetImplemented     |\n
| CSV           | JSON           |  NotYetImplemented     |\n
| JSON          | CSV            |  NotYetImplemented     |\n
| MessagePack   | JSON           |  NotYetImplemented     |\n
| MessagePack   | XML            |  NotYetImplemented     |\n
| YAML          | JSON           |  NotYetImplemented     |\n
| JSON          | YAML           |  NotYetImplemented     |\n
| YAML          | XML            |  NotYetImplemented     |\n
| XML           | YAML           |  NotYetImplemented     |\n
| JSON          | MessagePack    |  NotYetImplemented     |\n
| XML           | MessagePack    |  NotYetImplemented     |\n
----------------------------------------------------------
'''

#region---------------Imports-------------------------------
from typing import Union
import re
import json
from xml.etree import ElementTree as ET
import msgpack
from copy import deepcopy
import pandas
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

def JsonCSV(json):
    """
        Converts Json to CSV.\n
        @param json: json as dictionary/json.\n
        Returns CSV
    """
    return pandas.DataFrame(flatten_json(json))
#endregion---------------FromJsonAPIs-----------------------------

#region---------------FromXMLAPIs-------------------------------
def XmlJson(xml, flag=0):
    """
        Converts XMl to Json.\n
        @param xml: xml as string.\n
        @param flag: defaulted to 0 for internal puposes only, don't pass one.\n
        Returns Json
    """
    response = {}
    if(not flag):
        try:
            xml = ET.fromstring(xml)
            print(xml)
        except ET.ParseError:
            xml = '<root>' + xml + '</root>'
            xml = ET.fromstring(xml)
            # print(ET.dump(xml))

    for child in list(xml):
        if len(list(child)) > 0:
            print('>0T:',child.tag, 'V:',child.text)
            response[child.tag] = XmlJson(child,1)
        else:
            print('T:',child.tag, 'V:',child.text)
            response[child.tag] = child.text or ''
    return response

def XmlJsonv2(xml, flag=0):
    """
        Converts XMl to Json.\n
        @param xml: xml as string.\n
        @param flag: defaulted to 0 for internal puposes only, don't pass one.\n
        Returns Json
    """
    response = {}
    if(not flag):
        try:
            xml = ET.fromstring(xml)
            print(xml)
        except ET.ParseError:
            xml = '<root>' + xml + '</root>'
            xml = ET.fromstring(xml)
            # print(ET.dump(xml))
    
    for child in list(xml):
        if len(list(child)) > 0:
            print(child.tag, child.text)
            response[child.tag] = XmlJsonv2(child,1) if len(list(child)) > 0 else child.text or ''
    return response

def XmlJsonWithAttribs(xml):
    """
        Converts XMl to Json.\n
        @param xml: xml as string.\n
        @param flag: defaulted to 0 for internal puposes only, don't pass one.\n
        Returns Json with it's included Attributes 
            Eg : <name type="firstname"> as {'name': [{'@attributes': [{'type': 'firstname'}]}, {'$values': 'John'}]}
    """
    res=re.findall("<(?P<var>\S*)(?P<attr>[^/>]*)(?:(?:>(?P<val>.*?)</(?P=var)>)|(?:/>))",xml)
    if len(res)>=1:
        attreg="(?P<avr>\S+?)(?:(?:=(?P<quote>['\"])(?P<avl>.*?)(?P=quote))|(?:=(?P<avl1>.*?)(?:\s|$))|(?P<avl2>[\s]+)|$)"
        if len(res)>1:
            return [{i[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,i[1].strip())]},{"$values":XmlJsonWithAttribs(i[2])}]} for i in res]
        else:
            return {res[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,res[1].strip())]},{"$values":XmlJsonWithAttribs(res[2])}]}
    else:
        return xml

#endregion---------------FromXMLAPIs-------------------------------

#region---------------------HelperAPIs-----------------------------

def cross_join(left, right):
    new_rows = []
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem

def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows


#endregion---------------------HelperAPIs-----------------------------
