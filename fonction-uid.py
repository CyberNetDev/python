import math
import random
def generate():
    tab=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for j in range(1,10):
        for k in range(0,10):
            i=(int) (11+random.random()*62-11)
            print('{}'.format(tab[i]),end="")
        print()
generate()
