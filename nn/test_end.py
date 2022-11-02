import requests
import json
import jsonpath


def test_endtoend():
    url='https://thetestingworldapi.com/api/studentsDetails'
    f=open('C:/Users/akash/OneDrive/Desktop/code/ete.txt','r')
    json_inp=json.loads(f.read()) 
    res=requests.post(url,json_inp)
    id=jsonpath.jsonpath(res.json(),'id')
    print(id[0])
    
    tech_url='https://thetestingworldapi.com/api/technicalskills'
    f=open('C:/Users/akash/OneDrive/Desktop/code/techdetails.txt','r')
    json_inp=json.loads(f.read()) 
    json_inp['id']=int(id[0])
    json_inp['st_id']=id[0]
    res=requests.post(tech_url,json_inp)
    print(res.text)
    
    add_url='https://thetestingworldapi.com/api/addresses'
    f=open('C:/Users/akash/OneDrive/Desktop/code/address.txt','r')
    json_inp=json.loads(f.read()) 
    json_inp['st_id']=id[0]
    res=requests.post(add_url,json_inp)

    
    final_url='https://thetestingworldapi.com/StDetails/'+str(id[0])
    res=requests.get(final_url)
    print(res.text)