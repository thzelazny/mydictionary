person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person["children"][1])

print(person["pets"]["cat"])

for child in person["children"]:
    print(child)

for pet_name in person["pets"].values():
    print(pet_name)


#The following also works in finding the pet name:

for pet in person["pets"]:
    print(person["pets"][pet])