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
player_name_list_1.pop(0)# some problems on editing made me do it. However I think it's a good exercise in such types of commands
player_name_list_2 = list(df['player2'])
player_name_list_2.pop(0)# the same goes here as well as the other lists
tournament = list(df['tournament'])
tournament.pop(0)
date = list(df['date'])
date.pop(0)
result = list(df['result'])
question = input("Tell me a player please: ")
question_chart = []
for position, item in enumerate(player_name_list_1):
    if item == question:
        event = player_name_list_2[position], result[position],tournament[position], date[position]
        question_chart.append(event)
    elif question==player_name_list_2[position]:
        if result[position] == '1':
            result[position] = '0'
        elif result[position] == '0':
            result[position] = '1'
        event = player_name_list_1[position], result[position],tournament[position], date[position]
        question_chart.append(event)
else:
    print("Ready")
print(question_chart)

