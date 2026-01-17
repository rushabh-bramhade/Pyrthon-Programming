" normal array example with import array"



from array import array

#interger example ->
num = array('i', [2,4,5,6,7,75,24,26,2])

for i in range (len(num)):
    print(num[i],end=" ")



#double example ->

double_num =  array('d',[2.4,2.2,1.3,2])

print("\n double example -> \n")

for i in range(len(double_num)):
    print(double_num[i] , end=" ")

 
#float example 

float_num = array("f" , [2.3,4.3,24.3,9])

for i in range (len(float_num)):
    print(float_num[i])


""" 
'i' = interger
'f' = float
'd' = double

"""

