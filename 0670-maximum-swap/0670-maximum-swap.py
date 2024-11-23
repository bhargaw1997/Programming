class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters
        digits = list(str(num))
        
        # Record the last occurrence of each digit
        last_occurrence = {int(d): i for i, d in enumerate(digits)}
        
        # Traverse the digits
        for i, digit in enumerate(digits):
            # Check for a larger digit to swap
            for d in range(9, int(digit), -1):
                # If a larger digit exists and appears after the current position
                if d in last_occurrence and last_occurrence[d] > i:
                    # Swap and return the result as an integer
                    digits[i], digits[last_occurrence[d]] = digits[last_occurrence[d]], digits[i]
                    return int("".join(digits))
        
        # If no swap is made, return the original number
        return num
