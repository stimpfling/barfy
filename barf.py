def evMinions(minions):
    expectedVal = 0
    totalTime   = 0
    totalProb   = 1
    prevProb    = 0
    for i in range(len(minions)):
        time  = minions[i][0]
        num   = minions[i][1]
        denom = minions[i][2]
        totalTime += time
        prob  = num / float(denom)
        if i < len(minions)-1:
            totalProb = (prob) * totalProb
            expectedVal += totalTime * totalProb
        else:
            totalProb = 1-totalProb
            expectedVal += totalTime * totalProb
        
    return expectedVal


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def sortMinions(mins,current):
    
    copy = mins[:current+1]
    lowestVal = evMinions(mins[:current+1])
    verify = lowestVal
    
    #print current
    #print "current",copy,lowestVal
    for i in range(current,0,-1):
        #print "swapping",i,i-1
        
        #print copy,lowestVal
        print i,i-1
        print copy
        swap(copy,i,i-1)
        newVal = evMinions(copy)
        print "swapped",copy,newVal
        if newVal < lowestVal:
            lowestVal = newVal
            #print "big swappy"
            mins = copy

    return mins
    


###minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
##minions = [[276, 1023, 1024],[199, 148, 250],[390, 185, 624],[686, 351, 947]]
##minions=[[199, 148, 250],[276,1023,1024]]
###minions=[[276,1023,1024],[199, 148, 250]]
##print minions
##print evMinions(minions)
##position = range(len(minions))
###minions = [[5, 1, 5], [10, 1, 2]]
for i in range(len(minions)):
    minions = sortMinions(minions,i)

print minions
print evMinions(minions)


#minions=[[199, 148, 250],[276,1023,1024]]
#print minions
#print evMinions(minions)
##
minions = [[276, 1023, 1024],[199, 148, 250],[390, 185, 624],[686, 351, 947]] ##Correct order
print minions
print evMinions(minions)        
##        
##
####minions = [ [10, 1, 2],[5, 1, 5]]
####evMinions(minions)
##minions = [[5, 1, 5],[10, 1, 2]]
##print minions
##print evMinions(minions)
##
##minions = [ [10, 1,2],[5, 1, 4]]
##print minions
##print evMinions(minions)

##minions = [ [10, 1, 2], [5 , 1, 4], [10, 1, 4]]
##print minions
##print evMinions(minions)
##
##minions = [ [10, 1, 2], [10, 1, 4], [5 , 1, 4]]
##print minions
##print evMinions(minions)
##
##minions = [ [ 5, 1, 4], [10, 1, 2], [10, 1, 4]]
##print minions
##print evMinions(minions)
##
##minions = [ [ 5, 1, 4], [10, 1, 4], [10, 1, 2]]
##print minions
##print evMinions(minions)
##
##minions = [ [10, 1, 4],[ 5, 1, 4], [10, 1, 2] ]
##print minions
##print evMinions(minions)
##
##minions = [ [10, 1, 4], [10, 1, 2],[ 5, 1, 4] ]
##print minions
##print evMinions(minions)



#minions = [ [10, 1, 2], [5 , 1, 4], [10, 1, 4]]
#print minions
#print evMinions(minions)
        
