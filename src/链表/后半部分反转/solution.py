class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def create_nodes(arr):
    head0 = ListNode()
    dummy = head0
    for i in range(len(arr)):
        new_node = ListNode(arr[i])
        head0.next = new_node
        head0 = head0.next
    return dummy.next

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_node(head,middle):
    dummy = head
    pre = None
    cur = middle.next
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    middle.next = pre
   # middle.next.next = None
    return dummy

def print_node(head):
    cur = head
    arr = []
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    head = create_nodes(arr)
    print_node(head)
    head_middle = get_middle(head)
    print_node(head_middle)
    head0 = reverse_node(head,head_middle)
    print_node(head0)
