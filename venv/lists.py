fruits = ["peaches", "pears", "apples"]
years = [3, "1988", 2.5, 987, "1994"]


print(fruits, years)

fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [5, 1928, 4, 7, 68, 73.6, 20.458]
numbers.sort()
print(numbers)

print("apple" in fruits)
print("apples" in fruits)

print(fruits.count("apples"))

print(fruits.index("apples"))
#print(fruits.index("apple"))

fruits.insert(1,"Mango")
print(fruits)