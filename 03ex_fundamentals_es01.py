

def convert(n):
    if ord(n[1]) == 120:
        print("converst is: ", int(n , 16))
    elif ord(n[1]) == 98:
        print("converst is: ", int(n , 2))
    else:
        n = int(n)
        print("The hex is: ", hex(n))
        print("The bin is: ", bin(n))

i = input("enter: ")

convert(i)
