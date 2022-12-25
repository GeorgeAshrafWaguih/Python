def user_info(name , age=0, city="Dubai", *args, **kwargs):
    '''This function prints name , age and city
    from an argument provided to the function '''

    print(f"{name} is {age} years old from {city}")


user_info("Geo", 34, "Cairo, Egypt")
user_info("Janet")
user_info(age=40, name="Trinity")
user_info("Neo", 40, "Matrix", 7500, hire_date="September 2020")