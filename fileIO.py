import msgpack
from google.protobuf import text_format


def createJson(jsonContent, fileName):
    with open(str(fileName+'.json'), 'w') as opFile:
            opFile.write(str(jsonContent))
            return 'Created Json Successfully'

def createCSV(csvContent, fileName):
    csvContent.to_csv(str(fileName+'.csv'))

def createCSV2(csvContent, fileName):
    with open(str(fileName+'.csv'), 'w') as opFile:
            opFile.write(str(csvContent))
            return 'Created CSV Successfully'

def createMessagePack(msgPackContent, fileName):
    with open(str(fileName+'.msgpack'), 'wb') as opFile:
        packed = msgpack.packb(msgPackContent)
        opFile.write(packed)

def readMessagePack(fileName):
    with open(fileName, "rb") as inFile:
        byte_data = inFile.read()
        return msgpack.unpackb(byte_data).decode('latin-1')
    
def createXML(xmlContent, fileName):
    with open(str(fileName+'.xml'), 'w') as opFile:
            opFile.write(str(xmlContent))
            return 'Created XML Successfully'

def createYaml(yamlContent, fileName):
    with open(str(fileName+'.yaml'), 'w') as opFile:
            opFile.write(str(yamlContent))
            return 'Created YAML Successfully'

def createProtoBuf(protoMessage, fileName):
    with open(str(fileName+'.proto'), 'w') as opFile:
        text_format.PrintMessage(protoMessage, opFile)