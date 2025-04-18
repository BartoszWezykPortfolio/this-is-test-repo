print('###############1')
lists = []

new_list = [1, 3, 11, 24, 35]
lists.append(new_list)

print(lists)

print('#############2')
list1 = [1,2,3]
list2 = [4,5,6]

list_1_2 = list1 + list2

print(list_1_2)

print('############3')
my_list = [1,2,3,4,2]

my_list.pop(my_list.index(2))

print(my_list)

my_list.pop(len(my_list)-1)

print(my_list)

print('##################4')
my_list = [10, 20, 40, 30, 20]

print(my_list.index(40))

print('##################5')
my_list = [1, 2, 2, 3, 2, 4, 2]

print(my_list.count(2))

print('##################6')
#6 PRAWIE
def rotate_list(lst, k):
    new_list = lst[-k:] + lst[:-k]
    return new_list

print(rotate_list([1, 2, 3, 4, 5], 2))

print('Kolejny etap')