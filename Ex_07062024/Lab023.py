# List - shopping list
# Lists are mutable since they can be changed later
# milk , bread , book , ball
# 1. Add items
# 2. Remove items
# 3. Update items
# 4. view items
# 5. Exit

# List with same data types
Shopping_list = ["Milk" , "Ball" , "Curd", "Bottle"]
print(Shopping_list)
print(len(Shopping_list))
print(Shopping_list[1])
print(Shopping_list[-2])
print(type(Shopping_list))

Shopping_list.sort() # Will sort from small to big
print(Shopping_list)
# Adding , removing , updating etc
Shopping_list.append("Butter")  # Adding only one new item at the end only
print(Shopping_list)
Shopping_list.extend(["Biscuits" , "Bread"]) # Add multiple items at the end only
print(Shopping_list)
Shopping_list.pop() # Will delete or remove the last item from list
print(Shopping_list)
Shopping_list.reverse() # Will do the list reverse
print(Shopping_list)
Shopping_list.insert(1,"Cheese") # Adding objects in middle -- insert(index, object)
print(Shopping_list)
Shopping_list.insert(-1,"Bun") # adding in reverse
print(Shopping_list)
Shopping_list.remove("Bottle") # Remove item from list
print(Shopping_list)


# List with different data types also possible
my_list=[12,"ball",13.2 , True , "False"]
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[2])

