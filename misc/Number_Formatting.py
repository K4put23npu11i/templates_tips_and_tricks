"""
Created on Tue Nov 19 15:22:24 2019

"""

import re

###############################################################################

#zahl = 1234567
#zahl = "%.2f" % zahl
#zahl = zahl.replace(".",",")
#
#print(zahl)
#print(type(zahl))
#
#zahl = re.sub(r"(\d)(\d\d\d\D)", r"\1.\2", zahl)
#print(zahl[:-3])

###############################################################################

def number_format(zahl):
   zahl = "%.2f" % zahl
   zahl = zahl.replace(".",",")
   nochmal = 1 
   while nochmal:    
      (zahl,nochmal) = re.subn(r"(\d)(\d\d\d\D)",r"\1.\2",zahl)
   return zahl

###############################################################################

def format_integer(number, sep_t = '.'):
    number = int(number)
    number = str(number)
    form = ''
    index = len(number)
    length = len(number)
    counter = 0
    
    while(counter < length):
        if counter % 3 == 0 and counter != 0:
            form = number[index-1] + sep_t + form
        else:
            form = number[index-1] + form
        index -= 1
        counter += 1
    
    return(form)        
        
        
###############################################################################
 
def format_float(number, rounding_digit = 2, sep_t = '.', sep_d = ','):
    number = round(number, rounding_digit)
    number = str(number)
    print(number)
    if sep_t == '.' or sep_d == ',':
        number = number.replace('.', sep_d)
    form = ''
    index = len(number) - rounding_digit-1
    length = len(number) - rounding_digit-1
    counter = 0
    
    while(counter < length):
        if counter % 3 == 0 and counter != 0:
            form = number[index-1] + sep_t + form
        else:
            form = number[index-1] + form
        index -= 1
        counter += 1
        print(form)
    form += number[-(rounding_digit+1):]
    
    return(form)        
        
        
###############################################################################       

#print (number_format(12431554323.44))

#print (format_integer(12431543.44))
        
print('Format float:\n' + str(format_float(number=1234567.1234, 
                                           rounding_digit = 2, 
                                           sep_t = '.', 
                                           sep_d = ',')))




