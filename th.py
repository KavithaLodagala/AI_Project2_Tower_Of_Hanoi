class HanoiNode:
    def __init__(self, n, source_peg, target_peg, auxiliary_peg):
        self.n = n  # Number of disks
        self.source_peg = source_peg  # Source peg
        self.target_peg = target_peg  # Target peg
        self.auxiliary_peg = auxiliary_peg  # Auxiliary peg
        self.gn=0
        self.hn=0
        self.children = []

def build_hanoi_tree(n, source_peg, target_peg, auxiliary_peg):
    root = HanoiNode(n, source_peg, target_peg, auxiliary_peg)
    stack = [root]

    while stack:
        current_node = stack.pop()
        n = current_node.n

        if n == 1:
            continue  # Base case, no further recursion needed

        print(len(current_node.children))
        # Create child nodes and push them onto the stack
        auxiliary_node = HanoiNode(n - 1, source_peg, auxiliary_peg, target_peg)
        current_node.children.append(auxiliary_node)
        stack.append(auxiliary_node)

        move_node = HanoiNode(1, source_peg, target_peg, auxiliary_peg)
        current_node.children.append(move_node)

        stack.append(move_node)

        auxiliary_node = HanoiNode(n - 1, auxiliary_peg, target_peg, source_peg)
        current_node.children.append(auxiliary_node)
        stack.append(auxiliary_node)

    return root

def print_hanoi_tree(node, level=0):
    if node is not None:
        print(" " * (level * 2) + f"Move disk {node.n} from {node.source_peg} to {node.target_peg}")
        for child in node.children:
            print_hanoi_tree(child, level + 1)

n = 3  # Number of disks
source_peg = "A"
target_peg = "C"
auxiliary_peg = "B"

root = build_hanoi_tree(n, source_peg, target_peg, auxiliary_peg)
print_hanoi_tree(root)
