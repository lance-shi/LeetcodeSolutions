class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                pal_list = list(palindrome)
                pal_list[i] = "a"
                return "".join(pal_list)

        pal_list = list(palindrome)
        pal_list[-1] = "b"
        return "".join(pal_list)