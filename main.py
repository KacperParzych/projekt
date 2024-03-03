import sys

# # Typy danych
# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# ZmiennaTekstowa = 'Wizualizacja danych'
# print(ZmiennaTekstowa)
# print(type(ZmiennaTekstowa))
#
# # Dzialania matemtyczne
#
# Liczba1 = 6
# Liczba2 = 3
#
# Wynik=Liczba1+Liczba2
# print(Wynik)
# Wynik2=Liczba1-Liczba2
# print(Wynik2)
#
# Liczba3 = 4
# Wynik3=Liczba2//Liczba1
# print(Wynik3)
#
# Wynik4 = Liczba1//Liczba2
# print(Wynik4)
#
# Wynik5 = Liczba1**2
# print(Wynik5)
#
# Wynik6 = pow(6 , 1/2)
# print(Wynik6)
#
# Wynik7 = 6**(1/2)
# print(Wynik7)
#
# # Zmienne tekstowe
#
# Zmienna1 = 'Wizualizacja danych0'
# Zmienna2 = ' grupa 1'
# Zmienna3 = 1
# print(Zmienna1+Zmienna2)
# print('Liczba1 jest rowna {:.2f}, liczba2 jest rowna {:d}'
#       .format(Liczba1, Liczba2))
#
# a = input('Wprowadz liczbe: ')
# print(a)
# print(type(a))
# print(a*5)
# print(type(a))
#
# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline()
# print(b)
# print(type(b))

# lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2, 'c')
# print(lista)
# lista.extend([20, 21, 22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2, 3, 4])
# print(lista)
# del lista[1]
# print(lista)
# # del lista
# lista.reverse()
# print(lista)
# lista.sort() # Nie moze porownywac inta z stringiem
# print(lista)

# slownik = {'klucz': 'wartosc', 1: 2, 'a': 5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
# print(slownik)

# a = 8
# b = 8
#
# if a > b:
#       print("a is greater than b")
# elif a < b:
#       print("a is less than b")
# else:
#       print("a is equal to b")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a > b) | (c > d):
      print(a, c)
else:
      print(b, d)