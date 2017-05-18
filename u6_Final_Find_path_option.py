{'Freda': {'games': ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures'], 'friends': ['Olive', 'John', 'Debra']}, 'Nick': {'games': ['Seven Schemers', 'The Movie: The Game'], 'friends': []}, 'Ollie': {'games': ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game'], 'friends': ['Mercedes', 'Freda', 'Bryant']}, 'Debra': {'games': ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords'], 'friends': ['Walter', 'Levi', 'Jennie', 'Robin']}, 'Olive': {'games': ['The Legend of Corgi', 'Starfleet Commander'], 'friends': ['John', 'Ollie']}, 'Levi': {'games': ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma'], 'friends': ['Ollie', 'John', 'Walter']}, 'Jennie': {'games': ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms'], 'friends': ['Levi', 'John', 'Freda', 'Robin']}, 'Mercedes': {'games': ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures'], 'friends': ['Walter', 'Robin', 'Bryant']}, 'John': {'games': ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner'], 'friends': ['Bryant', 'Debra', 'Walter', 'Freda']}, 'Robin': {'games': ['Call of Arms', 'Dwarves and Swords'], 'friends': ['Ollie']}, 'Bryant': {'games': ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man'], 'friends': ['Olive', 'Ollie', 'Freda', 'Mercedes']}, 'Walter': {'games': ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man'], 'friends': ['John', 'Levi', 'Bryant']}}

And the code is

def find_path(current, network, user_A, user_B):
    if user_A == user_B:
        return True, [user_B]
    res = []
    for connection in network[user_A]['friends']:
        if connection not in current:
            current[connection] = False
        if not current[connection]:
            current[connection] = True
            rec = find_path(current, network, connection, user_B)
            if rec[0]:
                return True, [user_A] + rec[1]
            current[connection] = False
    return False, None


def find_path_to_friend(network, user_A, user_B):
    if user_A not in network:
        return None
    current = {user_A: True}
    res = find_path(current, network, user_A, user_B)
    if res[0]:
        for each in res[1]:
            print network[each]['friends']
        return res[1]
    return None