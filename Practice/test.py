word1 = "234"
word2 = "12313"
# print(word1.pop(0))
word_len =  len(word1) if len(word1) > len(word2) else len(word2)

class Solution:
    def isPalindrome(x: int) -> bool:
      if x < 0:
          return "False"
      
      str_num = str(x)
      if str_num == str_num[::-1]:
          return f"{x} is a palindrome"
      else:
          return 'False'

print(Solution.isPalindrome(10))
