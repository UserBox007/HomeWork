
calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info(string):
    count_calls ()
    p = (len(string), string.upper(), string.lower())
    return p

def is_contains(string, list_to_search):
    count_calls()
    for s in list_to_search:
        if s.upper() == string.upper():
            return True
    return False


string = "BanaN"
list_to_search =  ['ban', 'BaNaN', 'urBAN']
print(string_info(string))
print(is_contains(string, list_to_search))

string = "Armageddon"
list_to_search =  ['ban', 'BaNaN', 'urBAN', 'recycling']
print(string_info(string))
print(is_contains(string, list_to_search))

print(calls)