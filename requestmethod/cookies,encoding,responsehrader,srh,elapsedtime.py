import requests
url="https://reqres.in/api/users?page=2"
response=requests.get(url)
assert response.status_code == 200

#featch response header
print(response.headers)
#fetch specific response header
print(response.headers.get('date'))
print(response.headers.get('server'))
#fetch cookiess
print(response.cookies)
#fetch encoding
print(response.encoding)
#fetch elapsedtime
print(response.elapsed)