# @@ -0,0 +1,48 @@
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:40:19 2016

@author: Alexandros
"""
import datetime
import pandas as pd
df = pd.read_csv('C:/Users/Alexandros/Desktop/stratego-2.csv', names=['player1', 'player2', 'result', 'tournament', 'date'])
player_name_list_1 = list(df['player1'])
player_name_list_2 = list(df['player2'])
tournament = list(df['tournament'])
date = list(df['date'])
for day in date[1:]:
    day = str(day)
    day = datetime.datetime.strptime(day, "%d/%m/%Y").strftime("%Y-%m-%d")
    
"""above there was an error about not reading 'nan'. Apparently I forgot to add a couple of dates..."""
result = list(df['result'])
player_names = set(player_name_list_1 + player_name_list_2)
players_dict = dict()
for player_name in player_names:
    players_dict[player_name] = [0, 0, 0]

for index, values in df.iterrows():
    player1 = values[0]
    player2 = values[1]
    results = values[2]

    if results == '1':
        players_dict[player1][0] += 1
        players_dict[player2][2] += 1
    elif results == '0,5':
        players_dict[player1][1] += 1
        players_dict[player2][1] += 1
    elif results == '0':
        players_dict[player1][2] += 1
        players_dict[player2][0] += 1

players_and_results = sorted(players_dict.items(), key=lambda x: x[1])
# print (players_and_results)
question = input("Tell me a player please: ")
question_chart = []
for position, item in enumerate(player_name_list_1):
    if item == question:
        event = player_name_list_2[position], result[position],tournament[position], date[position]
        question_chart.append(event)
for position, item in enumerate(player_name_list_2):
    if item == question:
        if result[position] == '1':
            result[position] = '0'
        elif result[position] == '0':
            result[position] = '1'
        event = player_name_list_1[position], result[position],tournament[position], date[position]
        question_chart.append(event)
else:
    print("Ready")
print(question_chart)
