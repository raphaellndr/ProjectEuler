############ EXERCICE 16 ############
def power_digit_sum(number, power) :
    number_at_power = number**power
    number_list = [int(d) for d in str(number_at_power)]
    digit_sum = 0
    for i in number_list :
        digit_sum += i
    return digit_sum