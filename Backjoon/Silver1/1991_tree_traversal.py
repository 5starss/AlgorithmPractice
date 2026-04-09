def preorder(root):
    if root == '.':
        return

    pre_.append(root)
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.':
        return

    inorder(tree[root][0])
    in_.append(root)
    inorder(tree[root][1])

def postorder(root):
    if root == '.':
        return

    postorder(tree[root][0])
    postorder(tree[root][1])
    post_.append(root)

N = int(input())
tree = {}
for _ in range(N):
    n, l, r = input().split()
    tree[n] = [l, r]
pre_ = []
in_ = []
post_ = []
preorder('A')
inorder('A')
postorder('A')
print(''.join(pre_))
print(''.join(in_))
print(''.join(post_))
