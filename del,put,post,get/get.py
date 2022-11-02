import requests

#api url
url="https://reqres.in/api/users?page=2"

#get request
response=requests.get(url)

#display response code
print(response.content)
print(response.headers)


#validate statuscode
print(response.status_code)
assert response.status_code ==200