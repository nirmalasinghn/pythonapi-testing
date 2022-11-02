import requests
import json 
import jsonpath
import openpyxl
from dd import library

def test_p():
    #api
    url='https://thetestingworldapi.com/api/studentsDetails'
    f=open('C:\\Users\\akash\\OneDrive\\Desktop\\code\\kobe.json')
    json_req=json.loads(f.read())
    obj=library.chris('C:\\Users\\akash\\OneDrive\\Desktop\\code\\excel1.xlsx','Sheet1')
    col=obj.fetch_column()
    row=obj.fetch_rows()
    keylist=obj.fetch_keynames()
    for i in range(2,row+1):
        updated_json_req=obj.update_req(i,json_req,keylist)
        response=requests.post(url,updated_json_req)
        print(response)