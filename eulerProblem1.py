#think of natural numbers under 10 that
#are multiples of 3 and 5 (3,5,6,9 and sum is 23),
#go up to 100
t = 0
for x in range (0, 1000):
    while True:
        if x%3==0 or x%5==0:
            print (x)
            t = t + x
            #I added a print statement to be able
            #to tell which ones have been selected
            print (t)
            break
        else:
            break
#print (t)
