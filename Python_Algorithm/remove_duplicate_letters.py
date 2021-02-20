# s = "bcabc"
import collections

s = "cbacdcbc"

def remove_duplicate_letters(s):
    counter, seen, stack = collections.Counter(s), set(), []
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

    # 뒤에 붙일 문자가 남아있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)
    return ''.join(stack)



print(remove_duplicate_letters(s))