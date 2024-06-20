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
    string = """1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!"""
    string_2 = """2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!"""
    i = 0
    added = ""
    if bottles == 1:
        print(string)
    elif bottles == 2:
        print(string_2)
    else:
        for i in range(0,bottles - 2):
            adder = f"""{bottles - i} bottles of beer on the wall, {bottles - i} bottles of beer.
Take one down, pass it around, {bottles - 1 - i} bottles of beer on the wall.\n\n"""
            added = added + adder
            i = i + 1
        print(added+string_2)

