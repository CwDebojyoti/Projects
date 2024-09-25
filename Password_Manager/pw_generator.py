import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

letter_list = [random.choice(letters) for letter in range(0, nr_letters)]
symbol_list = [random.choice(symbols) for symbol in range(0, nr_symbols)]
number_list = [random.choice(numbers) for number in range(0, nr_numbers)]

char_list = letter_list + symbol_list + number_list

# print(char_list)
random.shuffle(char_list)
# print(char_list)
final_password = ""

for char in range(0, len(char_list)):
    final_password = final_password + char_list[char]

print(final_password)
