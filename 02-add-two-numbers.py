from typing import Optional
import pprint

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printnode(self):
        node = self
        while (node):
            print("(" + str(node.val) + ")->", end="")
            node = node.next
        print("")



class Solution:

    def evaluate(self, node):
        i, val = 0, 0
        while (node):
            val += node.val * pow(10, i)
            node = node.next
            i += 1
        return val

    def make_num_list(self, val):
        n = ListNode()
        loop_n_previous = None
        loop_n = n
        while (val > 0):
            loop_n.val = int(int(val) % 10)
            print("val=(%s), loop_n.val=(%s)" % (val, loop_n.val))
            loop_n_previous = loop_n
            loop_n.next = ListNode(None, None)
            loop_n = loop_n.next
            #   Initial solution: remove last digit from val, fails due to round errors when val becomes sufficently large
            #val = int(int(val) / 10)
            if val < 10:
                break
            val = int(str(val)[:-1])
        if (loop_n_previous):
            loop_n_previous.next = None
        n.printnode()
        return n

    #   
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.evaluate(l1)
        n2 = self.evaluate(l2)
        n = n1 + n2
        print(n1)
        print(n2)
        print(n)
        self.make_num_list(n)



def main():
    s = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l1 = s.make_num_list(1000000000000000000000000000001)

    s.addTwoNumbers(l1, l2)


if __name__ == "__main__":
    main()

