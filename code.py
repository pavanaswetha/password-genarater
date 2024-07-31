import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "/", "/", "?", "|"]
print("Welcome to Password Generator \n")
n_letters = int(input("Enter how many letters you want in your password: "))
n_numbers = int(input("Enter how many numbers you want in your password: "))
n_symbols = int(input("Enter how many symbols you want in your password: "))
password = ""
for num in range(n_letters):
    char = random.choice(letters)
    password += str(char)

for num in range(n_numbers):
    char = random.choice(numbers)
    password += str(char)

for num in range(n_symbols):
    char = random.choice(symbols)
    password += str(char)

print(password)
password_list = list(password)
random.shuffle(password_list)
finally_password = ''.join(password_list)
print(f"The password after shuffling is ",{finally_password}) 
