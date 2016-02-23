# Internetwache 2016 : Code (90)

**Category:** Code |
**Points:** 90 |
**Name:** Dark Forest |
**Solves:** 94 |
**Description:**

> Someone pre-ordered a forest and now I'm lost in it. There are a lot of binary trees in front and behind of me. Some are smaller or equal-sized than others. Can you help me to invert the path and find out of the forest? Hint: It's about (inverted) BSTs. Don't forget the spaces.
>
>Service: 188.166.133.53:11491

___

## Write-up
With only pre-order string, no one can establish that tree. Fortunately, the hint tells us that it's a BST(Binary Search Tree). Therefore, we can generate the tree.

use this as an example:
```
preOrder="[40, 38, 19, 6]"
```
As it's pre-order, the root is 40. And as it's a BST, we can tell the 38 and 19 is in 40's left children tree while 6 is in the right. Therefore, the tree can be easily generated using recursion.
```python
def CreateTree(root, nodeArray):
    root.data=int(nodeArray[0].strip())
    nodeArray=nodeArray[1:]
    i=0
    flag=False
    for i in range(0,len(nodeArray)):
        if int(nodeArray[i].strip())>root.data:
            flag=True
            break
    if flag:
        leftArray=nodeArray[0:i]
        rightArray=nodeArray[i:]
    else:
        leftArray=nodeArray
        rightArray=[]
    if len(leftArray)>0:
        root.left = Node()
        CreateTree(root.left, leftArray)
    if len(rightArray)>0:
        root.right = Node()
        CreateTree(root.right, rightArray)
```
To do the invert function, just use recursion, it's easy.
```python
def invert(root):
    if root != None:
        temp=root.left
        root.left=root.right
        root.right=temp
        invert(root.left)
        invert(root.right)
```
