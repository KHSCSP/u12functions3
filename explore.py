print("\n--- exploring positional and keyword arguments ---")
def full_info(name, age):
    print(name, "is", age, "years old.")

# call using positional arguments
full_info("jo", 42)
# wrong order not ok!
full_info(11, "no")


# call using keyword arguments
full_info(name="bo", age=13)
# wrong order OK!
full_info(age=18, name="mo")



print("\n--- exploring default parameters ---")
def describe_pet(pet_name, animal_type='dog'):
    print("I have a", animal_type)
    print("Its name is", pet_name)

print("--- default? ---")
describe_pet("December")
describe_pet("January", "cat")






print("\n--- a dog named 'Willie' ---")
describe_pet('Willie')
describe_pet(pet_name='Willie')
describe_pet('Willie', 'dog')
describe_pet(pet_name='Willie', animal_type='dog')
describe_pet(animal_type='dog', pet_name='Willie')


print("\n--- a hamster named 'Harry' ---")
describe_pet()
describe_pet()
describe_pet()













# (last part solution)
# describe_pet('Harry', 'hamster')
# describe_pet(pet_name='Harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='Harry')
