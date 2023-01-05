class Solution:
    def longestPalindrome(self, s: str) -> str:
        prolonged_s = "*" + "*".join(list(s)) + "*"
        prolonged_s_len = 2 * len(s) + 1
        centered_palindrome_lens = [0] * prolonged_s_len
        center = 0
        palindrome_len = 0
        while center < prolonged_s_len:
            while center - palindrome_len - 1 >= 0 and center + palindrome_len + 1 < prolonged_s_len and prolonged_s[center - palindrome_len - 1] == prolonged_s[center + palindrome_len + 1]:
                palindrome_len += 1
            centered_palindrome_lens[center] = palindrome_len

            old_center = center
            old_right_end = old_center + palindrome_len
            center += 1
            palindrome_len = 0
            while center < old_right_end:
                mirrored_new_center = 2 * old_center - center
                if centered_palindrome_lens[mirrored_new_center] < old_right_end - center:
                    # Twice symmetric transforms
                    centered_palindrome_lens[center] = centered_palindrome_lens[mirrored_new_center]
                    center += 1
                elif centered_palindrome_lens[mirrored_new_center] > old_right_end - center:
                    # An interesting, tricky, inspiring but intutive point -> twice symmetric transforms, new center's right end cannot exceed old_right_end.
                    centered_palindrome_lens[center] = old_right_end - center 
                    center += 1
                else:
                    # No contradictions detected -> has to be manually examined.
                    palindrome_len = old_right_end - center
                    break

        max_i = 0
        longest_palindrome_substring_len = 0
        for i in range(prolonged_s_len):
            if centered_palindrome_lens[i] > longest_palindrome_substring_len:
                longest_palindrome_substring_len = centered_palindrome_lens[i]
                max_i = i

        longest_palindrome_substring = "".join(prolonged_s[max_i - centered_palindrome_lens[max_i] : max_i + centered_palindrome_lens[max_i] + 1].split("*"))

        return longest_palindrome_substring



            

            
