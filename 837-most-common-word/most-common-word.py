import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.split()

        d = {}

        for word in words:
            if word not in banned:
                d[word] = d.get(word, 0) + 1

        maximum = 0
        res = ""

        for key, value in d.items():
            if value > maximum:
                maximum = value
                res = key

        return res