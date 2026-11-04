# Assessment 3.2: Array Program
# Last Name: MAYOR

name = "MAYOR"
arr = []

print("--- ADDING LETTERS TO ARRAY ---")
for letter in name:
    arr.append(letter)
    print(arr)

print("\n--- REMOVING LETTERS FROM ARRAY ---")
while len(arr) > 0:
    arr.pop()
    if len(arr) == 0:
        print("[EMPTY]")
    else:
        print(arr)