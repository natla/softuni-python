name = input("Enter your full name: \n")
name = name.split()

print("Your initials are ", end="")
for word in name:
    if word.isalpha():
        if word[0].isupper():
            print(word[0] + '.', end='')
    else:
        print('invalid. You entered a wrong name.')
        break

