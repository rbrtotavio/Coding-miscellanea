class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prnt = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data):
        node = TreeNode(data)
        self.root = node


def Inorder_Tree_Walk(node):
    if node != None:
        Inorder_Tree_Walk(node.left)
        print(node, end=" ")
        Inorder_Tree_Walk(node.right)


def Tree_Search(nodo, k):
    aux = None
    while nodo != None and k != nodo.data:
        if k < nodo.data:
            nodo = nodo.left
        else:
            nodo = nodo.right
    return nodo


def Tree_Minimum(nodo):
    while nodo.left != None:
        nodo = nodo.left
    return nodo


def Tree_Maximum(nodo):
    while nodo.right != None:
        nodo = nodo.right
    return nodo


def Tree_Successor(nodo):
    if nodo.right != None:
        return Tree_Minimum(nodo.right)
    y = nodo.prnt
    while y != None and nodo == y.right:
        nodo = y
        y = Tree_Minimum(y)
    return y


def Tree_Predecessor(nodo):
    while nodo.left != None:
        return Tree_Maximum(nodo.left)
    y = nodo.prnt
    while y != None and nodo == y.left:
        nodo = y
        y = Tree_Maximum(y)
    return y


def Tree_Insert(Tree, nodo):
    y = None
    x = tree.root
    while x != None:
        y = x
        if nodo.data < x.data:
            x = x.left
        else:
            x = x.right
    nodo.prnt = y
    if y == None:
        Tree.root = nodo
    else:
        if nodo.data < y.data:
            y.left = nodo
        else:
            y.right = nodo


def Tree_Delete(tree, nodo):
    y = TreeNode(None)
    x = TreeNode(None)
    if nodo.left == None or nodo.right == None:
        y = nodo
        y = Tree_Successor(nodo)
    if y.left != None:
        x = y.left
    else:
        x = y.right
    if x != None:
        x.prnt = y.prnt
    if y.prnt == None:
        tree.root = x
    else:
        if y == y.prnt.left:
            y.prnt.left = x
        else:
            y.prnt.right = x
    if y != nodo:
        nodo.data = y.data
    return y


if __name__ == "__main__":
    tree = BinaryTree(4)
    Tree_Insert(tree, TreeNode(2))
    Tree_Insert(tree, TreeNode(5))
    Tree_Insert(tree, TreeNode(1))
    Tree_Insert(tree, TreeNode(3))


    Inorder_Tree_Walk(tree.root)
    print(' ')
    print(Tree_Search(tree.root, 3))
    print(Tree_Minimum(tree.root))
    print(Tree_Maximum(tree.root))
    print(Tree_Successor(tree.root.left))
    print(Tree_Predecessor(tree.root.left))
    Tree_Insert(tree, TreeNode(6))
    Inorder_Tree_Walk(tree.root)
    Tree_Delete(tree, Tree_Search(tree.root, 5))
    print("")
    Inorder_Tree_Walk(tree.root)
