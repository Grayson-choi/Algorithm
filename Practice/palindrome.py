def is_palindrome(word):
    print(word)
    print(word[::-1])
    return word == word[::-1]

    # for i in range(int(len(word)/2)):
    #     if word[i] != word[-(i+1)]:
    #         return False
    # return True



# 테스트+8
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
