"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            print(key)
            d[key] = d.get(key, []) + [w]
        return d.values()

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())