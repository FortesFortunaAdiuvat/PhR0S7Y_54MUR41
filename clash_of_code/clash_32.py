#given a number n print a shape with #'s
# ex n =5
#output:
'''
#   
##    
###  
#### 
#####
 ####
  ###
   ##
    #
'''

n = int(input())

for i in range(1, n + 1):
    print("#" * i)

for i in range(n - 1, 0, -1):
    print(" " * abs(n - i) + "#" * abs(i))
