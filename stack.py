def is_valid_parentheses(s):
    
    stack = []
    open_bracket = ['(', '[', '{', '<']
    bracket_map = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>'   
    }
    
    for bracket in s:
        if bracket in open_bracket:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            else:
                last_bracket = stack.pop()
                if (bracket != bracket_map[last_bracket]):
                    return False
                
    if len(stack) == 0: 
        return True
    else:
        return False               

print(is_valid_parentheses('[[({<>})]]'))
print(is_valid_parentheses('({[)]}'))
print(is_valid_parentheses('})]]'))


def is_valid_parentheses_optimize(s):
    
    # optimize space complexity
    if len(s) % 2 != 0:
        return False
    # mapping open bracket with close bracket
    # apply this method help check close bracket faster
    bracket_mapping = {
        ']' : '[', 
        ')' : '(',
        '}' : '{',
        '>' : '<'
    }
    stack = []
    
    for char in s:
        # if close bracket
        if char in bracket_mapping:
            # get last element, if stack empty use fake value
            top_bracket = stack.pop() if stack else '#'
            
            a
        else:
            # if open bracket save to stack
            stack.append(char)
            
    return not stack # return True if stack empty

# Test cases
print(is_valid_parentheses_optimize('[[({<>})]]')) # True
print(is_valid_parentheses_optimize('({[)]}'))      # False
print(is_valid_parentheses_optimize('})]]'))        # False
            
            