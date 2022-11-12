# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# через list comprehension
n = input('Enter number N = ')
z = n.replace(',', '')
print(list(z))
sum_item = sum(list(int(i) for i in z))
print(sum_item)
