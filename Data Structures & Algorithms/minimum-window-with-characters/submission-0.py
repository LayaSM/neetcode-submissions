class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)

        res_left = -1
        res_right = -1
        res_len = len(s)+1

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                window_size = right - left + 1

                if window_size < res_len:
                    res_len = window_size
                    res_left = left
                    res_right = right

                left_char = s[left]
                window[left_char] -= 1

                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                left += 1

        if res_len <= len(s):
            return s[res_left : res_right + 1]
        else: 
            return ""





        