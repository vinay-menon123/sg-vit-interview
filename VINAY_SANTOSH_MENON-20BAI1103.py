#VALIDATING PASSWORD POLICY


def check_num_char(s):
    count_num = 0
    count_char = 0
    for i in s:
        if i in num:
            count_num+=1
        if i in char:
            count_char+=1
    if(count_num>=5 and count_char>=1):
        return True
    return False

def check_spec_char(s):
    count_spec = 0
    for i in s:
        if i in spec_char:
            count_spec+=1
    if(count_spec>=2):
        return True
    return False

s  = input()

#check_num_char checks if the string contains at least 5 numbers and 1 letter.
#check_spec_char checks if the string contains at least 2 special characters.

char = set()
num = set()
for i in range(96,122):
    char.add(chr(i))
for i in range(10):
    num.add(str(i))
spec_char = set(['#','$','%','^','&'])

if(check_num_char(s)):
    if(check_spec_char(s)):
        print("Good password")
    else:
        print("Not enough special characters.")
else:
    print("The above password does not meet the minimum number or minimum character requirement.")
