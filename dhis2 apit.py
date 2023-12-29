import http.client
import json

Sconn = http.client.HTTPConnection("172.16.2.249")
payload = ''
headers = {
  'Authorization': 'Basic c2thZGlkaWE6S2FkaWRpYUAxMjM=',
 }
Sconn.request("GET", "/api/users/iUd18qN1eza", payload, headers)
res = Sconn.getresponse()
data = res.read()
datal=json.loads(data.decode("utf-8"))
print(datal["phoneNumber"])
