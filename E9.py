def  even_odd_number(num):
    if num & 1 == 0:
        print("The a given number is even")
        return "even"
    else:
        print("The a given number is odd")
        return "odd"


even_odd_number(8)
even_odd_number(5)


def set_bits(num):
    counter = 0
    while num != 0:
        num &= (num - 1)
        counter += 1
    return counter


print("The number of set bits is" ,set_bits(7))
print("The number of set bits is" ,set_bits(4))
print("The number of set bits is" ,set_bits(15))