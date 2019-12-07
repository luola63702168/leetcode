def maxDepth(root):
    if not root:
        return 0
    curLevelNodeList = [root]
    length = 0
    while curLevelNodeList:
        tempNodeList = []
        for node in curLevelNodeList:
            if node.left is not None:
                tempNodeList.append(node.left)
            if node.right is not None:
                tempNodeList.append(node.right)
        curLevelNodeList = tempNodeList
        length += 1
    return length


if __name__ == '__main__':
    print(maxDepth([3, 9, 20, None, None, 15, 7]))
