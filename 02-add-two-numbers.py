from typing import Optional
import pprint

# Definition for singly-linked list.
class BasicListNode:

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
        n = BasicListNode()
        loop_n_previous = None
        loop_n = n
        while (val > 0):
            loop_n.val = int(int(val) % 10)
            print("val=(%s), loop_n.val=(%s)" % (val, loop_n.val))
            loop_n_previous = loop_n
            loop_n.next = BasicListNode(None, None)
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

    #   Runtime (leetcode): 80ms (beats 20%)
    def addTwoNumbers(self, l1: Optional[BasicListNode], l2: Optional[BasicListNode]) -> Optional[BasicListNode]:
        n1 = self.evaluate(l1)
        n2 = self.evaluate(l2)
        n = n1 + n2
        print(n1)
        print(n2)
        print(n)
        self.make_num_list(n)

    #   LINK: https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution.
    #   Runtime (leetcode): 68ms (beats 75%)
    def addTwoNumbers_Alt1(self, l1, l2):
        start = current = BasicListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = BasicListNode(carry%10)
            current = current.next
            carry //= 10
        return start.next


def main():
    s = Solution()

    l1 = BasicListNode(2)
    l1.next = BasicListNode(4)
    l1.next.next = BasicListNode(3)

    l2 = BasicListNode(5)
    l2.next = BasicListNode(6)
    l2.next.next = BasicListNode(4)

    l1 = s.make_num_list(1000000000000000000000000000001)

    s.addTwoNumbers(l1, l2)
    s.addTwoNumbers_Alt1(l1, l2)


if __name__ == "__main__":
    main()

