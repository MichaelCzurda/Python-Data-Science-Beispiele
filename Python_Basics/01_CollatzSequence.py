def collatz(number):
    if (number%2)==0:
        print(int(number / 2))
        return number / 2
    else:
        print(int(3*number+1))
        return (3*number+1)

running=True
while running:
    try:
        number = input("Nummer eingeben: ")
        if number == 'exit':
            sys.exit()
        else:
            number=int(number)
            running = False
    except:
        print("Das war keine Zahl. Erneut eingeben")
    
    
while number != 1:
    number = collatz(number)
    
