#  Default argument or value with age and user given
def introduce(name, age = 18):
    print("Hello, nice to meet you")
    print(f"My name is {name}, I'm {age} year old")

# default age value 
introduce("Pramod")
# user given 
introduce("Pramod", 19) 
"""
    The function `introduce` takes a `name` parameter and an optional `age` parameter with a default
    value of 18, and prints a greeting along with the provided name and age.
    
    :param name: name: Pramod
    :param age: age is a parameter in the introduce function that has a default value of 18 if not
    provided by the user, defaults to 18 (optional)
 """