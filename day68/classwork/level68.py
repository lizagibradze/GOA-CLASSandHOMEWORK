
# lambda

# add = lambda x, y: x + y

# print(add(5, 10))





# a = lambda x, y, z: (x + y + z) / 3

# print(a(5, 10, 15)) 



# a = lambda x, y: x if x > y else y


# print(a(20, 30)) 



m = lambda x, y: x if x < y else y

print(m(10, 20))

# ლუწი

even = lambda x, y: x if x % 2 == 0 else y if y % 2 == 0 else None

print(even(20, 25)) # gamoitans 20-s
print(even(23, 25)) # gamoitans none -s
print(even(21, 16)) # gamoitans 16


# კენტი

odd = lambda x, y: x if x % 2 != 0 else y if y % 2 != 0 else None

print(odd(20, 25))




even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


positive_sum = lambda x : sum(i for i in x if i > 0)

