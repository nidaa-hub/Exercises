class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def LCA(self, root, p, q):
        current = root
        while current is not None:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current.val


root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(15)
node3 = TreeNode(3)
node4 = TreeNode(7)
node5 = TreeNode(12)
node6 = TreeNode(18)
node7 = TreeNode(1)
node8 = TreeNode(4)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node3.left = node7
node3.right = node8

print("The Lowest Common Ancestor is :", root.LCA(root, node3, node5))


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert2(self.root, key)

    def insert2(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insert2(root.left, key)
        elif key > root.key:
            root.right = self.insert2(root.right, key)
        return root

    def search(self, key):
        return self.search2(self.root, key)

    def search2(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search2(root.left, key)
        return self.search2(root.right, key)

    def delete(self, key):
        self.root = self.delete2(self.root, key)

    def delete2(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete2(root.left, key)
        elif key > root.key:
            root.right = self.delete2(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

    def print_tree(self):
        print("Binary Search Tree:")
        self.print_tree2(self.root, 0)

    def print_tree2(self, root, level):
        if root:
            self.print_tree2(root.right, level + 1)
            print(str(root.key))
            self.print_tree2(root.left, level + 1)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(19)
bst.insert(93)
bst.insert(62)
bst.insert(87)
bst.insert(24)
bst.insert(8)
bst.print_tree()
search_result = bst.search(82)
if search_result:
    print(f"The key found in the BinarySearchTree")
else:
    print(f"The key not found in the BinarySearchTree")
bst.delete(5)
bst.print_tree()

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])
        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            if current not in visited:
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None


graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)
graph.add_edge(4, 8)
graph.add_edge(5, 9)
graph.add_edge(6, 10)

start_node = 1
end_node = 10

shortest_path = graph.shortest_path(start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {end_node}")