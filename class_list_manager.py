# Class List Manager - Group __
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Majd Al-Otaibi (Task 1)
def count_names(names):
    return len(names)

# Written by: Joud Bin-Alsheikh(Task 3)
def search_name(names, name):
    if name in names:
        return True
    else:
        return False

# Written by: Jana Alshamrani (Task 4)
def remove_duplicates(names):
    new_list = []

    for name in names:
        if name not in new_list:
            new_list.append(name)

    return new_list
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Names without duplicates:", remove_duplicates(names))

main()
