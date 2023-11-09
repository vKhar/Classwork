import random

class minHeap:
    # this is a minHeap that only handles only positive integers
    def __init__(self, size):
        pass

    def is_full(self):
        pass

    # Task 3.1
    # PSEUDO code
    PROCEDURE add(newItem)
        IF minHeap is not full THEN
        
            tree[count] <- newItem
            curr_ptr <- count
            parent_ptr <- QUOTIENT((curr_ptr - 1) DIV 2)
            
			// MISSING PSEUDO-CODE
            
            INCREMENT count BY 1
        ELSE
            OUTPUT "Heap is full. Cannot add."
        END IF
    END PROCEDURE

    def remove_minimum(self):
        if self._count != 0:
            root = self._tree[0]
            self._count -= 1
            temp = self._tree[self._count]
            self._tree[0] = temp
            self._tree[self._count] = -1
            
            done = False
            curr_ptr = 0
            left_ptr = curr_ptr*2 + 1
            right_ptr = curr_ptr*2 + 2
            while not done and left_ptr < self._count:
                if right_ptr < self._count:
                    #has left and right children
                    if self._tree[left_ptr] < self._tree[right_ptr] and self._tree[left_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[left_ptr] = self._tree[left_ptr], self._tree[curr_ptr]
                        curr_ptr = left_ptr
                    elif self._tree[right_ptr] < self._tree[left_ptr] and self._tree[right_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[right_ptr] = self._tree[right_ptr], self._tree[curr_ptr]
                        curr_ptr = right_ptr
                    else:
                        done = True                    
                else:
                    #has only left child
                    if self._tree[left_ptr] < self._tree[curr_ptr]:
                        self._tree[curr_ptr], self._tree[left_ptr] = self._tree[left_ptr], self._tree[curr_ptr]
                        curr_ptr = left_ptr
                    else:
                        done = True

                left_ptr = curr_ptr*2 + 1
                right_ptr = curr_ptr*2 + 2
            return root
        else:
            print("Tree is empty. Cannot remove.")
            return -1

    
    def sort(self):
        # Task 3.2
        # Make use of the function remove_minimum which is implemented for you,
        # implement sort() which returns a sorted list of the items in minHeap.
        # Take note that by calling remove_minimum, the root node is removed from minHeap.
        pass

    
    def display_all_paths(self):
        # Task 3.3
        # Implement display_path which will display all paths from the root of minHeap to its leaves.
        #
        # Hint: minHeap is actually a complete binary tree
        # It is a binary tree in which every level, except possibly the last,
        # is completely filled, and all nodes are as far left as possible.
        #
        # This means that the tree array indices from 0 to count -1 contain all the items in minHeap
        # and nothing after count.
        pass



