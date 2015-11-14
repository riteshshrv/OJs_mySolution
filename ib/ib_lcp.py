'''LCPBookmark
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be “a”.'''

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res = strs[0]
        for s in strs[1:]:
            n = len(s)
            for i, c in enumerate(res):
                if i >= n or res[i] != s[i]:
                    res = res[:i]
                    break
        return res
