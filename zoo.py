#Create a tuple named zoo that contains your favorite animals.
zoo = tuple(["Dog","Chicken","Lama","Otter"])

#Find one of your animals using the .index(value) method on the tuple.
num_of_chicken = zoo.index("Chicken")
print(num_of_chicken)

#Determine if an animal is in your tuple by using value in tuple.
print("Chicken" in zoo)

#Create a variable for each of the animals in your tuple with this cool feature of Python.


#Convert your tuple into a list.
zoo_list = list(zoo)
print(zoo_list)

#Use extend() to add three more animals to your zoo.
zoo_list.extend(["Zac", "Daniel", "Ousama"])
print(zoo_list)

#Convert the list back into a tuple.
zoo_list_tuple = tuple(zoo_list)
print(zoo_list_tuple)