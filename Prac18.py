def new_string(str):                                #DEFINITION
    if len(str) >= 3 and str[:3] == "the":
        return str
    return "the" + str

print(new_string("Array"))                          #CALLING
print(new_string("Empty"))
