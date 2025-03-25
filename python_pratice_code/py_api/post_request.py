import requests

url = "https://jsonplaceholder.typicode.com/posts"  # Replace with your API URL
data = {
    "title" : "The last chapter",
    "body" : "Follows one of the world's largest outlaw biker gangs, The Triple Sixers, whose unrivaled strength stretches throughout Canada, with one exception.",
    "id" : 2
}  
headers = {
    "Authorization": "bdhj7467473dg", # Replace with your API key/token
    "Content-Type": "application/json"    
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print("Resource Created:", response.json())
else:
    print("Error:", response.status_code)
