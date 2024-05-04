immutable_var = 7, 8, 9, False, 'Samuray'
immutable_var_2 = (7, 8, 9, False, 'Samuray')
immutable_var_3 = [7, 8, 9, False, 'Samuray']
print(immutable_var)
print(immutable_var_2)
print(immutable_var_3)
print(type(immutable_var))         # Особенность кортежа в том, что он не изменяемый!!! <class 'tuple'>
print(immutable_var[4])
# immutable_var[4]=700               # Выдает ошибку при попытке поменять!!!

mutable_list = [9, 7, 4, True, 'Defolt']
mutable_list[3]= 444
print(mutable_list)