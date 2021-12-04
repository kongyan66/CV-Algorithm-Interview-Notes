/**
 * @author: koncaihua
 * @date: 2021/12/4
 * @description:
 */

class ListNode:
    def __init__(self,value=1,next=None):
        self.value = value
        self.next = next
        
# create the List_node
def create_listnode(arr):
    head = Node(0)
    head_guard = head
    for i in range(len(arr)):
         new_node = Node(arr[i])
         head.next = new_node
         head = head.next
    return head_guard.next
 
# 反转链表
def reverseList(head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next  # 暂存后继节点 cur.next
        cur.next = pre  # 修改 next 引用指向
        pre = cur       # pre 暂存 cur
        cur = tmp       # cur 访问下一节点
    return pre
 
if __name__ == "__main__":
    # 主函数输入列表
    arr = [1, 4, 3, 2, 5]
    # 得到头节点
    headNode = create_listnode(arr)
    # 反转
    head_new = reverseList(headNode)
