class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        temp = []
        lg = len(words)
        for i in range(lg):
            for j in range(lg):
                if i == j:
                    continue

                if words[i] in words[j]:
                    temp.append(words[i])
                    break
        return temp
        