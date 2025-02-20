class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insert (root, value):


if __name__ == "__main__":
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    root = None

    node = TreeNode()
    node.data = groups[0]

    root = node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            elif group > current.data:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료")

    find_group = input("찾을 그룹명:")

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right


    delete_group = input('삭제할 그룹명:')

    current = root
    parent = None
    while True:
        if delete_group == current.data:

            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                elif parent.right == current:
                    parent.right = None
                print(current.data,"을(를) 삭제했습니다.")
                del current
                break
            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                elif parent.right == current:
                    parent.right = current.right
                print(current.data, "을(를) 삭제했습니다.")
                del current
                break
            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                elif parent.right == current:
                    parent.right = current.left
                print(current.data, "을(를) 삭제했습니다.")
                del current
                break
            elif current.left != None and current.right != None:
                current_copy_parent = current
                current_copy = current.right
                while current_copy.left is not None:
                    current_copy_parent = current_copy
                    current_copy = current_copy.left
                print(current.data,'을(를) 삭제했습니다.')
                current.data = current_copy.data

                break

        elif delete_group < current.data:
            if current.left is None:
                print(delete_group,'이(가) 트리에 없음')
                break
            parent = current
            current = current.left

        elif delete_group > current.data:
            if current.right is None:
                print(delete_group, '이(가) 트리에 없음')
                break
            parent = current
            current = current.right

    def inorder_traversal(node):
        if node is not None:
            print(node.data)
            inorder_traversal(node.left)
            inorder_traversal(node.right)


    # BST의 전체 노드 출력
    inorder_traversal(root)