# @@ -0,0 +1,48 @@
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:40:19 2016

@author: Alexandros
"""
import pandas as pd
def search_player(player):
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
    
df = pd.read_csv('C:/Users/Alexandros/Desktop/stratego - 4.csv', names=['player1', 'player2', 'result', 'tournament', 'date'])
print("Please the list should be in a chronological order")
player_name_list_1 = list(df['player1'])
player_name_list_2 = list(df['player2'])
tournament = list(df['tournament'])
date = list(df['date'])
result = list(df['result'])
question = input("Tell me the first player please: ")
question_2 = input("Tell me the second player please: ")
question_chart = []
# Below the programme looks over the data to spot the requested player
search_player(question)
search_player(question_2)

