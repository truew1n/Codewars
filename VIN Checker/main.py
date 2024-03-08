def check_vin(number):
    result = 0
    #alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabet = [65,90] # ASCII Range
    value = [1,2,3,4,5,6,7,8,".",1,2,3,4,5,".",7,".",9,2,3,4,5,6,7,8,9]
    weights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
    if len(number)!=17:
        return False
    elif(len(number)==17):
        for y, x in enumerate(number):
            try:
                result += int(x)*weights[y]
            except:
                if x == "I" or x=="O" or x=="Q" or x.lower() == x:
                    return False 
                result += value[ord(x)-65]*weights[y]
        result_mod = result%11
        if number[8] == f"{result_mod}":
            return True
        elif result_mod == 10 and number[8] == "X":
            return True
        else:
            return False
