import unittest

class Test_test_1(unittest.TestCase):
    def test_A(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEquals(findLCA(root, 4, 5), 2)
        self.assertEquals(findLCA(root, 4, 6), 1)
        self.assertEquals(findLCA(root, 3, 4), 1)
        self.assertEquals(findLCA(root, 2, 4), 2)

if __name__ == '__main__':
    unittest.main()