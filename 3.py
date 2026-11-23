def powitanie(imie="uzytkowniku", jezyk="polski"):
    if jezyk == "polski":
        print("czesc,", imie)
    elif jezyk == "angielski":
        print("hello,", imie)
    elif jezyk == "niemiecki":
        print("guten morgen,", imie)
    else:
        print("witaj,", imie)


powitanie()
powitanie("anna", "polski")
powitanie("john", "angielski")
powitanie("hans", "niemiecki")
powitanie("adam", "francuski")