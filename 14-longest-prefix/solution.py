def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # Empty array
    if len(strs) == 0:
        return ''
    # To compare rest of strings with
    firstWord = strs[0]
    
    # Iterate over the strs array and then iterate
    # over every word, whenever a character
    # doesn't match the first word, we return
    # a splice ignoring the rest of the word
    for i in range(len(firstWord)):
        for word in strs[1:]:
            if i == len(word) or firstWord[i] != word[i]:
                return firstWord[:i]
    return firstWord

    
    
print(longestCommonPrefix(["ab","a"]))