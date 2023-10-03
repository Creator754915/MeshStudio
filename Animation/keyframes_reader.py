import xml.etree.ElementTree as ET
import json
import xmltodict as xmltodict


def xml_to_dict(element):
    data = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child_data:
            if child.tag in data:
                if isinstance(data[child.tag], list):
                    data[child.tag].append(child_data)
                else:
                    data[child.tag] = [data[child.tag], child_data]
            else:
                data[child.tag] = child_data
    if not data:
        return element.text
    return data


xml_file_path = 'keyframes.kf'

tree = ET.parse(xml_file_path)
root = tree.getroot()

result = xml_to_dict(root)

xml_string = ET.tostring(root, encoding='utf-8', method='xml').decode()

xml_dict = xmltodict.parse(xml_string, xml_attribs=False)


print(json.dumps(result, indent=4))

with open('keyframes_json_converted.json', 'w') as json_file:
    json.dump(xml_dict, json_file, indent=4)
