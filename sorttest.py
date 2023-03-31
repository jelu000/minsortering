import random
import sortmodule

looping = True
listnumbers = []

for tnum in range(5):
    tslumptal = random.randint(0, 100)
    listnumbers.append(tslumptal)
    print(tslumptal)

while looping:

    val =  sortmodule.create_menu()

    if (val == "1"):
        print("\nSkriver ut lista med slumpade tal-----------")
        
        
        sortmodule.print_list_numbers(listnumbers)
        nysorterad_listnumbers = sortmodule.bubble_sort(listnumbers)
        print("SORTERAR")
        sortmodule.print_list_numbers(nysorterad_listnumbers)
        fortsatt = input("\nVill du fortsätta? j/n ")
        if(fortsatt == "n"):
            break

    elif (val == "2"):
        print("\n-Skriver listnumbers med slumpade tal-------------------")
        listnumbers2 = listnumbers
        sortmodule.print_list_numbers(listnumbers)
        print("\n-Sorterar med python sort-------------------")
        listnumbers2.sort()
        sortmodule.print_list_numbers(listnumbers2)

        fortsatt = input("\nVill du fortsätta? j/n ")
        if(fortsatt == "n"):
            break
    else:
        break