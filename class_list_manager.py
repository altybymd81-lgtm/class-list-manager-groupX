# Class List Manager - Group __
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Majd Al-Otaibi (Task 1)
def count_names(names):
    return len(names)


def main():
  print("Welcome to the Class List Manager!")
  print("Class list:", names)
  print("Number of names:", count_names(names))


main()
