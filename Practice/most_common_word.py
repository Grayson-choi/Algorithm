paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

def most_common_word(paragraph):
    words = paragraph.lower().split()
    print(words)

most_common_word(paragraph)