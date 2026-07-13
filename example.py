import client
import json

#POST REQUEST 

url = "https://httpbin.org/post" 
ua = "useragent goes here"
header = {
    "User-Agent": ua
}
body = json.dumps({
    "first":"Test"
})
client.post(url,body=body,header=header
)

#GET REQUEST

print(client.get("https://httpbin.org"))
