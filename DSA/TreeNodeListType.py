class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_type_data(self,type):
        match(type):
            case "name":
               return self.data[0]
            case "desig":
                return  self.data[1]
            case _:
               return self.data[0] +" (" + self.data[1] + ")"

    def print_tree(self,type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.get_type_data(type))
        if self.children:
            for child in self.children:
                child.print_tree(type)
    
    def print_tree_level(self,level,type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.get_type_data(type))
        #print(prefix + self.data)
        if self.children:
            for child in self.children:
                if self.get_level()<level:
                    child.print_tree_level(level,type)
       