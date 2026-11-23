def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    print("twoje bmi wynosi:", round(bmi, 2))

    if bmi < 18.5:
        print("niedowaga")
    elif bmi < 25:
        print("pozadana masa ciala")
    elif bmi < 30:
        print("nadwaga")
    elif bmi < 35:
        print("otylosc i stopnia")
    elif bmi < 40:
        print("otylosc ii stopnia")
    else:
        print("otylosc iii stopnia")

    return bmi


waga = float(input("podaj wage w kg: "))
wzrost = float(input("podaj wzrost w metrach: "))

oblicz_bmi(waga, wzrost)