"""
 Remove Two Letters
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Dmitry has a string s
, consisting of lowercase Latin letters.

Dmitry decided to remove two consecutive characters from the string s
 and you are wondering how many different strings can be obtained after such an operation.

For example, Dmitry has a string "aaabcc". You can get the following different strings: "abcc"(by deleting the first two or second and third characters), "aacc"(by deleting the third and fourth characters),"aaac"(by deleting the fourth and the fifth character) and "aaab" (by deleting the last two).

Input
The first line of input data contains a single integer t
 (1≤t≤104
) — number of test cases.

The descriptions of the test cases follow.

The first line of the description of each test case contains an integer n
 (3≤n≤2⋅105
).

The second line of the description of each test case contains a string s
 of length n
 consisting of lowercase Latin letters.

It is guaranteed that the sum of n
 for all test cases does not exceed 2⋅105
.

Output
For each test case print one integer — the number of distinct strings that can be obtained by removing two consecutive letters.

Example
inputCopy
7
6
aaabcc
10
aaaaaaaaaa
6
abcdef
7
abacaba
6
cccfff
4
abba
5
ababa
outputCopy
4
1
5
3
3
3
1
Note
The first example is explained in the statement.

In the third example, the following strings are obtained: "cdef", "adef", "abef", "abcf", "abcd".

In the seventh example, any deletion will result in the string "aba".


    

    """

# SOLUTION

# correct solution which touches all edge cases
# code is self explanatory
# time complexity is O(n)
# space complexity is O(1)

mod = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ans = 0
    for i in range(n - 1):
        if i == n - 2:
            ans += 1
            break
        else:
            if s[i] == s[i + 2]:
                continue
            else:
                ans += 1
    print(ans)