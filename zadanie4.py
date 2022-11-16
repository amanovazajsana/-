Яманова Зайсана 21-ИС 15.11.2022
#Задание 4. If15.Даны три числа.Найти сумму двух наибольших из них.
a=int(input())
b=int(input())
c=int(input())

 if (a <= b and b <= c) or (a <= c and a <= b):
       m=b+c
 elif (b <= a and a <= c) or (b <= c and c <= a):
       m=c+a
 elif (c <= b and b <= a) or (c <= a and a <= b):
       m=b+a