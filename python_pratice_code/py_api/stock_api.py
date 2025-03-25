import requests

url = "https://api.freeapi.app/api/v1/public/stocks"
response = requests.get(url)

if response.status_code ==200:
    data = response.json()
    stock_data = data.get("data",{}).get("data",[])
    for full_data in stock_data:
        print(f"Name : {full_data["Name"]}, MarketCap : {full_data["MarketCap"]}")