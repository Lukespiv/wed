letter_count = 0
number_count = 0
def is_letter(char):
    return ("A"<=char.upper() and char.upper()<="Z")
def is_number(char):
    return ("0" <= char and char <= "9")

with open("mydefaults.ini.txt") as file:
    for line in file:
        for char in line:
            if is_letter(char):
                letter_count += 1
            elif is_number(char):
                number_count +=1
                

print(f"total letter count {letter_count}, total number count {number_count}")