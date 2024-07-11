from TreeNodeListType import TreeNode

def build_location_tree():
     # CTO Hierarchy
    infra_head = TreeNode(("Vishwa","Infrastructure Head"))
    infra_head.add_child(TreeNode(("Dhaval","Cloud Manager")))
    infra_head.add_child(TreeNode(("Abhijit", "App Manager")))

    cto = TreeNode(("Chinmay", "CTO"))
    cto.add_child(infra_head)
    cto.add_child(TreeNode(("Aamir", "Application Head")))

    # HR hierarchy
    hr_head = TreeNode(("Gels","HR Head"))

    hr_head.add_child(TreeNode(("Peter","Recruitment Manager")))
    hr_head.add_child(TreeNode(("Waqas", "Policy Manager")))

    ceo = TreeNode(("Nilupul", "CEO"))
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree("both")
    
