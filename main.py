import os
from country_code import get_country_code
from transfer_wise import get_converted


def input_num():
    while True:
        try:
            num = int(input("#: "))
            return num
        except:
            print("That wasn't a number")


def get_code(num):
    return country_code[num]['code']


def check_in_list(num):
    if num >= len(country_code):
        print("Choose a number from the list.")
        return False
    else:
        return True


codes = []


def get_codes():
    if len(codes) == 0:
        while True:
            num = input_num()
            if check_in_list(num):
                break
        codes.append(get_code(num))
        print(f"{country_code[num]['country']}")
        print("Now choose another country\n")
        get_codes()
    elif len(codes) == 1:
        while True:
            num = input_num()
            if check_in_list(num):
                break
        codes.append(get_code(num))
        print(f"{country_code[num]['country']}")
    return codes


os.system('clear')

country_code = get_country_code()

print("Hello! Please choose select a country by number: ")

for index in range(len(country_code)):
    print(f"# {index} {country_code[index]['country']}")

print("Where are you from? Choose a country by number.\n")

source_code, target_code = get_codes()

print(f"\nHow many {source_code} do you want to convert to {target_code}")
amount = input_num()

converted_amount = get_converted(source_code, target_code, amount)

if converted_amount:
    print(f"\n{source_code}{amount:,} is {target_code}{float(converted_amount):,}")
