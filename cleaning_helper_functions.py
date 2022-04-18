

def player_df_cleanup(row, name):
    """
    Helper function to transform our with our player's name in each column into just a df of their opponents' info
    Returns a row as a list with relevant information
    """
    new_row = []

    if row[0] == name: # player plays white
        new_row.append(row[1]) # opp
        new_row.append('white') # opp color (1 is black)
        new_row.append(row[3]) # opp rating
        new_row.append(row[2]) # player rating
    else: # plyaer plays black
        new_row.append(row[0]) # opp
        new_row.append('black') # opp color (1 is black)
        new_row.append(row[2]) # opp rating
        new_row.append(row[3]) # player rating

    # if wp == name: # player plays white
    #     new_row.append(bp) # opp
    #     new_row.append(1) # opp color (1 is black)
    #     new_row.append(bpr) # opp rating
    #     new_row.append(wpr) # player rating
    # else: # plyaer plays black
    #     new_row.append(wp) # opp
    #     new_row.append(0) # opp color (0 is white)
    #     new_row.append(wpr) # opp rating
    #     new_row.append(bpr) # player rating
    
    return new_row