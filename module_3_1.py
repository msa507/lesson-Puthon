from http.cookiejar import uppercase_escaped_char
calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    capy = string[0:8]
    arm = string[8:]
    upper_capy = capy.upper()
    lower_capy = capy.lower()
    upper_arm = arm.upper()
    lower_arm = arm.lower()
    a = (len(capy), upper_capy, lower_capy)
    b = (len(arm), upper_arm, lower_arm)
    print(a)
    print(b)


def is_contains(string, list_to_search):
    count_calls()
    str = list(string)
    str1 = string[0]
    str1 = str1.lower()
    str2 = string[1]
    str2 = str2[0:3]
    str2_low = [str2_low.lower() for str2_low in str2]
    if str1 in str2_low:
        print('True')
    else:
        print('False')
    count_calls()
    lis = list(list_to_search)
    lis1 = string[0]
    lis1 = lis1.lower()
    lis2 = string[1]
    lis2 = lis2[0:2]
    lis2_low = [lis2_low.lower() for lis2_low in lis2]
    if lis in list_to_search:
        print('True')
    else:
        print('False')


count_calls()
string_info('Capybara''Armageddon')
is_contains(('Urban', ['ban', 'BaNaN', 'urBAN']),('cycle', ['recycling', 'cyclic']))
print(calls)
