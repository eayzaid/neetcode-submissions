class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode ( word ) : 
            tab = [0] * 26
            for char in word : 
                tab[ord(char) - ord('a')] += 1
            return "_".join([str(num) for num in tab])
        dict = {}
        for word in strs : 
            key = encode(word)
            dict.setdefault(key,[]).append(word)
        return [dict[key] for key in dict.keys()]