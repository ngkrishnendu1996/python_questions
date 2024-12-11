#Write a function generate_parentheses(n) that takes an integer n and returns all combinations of well-formed parentheses with n pairs.

def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        # If the current combination is complete, add it to the result
        if len(current) == 2 * n:
            result.append("".join(current))
            return
        
        # If we can add an open parenthesis, do so
        if open_count < n:
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()  # Backtrack
        
        # If we can add a close parenthesis, do so
        if close_count < open_count:
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()  # Backtrack

    result = []
    backtrack([], 0, 0)
    return result

# Example usage:
n = 3
print(generate_parentheses(n))
