print("WELCOME TO A SIMPLE MENSURATION PROGRAM")
while True:
    print("\nMAIN MENU")
    print("1. Check Palindrome")
    print("2. Check Armstrong")
    print("3. Exit")
    choice1 = int(input("Enter the Choice:"))
    if choice1 == 1:
        print("1.string")
        print("2.Number")
        print("3.Exit")
        choice2 = int(input("Enter the Choice"))
        if choice2 == 1:
            str = input("Enter string:")
            first, last = 0, len(str) - 1
            while first < last:
                if str[first] == str[last]:
                    first += 1
                    last -= 1
                else:
                    print("The string is a palindrome!")
            else:
                print("The string is palindrome")
        elif choice2 == 2:
            n = int(input("Enter number:"))
            temp = n
            rev = 0
            while n > 0:
                dig = n % 10
                rev = rev * 10 + dig
                n = n // 10
            if temp == rev:
                print("The number is a palindrome!")
            else:
                print("The number isn't a palindrome!")
        elif choice2 == 3:
            break
        else:
            print("oppss,wrong choice")
    elif choice1 == 2:
        n = int(input("Enter Number:"))
        temp = n
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 3
            n = n // 10
        if temp == sum:
            print("The number is Armstrong")
        else:
            print("The Number is not Armstrong")
    elif choice1 == 3:
        break
    else:
        print("oppsss,wrong choice")
