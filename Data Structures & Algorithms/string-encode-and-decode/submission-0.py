class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""  # Start off with an empty string
        for s in strs:  # for all the worths in the string
            res += (
                str(len(s)) + "#" + s
            )  # here it encodes the length and then a # before each string
        return res  # here is returns the word with a number and # in front

    def decode(self, s: str) -> List[str]:
        res, i = [], 0  # you want a list to be returned and i is a pointer

        while i < len(s):  # while i is less than the length of s
            j = i  # j and i start of in the same place
            while s[j] != "#":  # as long as j has not reached a #
                j += 1  # then j keeps traversing
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res