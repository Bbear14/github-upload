#Functions Dice Rolls

def dicey2(x,modifier=0,threshold=0):
    '''Assumes X is a list of positive integers. Both Modifier and Threshold
        are int.  Modifier is a number that affects the player and the
        Threshold is a number that affects the enemy.
        Returns the probability whether the sum of dices can beat the
        threshold value.'''
    import numpy as np

    if len(x) == 0:       
        return None
    if len(x) == 1:
        array = np.arange(x[0])+1    
    if len(x) >= 2:

        array = np.arange(1)    #creates array with one element
        while len(x) >= 1:
            a0 = np.arange(x[0])+1
            a1 = array[:]
            array = np.arange(0)  #creates an empty array
            for i in range(len(a0)):
                total = a0[i]+a1
                array = np.append(array,total)
            x = x[1:]

    value1 = (array >= (threshold-modifier) ).sum()
    value2 = len(array)
    prob = float(value1)/value2
    return prob


#end
'''
        a0 = np.arange(x[0])+1
        a1 = np.arange(x[1])+1
        array = np.arange(0)  #creates an empty array
        for i in range(len(a0)):
            total = a0[i]+a1
            array = np.append(array, total)
        x = x[2:]

        while len(x) >= 1:
            a0 = np.arange(x[0])+1
            a1 = array[:]
            array = np.arange(0)  #creates an empty array
            for i in range(len(a0)):
                total = a0[i]+a1
                array = np.append(array,total)
            x = x[1:]
'''
