class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        
        counter = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            for char in counter:
                counter[char] = min(counter[char], word_count[char])
        
        result = []
        for char, count in counter.items():
            result.extend([char] * count)
        
        return result
