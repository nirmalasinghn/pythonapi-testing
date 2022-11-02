import requests
import json
import jsonpath
url="https://reqres.in/api/users?page=2"
response=requests.get(url)
json_response=json.loads(response.text)
print(json_response)

#fetch value using jsonpath
pages=jsonpath.jsonpath(json_response,'total_pages')
assert pages[0] == 5