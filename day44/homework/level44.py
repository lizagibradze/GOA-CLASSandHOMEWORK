# 1

def validate_pin(pin):
    if pin.numeric () and len(pin) in [4,6]:
        return True
    return False


# 2
def row_sum_odd_numbers(n):
    return n ** 3


# 3
def binary_array_to_number(arr):
    box = 0
    index = 0
    arr.reverse()
    for x in arr:
        if x == 1:
            box += 2 ** index
            print(box)
        index += 1
    return box




# 4

def min_max(lst):
  min, max = lst[0], lst[0]

  for x in lst:
      if x > max:
          max = x
      elif x < min:
          min = x
        
  return [min, max]



# 5




def divisors(n):
    g = []
    for i in range(2,n):
        if n % i == 0:
            g.append(i)
    if g == []:
        return str(n)+ " is prime"
    else:
        return g
