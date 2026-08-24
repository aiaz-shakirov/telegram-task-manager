a = input("Введите строку: ")
stack = []
flag = True
for i in a:
    if i in "{[(":
        stack.append(i)
    elif i in "}])":
        if len(stack) == 0:
            flag = False
            break
        cl = stack.pop()
        if cl == "{" and i == "}":
            continue
        if cl == "[" and i == "]":
            continue
        if cl == "(" and i == ")":
            continue
        flag = False
        break
if flag and len(stack) == 0:
    print("Success")
else:
    print("Error")
