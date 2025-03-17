# 1
def nugzar_chubinidze(sadgerdzelo,limit):
    if sadgerdzelo > limit:
        return "ნუგზარი აღარ დალიო მეტი!"
    else:
        return "მოდი ახლა მართლა, დამილოცნიე!" 






# 2

def yuri_gagarini(pulse, pressure):
    pres = 120
    pul = 80
    if pressure == pres and pulse == pul:
        return True
    else:
        return False

# 3

    
def captinjack(coins):
    if coins == 0:
        return "აჯანყდა ეკიპაჟი"
    if coins == 150:
        return "იყიდა გემი"
    if coins == 200:
        return "იყიდა გემი"
    if coins == 250:
        return "იყიდა გემი"
    if coins == 300:
        return "იყიდა გემი"
    if coins == 350:
        return "ხურდა გვეკუთნის"



# 4

# def duplicat_remove(arr):
#     return set(arr)


def duplicat_remove(arr):
    new_arr = ["პანტა"]
    for apple in arr:
        if apple not in new_arr:
            new_arr.append(apple)
    return new_arr





print(duplicat_remove(["პანტა", "პანტა", "გორული", "გორული", "გორული"]))






# --

def no_boring_zeros(n):
    if n:
        return int(str(n).rstrip('0'))
    else:
        return 0
    
    