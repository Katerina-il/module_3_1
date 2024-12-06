calls = 0



def count_calls():

global calls

calls += 1



count_calls()



def string_info(string):

count_calls()

b = len(string)

lowercase_string = string.lower()

uppercase_string = string.upper()



string_1 = (b, lowercase_string, uppercase_string)

return string_1



def is_contains(string, list_to_search):

count_calls()

lowercase_string = string.lower()

lower_list_to_search = [x.lower() for x in list_to_search]

return lowercase_string in lower_list_to_search


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)