
def alien_dictionary(words):
    adj_list = [[] for _ in range(4)]

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        for ind in range(0, min(len(word1), len(word2))):
            if word1[ind] != word2[ind]:
                adj_list[ord(word1[ind]) - ord('a')].append(ord(word2[ind]) - ord('a'))
                break

    indegree = [0 for _ in range(len(adj_list))]
    for node_ind in range(len(adj_list)):
        for adj_node in adj_list[node_ind]:
            indegree[adj_node] += 1

    queue = []
    for node_ind in range(len(adj_list)):
        if indegree[node_ind] == 0:
            queue.append(node_ind)
    ans = []
    while len(queue) != 0:
        node = queue.pop(0)
        ans.append(node)

        for adj_node in adj_list[node]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                queue.append(adj_node)

    for ind in range(len(ans)):
        ans[ind] = chr(ans[ind] + ord('a')) # chr => [int to char] and ord => [char to int]

    return ans

def main():
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print(alien_dictionary(words))
main()