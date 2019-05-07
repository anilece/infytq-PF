#PF-Exer-28
                                              

def find_winner_of_the_day(*match_tuple):
  
    Team1_count=0
    Team2_count=0
    for i in (match_tuple):
        if (i=='Team1'):
            Team1_count+=1
        elif (i=='Team2'):
            Team2_count+=1
    if Team2_count>Team1_count:
        return ('Team2')
    else:
        return ("Team1")
    


print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))

