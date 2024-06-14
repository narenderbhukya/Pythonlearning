# Functions in python perform repetitive task
# some functions are sum() , len() , max() , min() , print() , avg() , type()

# Functions in strings
name = "NaRenDeR"
print(name)
print(type(name))  # prints type input
print(id(name))   # print the address of the stored variable
print(len(name))  # prints the lenght of string -- which always starts with 1 since zero lenght is not valid
print(name.upper())
print(name.lower())
print(name.count('e'))
print(name.count('n')) # prints only one  since python is case sensitive N and n
print(name.count('r')) # prints zero as both r are in capital letter R and R
print(name.count('R')) # prints two
print(name.count('a'))

# Index -- positions of elements -- starts with zero
print(name[0])
print(name[5])
# In pythons whole string can be changed
# In python strings are immutable -- values cant be changed
mass = "name"
mass = "man"
print(mass)
print(mass[2])

# In string , character cannot be changed ex - Name -- any of the character cant be changed once assigned

mass[0] = "R"   # 'str' object does not support item assignment
print(mass)