def factorial_number(num):
    if num == 1:
        return 1
    else:
        return num * factorial_number(num - 1)


print(factorial_number(5))

def permutations(str, current=""):
    for i in range(len(str)):
        current_char = str[i]
        remaining_chars = str[:i] + str[i + 1:]
        permutations(remaining_chars, current + current_char)
    if not str:
        print(current)

permutations("abc")