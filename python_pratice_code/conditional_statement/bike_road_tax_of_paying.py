price_of_bike = int(input("Enter the price of bike in INR: "))

if price_of_bike<=50000:
    road_Tax = (price_of_bike/100)*5
    print("The road tax of bike paid is: ",road_Tax)
elif price_of_bike>50000 and price_of_bike<=100000:
    road_Tax = (price_of_bike/100)*10
    print("The road tax of bike paid is: ",road_Tax)
else:
    road_Tax = (price_of_bike/100)*15
    print("The road tax of bike paid is: ",road_Tax)
    
