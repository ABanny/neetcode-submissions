class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            chars_s = []
            chars_t = []
            for a in s:
                chars_s.append(a)
            for b in t:
                chars_t.append(b)

            chars_s.sort()
            chars_t.sort()

            for n in range(len(chars_s)):
                if chars_s[n] == chars_t[n]:
                    anagram = True
                else:
                    anagram = False
                    break

            return anagram

        else:
            return False