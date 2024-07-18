import random
import string

def gen_pass():
    print("###Password Generator###\n")

    inc_lower = input("1/5. Include Small Letters(0/1): ").strip()
    inc_upper = input("2/5. Include Capital Letters(0/1): ").strip()
    inc_digits = input("3/5. Include Integers(0/1): ").strip()
    inc_special = input("4/5. Include Special Characters(0/1): ").strip()

    pattern = inc_lower + inc_upper + inc_digits + inc_special
    if pattern == "0000":
        print("\nError: Nothing selected to create password.")
        return

    length = int(input("5/5. Max Length Of Password: "))

    create_pass(length, pattern)

    print("END")
    return

def create_pass(length, pattern):
    pwd = ""
    chars_left = length

    # getting occurrences of each included character
    count_lower = 0
    count_upper = 0
    count_digits = 0
    count_special = 0

    if int(pattern[0]) == 1:
        count_lower = random.randint(0, chars_left)
        chars_left -= count_lower

    if int(pattern[1]) == 1:
        count_upper = random.randint(0, chars_left)
        chars_left -= count_upper

    if int(pattern[2]) == 1:
        count_digits = random.randint(0, chars_left)
        chars_left -= count_digits

    if int(pattern[3]) == 1:
        count_special = random.randint(0, chars_left)
        chars_left -= count_special

    # creating password
    pwd = (
        pwd
        + "".join(random.sample(string.ascii_lowercase, k=count_lower))
        + "".join(random.sample(string.ascii_uppercase, k=count_upper))
        + "".join(random.sample(string.digits, k=count_digits))
        + "".join(random.sample(string.punctuation, k=count_special))
    )

    # shuffling the characters
    pwd_list = list(pwd)
    random.shuffle(pwd_list)
    pwd = "".join(pwd_list)

    print("\nPassword: ", pwd)

    recreate = input("Recreate Password?(0/1): ")
    if recreate == "1":
        create_pass(length, pattern)

    return

gen_pass()
