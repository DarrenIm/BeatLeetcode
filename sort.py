class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def twoSum(numbers, target):
    # Approach 1: Hashmap
    # T(n) = O(n)
    # S(n) = O(n)
    num_to_idx = dict()
    for i in range(len(numbers)):
        if target - numbers[i] in num_to_idx:
            return [num_to_idx[target - numbers[i]], i]
        num_to_idx[numbers[i]] = i
    return []

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # write your code here
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[1])
        return merged



'''
Leetcode 147:  Sort a linked list using insertion sort.

Given 1 -> 3 -> 2 -> 4 - > null

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
               |    |
              ptr toInsert
-- locate ptr = 3 by (ptr.val > ptr.next.val)
-- locate toInsert = ptr.next

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
          |         |
   toInsertPre     toInsert
-- locate preInsert = 1 by preInsert.next.val > toInsert.val
-- insert toInsert between preInsert and preInsert.next
Java

    public ListNode insertionSortList(ListNode ptr) {    
        if (ptr == null || ptr.next == null)
            return ptr;
        
        ListNode preInsert, toInsert, dummyHead = new ListNode(0);
        dummyHead.next = ptr;

        while (ptr != null && ptr.next != null) {
            if (ptr.val <= ptr.next.val) {
                ptr = ptr.next;
            } else {      
                toInsert = ptr.next;
                // Locate preInsert.
                preInsert = dummyHead;
                while (preInsert.next.val < toInsert.val) {
                    preInsert = preInsert.next;
                }
                ptr.next = toInsert.next;
                // Insert toInsert after preInsert.
                toInsert.next = preInsert.next;
                preInsert.next = toInsert;
            }
        }
        
        return dummyHead.next;
    }
Python：
'''
def insertionSortList(self, head):

    dummyHead = ListNode(0)
    dummyHead.next = head

    while head and head.next:
        if head.val > head.next.val:
            # Locate nodeToInsert.
            nodeToInsert = head.next
            # Locate nodeToInsertPre.
            nodeToInsertPre = dummyHead
            while nodeToInsertPre.next.val < nodeToInsert.val:
                nodeToInsertPre = nodeToInsertPre.next

            head.next = nodeToInsert.next
            # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
            nodeToInsert.next = nodeToInsertPre.next
            nodeToInsertPre.next = nodeToInsert
        else:
            head = head.next

    return dummyHead.next


if  __name__ == "__main__":
    print(twoSum([1,0,-1], 1))