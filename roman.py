import re

ROMAN_NUMBERS = (('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000))

def roman_to_integer(value):
    
    # 1. Initialize variables and compile regular expressions
    total = 0
    pattern_1 = re.compile(r"(.*VX)|(.*XD)")
    pattern_2 = re.compile(r".*I[V,X,L,C,D,M]+")

    # 2. Validation of the input
    if isinstance(value,int) or re.match(pattern_1,value):
        raise ValueError("{0} is not a valid roman number".format(value))

    # 3. If input is valid, convert to roman number the input
    if 'I' in value:
        if re.match(pattern_2,value):
            total = total - 1;
            #remove I from string
            value = value.replace("I", "")
    for letter in value:
         for item in ROMAN_NUMBERS:
             if item[0] == letter:
                 total += item[1]

    # 4. Return the final result
    return total
