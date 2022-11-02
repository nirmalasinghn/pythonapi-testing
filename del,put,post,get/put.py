import requests
import json
import jsonpath

url='https://reqres.in/api/users/2'
#read input json file 
file=open('C:/Users/akash/OneDrive/Desktop/py/user.json','r')
json_input=file.read()
req_json=json.loads(json_input)

#make put request with json input body
res=requests.put(url,req_json)

#validate response code
assert res.status_code == 200

#parse response content
res_json=json.loads(res.text)
update=jsonpath.jsonpath(res_json,'updatedAt')
print(update[0])



