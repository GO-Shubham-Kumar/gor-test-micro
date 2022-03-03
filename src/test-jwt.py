import http.client

conn = http.client.HTTPSConnection("dev-au0bmyjp.us.auth0.com")

payload = "{\"client_id\":\"ILvkwBIIx1b4QgAJkxVZtJklj59zlsQH\",\"client_secret\":\"ht_dCB7Z8XMzkekbzfZkz_HlkjvyDeco5X65myJIE452NQxGVHjmyyZql0qgTFyo\",\"audience\":\"http://go-policy-test.us-e2.cloudhub.io/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))