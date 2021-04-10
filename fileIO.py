import msgpack


def createJson(jsonContent, fileName):
    with open(str(fileName+'.json'), 'w') as opFile:
            opFile.write(str(jsonContent))
            return 'Created Json Successfully'


def createCSV(csvContent, fileName):
    csvContent.to_csv(str(fileName+'.csv'))

def createMessagePack(msgPackContent, fileName):
    with open(str(fileName+'.json'), 'w') as opFile:
        packed = msgpack.packb(msgPackContent)
        opFile.write(packed)

def readMessagePack(fileName):
    with open(fileName, "rb") as inFile:
        byte_data = inFile.read()
        return msgpack.unpackb(byte_data)