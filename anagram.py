#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def groupAnagrams(self, strs):
        """
        Groups anagrams in a list of strings.

        Args:
        strs (List[str]): The list of strings to group.

        Returns:
        List[List[str]]: The groups of anagrams.
        """
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())

ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# In[ ]:




