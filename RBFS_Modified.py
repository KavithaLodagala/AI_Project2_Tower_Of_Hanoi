from itertools import product

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
        self.hn=self.heuristic()
        self.fn=self.gn+self.hn
        self.child=[]

    
    def heuristic(self):
        hn=0
        sn=len(self.source_rings)
        for i in range(len(self.source_rings)):
            hn+=sn-i-1
            hn+=self.source_rings[i]

        tn=len(self.target_rings)
        for i in range(len(self.target_rings)):
            if(self.n-i-self.target_rings[i]!=0):
                hn+=tn-i
                hn+=self.target_rings[i]
        
        an=len(self.auxiliary_rings)
        for i in range(len(self.auxiliary_rings)):
            hn+=an-i-1
            hn+=self.auxiliary_rings[i]
        return hn

    def print_tower_of_hanoi(self):
        print("g(n):",self.gn," h(n):",self.hn," f(n)=",self.fn)
        print(self.source_peg,"-->",self.source_rings)
        print(self.target_peg,"-->",self.target_rings)
        print(self.auxiliary_peg,"-->",self.auxiliary_rings)
    

    def goal_test(self,node):
        s=node.source_peg+''.join(list(map(str,node.source_rings)))+node.target_peg+''.join(list(map(str,node.target_rings)))+node.auxiliary_peg+''.join(list(map(str,node.auxiliary_rings)))
        p=''.join(list(map(str,list(range(node.n,0,-1)))))
        if(s=='AB'+p+'C'):
            return True
        else:
            return False

    def Recursive_best_first_search(self,initial_node):
        return self.RBFS_TowerOfHanoi(initial_node,10000)
        
    def check_in_visited(self):
        s=self.source_peg+''.join(list(map(str,self.source_rings)))+self.target_peg+''.join(list(map(str,self.target_rings)))+self.auxiliary_peg+''.join(list(map(str,self.auxiliary_rings)))
        if(s not in visited_nodes):
            visited_nodes.append(s)
            return False
        else:
            return True
    
    def RBFS_TowerOfHanoi(self,node,f_limit):
        global expanded_nodes
        if(self.goal_test(node)): 
            return "Success",node.fn
        successors=[]
                    
        sn=len(node.source_rings)
        tn=len(node.target_rings)
        an=len(node.auxiliary_rings)
        #print("children nodes")
        #node.print_tower_of_hanoi()
        if(node not in expanded_nodes):
            expanded_nodes.append(node)
            if(sn>0):
                if(tn<n and ((tn>0 and sn>0 and node.source_rings[-1]<node.target_rings[-1]) or tn==0)):
                    ring=node.source_rings[-1]
                    child_node = TowerOfHanoi(n,node.source_peg, node.source_rings[:sn-1], node.target_peg, node.target_rings+[ring],node.auxiliary_peg,node.auxiliary_rings,node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and sn>0 and node.source_rings[-1]<node.auxiliary_rings[-1]) or an==0)):
                    ring=node.source_rings[-1]
                    child_node = TowerOfHanoi(n,node.source_peg, node.source_rings[:sn-1], node.target_peg, node.target_rings,node.auxiliary_peg,node.auxiliary_rings+[ring],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
            if(tn>0):
                if(sn<n and ((sn>0 and tn>0 and node.target_rings[-1]<node.source_rings[-1]) or sn==0)):
                    ring=node.target_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings+[ring], node.target_peg, node.target_rings[:tn-1],node.auxiliary_peg, node.auxiliary_rings,node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and tn>0 and node.target_rings[-1]<node.auxiliary_rings[-1]) or an==0)):
                    ring=node.target_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings, node.target_peg, node.target_rings[:tn-1],node.auxiliary_peg,node.auxiliary_rings+[ring],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
            if(an>0):
                if(sn<n and ((sn>0 and an>0 and node.auxiliary_rings[-1]<node.source_rings[-1]) or sn==0)):
                    ring=node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings+[ring], node.target_peg, node.target_rings,node.auxiliary_peg,node.auxiliary_rings[:an-1],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
                if(tn<n and ((tn>0 and an>0 and node.auxiliary_rings[-1]<node.target_rings[-1]) or tn==0)):
                    ring=node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,node.source_peg, node.source_rings, node.target_peg, node.target_rings+[ring],node.auxiliary_peg,node.auxiliary_rings[:an-1],node.gn+1)
                    if(not child_node.check_in_visited()):
                        node.child.append([child_node,child_node.fn])
                        successors.append([child_node,child_node.fn])
                    #child_node.print_tower_of_hanoi()
        else:
            successors=node.child
        if(successors==[]):
            print("Failure",10000,f_limit)
            return "Failure", 10000

        for s in successors:
            s[0].fn=max(s[0].fn , node.fn)
            s[1]=s[0].fn
    
        while(1):
            successors.sort(reverse=True,key=lambda x:x[1])
            best_node=successors[-1]

            if(best_node[0].fn>f_limit):
                print("Failure",best_node[0].fn,f_limit)
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


n = 5 # Number of rings
source_peg = "A"
target_peg = "B"
auxiliary_peg = "C"

visited_nodes=[]
expanded_nodes=[]
expected_rings_order=list(range(n,0,-1))
root = TowerOfHanoi(n,source_peg, expected_rings_order, target_peg, [],auxiliary_peg,[],0)
result,f_value=root.Recursive_best_first_search(root)
print(result,f_value)
print("Number of Nodes generated is ",len(expanded_nodes))

