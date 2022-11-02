import requests
import json
import jsonpath

url='https://reqres.in/api/users'
#read input json file 
file=open('C:/Users/akash/OneDrive/Desktop/py/user.json','r')
json_input=file.read()
req_json=json.loads(json_input)

#make post request with json input body
res=requests.post(url,req_json)

#validate response code
assert res.status_code == 201

#fetch header from response
print(res.headers.get('connection'))

#parse response to json format
res_json=json.loads(res.text)

#pick id using jsonpath
id=jsonpath.jsonpath(res_json,'id')
print(id[0])

