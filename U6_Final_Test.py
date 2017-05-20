#Final Project Description
#Congratulations on making it to the final project! Your job is to take simple text strings #like "Alex likes Carla, Ryan, and Priya" and turn them into a social network_tim. To do this, #you must complete a number of required procedures, as described on the next screen. You must #also create a "make-your-own" procedure.

#Most of this project will take place inside the browser and most of it will be auto-graded. #Feel free to share your final code with your peers in the Discussion Forum for additional #feedback.

#If you have any questions, ask on the Discussion Forum!

# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network_tim site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network_tim information 
# and to define several procedures that operate on the network_tim. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network_tim. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 
example_input2 = ""
# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network_tim information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network_tim with no users.
# 
# Return:
#   The newly created network_tim data structure
def create_data_structure(string_input):
    master_list = {}
    current = 0
    n = 0
    while True:
        if string_input.find('.',current) == -1:
            return master_list
        line = string_input[current:string_input.find('.', current)] # Get Next Line
        name = line[0:line.find(' ',0)] # Get Name in Line
        if name not in master_list:
            master_list[name] = {}  # If name not in master yet
        if line.find('connected') > 0:
            master_list[name]['Connections'] = line[line.find('connected')+13:len(line)].split(', ')
        if line.find('play') > 0:
            master_list[name]['Games'] = line[line.find('play')+5:len(line)].split(', ')
        current = string_input.find('.', current) + 1

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network_tim' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network_tim'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network_tim, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network_tim: the gamer network_tim data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network_tim, return None.

def get_connections(network_tim, user):
    if user in network_tim:
        if 'Connections' in network_tim[user]:
	        return network_tim[user]['Connections']
        else:
            return []
    else:
        return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network_tim, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network_tim: the gamer network_tim data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network_tim, return None.
def get_games_liked(network_tim,user):
    if user in network_tim:
        if 'Games' in network_tim[user]:
	        return network_tim[user]['Games']
        else:
            return []
    else:
        return None

# ----------------------------------------------------------------------------- 
# add_connection(network_tim, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network_tim.
# 
# Arguments: 
#   network_tim: the gamer network_tim data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network_tim with the new connection added.
#   - If a connection already exists from user_A to user_B, return network_tim unchanged.
#   - If user_A or user_B is not in network_tim, return False.
def add_connection(network_tim, user_A, user_B):
    if user_A in network_tim and user_B in network_tim:
        if user_B in network_tim[user_A]['Connections']:
            return network_tim
        network_tim[user_A]['Connections'].append(user_B)
        return network_tim
    else:
        return False
	#return network_tim

# ----------------------------------------------------------------------------- 
# add_new_user(network_tim, user, games): 
#   Creates a new user profile and adds that user to the network_tim, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network_tim: the gamer network_tim data structure
#   user:    a string containing the name of the user to be added to the network_tim
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network_tim with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network_tim, return network_tim *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network_tim, user, games):
    if user in network_tim:
        return '*UNCHANGED*'
    else:
        network_tim[user] = {}
        network_tim[user]['Games'] = games
        network_tim[user]['Connections'] = []
    return network_tim
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network_tim, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network_tim: the gamer network_tim data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network_tim, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network_tim, user):
    second_connects = []
    if user in network_tim:
        if 'Connections' in network_tim[user]:
            for element in network_tim[user]['Connections']:
                for item in network_tim[element]['Connections']:
                    if item not in second_connects:
                        second_connects.append(item) 
        return second_connects
    else:
        return None


# ----------------------------------------------------------------------------- 	
# count_common_connections(network_tim, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network_tim: the gamer network_tim data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network_tim, return False.
def count_common_connections(network_tim, user_A, user_B):
    if user_A in network_tim and user_B in network_tim:
        count = 0
        if 'Connections' not in network_tim[user_A]:
            return count
        if 'Connections' not in network_tim[user_B]:
            return count
        for element in network_tim[user_A]['Connections']:
            if element in network_tim[user_B]['Connections']:
                count = count + 1
        return count
    else:
        return False    
    

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network_tim, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network_tim: The network_tim you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network_tim, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network_tim, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network_tim, user_A, and user_B.

def find_path(current, network_tim, user_A, user_B):
    if user_A == user_B:
        return True, [user_B]
    res = []
    for connection in network_tim[user_A]['Connections']:
        if connection not in current:
            current[connection] = False
        if not current[connection]:
            current[connection] = True
            rec = find_path(current, network_tim, connection, user_B)
            if rec[0]:
                return True, [user_A] + rec[1]
            current[connection] = False
    return False, None


def find_path_to_friend(network_tim, user_A, user_B):
    if user_A not in network_tim:
        return None
    current = {user_A: True}
    res = find_path(current, network_tim, user_A, user_B)
    if res[0]:
        return res[1]
    return None
    
        

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network_tim data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network_tim (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!
# COMMENT TIM
# Procedure to add, who has the most connections
# Who plays a particular game
# etc. Data analysis stuff.

# This was a simple procedure to print user data for people in the network_tim.
# You can print the entire network_tim by passing in '[]' for user
# If user not in network_tim it will return "Is Not in Network"
def print_net(net,users):
    print '----------------------------------'
    if len(users) == 0:
        for element in net:
            users.append(element)
    for element in users:
        print 'name:', element
        if element in net:
            for item in net[element]:
                print item, ':', net[element][item]
            print '-------------'
        else:
            print 'Is Not In Network'
            print '-------------'  
                      
# This was a simple procedure to print headers.    It does nothing with the date  
def print_header(header,action):
    if action == 'header':
        print ' '
        print '*************************************************************'
        print header
        print '*************************************************************' 
    if action == 'line':
        print ' '
        line_out = '- ' + header + ' -'
        count = len(line_out)
        while count < 61:
            line_out = line_out + '-'
            count = len(line_out)
        print line_out
 
# This procedure determines the games played, the ranking of the games played,
# and the users who play them. 
# It prints the ordered list of games and who plays along with the highest 
# ranked game at the bottom.
# There are many more things I could think to analyze and write code for,
# but wanted to get this turned in and keep working on next classes.     
def game_count(network_tim):
    games = {}
    best_game = ''
    for element in network_tim:
        game_list = []
        if 'Games' in network_tim[element]:
            game_list = network_tim[element]['Games']
            for game in game_list:
                if game in games:
                    games[game]['count'] = games[game]['count'] + 1
                    games[game]['players'].append(element)
                else:
                    games[game] = {}
                    games[game]['count'] = 1
                    games[game]['players'] = [element]
    highest_rank = 0
    for element in games:
        if games[element]['count'] > highest_rank:
            highest_rank = games[element]['count']
            best_game = element 
    n = 0
    if len(games) == 0:
        print '* No Games In Network *'
        return None
    while n <= highest_rank:
        for element in games:
            if games[element]['count'] == n:
                print '-----------------------------------------'
                print games[element]['count'], 'players chose: "', element, '"'
                print 'played by:', games[element]['players']
        n = n + 1
    print '-----------------------------------------'
    print 'And the Highest Ranked Game Is ----------'
    print best_game, '--- with:', games[best_game]['count'], 'players'   
    return games, best_game
            
            
        

# ------------------------------------------
print_header('BUILD THE NETWORK','header')
net = create_data_structure(example_input)
# ------------------------------------------
print_net(net,[])
# ------------------------------------------
print_header('GET CONNECTIONS','header')
print_header('Connections for Debra', 'line')
print get_connections(net, "Debra")
print_header('Connections for Mercedes', 'line')
print get_connections(net, "Mercedes")
print_header('Connections for oinker', 'line')
print get_connections(net,"oinker")
print_header('Connections for Kathy (who has no connections)', 'line')
print get_connections(net,"Kathy")
# ------------------------------------------
print_header('GET GAMES','header')
print_header('Games For John', 'line')
print get_games_liked(net, "John")
print_header('Games For Oinker (who is not in the network_tim)', 'line')
print get_games_liked(net, "oinker") 
print_header('Games For Franklin who has no games', 'line')
print get_games_liked(net, "Franklin") 
# ------------------------------------------
print_header('ADD CONNECTION','header')
print_header('Add Connection from John to Freda', 'line')
print_net(net,['John'])
print_header('Function to add Freda to John', 'line')
print add_connection(net, "John", "Freda")
print_net(net,['John'])
print_header('Add Connection from John to Oink', 'line')
print add_connection(net, "John", "Oink")
print_net(net,['John'])
print_header('Add Connection from John to Bryant (Who John is already connection)', 'line')
print add_connection(net, "John", "Bryant")
print_net(net,['John'])
# ------------------------------------------
print_header('ADDING USERS','header')
print_header('Add user Debra (who already exists)','line')
print add_new_user(net, "Debra", []) 
print_net(net,['Debra'])
print_header('Add user Nick with Games','line')
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print_net(net,['Nick'])
# ------------------------------------------
print_header('GET SECONDARY CONNECTIONS','header')
print_header('Seconday_connections for Mercedes','line')
print_net(net,['Mercedes'])
print_net(net,['Walter', 'Robin', 'Bryant'])
print get_secondary_connections(net, "Mercedes")
print_header('Seconday_connections for Kathy who has no connections','line')
print get_secondary_connections(net, "Kathy")
print_header('Seconday_connections for Kathy who has no connections','line')
print get_secondary_connections(net, "Kathy")
# ------------------------------------------
print_header('GET COMMON CONNECTIONS COUNT','header')
print_header('Common Connections for John and Mercedes','line')
print count_common_connections(net, "Mercedes", "John")
print_net(net,['Mercedes', 'John'])
print_header('Common Connections for Freda and Bryant','line')
print count_common_connections(net, "Freda", "Bryant")
print_net(net,['Freda', 'Bryant'])
print_header('Common Connections for Bryant and oink','line')
print count_common_connections(net, "Bryant", "Oink")
print_net(net,['Freda', 'Oink'])
print_header('Common Connections for Bryant and Kathy(who has no connections)','line')
print count_common_connections(net, "Bryant", "Kathy")
print_net(net,['Bryant', 'Kathy'])
# ------------------------------------------
#print_header('FIND PATH TO BETWEEN CONTACTS','header')
#print_header('Path Between John and Ollie','line')
#print find_path_to_friend(net, "John", "Ollie")
#print_header('Path Between John and Kathy(who has no connections)','line')
#print find_path_to_friend(net, "John", "Kathy")
print_header('Path Between Ollie and Jennie','line')
print find_path_to_friend(net, "Ollie", "John")
#print_header('Path Between John and Bryant','line')
#print find_path_to_friend(net, "John", "Bryant")

# ------------------------------------------
print_header('MYOP - Game Count','header')
#game_count(net)
print add_new_user(net, 'Alice', [])
print_net(net,['Alice'])
print get_connections(net,'Alice')