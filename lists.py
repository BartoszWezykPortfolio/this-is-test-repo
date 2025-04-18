############################## #List

# cities = ['Warszawa', 'Kraków', 'Radom']
#
# print(cities)

################################# #Insert

# cities.insert(int(input('Podaj index w którym dodać miasto')),'Ełk')
#
# print(cities)

# ##################################Append

# cities2 = ['Chicago', 'Toronto', 'London']
#
# cities.append(cities2)
#
# print(f'New cities list with appended cities2 list is \n{cities}')

################################# #How to find index of element

# cities3 = ['Warszawa', 'Radom', 'Ełk']
#
# check = cities3.index('Warszawa')
#
# print(check)

# ######################################Extend

# extend_list = []
#
# extend_list.extend([1, 2])
#
# print(extend_list)
#
# extend_list.extend((3, 4))
#
# print(extend_list)
#
# print(len(extend_list))

# ############################################Concatenation

# evens = [2, 4, 6]
# odds = [1, 3, 5]
#
# nums = odds + evens
#
# print(nums)

######################################################Modifying items in list
# animals = ['Cow', 'Crab', 'Dog', 'Cat']
#
# print(animals)
#
# animals[0] = 'Human'
#
# print(animals)

#####################################################Remove
# cities = ['Warszawa', 'Radom']
# print(cities)
#
# cities.remove('Warszawa')
# print(cities)

##################################################Sort
# animals = ['A.Cow', 'D.Crab', 'B.Dog', 'C.Cat']
#
# print(animals)
#
# animals.sort(reverse=True)
# print(animals)

################################################Pop
# animals = ['A.Cow', 'D.Crab', 'B.Dog', 'C.Cat']
#
# animals.pop(2)
# print(animals)

##############################################Listy wielopoziomowe
values = [
    [1,5],
    [10,12]
]

print(values)