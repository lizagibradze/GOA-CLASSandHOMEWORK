


# 1






# 2






# 3






# 4

def string_to_array(s):
    return s.split(" ")





# 5
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p1 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == p2:
       return "Draw!"
    
 ###





# 6
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"





# 7






# 8

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        return [human_years, cat_years, dog_years]

    




# 9






# 10






