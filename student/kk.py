import json
import jsonpath
import requests

def test_student():
    url='https://thetestingworldapi.com/api/studentsDetails'
    file= open('C:\\Users\\akash\\OneDrive\\Desktop\\py\\studetails.txt','r')
    json_inp=json.loads(file.read())
    res=requests.post(url,json_inp)
    print(res.text)
    
    
def test_update():
    url='https://thetestingworldapi.com/api/studentsDetails/3875295'
    file= open('C:\\Users\\akash\\OneDrive\\Desktop\\py\\studetails.txt','r')
    json_inp=json.loads(file.read())
    res=requests.put(url,json_inp)
    print(res.text)
    
def test_del():
    url='https://thetestingworldapi.com/api/studentsDetails/3875295'
    res=requests.delete(url)
    print(res)
    
    
def test_get():
    url='https://thetestingworldapi.com/api/studentsDetails/3875295'
    res=requests.get(url)
    json_res=res.json()
    id=jsonpath.jsonpath(json_res,'data.id')
    