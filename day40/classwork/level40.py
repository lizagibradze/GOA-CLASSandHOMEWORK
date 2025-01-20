


# def friend(x):
#     friends = [] # rom saxelebi shevinaxot
    
#     for name in x:
#         # tu megobris saxeli aris 4 aso mashin megobaria. tu ara mashin ar aris megobari

#         if len(name) == 4:
#             friends.append(name)
#     return friends


# def friend(x):
#     friends = []  # rom saxelebi shevinaxot
#     for person in x:
#         if len(person) == 4:
#             friends.append(person)
#     return friends




#1
def friend(x):
    friends = []  
    for person in x:
        if len(person) == 4:
            friends.append(person)
    return friends

 # for loopit davitvalot 



# def validate_pin(pin):
#     pinn = []
#     for pinnn in pin:
#         if (len(pinnn) == 4 or len(pinnn) == 6) and pin.isdigit():
#             return True
#         else:
#             return False



        
# 2


def validate_pin(pin):

    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
    
    # es marto nomrebze mushaobs







# 2



def validate_pin(pin):

    if len(pin) == 4 or len(pin) == 6 and pin.isdigit():
        return True
    return False
        

#3

def add(n):
    def adder(x):
        return x + n
    return adder
    



