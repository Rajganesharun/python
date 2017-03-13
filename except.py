while True:
    try:


        number = int(input("enter any number you like to try this game ..\n"))
        print(18/number)
        break

    except ValueError:
        print("lol entre a number ")

    except ZeroDivisionError:
        print("lol dont enter zero be a hero ffs")
    finally:
        print("loop out")



