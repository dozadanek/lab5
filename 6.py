
import math

def pole_trojkata(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki muszą być większe od zera.")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Z podanych boków nie można utworzyć trójkąta.")

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return pole

    except ValueError as e:
        print("Błąd:", e)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", e)


try:
    a = input("Podaj bok a: ")
    b = input("Podaj bok b: ")
    c = input("Podaj bok c: ")

    wynik = pole_trojkata(a, b, c)

    if wynik is not None:
        print(f"Pole trójkąta wynosi: {wynik:.2f}")

except Exception as e:
    print("blad:", e)
