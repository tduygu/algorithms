"""
Given a string, find the length of the longest substring without repeating characters
"""
def findLongestSubstring(s: str) -> int:
    m = {}
    left = 0
    right = 0
    ans = 0
    n = len(s)
    while left < n and right < n:
        el = s[right]
        if el in m:
            left = max(left, m[el] + 1)
        m[el] = right
        ans = max(ans, right - left + 1)
        right += 1
    return ans


def find_longest_nonrepeating(arr) -> int:
    i = 0
    j = 1
    last_index = len(arr) - 1
    max_length = 0
    if last_index == 0:
        return 1
    while i <= last_index and j <= last_index:
        if not (arr[j] in arr[i:j]):
            j += 1
            if j == len(arr) and i == 0:
                length = j - i
                max_length = length if length > max_length else max_length
        else:
            length = j - i
            i += 1
            if i == j:
                j += 1

            max_length = length if length > max_length else max_length

    return max_length


str1 = "abcabcbb"
print(findLongestSubstring(str1))
#
# str2 = "abdabdeafg"
# print(find_longest_nonrepeating(str2))
#
# print(find_longest_nonrepeating("a"))
# print(find_longest_nonrepeating("bbbbb"))
# print(find_longest_nonrepeating("au"))
# print(find_longest_nonrepeating("abcdefghi"))
print(findLongestSubstring("aab"))


