import json

def converter(value, value2):
    sum = float(value) + float(value2)
    re = int(sum)
    if type(value) or type(value2) == int or float:
        print (re) 
    elif type(value) or type(value2) == str or float:
        num = json.loads(value, value2)
        print (re)
    elif value or value2 ==True:
        return value or value2 == 1
        print(re)  
    elif value or value2 == False:
        return value or value2 == 0
        print(re)
    

converter(3,5.0)