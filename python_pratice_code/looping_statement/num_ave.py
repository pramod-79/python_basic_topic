sum_of_num = 0
for user_num in range(1,11):
    user_num = int(input(f"Enter the {user_num} number"))
    sum_of_num = sum_of_num + user_num
    Average_of_num = sum_of_num/10
print(f"The sum of all number {sum_of_num }:-")
print(f"The average of all number {Average_of_num}:-")

# Time complexity of code is Big O(n)