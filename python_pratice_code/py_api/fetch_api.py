import requests

def fetch_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    # print(type(response))

    if response.status_code == 200:
        data= response.json()
        # print(type(data))
        user_data = data["data"]
        user_id = user_data["login"]["uuid"]
        user_name = user_data["login"]["username"]
        user_phone_number = user_data["phone"]
        user_country = user_data["location"]["country"]
        user_city = user_data["location"]["city"]
        # print(user_data)
        return user_id, user_name, user_phone_number, user_country, user_city
    else:
    
        print(f"the data can not fetched{response.status_code}")

def main():
    try:
        user_id, user_name, user_phone_number, user_country, user_city = fetch_user_data()
        print(f" User_id : {user_id}\n User_Name : {user_name}\n User_Phone_number : {user_phone_number}\n User_Country : {user_country}\n User_City : {user_city}")
    except:
        print("can not fetch the data from api")
                

if __name__=="__main__":
    main()