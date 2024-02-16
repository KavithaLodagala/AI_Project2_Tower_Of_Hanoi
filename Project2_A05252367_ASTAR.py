"""
******************* File Name: Project1_A05252367_Astar.py **********************
# This file contains the implementation of A* search algorithm
# TowerOfHanoi is a class which can be used to build the tree
# Possible moves of particular node will be generated as child node
# Once a node matches the goal node then loop breaks
# This process repeats for all the disks starting from 
# n=3 to 11( which complete in 30 Mins)
*********************************************************************************
"""

from itertools import product
import time
import matplotlib.pyplot as plt
import psutil
from tabulate import tabulate

class TowerOfHanoi:

    '''
    **************************Constructor************************************
    # In this we initialize all the variables required for each node.
    # This function is called whenever a node is created 
    # Here the source peg is 'A', Target peg is 'B', Auxiliary peg id 'C'
    # source rings contains rings containing in source peg
    # target rings contains rings containing in target peg
    # Auxiliary rings contains rings containing in Auxiliary peg
    # gn is the level of node in the tree, which is level of parent node + 1
    # hn is the heuristic value of a node
    *************************************************************************
    '''
    def __init__(self,n,source_peg, source_rings, target_peg, target_rings,auxiliary_peg,auxiliary_rings,level):
        self.n = n  # Number of disks
        self.source_peg = source_peg  # Source peg
        self.source_rings=source_rings # Rings present in source peg
        self.target_peg = target_peg  # Target peg
        self.target_rings = target_rings # Rings present in target peg
        self.auxiliary_peg = auxiliary_peg  # Auxiliary peg
        self.auxiliary_rings = auxiliary_rings  # Rings present in auxiliary peg
        self.gn=level # level of the tree which g(n)
        #self.hn=self.heuristic_roopika(expected_rings_order) # heuristic function1
        self.hn=self.heuristic_sakshi() # heuristic function2
        #self.hn=self.heuristic_kavitha() # heuristic function3
        self.child = []

    '''
    ******************Function Name: heuristic_roopika***************
    # This function takes number of disks as input parameter
    # 
    # Returns the heuristic value
    *****************************************************************
    '''
    def heuristic_roopika(self,reference_sequence):
        hn=0
        #reference_sequence = 

        # Check if the array is empty
        if not self.target_rings:
            return 3  # Return 3 for an empty array

        # Check if the order of any one element in the input array matches the reference array
        for i in range(len(self.target_rings)):
            if self.target_rings[i] == reference_sequence[i]:
                # Calculate the number of empty slots and mismatched elements in comparison to the reference array
                empty_slots = len(reference_sequence) - len(self.target_rings)
                mismatched_elements = sum(1 for x, y in zip(self.target_rings, reference_sequence) if x != y)
                hn = mismatched_elements + empty_slots
                return hn
            
        hn =3
        return hn 


    '''
    *****************Function Name: heuristic_kavitha ******************
    # This heuristic function calculates an estimate (hn) for the Tower of Hanoi problem by considering the number 
    # and arrangement of rings on the three rods (source, target, and auxiliary). 
    ********************************************************************
    '''
    def heuristic_kavitha(self):
        hn=0
        
        sn=len(self.source_rings)# number of rings in source peg

        # iterates through each ring, adding values based on its position (distance from the top) and its size
        for i in range(len(self.source_rings)):
            hn+=sn-i-1
            hn+=self.source_rings[i]

        tn=len(self.target_rings)# number of rings in target peg

        #checks if each ring is not in the correct position, and if so, it adds values based on both the position and size of the ring
        for i in range(len(self.target_rings)):
            if(self.n-i-self.target_rings[i]!=0):
                hn+=tn-i-1
                hn+=self.target_rings[i]
        
        an=len(self.auxiliary_rings)# number of rings in auxiliary peg

        #iterates through each ring, adding values based on its position (distance from the top) and its size
        for i in range(len(self.auxiliary_rings)):
            hn+=an-i-1
            hn+=self.auxiliary_rings[i]
        
        return hn
   
    
    '''
    ******************* Function Name: heuristic_sakshi *******************
    # this heuristic calculates the weighted sum of the number of discs not on the destination rod
    ***********************************************************************
    '''
    def heuristic_sakshi(self):
        tn = len(self.target_rings)
        sum = 0
        for i in range(1, self.n + 1):
            if not (i in self.target_rings): sum += i
        return sum
   

    '''
    ******************Function Name: get_fn *********************
    # returns evaluation function values that sum of gn and hn
    # f(n) = g(n) + h(n)
    # returns the fn value
    *************************************************************
    '''
    def get_fn(self):
        return self.gn+self.hn
    
    '''
    ***************** Function Name: print_tower_of_hanoi *****************
    # This function prints the present state of the node which means rings 
    present in source peg, target peg and auxiliary peg
    ***********************************************************************
    '''
    def print_tower_of_hanoi(self):
        print("g(n):",self.gn," h(n):",self.hn," f(n)=",self.gn+self.hn)
        print(self.source_peg,"-->",self.source_rings)
        print(self.target_peg,"-->",self.target_rings)
        print(self.auxiliary_peg,"-->",self.auxiliary_rings)
    
    
    '''
    **************** Function Name: check_in_visited ***********************
    # This function checks whether a node is visited or not
    # If a node is visited then return true 
    # Otherwise it adds the node to visited_nodes list and returns flase
    ************************************************************************
    '''
    def check_in_visited(self):
        global visited_nodes
        s=self.source_peg+''.join(list(map(str,self.source_rings)))+self.target_peg+''.join(list(map(str,self.target_rings)))+self.auxiliary_peg+''.join(list(map(str,self.auxiliary_rings)))

        # check whether the node is presen in visited nodes or not
        if(s not in visited_nodes): 
            # If node not in visited then add nodes to the visited
            visited_nodes.append(s)
            return False
        else:
            # Node already visited 
            return True

    '''
    ****************** Function Name: generate_child_nodes *****************
    # This function generate the childrens of a given node
    ************************************************************************
    '''    
    def generate_child_nodes(self,best_node):
        global visited_nodes
        global count
    
        sn=len(best_node.source_rings)# number of rings in source peg
        tn=len(best_node.target_rings)# number of rings in target peg
        an=len(best_node.auxiliary_rings)# number of rings in auxiliary peg

        print("****child nodes")
        # Checking whether source peg has any rings 
        if(sn>0):
            # creating a new node by moving top most ring from source peg to target peg only if the source peg top ring 
            # is smaller than the target top most ring or if target peg has no rings then move ring from source directly
            if(tn<n and ((tn>0 and sn>0 and best_node.source_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                ring=best_node.source_rings[-1]

                #creating a child node with new move
                child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                best_node.child.append(child_node)
                
                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()
            
            # creating a new node by moving top most ring from source peg to auxiliary peg only if the source peg top ring 
            # is smaller than the auxiliary top most ring or if auxiliary peg has no rings then move ring from source directly
            if(an<n and ((an>0 and sn>0 and best_node.source_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                ring=best_node.source_rings[-1]

                #creating a child node with new move
                child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                best_node.child.append(child_node)

                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()

        # Checking whether target peg has any rings 
        if(tn>0):
            # creating a new node by moving top most ring from target peg to source peg only if the target peg top ring 
            # is smaller than the source top most ring or if source peg has no rings then move ring from target directly
            if(sn<n and ((sn>0 and tn>0 and best_node.target_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                ring=best_node.target_rings[-1]

                #creating a child node with new move
                child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                best_node.child.append(child_node)

                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()

            # creating a new node by moving top most ring from target peg to auxiliary peg only if the target peg top ring 
            # is smaller than the auxiliary top most ring or if auxiliary peg has no rings then move ring from target directly
            if(an<n and ((an>0 and tn>0 and best_node.target_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                ring=best_node.target_rings[-1]
                
                #creating a child node with new move
                child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                best_node.child.append(child_node)

                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()
        
        # Checking whether auxiliary peg has any rings 
        if(an>0):

            # creating a new node by moving top most ring from auxiliary peg to source peg only if the auxiliary peg top ring 
            # is smaller than the source top most ring or if source peg has no rings then move ring from auxiliary directly
            if(sn<n and ((sn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                ring=best_node.auxiliary_rings[-1]

                #creating a child node with new move
                child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                best_node.child.append(child_node)

                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()
            
            # creating a new node by moving top most ring from auxiliary peg to target peg only if the auxiliary peg top ring 
            # is smaller than the target top most ring or if target peg has no rings then move ring from auxiliary directly
            if(tn<n and ((tn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                ring=best_node.auxiliary_rings[-1]

                #creating a child node with new move
                child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                best_node.child.append(child_node)

                # checking if the child node visited or not if  visited then ignored otherwise child node is added to open
                if(not child_node.check_in_visited()):
                    open.append([child_node,states[count],child_node.get_fn()])
                    count+=1
                    child_node.print_tower_of_hanoi()

    ''' 
    ***************** Function Name: print_open_closed *******************
    # This function prints nodes present in open and closed 
    **********************************************************************
    '''

    def print_open_closed(self,open,closed):
            print("**********Printing Open List and Closed List*********")
            print("\nOpen-->[",end="")
            for i in range(len(open)):
                print(open[i][1]+str(open[i][2]),end=" ")
            print("]")
            
            print("Closed-->[",end="")
            for i in range(len(closed)):
                print(closed[i][1]+str(closed[i][2]),end=" ")
            print("]")
            
        
    ''' 
    ****************** Function Name: build_hanoi_tree ********************
    # This function does the actual A* search
    # Initially root node added to open and loop continue to expand the node with less fn value
    # The node with least fn value is the best node 
    # If the best node is goal node then loop breaks
    # Otherwise best node is expanded by calling the function generate child nodes
    # Returns number of nodes generated and number of nodes expanded.
    ***********************************************************************
    '''
    def build_hanoi_tree(self):

        # using global count to store the number of nodes generated
        global count

        # Closed list stores the nodes that are expanded
        closed=[]

        # best_node stores the node that is poped from open that is the no  de with less fn value
        best_node=None

        #adding the current node to the visited by calling check_in_visited() function name
        s=self.check_in_visited()

        # loop runs until open becomes empty or a goal node is found
        while(open):

            # sorting the open based on fn value
            open.sort(reverse=True,key=lambda x:x[2])

            # self.print_open_closed(open,closed)  #this prints the tracing of the open and closed          
            
            # best node will be stored in best_node
            best_node=open.pop()

            # best node will be added to closed  
            closed.append(best_node)

            best_node=best_node[0]
        
            print("****** Selected Best node ****** " )
            best_node.print_tower_of_hanoi()

            #checking whether the best node is goal node
            if((best_node!=None and best_node.target_rings==expected_rings_order)):
                print("Disks are placed in target pole B")
                best_node.print_tower_of_hanoi()
                break

            # expanding the best node 
            self.generate_child_nodes(best_node)

        print("total number of nodes generated : ", len(open)+len(closed), "Total number of Best nodes expanded : ", len(closed))


        return (len(open)+len(closed),len(closed))



n = 6  # Number of rings  and n starts with 3
No_of_disks=[] # stores number of disk of tower hanoi that are solved
Node_Generated=[] # stores number of nodes generated for each disk count
Node_Expanded=[] # stores number of nodes expanded for each disk count

# In order to give each state a name like ('A','B','C'...) below loop is run to get distinct state names
alp=list(map(chr, range(65, 91)))

# To get a combination of alphabets from a single letter to 6 letters 
states=[]
for i in range(1,6):
    for comb in product(alp, repeat=i):
        states.append(''.join(comb))

# table_data list is to store the number of disks, elapsed time, memory used, 
# nodes generated and nodes expanded in a tabular formate using tabulate package
table_data=[]
table_data.append(["Number of Disks","Elapsed Time","Memory Used","Nodes Generated","Nodes Expanded"])

# A* search algorithm solves tower hanoi for 3 to 11 disks in 30 mins
# so running loop for n starting from n=3 to 11
while(n<7):
    print("\nstarting A* algorithm for",n, "disks")
    count = 0 # count stores number of nodes generated
    
    #To set the expected order of rings on the target peg and source peg
    expected_rings_order=list(range(n,0,-1))
    
    #Set the root node by calling the class and initializing them
    root = TowerOfHanoi(n,'A', expected_rings_order, 'B', [],'C',[],0)
    
    #add the root to the open list along with state and f(n) value of the root node
    open=[[root,states[count],root.get_fn()]]
    
    count+=1
    
    # visited nodes contains the nodes that are generated
    visited_nodes=[]
    
    # Record the start time
    start_time = time.time()
    
    #build the tower of hanoi tree using this root node.
    generated,expanded=root.build_hanoi_tree()
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    
    # Memory allocated for each disk count will be calculated and added to table_data
    memory = psutil.Process().memory_info().rss / (1024 * 1024)
    
    # storing the number of nodes generated and number of nodes expanded for each disk count
    Node_Generated.append(generated)
    Node_Expanded.append(expanded)
    
    # table_data is used to tabulate all the details for each disk
    table_data.append([n,elapsed_time,memory,generated,expanded])
    
    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time} seconds")
    
    # Print the memory consumed
    print("Memory consumed : ", memory, "MB")
    
    # adding the disk count for plotting
    No_of_disks.append(n)
    
    # increamenting the disk count to continue solving of Tower Hanoi using A* search
    n+=1

# Prints the all disk count and corresponding time, memory , nodes generated and expanded
print(tabulate(table_data))

# plotting graph to compare number of nodes generated and number of nodes expanded for each disk count
x= No_of_disks
y1=Node_Generated
y2=Node_Expanded
plt.plot(x,y1, label = "no of disks VS no of nodes generated")
plt.plot(x,y2, label = "no of disks VS no of nodes expanded")

# Adding labels and title
plt.xlabel('Number of disks')
plt.ylabel('Number of nodes')
plt.title('A* Algorithm for Tower of Hanoi')
plt.legend()

# Display the plot
plt.show()


