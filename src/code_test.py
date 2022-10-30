class Solution:
    def __init__(self):
        self.pre = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recursion(root)

    def recursion(self, root):
        if not root:
            return 
        
        self.recursion(root.left)
        self.recursion(root.right)

        root.left = None
        root.right = self.pre
        self.pre = root

 
        
            
            

    


    

