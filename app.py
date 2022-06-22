values = [0] # This array will hold all of the numbers

numCount = 10 # 

def golden_ratio_experienco(manyTimes, arrayy): 
    count = 0
    workingnum = 1
    while count < manyTimes:
        currlength = len(arrayy)
        if currlength < 3:
            nextnum = arrayy[currlength-1] + workingnum 
            arrayy.append(nextnum)
            workingnum = nextnum
        else:
            nextnum = arrayy[currlength-1] +  arrayy[currlength-2]
            arrayy.append(nextnum)
            workingnum = nextnum
        count = count +1

#Calling the function
golden_ratio_experienco(numCount,values)

#Printing all of the numbers from array
for i in values:
    print(i,"\n")

#Printing the Golden Ratio
requiem = values[-1]/values[-2]
print(requiem)