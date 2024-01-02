import random

def make():
    letter=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers=['0','1','2','3','4','5','6','7','8','9','0']
    symbols=['!','#','$','%','&','(',')','*','+']
    no_letters=random.randint(8,10)
    no_symbols=random.randint(2,4)
    no_numbers=random.randint(2,4)

    password_list=[]

    password_list=[random.choice(letter) for item in range(no_letters)]
    password_list+=[random.choice(symbols) for item in range(no_symbols)]
    password_list += [random.choice(numbers) for item in range(no_numbers)]

    random.shuffle(password_list)
    password="".join(password_list)
    # for char in password_list:
    #     password+=char
    return password
