import socket
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

result=""

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

def PreOrder(root):
    if root != None:
        global result
        result+=', '+str(root.data)
        PreOrder(root.left)
        PreOrder(root.right)

def invert(root):
    if root != None:
        temp=root.left
        root.left=root.right
        root.right=temp
        invert(root.left)
        invert(root.right)
'''
preOrder="[40, 38, 19, 6]"
preOrderStr=preOrder.replace("]","").replace("[","")
root=Node()
CreateTree(root,preOrderStr.split(","))
PreOrder(root)
print result
invert(root)
result=""
PreOrder(root)
print result

'''
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(('188.166.133.53',11491))

data = s.recv(512)

print data
while True:
    print "hohohohoh"
    datas=data.split("\n")
    print len(datas)
    if len(datas)>2:
        preOrderStr=datas[1]
    else:
        preOrderStr=s.recv(512)
    print preOrderStr
    result=""
    preOrderStr=preOrderStr.replace("\n","").split(':')[1].strip()
    preOrderStr=preOrderStr.replace("]","").replace("[","")
    root=Node()
    CreateTree(root,preOrderStr.split(","))
    PreOrder(root)
    print result
    invert(root)
    result=""
    PreOrder(root)
    print result
    result=result.lstrip(",")
    result='['+result.strip()+']'
    print result
    s.send(result+'\n')
    data=s.recv(512)
    print data

s.close()
