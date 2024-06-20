def get_starting_number():
    run = True
    while run is True:
        num = input("Enter the number of bottles, an integer please: ")
        if num.isnumeric() is True:
            num = int(num)
            if num >= 1:
                run = False
    return num

def sing(bottles):
    if bottles == 1:
        print("""1 bottle of beer on the wall, 1 bottle of beer.
              Take it down, pass it around, no more bottles of beer on the wall!""")
    elif bottles == 2:
        print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!""")
    else:
        i = 0
        n = True
        while n is True:
            print(f"""{bottles - i} bottles of beer on the wall, {bottles - i} bottles of beer.
Take one down, pass it around, {bottles - 1 - i} bottles of beer on the wall.\n""")
            if i == bottles - 3:
                n = False
                print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.
            
1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!""")
            else:
                i = i + 1
