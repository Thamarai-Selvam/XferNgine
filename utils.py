from typing import Union
import re
import json

def JsonXml(data: Union[dict, bool], rootElement='root'):
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

def XmlJson(xml):
  response = {}

  for child in list(xml):
    if len(list(child)) > 0:
      response[child.tag] = XmlJson(child)
    else:
      response[child.tag] = child.text or ''

  return response

def XmlJsonv2(xml):
    response = {}

    for child in list(xml):
        if len(list(child)) > 0:
            response[child.tag] = XmlJsonv2(child) if len(list(child)) > 0 else child.text or ''
    
    return response

def XmlJsonv3(xml):
    res=re.findall("<(?P<var>\S*)(?P<attr>[^/>]*)(?:(?:>(?P<val>.*?)</(?P=var)>)|(?:/>))",xml)
    if len(res)>=1:
        attreg="(?P<avr>\S+?)(?:(?:=(?P<quote>['\"])(?P<avl>.*?)(?P=quote))|(?:=(?P<avl1>.*?)(?:\s|$))|(?P<avl2>[\s]+)|$)"
        if len(res)>1:
            return [{i[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,i[1].strip())]},{"$values":XmlJsonv3(i[2])}]} for i in res]
        else:
            return {res[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,res[1].strip())]},{"$values":XmlJsonv3(res[2])}]}
    else:
        return xml