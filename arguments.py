#Arguments

def user_info (name, age = 27, city = "Cairo", *args, **kwargs):
    '''This function prints user's info which: name, age and city'''
    
    print("{} is {} years old from {}".format(name,age,city))

user_info("Toka", 26, "Alexandria", 20000, hello = "Test")
user_info ("Aliaa")