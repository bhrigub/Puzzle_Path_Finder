"""
Created on Mon Sept 28 18:44:17 2017

@author: bhrigu_bhargava
References: https://www.csee.umbc.edu/courses/graduate/671/fall17/Slides/4-uninf_search-aiF17.pdf
            https://www.csee.umbc.edu/courses/graduate/671/fall17/Slides/5-inf_search-aiF17.pdf
            https://en.wikipedia.org/wiki/A*_search_algorithm            
            https://www.ics.uci.edu/~welling/teaching/ICS175winter12/A-starSearch.pdf
            http://www.cs.cmu.edu/~cga/ai-course/astar.pdf
            http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html
            Artificial Intelligence- A Modern Approach (Third Edition) by Stuart Russell and Peter Norvig
Logic: Solved the problem using index values and used array as distance measurement matrix
"""

def solve (inputArray):
    """
    Function to calculate heuristic values and return the next preffered node for expansion
    """
    #Store value of f(n), current node, next node
    storeFunction=[]
    #To solve the purpose of heuristic function
    distanceTravel = 0
    #Nodes visited 
    visitedNodes=[]
    #available nodes to expand
    openNodes=[]
    #neighbouring nodes of the expanded node
    neighbourNodes=[]
    #To provide result of the navigation in tree
    pathFunction={}
    #current location of the pointer and considering the index
    currentNode = 0
    #Calculate number of iterations to debug
    iterations = 0
    
    openNodes.append(currentNode)
    #loop to do node processing and function value check
    while openNodes:    
        iterations+=1
        #Debug: 
        #print ("CurrentNode:", currentNode)
        
        #check for values out of range in elements
        arcCheck = inputArray[currentNode]
        if (currentNode+arcCheck) > len(inputArray) and not(neighbourNodes):
            if ((currentNode-arcCheck) <= 0):    
                return ("Value out of range at element", currentNode)
        #check for 0 that have no alternative solution in elements
        if (arcCheck == 0) and not(neighbourNodes):         
            return ("Incorrect value at element", currentNode) 
        #create neighbours of current node
        neighbourNodes = neighbourNodes[2:]
        if (((currentNode-arcCheck) >= 0) and ((currentNode-arcCheck) < len(inputArray))): #and not(arcCheck == 0)):
            #if (currentNode-arcCheck) not in openNodes:
            if (currentNode-arcCheck) not in visitedNodes:
                neighbourNodes.append(currentNode-arcCheck)
        if (((currentNode+arcCheck) >= 0) and ((currentNode+arcCheck) < len(inputArray))): #and not(arcCheck == 0)):
            #if (currentNode+arcCheck) not in openNodes:
            if (currentNode+arcCheck) not in visitedNodes:
                neighbourNodes.append(currentNode+arcCheck)
        #Debug: 
        print ("neighbourNodes:",neighbourNodes)
        
        #Process open nodes that can be expanded and nodes that have been visited
        for j in range (0, len(neighbourNodes)):
            if neighbourNodes[j] in visitedNodes:
                continue
            if neighbourNodes[j] not in openNodes:
                if (currentNode-arcCheck) not in visitedNodes:
                    if (((currentNode-arcCheck) >= 0) and ((currentNode-arcCheck) < len(inputArray))):
                        openNodes.append(currentNode-arcCheck)
                if (currentNode+arcCheck) not in visitedNodes:
                    if (((currentNode+arcCheck) >= 0) and ((currentNode+arcCheck) < len(inputArray))):
                        openNodes.append(currentNode+arcCheck)
                else:
                    return ("No possible path")
        #Debug:
        #print ("openNodes:",openNodes)
        
        #remove expanded nodes
        if currentNode in openNodes:
           openNodes.remove(currentNode)
        
        #Debug:
        print ("openNodes2:",openNodes)
        print ("visitedNodes:",visitedNodes)
        
        #calculate function and next best node for expansion
        for j in range (0, len(neighbourNodes)):
            if neighbourNodes[j] in openNodes:
                #g(n) function to compute the total distance travelled
                gLeftFunction = distanceTravel
                #h(n) function to compute the heuristic value in terms of remaining distance
                hLeftFunction = len(inputArray) - neighbourNodes[j]
                 #A* function calculation
                function = gLeftFunction + hLeftFunction
                
                #Debug:
                print("fun1", function)
                
                #Store currently active functions value
                #j is 0 when left and 1 when right
                storeFunction.append((function, currentNode, neighbourNodes[j]))  
                #Sort the function values with relation to heuristic function value
                storeFunction.sort()
        
        distanceTravel = distanceTravel + currentNode
        #Debug:
        print ("storefunction:", storeFunction)
        
        if not (storeFunction):
            return ("No Solution Found")
        #To add values to path function for calculating Left Right
        if ((storeFunction[0][2]) not in visitedNodes):
            currentNode =  storeFunction[0][2]
            tempdict = {storeFunction[0][2]: (storeFunction[0][1],storeFunction[0][2])}
            pathFunction.update(tempdict)
            storeFunction = storeFunction[1:]
            visitedNodes.append(currentNode)
        else: 
            storeFunction = storeFunction[1:]
        
        #Debug:
        print ("nextNode:", currentNode)
        #print ("iterations",iterations)
        print (len(inputArray))
        print ("path function:",pathFunction, "\n")
        
        #solution found, then triggers path finding function
        if (len(inputArray)-1) in visitedNodes:
            print(pathFunction)
            travelDirection =pathFinder(pathFunction, inputArray)
            return  (travelDirection)

    return (travelDirection)
            
#Path finder function
def pathFinder (pathFunction, inputArray):
    #check for end location
    finalLocation = len(inputArray) - 1
    #create string
    pathTravel = ""
    #Find path to be followed using L for left and R for right
    while (pathFunction[finalLocation]):
        node = pathFunction[finalLocation]
        finalLocation = node[0]
        #compares node values to find left right
        if node[1] < node[0]:   
            pathTravel= 'L' + pathTravel 
        elif node[1] > node[0]:
            pathTravel= 'R'  + pathTravel
        else:
            return ("Invalid path error detected")
        if node[0] == 0:
            break
            if node[1] < node[0]:   
                pathTravel= 'L' + pathTravel
            elif node[1] > node[0]:
                pathTravel= 'R'  + pathTravel
            break
    return pathTravel

#Debug:
#def main ():   
    #1 and 4th
    #Debug:
    #input1 = [6, 10, 1, 11, 5, 3, 10, 10, 3, 6, 13, 7, 2, 11, 10, 2, 5, 3, 0, 8, 11, 9, 0, 2]
    #input2 = [12, 20, 3, 6, 10, 3, 10, 6, 5, 4, 4, 5, 5, 0, 1, 7, 10, 11, 10, 4, 7, 2, 0, 6]
    #input3 = [7, 22, 3, 5, 11, 1, 4, 2, 5, 10, 6, 5, 6, 7, 13, 3, 10, 9, 2, 5, 7, 3, 0, 11]
    #input4 = [5, 22, 8, 5, 12, 4, 8, 5, 6, 5, 3, 9, 2, 1, 7, 4, 15, 3, 1, 7, 1, 0, 0, 10]
    #input5 = [17, 2, 14, 4, 7, 5, 8, 0, 11, 11, 8, 4, 6, 9, 11, 6, 7, 12, 10, 11, 7, 7, 0, 11]
    #input6 = [1, 2, 10, 17, 0, 7, 2, 12, 6, 4, 4, 3, 10, 3, 4, 6, 8, 12, 9, 7, 5, 2, 0, 4]
    #input7 = [0, 1, 3, 5, 7]
    #inputArray = [3, 4, 0, 2, 5, 0, 9, 3]
    #input9 = [4, 3, 6, 1, 5, 8, 9]
    #t1 = solve(input9)
    #t2 = solve(input2)
    #t3 = solve(input3)
    #t4 = solve(input4)
    #t5 = solve(input5)
    #t6 = solve(input6)
    #t7 = solve(input7)
    #t8 = solve(input8)
    #t9 = solve(input9)
    #print (t1)
    
    #print (t1,"\n", t2,"\n", t3,"\n",  t4,"\n",  t5,"\n",  t6,"\n",  t7,"\n",  t8,"\n",  t9)    

#if __name__ == "__main__":
#    main()           