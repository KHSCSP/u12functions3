
def describe_pet(pet_name, animal_type='dog'):
  print("I have a", animal_type)
  print("Its name is", pet_name)

# this will use the 'default' second parameter
describe_pet("December")
describe_pet("January", "cat")





# a dog named 'Willie'
describe_pet('Willie')
describe_pet(pet_name='Willie')
describe_pet('Willie', 'dog')
describe_pet(pet_name='Willie', animal_type='dog')
describe_pet(animal_type='dog', pet_name='Willie')


# a hamster named 'Harry'
describe_pet('Harry', 'hamster')
describe_pet(pet_name='Harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='Harry')

