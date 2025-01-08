from module import module_first as mod_f
from module import module_second as mod_s 

usrInput = input("Введите текст")

print(f'Функция первого модуля выводит: {mod_f.HelloMTUCI()}')
print(f'Функция второго модуля выводит: {mod_s.texting(usrInput)}')
