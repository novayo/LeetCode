class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # O(row * k) time / O(1) space - where k is the max length of string in sentence
        whole_sentence = ' '.join(sentence) + ' '
        n = len(whole_sentence)
        i = 0
        for _ in range(rows):
            i += cols
            while i > 0 and whole_sentence[i%n] != ' ':
                i -= 1
            i += 1
        return i // n