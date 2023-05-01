def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f'{i + 1}. {names[i]}')
        i += 1
        

def summon_captain_planet(names):
    list = [f'{name.title()}!' for name in names]
    return list

def long_planeteer_calls(words):
    list = [True for word in words if len(word) > 4 ]
    if list:
        return True
    else:
        return False

def find_the_cheese(lists):
    for list in lists:
        if list == 'cheddar' or list == 'gouda' or list == 'camembert':
            return list
        
