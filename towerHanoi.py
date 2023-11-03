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
        self.children = []

    
    def heuristic(self):
        hn=0
        sn=len(self.source_rings)
        for i in range(len(self.source_rings)):
            hn+=sn-i-1
            hn+=self.n-self.source_rings[i]+1

        tn=len(self.target_rings)
        for i in range(len(self.target_rings)):
            if(self.n-i-self.target_rings[i]!=0):
                hn+=tn-i
                hn+=self.n-self.target_rings[i]+1
        
        an=len(self.auxiliary_rings)
        for i in range(len(self.auxiliary_rings)):
            hn+=an-i-1
            hn+=self.n-self.auxiliary_rings[i]+1
        
        return hn

    def get_fn(self):
        return self.gn+self.hn

    def print_tower_of_hanoi(self):
        print("g(n):",self.gn," h(n):",self.hn," f(n)=",self.gn+self.hn)
        print(self.source_peg,"-->",self.source_rings)
        print(self.target_peg,"-->",self.target_rings)
        print(self.auxiliary_peg,"-->",self.auxiliary_rings)
    

    def check_in_visited(self):
        s=self.source_peg+''.join(list(map(str,self.source_rings)))+self.target_peg+''.join(list(map(str,self.target_rings)))+self.auxiliary_peg+''.join(list(map(str,self.auxiliary_rings)))
        if(s not in visited_nodes):
            visited_nodes.append(s)
            return False
        else:
            return True
    

    def build_hanoi_tree(self):
        global count
        closed=[]
        best_node=None
        s=self.check_in_visited()
        while(open):
            open.sort(reverse=True,key=lambda x:x[2])
            
            """
            print("\n**********Best Node picked from open*********")
            print("\nOpen-->[",end="")
            for i in range(len(open)):
                print(open[i][1]+str(open[i][2]),end=" ")
            print("]")
            
            print("Closed-->[",end="")
            for i in range(len(closed)):
                print(closed[i][1]+str(closed[i][2]),end=" ")
            print("]")
            """
            
            best_node=open.pop()
            closed.append(best_node)
            best_node=best_node[0]
            sn=len(best_node.source_rings)
            tn=len(best_node.target_rings)
            an=len(best_node.auxiliary_rings)
            print("******Best node")
            best_node.print_tower_of_hanoi()
            if((best_node!=None and best_node.target_rings==expected_rings_order)):
                print("Disks are placed in target pole B")
                break
            #print("****Expanding the best node****")
            if(sn>0):
                if(tn<n and ((tn>0 and sn>0 and best_node.source_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                    ring=best_node.source_rings[-1]
                    child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and sn>0 and best_node.source_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                    ring=best_node.source_rings[-1]
                    child_node = TowerOfHanoi(n,best_node.source_peg, best_node.source_rings[:sn-1], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()
            if(tn>0):
                if(sn<n and ((sn>0 and tn>0 and best_node.target_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                    ring=best_node.target_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings,best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()
                if(an<n and ((an>0 and tn>0 and best_node.target_rings[-1]<best_node.auxiliary_rings[-1]) or an==0)):
                    ring=best_node.target_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings[:tn-1],best_node.auxiliary_peg,best_node.auxiliary_rings+[ring],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()

            if(an>0):
                if(sn<n and ((sn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.source_rings[-1]) or sn==0)):
                    ring=best_node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings+[ring], best_node.target_peg, best_node.target_rings,best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()

                if(tn<n and ((tn>0 and an>0 and best_node.auxiliary_rings[-1]<best_node.target_rings[-1]) or tn==0)):
                    ring=best_node.auxiliary_rings[-1]
                    child_node= TowerOfHanoi(n,best_node.source_peg, best_node.source_rings, best_node.target_peg, best_node.target_rings+[ring],best_node.auxiliary_peg,best_node.auxiliary_rings[:an-1],best_node.gn+1)
                    best_node.children.append(child_node)
                    if(not child_node.check_in_visited()):
                        open.append([child_node,states[count],child_node.get_fn()])
                        count+=1
                        #child_node.print_tower_of_hanoi()
        return root



n = 6  # Number of rings
source_peg = "A"
target_peg = "B"
auxiliary_peg = "C"
count=0

alp=list(map(chr, range(65, 91)))

states=[]
for i in range(1,4):
    for comb in product(alp, repeat=i):
        states.append(''.join(comb))

expected_rings_order=list(range(n,0,-1))
root = TowerOfHanoi(n,source_peg, expected_rings_order, target_peg, [],auxiliary_peg,[],0)
open=[[root,states[count],root.get_fn()]]
count+=1
visited_nodes=[]
root.build_hanoi_tree()

