import random
import string
sample = []
def password_strength_checker(user_pass_word, yrn):
    if yrn == True:
        password = user_pass_word
    else:
        print("Welcome to Password Strength Checker")
        password = input("Enter Password for testing: ")
    pass_len = len(password)
    letter_count = {}
    is_al = []
    case_li = []
    sp_li = []
    space = []
    for i in password:
        if i not in letter_count:
            letter_count[i] = 1
        else:
            letter_count[i] += 1

        if i.isnumeric():
            is_al.append(True)
        else:
            pass
        
        if i.isupper():
            case_li.append(True)
        else:
            pass

        if i in "!@#$%^&*()_+-=[]}{\|;:,./<>?`~":
            sp_li.append(True)
        else:
            pass
        if i ==  ' ':
            space.append(True)

        else:
            pass

    def checker():
        # Password strength checker
        total = [] # All numbers are out of 5
        def len_check():
            if pass_len < 3:
                print("Strength of password(Length): VERY WEAK")
                total.append(1)

            elif pass_len < 5 and pass_len > 3:
                print("Stength of password(Length): WEAK")
                total.append(2)

            elif pass_len < 8 and pass_len > 5:
                print("Stength of password(Length): ACCEPTABLE")
                total.append(3)

            elif pass_len < 13 and pass_len > 8:
                print("Stength of password(Length): STRONG")
                total.append(5)

            elif pass_len < 17 and pass_len > 13:
                print("Stength of password(Length): VERY STRONG")
                total.append(5)
            else:
                print("Strength of password(Length): EXTREMELY STRONG")
                total.append(5)

        def num_check():

            if len(is_al) == 2:
                print("Expected more than 2 numbers in the password")
                total.append(4)
            elif len(is_al) == 1:
                print("Expected more than 2 numbers in the password")
                total.append(2)
            elif len(is_al) == 0:
                print("Expected more than 2 numbers in the password")
                total.append(0)
            else:
                total.append(5)

        def upper_check():
            if len(case_li) < 1:
                print("Atleast 1 upper case letter to be used")
                total.append(0)
            else:
                total.append(5)

        def special_check():
            if len(sp_li) < 1:
                print("Atleast one special charecter to be used")
                total.append(0)
            else:
                total.append(5)
                
        def space_check():
            if len(space) >=  1:
                print("Spaces are not allowed in the password")
                total.append(0)
            else:
                total.append(5)

        len_check()
        num_check()
        upper_check()
        special_check()
        space_check()
        total_sum = 0
        for i in total:
            total_sum += i
        total_percent = ((total_sum/len(total)*5)*10)/2.5

        print(f"Total Acceptance rate: {total_percent}%")
        try:
            sample.clear()
        except:
            pass
        sample.append(total_percent)   

    checker()

def password_maker():
    print("A Strong password will be generated soon...")
    list_pass = []
    def pass_make():
        for i in range(17):
            ran = random.choice(string.ascii_letters + string.digits + "!@$%&_")
            list_pass.append(ran)
    pass_make()
    password_strength_checker("".join(list_pass), True)
    if sample[0] > 90:
        print("Password: " + "".join(list_pass))
    else:
        password_maker()

print("Welcome to USER PASSWORD")
user_text = """
Enter 1 for Password strength checker.
Enter 2 for Password generator : """
user_input = input(user_text)
if user_input == '1':
    password_strength_checker(1,False)
elif user_input == '2':
    password_maker()