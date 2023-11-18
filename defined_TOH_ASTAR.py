from itertools import product
import time
import matplotlib.pyplot as plt
import psutil
from tabulate import tabulate

class TowerOfHanoi:

    def __init__(self,n,source_peg, target_peg,auxiliary_peg,level):
        self.root=None


    def __init__(self,n,source_peg, source_rings, target_peg, target_rings,auxiliary_peg,auxiliary_rings,level):
        self.n = n  # Number of disks
        self.source_peg = source_peg  # Source peg
        self.source_rings=source_rings
        self.target_peg = target_peg  # Target peg
        self.target_rings = target_rings
        self.auxiliary_peg = auxiliary_peg  # Auxiliary peg
        self.auxiliary_rings = auxiliary_rings
        self.gn=level
        self.hn=self.heuristic_roopika(expected_rings_order)
        #self.hn=self.heuristic()
        self.children = []

    def heuristic_roopika(self,reference_sequence):
        hn =0
        mismatched_elements =0
        empty_slots =0 
        # Check if the array is empty
        if not self.target_rings:
            return 3  # Return 3 for an empty array
        #else:
        if len(self.target_rings) < 3:
                empty_slots = len(reference_sequence) - len(self.target_rings)
            # Check if the order of any one element in the input array matches the reference array
        for i in range(len(self.target_rings)):
                if self.target_rings[i] != reference_sequence[i]:
                    mismatched_elements = mismatched_elements + 1
        hn= mismatched_elements + empty_slots
        return hn

       
    def heuristic_kavitha(self):
        hn=0
        sn=len(self.source_rings)
        for i in range(len(self.source_rings)):
            hn+=sn-i-1
            hn+=self.source_rings[i]

        tn=len(self.target_rings)
        for i in range(len(self.target_rings)):
            if(self.n-i-self.target_rings[i]!=0):
                hn+=tn-i-1
                hn+=self.target_rings[i]
        
        an=len(self.auxiliary_rings)
        for i in range(len(self.auxiliary_rings)):
            hn+=an-i-1
            hn+=self.auxiliary_rings[i]
        
        return hn
   
    
    # this heuristic calculates the weighted sum of the number of discs not on the destination rod
    def heuristic_sakshi(self):
        tn = len(self.target_rings)
        sum = 0
        for i in range(1, self.n + 1):
            if not (i in self.target_rings): sum += i
        return sum
   
    # returns evaluation function values
    def get_fn(self):
        return self.gn+self.hn
    #prints states of tower of hanoi
    def print_tower_of_hanoi(self, count):
        print("g(n):",self.gn," h(n):",self.hn," f(n)=",self.gn+self.hn)
        print(self.source_peg,"-->",self.source_rings)
        print(self.target_peg,"-->",self.target_rings)
        print(self.auxiliary_peg,"-->",self.auxiliary_rings)
        #print("\n")
        #print("This is the current count for the nodes generated : ", count)
        #total_node_expanded =[]
        #heuristic_of_expanded =[]
        total_node_expanded.append(count)
        heuristic_of_expanded.append(self.hn)
    
    
    #function to check visited nodes 
    def check_in_visited(self):
        s=self.source_peg+''.join(list(map(str,self.source_rings)))+self.target_peg+''.join(list(map(str,self.target_rings)))+self.auxiliary_peg+''.join(list(map(str,self.auxiliary_rings)))
        if(s not in visited_nodes):
            visited_nodes.append(s)
            return False
        else:
            return True
    #function to generate child nodes (states/function calls)
    def generate_child_nodes(self,best_node, sn, tn, an,count):
            if(sn>0):
                if(tn<n and ((tn>0 and sn>0 and best_node.source_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                    ring=best_node.source_rings[-1]
                    child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("generated child node number=",count)
                        #print("This is the current count for the nodes generated : ", count)
                        #child_node.print_tower_of_hanoi(count)
                if(an<n and ((an>0 and sn>0 and best_node.source_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                    ring=best_node.source_rings[-1]
                    child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("generated child node number=", count)
                        #child_node.print_tower_of_hanoi(count)
            if(tn>0):
                if(sn<n and ((sn>0 and tn>0 and best_node.target_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                    ring=best_node.target_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("generated child node number=", count)
                        #child_node.print_tower_of_hanoi(count)
                if(an<n and ((an>0 and tn>0 and best_node.target_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                    ring=best_node.target_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("generated child node number=", count)
                        #child_node.print_tower_of_hanoi(count)

            if(an>0):
                if(sn<n and ((sn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                    ring=best_node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("generated child node number=", count)
                        #child_node.print_tower_of_hanoi(count)

                if(tn<n and ((tn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                    ring=best_node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #print("Generated child node number=", count)
                        #child_node.print_tower_of_hanoi(count)
            return count

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
            
        
    def build_hanoi_tree(self):
        global count
        #global count_1
        closed=[]
        best_node=None
        s=self.check_in_visited()
        while(open):
            open.sort(reverse=True,key=lambda x:x[2])
            #self.print_open_closed(open,closed)            
            best_node=open.pop()
            #print("This is best node : ", best_node[0], "This is the heuristic of best node  : ", best_node[2])
            closed.append(best_node)
            best_node=best_node[0]
            sn=len(best_node.source_rings)
            tn=len(best_node.target_rings)
            an=len(best_node.auxiliary_rings)
            #print("\n")
            print("****** Selected Best node ****** " )
            best_node.print_tower_of_hanoi(count)
            if((best_node!=None and best_node.target_rings==expected_rings_order)):
                print("\n")
                print("Disks are placed in target pole B")
                break
            count = self.generate_child_nodes(best_node, sn, tn, an,count)
        print("\n")
        print("total number of nodes generated : ", len(open)+len(closed)," " "Total number of Best nodes expanded : ", len(closed))

        return (len(open)+len(closed),len(closed))

start_time1=time.time()
n = 3  # Number of rings
Time_Elapsed=[]
No_of_disks=[]
Node_Generated=[]
Node_Expanded=[]
Memory_Used=[]
table_data=[]
table_data.append(["Number of Disks","Elapsed Time","Memory Used","Nodes Generated","Nodes Expanded"])
#time.time()-start_time1<600
while(n<12):
    #print(time.time()-start_time1,time.time()-start_time1>10)
    print("starting A* algorithm for",n, "disks")
    print("\n")
    count = 0
    source_peg = "A"
    target_peg = "B"
    auxiliary_peg = "C"
    count_1=0

    #To get a combination of alphabets from a single letter to 4 letters 
    alp=list(map(chr, range(65, 91)))
    #To set these combinations as state names
    states=[]
    for i in range(1,6):
        for comb in product(alp, repeat=i):
            states.append(''.join(comb))

    #To set the expected order of rings on the target peg and source peg
    expected_rings_order=list(range(n,0,-1))
    
    #Set the root node by calling the class and initializing them
    root = TowerOfHanoi(n,source_peg, expected_rings_order, target_peg, [],auxiliary_peg,[],0)

    #add the root to the open list along with state and f(n) value of the root node
    open=[[root,states[count],root.get_fn()]]
    count+=1
    visited_nodes=[]
    total_node_expanded =[]
    heuristic_of_expanded =[]

    # Record the start time
    start_time = time.time()

    
    #build the tower of hanoi tree using this root node.
    generated,expanded=root.build_hanoi_tree()

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    
    memory = psutil.Process().memory_info().rss / (1024 * 1024)
    Memory_Used.append(memory)
    Node_Generated.append(generated)
    Node_Expanded.append(expanded)

    table_data.append([n,elapsed_time,memory,generated,expanded])
    
    # Print the elapsed time
    print("\n")
    print(f"Elapsed time: {elapsed_time} seconds")
    print("\n")
    print("Memory consumed : ", memory, "MB")
    No_of_disks.append(n)
    n+=1

print("\n")
print(tabulate(table_data))
# graph plotting for each heuristic to compare number of nodes generated and number of nodes expanded for each disk count
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



