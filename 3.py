# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Example - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# через map
a = [1.1, 1.2, 3.1, 5.3, 10.01]

def show_drob_part (drop_part):
    return round (drop_part % 1, 2)

st = list(map(show_drob_part, a))
print(st)

print (f'Max elements {max(st)} - min element {min(st)} = {max(st) - min(st)}')