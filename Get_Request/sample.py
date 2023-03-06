# list1 = ["apple", "mango", "banana"]
# list1.append("cherry")
# print(list)
# list1.extend("ball")
# print(list)

# # list.delete[1]

# a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 5]

# data = set(a)
# print(data)
# e = (list(data))
# print(e)
# s = (list(e))
# print(string(e))

# company = {"A": "Pune", "B": "Chennai"}
# pincode = {"Pune": 113, "Chennai": 123}

# print(company["A"])


# print(pincode[company["A"]])

my_sentence = 'The sky is blue'[::-1]
output: 'blue is sky The'

a = my_sentence.split()
# my_sentence
print(a)
print(my_sentence)

A = ("saritha", "ragasvi", "Vishnu", "bhargavi", "venkat")

x = " # ".join(A)

print(x)

era = {"name": "John", "country": "Norway"}
mySeparator = "^^"

x = mySeparator.join(era)

print(x)

# grocery = ["milk", "bread", "butter"]
# a = enumerate(grocery)
# print(a)
# print(list(a))


# class Person:
#     def display(self):
#         print("can work")
#     def show(self):
#         print("Person class")


# class Employee(Person):
#     def show(self):
#         print("various roles in his life")


# class Programmer(Employee):
#     def display(self):
#         print("coding")


# object1 = Programmer()
# object1.display()
# object1.show()

# a = 10
# b = 20
# print(sum(a,b))


dict = {1: 'saritha', 2: 'nitya', 3: 'dina', 4: 'Dhana'}

for i, k in dict.items():
    print(k, end=' ')

dict1 = {a:'apple', b:'mango', c: 'cherry'}
