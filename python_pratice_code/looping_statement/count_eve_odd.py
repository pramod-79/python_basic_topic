list = [1,2,3,4,5,6,7,8,9,10,74,12,85,93,24,9273,55,355]
Even = 0
Odd = 0 

for num in list:
    if num%2==0:
        Even += 1     
    else:
        Odd += 1
print("The count of even number is -",Even)        
print("The count of odd number is -",Odd)        
