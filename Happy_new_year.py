import random
import time

#Çalışma alanı 1 - 60 arası


for i in range(100):
    
    line = ""

    a = random.randrange(0,12)
    b = random.sample(range(1,80),a)
    k = random.randrange(1,66)
    m = random.randrange(0,3)
    for x in range(1,80):
        if x in b and x != k:
            line += "*"
        elif x == k and m == 1:
            line += "{}"
        else:
            line += " "
    time.sleep(0.6)
    
    try:
        print(line.format("HAPPY NEW YEAR"))

    except:
        print("HAPPY NEW YEAR")
