import random

num_set = set()

def get_numbers_ticket(min, max, quantity):
    global num_set
    if min >= 1 and max <1000 and quantity > 0:
        while len(num_set) != quantity:
            num = random.randrange(min, max)
            num_set.add(num)
    lst_num = list(num_set)
    lst_num.sort()
    return lst_num


try:
    lottery_numbers = get_numbers_ticket(1, 49, 0)
    print("Ваші лотерейні числа:", lottery_numbers)
except NameError:
    print("Error enter value!")
