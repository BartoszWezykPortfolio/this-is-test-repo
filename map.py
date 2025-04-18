#MAPOWANIE JEST PODOBNE DO FUNKCJI FOR ... IN ..., ALE MA TĄ ZALETĘ, ŻE DZIAŁA NA ELEMENTACH POJEDYNCZO NIE
#TWORZĄC ICH KOPII, CO MOŻE BYĆ PRZYDATNE PRZY WIĘKSZEJ LICZBIE DANYCH

nums = [1,2,3,4,5,6,7]

multiply_nums = map(lambda x: x * x, nums) #-> interujemy tutaj przez nums robiąć x * x na każdym elemencie
#i tworzymy kopię tej tablicy, tylko z pomnożonymi przez siebie elementami

print(list(multiply_nums))

users = ['Kasia','Karol','Jadwiga','Jan', 'Aga']

map_users = list(map(lambda x: f'To jest {x}', users))

print(map_users)

def change_user(x):
    return f'To jest {x}'

users2 = list(map(change_user, users))

print(users2)

#FILTER CZYLI W SUMIE TAKIE FILTROWANIE NA ZASADZIE FOR...IN..., DO KTÓREGO TRZEBA DODAĆ APPEND

users_filter = list(filter(lambda x: len(x) < 5, users))

print(users_filter)

