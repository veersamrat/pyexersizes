from BSTreeNode import BinarySearchTreeNode

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print(f"Minimun Element is {country_tree.find_min_element()}")
    print(f"Maximum Element is {country_tree.find_max_element()}")
    # print(f"Sum of elements is {country_tree.sum_elements()}")

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree)
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    # print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    # print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    # print(f"Minimun Element is {numbers_tree.find_min_element()}")
    # print(f"Maximum Element is {numbers_tree.find_max_element()}")
    # print(f"Sum of elements is {numbers_tree.sum_elements()}")
    numbers_tree.delete_replace_with_left(20)
    print("after delete:",numbers_tree.in_order_traversal())
    
    
    
    
