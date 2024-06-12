class Solution:
    def similarPairs(self, words: List[str]) -> int:
        similar_pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    similar_pairs += 1
        return similar_pairs
