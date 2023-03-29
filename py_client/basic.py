import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello World"}) # HTTP Reuqest
print(get_response.text)    # print raw text response


# HTTP Request -> HTML
# REST API HTTP Request -> JSON (xml)
# JavaScript Object Notation ~= Python Dict
print(get_response.json())
print(get_response.status_code)