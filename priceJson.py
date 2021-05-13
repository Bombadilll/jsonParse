import json

inFile='input.json'
outFile= 'output.json'

def openFile(afile) :
    with open (afile,'r') as file:
        data=json.load(file)
    print('Input data loaded!')
    return data

def writeFile(data,afile):
    with open (afile,'w') as file:
       json.dump(data,file,indent=2)
    print('Output data recorded!')
    return

def parseJson(data):
    tax=data['tax']
    margin=data['margin']
    total_price=0

    for i in data['products']:
        i['price']= i['net_cost']+i['net_cost']*(tax*0.01)+i['net_cost']*(margin*0.01)
        print(i['price'])
        total_price+=i['price']
        del i['net_cost']

    data['total_price']=total_price
    del  data['tax']
    del  data['margin']

    return data

inData = openFile(inFile)
outData = parseJson(inData)
writeFile (outData, outFile)
