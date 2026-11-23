def potega(a, n):
    if n == 0:
        return 1
    else:
        return a * potega(a, n - 1)


a = float(input("podaj liczbe a: "))
n = int(input("podaj potege n: "))

print("wynik:", potega(a, n))