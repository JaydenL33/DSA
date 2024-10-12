from typing import List


def beautifulIndices(s: str, a: str, b: str, k: int):
    result = []
    # List to store the start indices where 'a' occurs in 's'
    a_indices = []
    # List to store the start indices where 'b' occurs in 's'
    b_indices = []
    
    for i in range(len(s)):
        x = s[i:i + len(a)]
        y = s[i:i + len(b)]
        if x == a:
            a_indices.append(i)
        if y == b:
            b_indices.append(i)
    for i in a_indices:
        for j in b_indices:
            if abs(i - j) <= k:
                result.append(i)
                break  # Once we find a valid j, we can stop for this i
    return result

def beautifulIndices(s: str, a: str, b: str, k: int) -> List[int]:
        i, j, res = s.find(a), s.find(b), []
        while i != -1:
            while 0 <= j < i-k: j = s.find(b,j+1)
            if j == -1:         break
            if j <= i+k:        res.append(i)
            i = s.find(a,i+1)
        return res

# Example usage
s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
print(beautifulIndices(s, a, b, k))  # Output: [16, 33]

