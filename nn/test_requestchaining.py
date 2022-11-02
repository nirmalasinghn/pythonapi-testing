import requests
import json
import jsonpath

def test_newstu():
    global id
    url='https://thetestingworldapi.com/api/studentsDetails'
    file=open('C:\\Users\\akash\\OneDrive\\Desktop\\code\\ete.txt','r')
    json_req=json.loads(file.read())
    res=requests.post(url,json_req)
    id=jsonpath.jsonpath(res.json(),'id')
    print(id[0])
    
def test_get():
    url='https://thetestingworldapi.com/api/studentsDetails'+str(id[0])
    res=requests.get(url)
    print(res.text)