"""
import copy
class Solution:
    def findSubstring(self, s, words):
        res = []
        def backtrack(WORD, word, n):
            copywords = copy.deepcopy(WORD)
            if n == 0:
                res.append(word)
            else:
                for i,item in enumerate(copywords):
                    WORD = copywords[:i] + copywords[i+1:]
                    backtrack(WORD, word+item, n-1)
        
        backtrack(words, "", len(words))
        res = list(set(res))
        length = len(res[0])
        count = []
        for i in range(0, (len(s)-length+1)):
            if s[i:(i+length)] in res:
                count.append(i)
        return count

s = "barfoofoobarthefoobarman"
words = ["bar","man"]
sol = Solution()
print(sol.findSubstring(s, words))
"""
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            current_count = Counter()
            
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                
                if word in word_count:
                    current_count[word] += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    if j + word_len - left == total_len:
                        result.append(left)
                else:
                    current_count.clear()
                    left = j + word_len
        
        return result
    
s = "barfoofoobarthefoobarman"
words = ["bar","foo", "the"]
sol = Solution()
print(sol.findSubstring(s, words))