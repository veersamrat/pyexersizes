class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        return elements
    
    def find_min_element(self):
        if self.left:
           return self.left.find_min_element()
        else:
            return self.data
    
    def find_max_element(self):
        if self.right:
           return self.right.find_max_element()
        else:
            return self.data
    
    def sum_elements(self):
        countr = 0
        if self.left:
            countr +=self.left.sum_elements()
        if self.right:
            countr +=self.right.sum_elements()
        
        countr +=self.data
        return countr
    
    def delete_replace_with_right(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_replace_with_right(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_replace_with_right(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min_element()
            self.data = min_val
            self.right = self.right.delete_replace_with_right(min_val)

        return self
    
    def delete_replace_with_left(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_replace_with_left(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_replace_with_left(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max_element()
            self.data = max_val
            self.left = self.left.delete_replace_with_left(max_val)

        return self
    
    