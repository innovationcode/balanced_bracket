def balance_check(s):
    if len(s) % 2 != 0:
        return False
    opening = set('([{')
    matches = set([ ('(', ')'), 
                    ('[', ']'),
                    ('{', '}')
                  ])
    stack = []
    for paren in s:
        if paren in opening:
          stack.append(paren)
        else:
          if len(stack) == 0:
            return False
          last_open = stack.pop() 
          if(last_open, paren) not in matches:
              return False
    return len(stack) == 0

print("1   :  ",balance_check('{[()]}'))           # True 
print("2   :  ",balance_check('['))                # False
print("3   :  ",balance_check('{[()]})))'))        # False
print("4   :  ",balance_check('{[([[[])]}'))       # False
print("5   :  ",balance_check('{{{{{([])}'))       # False