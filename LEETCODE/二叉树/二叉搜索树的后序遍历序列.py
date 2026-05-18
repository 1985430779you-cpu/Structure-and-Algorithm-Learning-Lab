class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return True
        if len(sequence) == 1:
            return True
        
        index = 0
        while sequence[index] < sequence[-1]:
            index += 1
        list1 = sequence[:index]
        list2 = sequence[index:-1]

        while index < len(sequence)-1:
            if sequence[index] < sequence[-1]:
                return False
            index += 1

        return self.VerifySquenceOfBST(list1) and self.VerifySquenceOfBST(list2)
    
sequence = [5,7,6,9,11,10,8]
sol = Solution()
print(sol.VerifySquenceOfBST(sequence))        