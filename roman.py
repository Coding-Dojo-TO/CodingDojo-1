def roman_to_integer(value):
    number_dict = {'I':1, "V":5, "X":10, "L":50}
    total = 0
    i_sum = value.count("I")
    v_sum = value.count("V")

    if value == "IV":
        return 4
    if value == "IX":
        return 9
    for c in value:
         total += number_dict[c]
    return total
