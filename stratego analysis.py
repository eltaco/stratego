# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:40:19 2016

@author: Alexandros
"""

import pandas as pd
from collections import Counter
df = pd.read_csv('C:/Users/Alexandros/Desktop/stratego.csv',names=['player1','player2','result','tournament','date'])

player_name_list_1 = list(df['player1'])
player_name_list_2 = list(df['player2'])
tournament = list(df['tournament'])
dates = list(df['date'])

player_names = set(player_name_list_1 + player_name_list_2)

players_dict = dict()
for player_name in player_names:
    players_dict[player_name] = [0, 0, 0]

for index, values in df.iterrows():
    player1 = values[0]
    player2 = values[1]
    result = values[2]

    if result == '1':
        players_dict[player1][0] += 1
        players_dict[player2][2] += 1
    elif result == '0,5':
        players_dict[player1][1] += 1
        players_dict[player2][1] += 1
    elif result == '0':
        players_dict[player1][2] += 1
        players_dict[player2][0] += 1

players_and_results = sorted(players_dict.items(), key=lambda x: x[1])
#print (players_and_results)
question = input("Tell me a player please: ")
print()
if question in (player_name_list_1):
    print (players_dict[question])
    print
else:
    print("bad")
#print (Counter(tournament))
#print (Counter(dates))