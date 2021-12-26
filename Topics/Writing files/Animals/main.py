# read animals.txt
# and write animals_new.txt
animals = open('animals.txt')
animals_new = open('animals_new.txt', 'w')

list_ = animals.readlines()

for entry in list_:
    animals_new.write(entry.rstrip('\n') + ' ')

animals.close()
animals_new.close()
