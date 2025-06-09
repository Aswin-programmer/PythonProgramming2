class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        st = set(wordList)
        st.discard(beginWord)

        queue = []
        removed_deff_level = []
        ans = []
        level = 1

        queue.append([beginWord])
        removed_deff_level.append(beginWord)

        while len(queue) != 0:
            words = queue.pop(0)
            word = words[len(words) - 1]

            if level < len(words):
                level += 1
                for rem in removed_deff_level:
                    st.discard(rem)
                removed_deff_level = []

            if word == endWord:
                if len(ans) == 0:
                    ans.append(words)
                elif len(ans[0]) == len(words):
                    ans.append(words)

            for x in range(len(word)):
                for y in range(ord('a'), ord('z') + 1):
                    new_word = word[: x] + chr(y) + word[x + 1:]
                    if new_word in st:
                        for k in words:
                            removed_deff_level.append(k)

                        # words.append(new_word)
                        # queue.append(words) # <= Find why this is causing error.
                        queue.append(words + [new_word])
        return ans


def main():
    sol = Solution()
    print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
main()