# Assessment 3.2: Stack (LIFO) Program
# Last Name: MAYOR

name = "MAYOR"
stack = []

print("--- PUSHING LETTERS ONTO STACK ---")
for letter in name:
    stack.append(letter)
    print(stack)

print("\n--- POPPING LETTERS FROM STACK ---")
while len(stack) > 0:
    stack.pop()
    if len(stack) == 0:
        print("[EMPTY]")
    else:
        print(stack)