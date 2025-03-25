import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Replace with your API URL
data = {
    "title" : "The last ",
    "body" : "Follows one of the world's largest",
    "id" : 2000
}  
headers = {
    "Authorization": "bdhj7467473dg", # Replace with your API key/token
    "Content-Type": "application/json"    
}

response = requests.put(url, json=data, headers=headers)

if response.status_code == 200:
    print("Resource Created:", response.json())
else:
    print("Error:", response.status_code)
    
