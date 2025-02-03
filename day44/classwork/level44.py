


def count_by(x, n):

    arr = []

    for i in range(1, n + 1):
        arr.append(i*x)

    return arr













# def get_planet_name(id):

#     name={

#     # switch id:
#          1: name = "Mercury"
#          2: name = "Venus"
#          3: name = "Earth"
#          4: name = "Mars"
#          5: name = "Jupiter"
#          6: name = "Saturn"
#          7: name = "Uranus"  
#          8: name = "Neptune"
#     }

#     return name


    



def human_years_cat_years_dog_years(human_years):
    
    if human_years == 1:
        return [1,15,15]
    if human_years == 2:
        return [2,24,24]
    else:
        return[human_years, 24 + ((human_years-2) * 4), 24 +((human_years-2) * 5)]















