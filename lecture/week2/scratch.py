def func6(var6):
    var6 += " world"
    print(var6, "from func6") 
var6  = "hello"
func6(var6)
print(var6, "from indent level 0") 
print("=" * 45)



string1 = "I am a string"
print(string1[3])
tuple1 = (1, 2, 3)
print(tuple1[2])

print("=" * 45)

def change_it(the_list):
    the_list.append('d')
g_list = ['a', 'b', 'c']
change_it(g_list)
print(g_list) # prints "['a', 'b', 'c', 'd']"

print("=" * 45)

def dict_update(local_dict):
    local_dict['g'] = 'grapefruit'
    local_dict['n'] = 'nectarine'
global_dict = {'g': 'grape', 'p': 'plum', 'o': 'orange'}
dict_update(global_dict)
print(global_dict['g'])
print(global_dict['n'])
print(global_dict['p'])

print("=" * 45)

def list_remind(message, data):
    print('2', message, data[-1])
    message = 'don\'t forget!'
    data.append('eggs')
    print('3', message, data[-1])

groceries = ['milk', 'bread']
reminder = 'please pick up'
print('1', reminder, groceries[-1])
list_remind(reminder, groceries)
print('4', reminder, groceries[-1])