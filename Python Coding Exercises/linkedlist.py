class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        if temp == None:
            print "Empty"
        while temp:
            print temp.data,
            temp = temp.next

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,data):
        if prev_node == None:
            push(data)
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node = self.head
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node

    def deletedups(self):
        d = {}
        prev = None
        n = self.head
        while n:
            if n.data in d:
                prev.next = n.next
            else:
                d[n.data]=None
                prev = n
            n = n.next

    def deletenode(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def deletenodeatpos(self,position):
        if self.head is None:
            return
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return
        #Find the previous node
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        #get the position of the node ahead of the node to be deleted
        next = temp.next.next
        #unlink the previous node and node to be deleted.
        temp.next = None
        #link previous and node ahead of deleted node.
        temp.next = next

    def findlength(self):
        temp = self.head
        count = 0
        if temp is None:
            print "Count is:",count
        while temp:
            count+=1
            temp = temp.next
        print "Count is ",count

    def findlengthrecur(self,node):
        if node is None:
            return 0
        else:
            return 1 + self.findlengthrecur(node.next)

    def getCount(self):
        return self.findlengthrecur(self.head)

    def swapnodes(self,x,y):
        #do nothing if x and y are same
        if x == y:
            return
        #search for x and keep a track of prev and current
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        #search for y and keep track of prev and curr
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        #if anyone of the nos not present then do nothing
        if currX == None or currY == None:
            return
        #x is not the head of the linked list
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        #y is not the head of the linked list
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX
        #swap pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def getNthnode(self,index):
        curr = self.head
        count = 0
        while curr:
            if curr == index:
                return curr.data
            count+=1
            curr = curr.next

        assert(False)
        return 0

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
        print "Middle element is:",slow_ptr.data

    def printnthnodefromend(self,pos):
        temp = self.head
        len = 0
        while temp:
            temp=temp.next
            len+=1
        if len<pos:
            return
        #start again from head
        temp = self.head
        for i in range(1,len-pos+1):
            temp = temp.next

        print temp.data

    def deletelist(self):
        self.head=None

    def deletenodewithoutprev(self,n1):
        if n1 is None or n1.next is None:
            return False
        new_data = n1.next.data
        n1.data = new_data
        n1.next = n1.next.next
        return True

    def totaloccur(self,n):
        temp = self.head
        count = 0
        while temp:
            if temp.data==n:
                count+=1
            temp = temp.next
        print "count of %d is:"%(n),count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    #Floyd cycle finding algorithm
    def findloop(self):
        slowptr = self.head
        fastptr = self.head
        while slowptr and fastptr and fastptr.next:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if slowptr == fastptr:
                print "Loop found"
                return

    def sortedinsert(self,new_data):
        temp = self.head
        new_node = Node(new_data)
        if temp is None:
            new_node.next = temp
            temp = new_node

        elif temp.data >= new_node.data:
            new_node.next = temp
            temp = new_node
        else:
            while temp.next is not None and temp.data<new_node.data:
                temp = temp.next
        new_node.next =temp.next
        temp.next = new_node
   
l = LinkedList()
l.push(1)
l.push(2)
l.append(3)
l.insertAfter(l.head.next.next,10)
l.deletenode(10)
l.push(1)
l.push(2)
#l.deletenodeatpos(0)
l.push(10)
l.deletenodewithoutprev(l.head)
#l.append(20)
#l.append(30)
#l.deletedups()
#l.printlist()
#l.findlength()
#l.swapnodes(10,30)
##l.push(30)
#l.printlist()
#print "num on 3rd node is : ",l.getNthnode(3)
#l.printMiddle()
#l.deletelist()
#l.reverse()
#l.printlist()
#l.totaloccur(30)
#l.head.next.next.next.next = l.head
#l.findloop()
#print "nth node from last is:"l.printnthnodefromend(1)
#l.sortedinsert(13)
l.printlist()
            
