class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ""
        for char in s: 
            if char.isalnum():
                clean_s += char.lower()
                
        front = 0
        back = len(clean_s)-1

        while front < back:
            if(clean_s[front] != clean_s[back]):
                return False
            else:
                front += 1
                back -= 1
        return True
