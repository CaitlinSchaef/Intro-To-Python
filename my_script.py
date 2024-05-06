# print('Start programming...')

#QUESTION 1 DONE ABOVE

# species = 'Monkey'
# is_mammal = True
# num_legs = 2
# has_tail = True

#QUESTION 2 DONE ABOVE

# def favorite_animal(species, is_mammal, num_legs, has_tail):

#     print("My favorite animal is a", species, "Is it a mammal? That is:", is_mammal, "How many legs does it have? It has:", num_legs,"legs.", "Does it have a tail? That is:", has_tail)

# favorite_animal(species, is_mammal, num_legs, has_tail)

#QUESTION 3 DONE ABOVE

# species = input('What is your favorite animal?(name of animal)')
# is_mammal = input('Is your favorite animal a mammal? (is/is not)')
# num_legs = input('How many legs does your favorite animal have?(number)')
# has_tail = input('Does your favorite animal have a tail?(does/does not)')

# def favorite_animal(species, is_mammal, num_legs, has_tail):
#     print("My favorite animal is:", species, ".", "My favorite animal", is_mammal, "a mammal.", "My favorite animal has", num_legs, "legs.", "My favorite anima", has_tail, "have a tail."  )

# favorite_animal(species, is_mammal, num_legs, has_tail)

#QUESTION 4 DONE ABOVE

# for i in range(11):
#     print (i)

#QUESTION 5 DONE ABOVE

# i = 5
# while i < 16:
#     print(i)
#     i += 1

#QUESTION 6 DONE ABOVE

# five_foods = ['bread', 'bacon', 'lettuce', 'tomato', 'mayo']

#QUESTION 7 DONE ABOVE 

# for item in five_foods:
#     print(item)

#QUESTION 8 DONE ABOVE 

animal_info = {
    'species': '',
    'is_mammal': '',
    'num_legs': '',
    'has_tail': '',
    'num_seen': ''
}
#QUESTION 9 DONE ABOVE

def create_animal_info(animal_info):
    animal_info['species'] = input('What is your favorite animal?(name of animal)')
    animal_info['is_mammal'] = input('Is your favorite animal a mammal? (is/is not)')
    animal_info['num_legs'] = input('How many legs does your favorite animal have?(number)')
    animal_info['has_tail'] = input('Does your favorite animal have a tail?(does/does not)')
    animal_info['num_seen'] = input('How many [species] have you seen in person? A rough guess is fine.')



create_animal_info(animal_info)
print("My favorite animal is:", (animal_info['species']), ".", "My favorite animal", (animal_info['is_mammal']), "a mammal.", "My favorite animal has", (animal_info['num_legs']), "legs.", "My favorite anima", (animal_info['has_tail']), "have a tail.", "I have seen", (animal_info['num_seen']), "in person!"  )

#in the print you do not need to put a comma between the key and the value! This now works to print everything that is in the library.
#QUESTION 10 DONE ABOVE

animal_info['num_seen'] = 0


if animal_info['num_seen']  < 10:
 print('The number seen is less than or equal to 10.')
elif animal_info['num_seen']  > 11:
 print('The number seen is more than 10 and less than 100.')
elif animal_info['num_seen']  > 99:
 print('The number seen is greater than or equal to 100.')
else:
  print('Thats a spicy meatball')

#I tried to do a fancier if else but it broke
#QUESTION 11 DONE ABOVE

animal_info['is_mammal'] = 'is'
animal_info['has_tail'] = 'does'



if (animal_info['is_mammal'] == 'is') and (animal_info['has_tail'] == 'does'):
  False   
  print((animal_info['species']), 'is both a mammal and has a tail.') 
elif (animal_info['is_mammal'] == 'is not') and (animal_info['has_tail'] == 'does'):
  True 
  print((animal_info['species']), 'is either a mammal or has a tail. But not both.')
elif (animal_info['is_mammal'] == 'is not') and (animal_info['has_tail'] == 'does not'):
  False   
  print((animal_info['species']), 'is both not a mammal and does not have a tail.') 
elif (animal_info['is_mammal'] == 'is') and (animal_info['has_tail'] == 'does not'):
  True 
  print((animal_info['species']), 'is either a mammal or has a tail. But not both.')

#QUESTION 12 DONE ABOVE

