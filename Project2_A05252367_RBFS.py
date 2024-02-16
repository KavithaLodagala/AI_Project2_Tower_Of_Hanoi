
"""
******** File Name: Project1_A05252367_RBFS.py **************
# This file contains the implementation of Recurssive Best Firs Search algorithm
# TowerOfHanoi is a class which can be used to build the tree
# Possible moves of particular node will be generated as child node
# Once the child node is generated best successor and alternative best successors are stored
# Now the best node child nodes are generated and if the best child node fn value is greater than alternative then 
# alternative node is expanded this process continues recursively until a goal node is found
# This process repeats for all the disks starting from n=3 to 11( which complete in 30 Mins)
*************************************************************************
"""

from itertools import product
import time
import matplotlib.pyplot as plt
import psutil
from tabulate import tabulate


class TowerOfHanoi:

    '''
    ********************Constructor*****************************************
    # In this we initialize all the variables required for each node.
    # This function is called whenever a node is created 
    # Here the source peg is 'A', Target peg is 'B', Auxiliary peg id 'C'
    # source rings contains rings containing in source peg
    # target rings contains rings containing in target peg
    # Auxiliary rings contains rings containing in Auxiliary peg
    # gn is the level of node in the tree, which is level of parent node +1
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
        self.auxiliary_rings = auxiliary_rings # Rings present in auxiliary peg
        self.gn=level #level of the tree which g(n)
        self.hn=self.heuristic_roopika(expected_rings_order)  # heuristic function1
        #self.hn=self.heuristic_sakshi()  # heuristic function2
        #self.hn=self.heuristic_kavitha()  # heuristic function3
        self.fn=self.gn + self.hn # evaluation function values that sum of gn and hn f(n) = g(n) + h(n)
        self.child=[]
        
    
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
    ***************** Function Name: print_tower_of_hanoi *****************
    # This function prints the present state of the node which means rings 
    present in source peg, target peg and auxiliary peg
    ***********************************************************************
    '''
    def print_tower_of_hanoi(self):
        print("g(n):",self.gn," h(n):",self.hn," f(n)=",self.fn)
        print(self.source_peg,"-->",self.source_rings)
        print(self.target_peg,"-->",self.target_rings)
        print(self.auxiliary_peg,"-->",self.auxiliary_rings)
    

    '''
    ******************* Function Name: goal_test *********************
    # This function takes node as input and checks whether the current 
    node is the goal node or not
    ******************************************************************
    '''
    def goal_test(self,node):
        #checking current node is the goal or not
        if(node.target_rings==list(range(self.n,0,-1))):
            return True
        else:
            return False

    '''
    ******************* Function Name: Recursive_best_first_search *********************
    # This function takes initial node as input parameter and calls RBFS_TowerOfHanoi function
    # and returns the output
    ************************************************************************************
    '''
    def Recursive_best_first_search(self,initial_node):
        return self.RBFS_TowerOfHanoi(initial_node,10000)
        
    '''
    **************** Function Name: check_in_visited ***********************
    # This function checks whether a node is visited or not
    # If a node is visited then return true 
    # Otherwise it adds the node to visited_nodes list and returns flase
    ************************************************************************
    '''
    def check_in_visited(self):
        s=self.source_peg+''.join(list(map(str,self.source_rings)))+self.target_peg+''.join(list(map(str,self.target_rings)))+self.auxiliary_peg+''.join(list(map(str,self.auxiliary_rings)))

        # check whether the node is presen in visited nodes or not
        if(s not in visited_nodes):
            # If node not in visited then add nodes to the visited
            visited_nodes.append(s)
            return False
        else:
            # Node already visited 
            return True
    
    def RBFS_TowerOfHanoi(self,node,f_limit):
        global expanded_nodes
        if(self.goal_test(node)): 
            node.print_tower_of_hanoi()
            return "Success",node.fn
        successors=[]
                    
        sn=len(node.source_rings)
        tn=len(node.target_rings)
        an=len(node.auxiliary_rings)
        #print("Best node")
        node.print_tower_of_hanoi()
        print("Child nodes")
        if(node not in expanded_nodes):
            expanded_nodes.append(node)
            if(sn>0):
                if(tn<n and ((tn>0 and sn>0 and node.source_rings[-1]<node.target_rings[-1]) or tn==0)):
                    ring=node.source_rings[-1]
                    child_node = TowerOfHanoi(n,node.source_peg, node.source_rings[:sn-1], node.target_peg, node.target_rings+[ring],node.auxiliary_peg,node.auxiliary_rings,node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                        child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and sn>0 and node.source_rings[-1]<node.auxiliary_rings[-1]) or an==0)):
                    ring=node.source_rings[-1]
                    child_node = TowerOfHanoi(n,node.source_peg, node.source_rings[:sn-1], node.target_peg, node.target_rings,node.auxiliary_peg,node.auxiliary_rings+[ring],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                        child_node.print_tower_of_hanoi()
            if(tn>0):
                if(sn<n and ((sn>0 and tn>0 and node.target_rings[-1]<node.source_rings[-1]) or sn==0)):
                    ring=node.target_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings+[ring], node.target_peg, node.target_rings[:tn-1],node.auxiliary_peg, node.auxiliary_rings,node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                        child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and tn>0 and node.target_rings[-1]<node.auxiliary_rings[-1]) or an==0)):
                    ring=node.target_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings, node.target_peg, node.target_rings[:tn-1],node.auxiliary_peg,node.auxiliary_rings+[ring],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                        child_node.print_tower_of_hanoi()
            if(an>0):
                if(sn<n and ((sn>0 and an>0 and node.auxiliary_rings[-1]<node.source_rings[-1]) or sn==0)):
                    ring=node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings+[ring], node.target_peg, node.target_rings,node.auxiliary_peg,node.auxiliary_rings[:an-1],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    child_node.print_tower_of_hanoi()
                if(tn<n and ((tn>0 and an>0 and node.auxiliary_rings[-1]<node.target_rings[-1]) or tn==0)):
                    ring=node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings, node.target_peg, node.target_rings+[ring],node.auxiliary_peg,node.auxiliary_rings[:an-1],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                        child_node.print_tower_of_hanoi()
        else:
            expanded_nodes.append(node)
            successors=node.child
            for suc in successors:
                s=suc[0].source_peg+''.join(list(map(str,suc[0].source_rings)))+suc[0].target_peg+''.join(list(map(str,suc[0].target_rings)))+suc[0].auxiliary_peg+''.join(list(map(str,suc[0].auxiliary_rings)))
                visited_nodes.append(s)
        if(successors==[]):
            #print("Failure",10000,f_limit)
            return "Failure", 10000

        for s in successors:
            s[0].fn=max(s[0].fn , node.fn)
            s[1]=s[0].fn
    
        while(1):
            successors.sort(reverse=True,key=lambda x:x[1])
            best_node=successors[-1]

            if(best_node[0].fn>f_limit):
                #print("Failure",best_node[0].fn,f_limit)
                return "Failure",best_node[0].fn
            if(len(successors)>=2):
                alternative_node=successors[-2]
                print("best node")
                best_node[0].print_tower_of_hanoi()
                print("alternative node")
                alternative_node[0].print_tower_of_hanoi()
                result,best_node[0].fn=self.RBFS_TowerOfHanoi(best_node[0],min(f_limit,alternative_node[0].fn))
                best_node[1]=best_node[0].fn
            else:
                result,best_node[0].fn=self.RBFS_TowerOfHanoi(best_node[0],f_limit)
                best_node[1]=best_node[0].fn
            if(result!="Failure"):
                return result,best_node[0].fn
start_time1=time.time()


n = 4 # Number of rings  and n starts with 3
No_of_disks=[] # stores number of disk of tower hanoi that are solved
Node_Generated=[] # stores number of nodes generated for each disk count
Node_Expanded=[] # stores number of nodes expanded for each disk count

# table_data list is to store the number of disks, elapsed time, memory used, 
# nodes generated and nodes expanded in a tabular formate using tabulate package
table_data=[]
table_data.append(["Number of Disks","Elapsed Time","Memory Used","Nodes Generated","Nodes Expanded"])

while(n==4):
    #print(time.time()-start_time1,time.time()-start_time1>10)
    print("\nstarting Recursive best first search algorithm for",n, "disks")
    

    expanded_nodes=[]
    
    #To set the expected order of rings on the target peg and source peg
    expected_rings_order=list(range(n,0,-1))

    # visited nodes contains the nodes that are generated
    visited_nodes=[]

    #Set the root node by calling the class and initializing them
    root = TowerOfHanoi(n,'A', expected_rings_order, 'B', [],'C',[],0)
    
    start_time = time.time()

    # Set the root node by calling the class and initializing them
    result,f_value=root.Recursive_best_first_search(root)
    
    end_time = time.time()
    
    # Calculate the elapsed time
    execution_time = end_time - start_time
    
    # Memory allocated for each disk count will be calculated and added to table_data
    memory = psutil.Process().memory_info().rss / (1024 * 1024)
    
    # Print the memory consumed
    table_data.append([n,execution_time,memory,len(visited_nodes), len(expanded_nodes)])

    Node_Generated.append(len(visited_nodes))
    Node_Expanded.append(len(expanded_nodes))
    
    print("total number of nodes generated : ", len(visited_nodes), "Total number of Best nodes expanded : ", len(expanded_nodes))

    # Print the elapsed time
    print(f"Elapsed time: {execution_time} seconds")
    
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
plt.title('RBFS Algorithm for Tower of Hanoi')
plt.legend()

# Display the plot
plt.show()

