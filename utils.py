#region---------------Imports-------------------------------

from copy import deepcopy
import re
#endregion---------------Imports-------------------------------

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
        
def XmlJsonWithAttribsHelper(xml):
    res=re.findall("<(?P<var>\S*)(?P<attr>[^/>]*)(?:(?:>(?P<val>.*?)</(?P=var)>)|(?:/>))",xml)
    if len(res)>=1:
        attreg="(?P<avr>\S+?)(?:(?:=(?P<quote>['\"])(?P<avl>.*?)(?P=quote))|(?:=(?P<avl1>.*?)(?:\s|$))|(?P<avl2>[\s]+)|$)"
        if len(res)>1:
            return [{i[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,i[1].strip())]},{"$values":XmlJsonWithAttribsHelper(i[2])}]} for i in res]
        else:
            return {res[0]:[{"@attributes":[{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg,res[1].strip())]},{"$values":XmlJsonWithAttribsHelper(res[2])}]}
    else:
        return xml.strip()

def parse_element(element):
    dict_data = dict()
    if element.nodeType == element.TEXT_NODE:
        dict_data['data'] = element.data
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_NODE, 
                                element.DOCUMENT_TYPE_NODE]:
        for item in element.attributes.items():
            dict_data[item[0]] = item[1]
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_TYPE_NODE]:
        for child in element.childNodes:
            child_name, child_dict = parse_element(child)
            if child_name in dict_data:
                try:
                    dict_data[child_name].append(child_dict)
                except AttributeError:
                    dict_data[child_name] = [dict_data[child_name], child_dict]
            else:
                dict_data[child_name] = child_dict 
    return element.nodeName, dict_data
#endregion---------------------HelperAPIs-----------------------------
