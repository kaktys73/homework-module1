my_dict = {'Yulia' : 2000, 'Nastya' : 2001, 'Evgeniy' : 1997} #словарь
print(my_dict)
print(my_dict['Yulia'])
print(my_dict.get('Sasha'))
my_dict.update({'Max' : 2002,
                'Alex' : 2005})
a = my_dict.pop('Nastya')
print(a)
print(my_dict)

my_set = {22,25,28,22,True,'eat',30,True,28} #множество
print(my_set)
my_set.add((101,'potato'))
my_set.discard(22)
print(my_set)
