import requests
import json
import jsonpath
url="https://reqres.in/api/users?page=2"
response=requests.get(url)
json_response=json.loads(response.text)
print(json_response)

#fetch value using jsonpath
for i in range(0,3):
    first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print((first_name[0]))