# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 16:43:03 2025

@author: ecama
"""


#%% 

def bsd_rand(seed):
   def rand():
      rand.seed = (1103515245*rand.seed + 12345) & 0x7fffffff
      return rand.seed
   rand.seed = seed
   return rand             # https://rosettacode.org/wiki/Linear_congruential_generator (not really statistically robust or high entropy but it's ok for a test)


random_generator = bsd_rand(20251005)


dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]


a = random_generator() 
b = str(a)
b = int(b[6])

if b in dice_1:

    draw_1 = b

c = random_generator() 
d = str(c)
d = int(d[6])

if d in dice_2:
    
    draw_2 = d
    
#%%


def bsd_rand(seed):
   def rand():
      rand.seed = (1103515245*rand.seed + 12345) & 0x7fffffff
      return rand.seed
   rand.seed = seed
   return rand

random_generator = bsd_rand(20251006)

def twoDice ():
    
    dice_1 = [1,2,3,4,5,6]
    dice_2 = [1,2,3,4,5,6]
    
    a = random_generator() 
    b = str(a)
    b = int(b[-4])

    if b in dice_1:

        draw_1 = b
    else:
        a = random_generator() 
        b = str(a)
        b = int(b[-4])
        
        if b in dice_1:

            draw_1 = b
        else:
            a = random_generator() 
            b = str(a)
            b = int(b[-4])

            if b in dice_1:

                draw_1 = b
                
            else:
                a = random_generator() 
                b = str(a)
                b = int(b[-4])
                
                if b in dice_1:

                    draw_1 = b
                
                else:
                    a = random_generator() 
                    b = str(a)
                    b = int(b[-4])
                    
                    if b in dice_1:

                        draw_1 = b
                    
                    else:
                        a = random_generator() 
                        b = str(a)
                        b = int(b[-4])
                        
                        if b in dice_1:

                            draw_1 = b
                        
                        else:
                            a = random_generator() 
                            b = str(a)
                            b = int(b[-4])
                            
                            if b in dice_1:

                                draw_1 = b
                            else:
                                a = random_generator() 
                                b = str(a)
                                b = int(b[-4])
                                
                                if b in dice_1:

                                    draw_1 = b
                                else:
                                    a = random_generator() 
                                    b = str(a)
                                    b = int(b[-4])
                                    
                                    if b in dice_1:

                                        draw_1 = b
                                    else:
                                        a = random_generator() 
                                        b = str(a)
                                        b = int(b[-4])
                                        
                                        if b in dice_1:

                                            draw_1 = b
                        
                
        

    c = random_generator() 
    d = str(c)
    d = int(d[-4])

    if d in dice_2:
        
        draw_2 = d
    else:
        c = random_generator() 
        d = str(c)
        d = int(d[-4])

        if d in dice_2:
            
            draw_2 = d
            
        else:
            c = random_generator() 
            d = str(c)
            d = int(d[-4])

            if d in dice_2:
                
                draw_2 = d
            
            else:
                c = random_generator() 
                d = str(c)
                d = int(d[-4])

                if d in dice_2:
                    
                    draw_2 = d
                
                else:
                    c = random_generator() 
                    d = str(c)
                    d = int(d[-4])

                    if d in dice_2:
                        
                        draw_2 = d
                    else:
                        c = random_generator() 
                        d = str(c)
                        d = int(d[-4])

                        if d in dice_2:
                            
                            draw_2 = d
                        else:
                            c = random_generator() 
                            d = str(c)
                            d = int(d[-4])

                            if d in dice_2:
                                
                                draw_2 = d
                            else:
                                c = random_generator() 
                                d = str(c)
                                d = int(d[-4])

                                if d in dice_2:
                                    
                                    draw_2 = d
                                else:
                                    c = random_generator() 
                                    d = str(c)
                                    d = int(d[-4])

                                    if d in dice_2:
                                        
                                        draw_2 = d
                                    else:
                                        c = random_generator() 
                                        d = str(c)
                                        d = int(d[-4])

                                        if d in dice_2:
                                            
                                            draw_2 = d
                        
    
    draw = draw_1 + draw_2
        
    return draw


#%%

nRolls = 100

def diceFrequency (nRolls):
    
    freq_dict = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    prob_dict = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    
    if nRolls == True:
        for x in range(nRolls-1):
            n = twoDice()
            freq_dict[n]=freq_dict.get(n)+1
    
    else: 
        nRolls = 100
        for i in range(nRolls-1):
            n = twoDice()
            freq_dict[n]=freq_dict.get(n)+1
            
    
    for value in freq_dict:
        prob_dict[value] = round(freq_dict[value]/nRolls,2)
        
    print(f'_________________________\n|Roll Dice | Probability |\n|     2    |    {prob_dict[2]}     |\n|     3    |    {prob_dict[3]}     |\n|     4    |    {prob_dict[4]}     |\n|     5    |    {prob_dict[5]}     |\n|     6    |    {prob_dict[6]}     |\n|     7    |    {prob_dict[7]}     |\n|     8    |    {prob_dict[8]}     |\n|     9    |    {prob_dict[9]}      |\n|    10    |    {prob_dict[10]}     |\n|    11    |    {prob_dict[11]}     |\n|    12    |    {prob_dict[12]}     |\n-------------------------')
    
#%%

diceFrequency(nRolls)

