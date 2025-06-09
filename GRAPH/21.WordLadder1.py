class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        st = set(wordList)
        st.discard(beginWord)

        queue = []
        queue.append((beginWord, 1))

        while len(queue) != 0:
            (node, step) = queue.pop(0)
            if node == endWord:
                return step

            for x in range(len(node)):
                for y in range(ord('a'), ord('z') + 1):
                    next_word = node[: x] + chr(y) + node[x + 1:]
                    if next_word in st:
                        queue.append((next_word, step + 1))
                        st.discard(next_word)
        return 0


