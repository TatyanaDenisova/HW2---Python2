# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions
first = '3/4'
second = '1/5'


f1 = fractions.Fraction(3, 4)
f2 = fractions.Fraction(1, 5)
print('sum with function', f1 + f2)
print('mult with function', f1 * f2)

num1 = first.split('/')
numerator1 = int(num1[0])
denomirator1 = int(num1[1])
num2 = second.split('/')
numerator2 = int(num2[0])
denomirator2 = int(num2[1])

sum_num = numerator1 * denomirator2 + numerator2 * denomirator1
sum_den = denomirator1 * denomirator2
print(f'sum {sum_num}/{sum_den}')

mult_num = numerator1 * numerator2
mult_den = denomirator1 * denomirator2
print(f'mult {mult_num} / {mult_den}')