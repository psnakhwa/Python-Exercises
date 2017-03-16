class Node:
    def __init__(self,data,_next=None):
        self.data=None
        self.next=None
    
def main():
    nodes=[]
    num= int(input("Enter Number: "))
    while num !=-1:
        n = Node(num)
        nodes.append(n)
        num=int(input("Enter Number: "))


    if len(nodes) == 0:
        return
    
    nodes = sorted(nodes, key = lambda nodes: nodes.data)

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        print nodes[i].data,

    print nodes[-1].data

main()
