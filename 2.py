# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Программа для удаления из текста слов, содержащих 'абв'
#  через filter
text = 'абвтория как приабвкзал, есть абв'

new_text = list(filter(lambda x: 'абв' not in x, text.split()))
print(new_text)
