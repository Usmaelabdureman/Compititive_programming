    """
    The Festive Evening
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

It's the end of July – the time when a festive evening is held at Jelly Castle! Guests from all over the kingdom gather here to discuss new trends in the world of confectionery. Yet some of the things discussed here are not supposed to be disclosed to the general public: the information can cause discord in the kingdom of Sweetland in case it turns out to reach the wrong hands. So it's a necessity to not let any uninvited guests in.

There are 26 entrances in Jelly Castle, enumerated with uppercase English letters from A to Z. Because of security measures, each guest is known to be assigned an entrance he should enter the castle through. The door of each entrance is opened right before the first guest's arrival and closed right after the arrival of the last guest that should enter the castle through this entrance. No two guests can enter the castle simultaneously.

For an entrance to be protected from possible intrusion, a candy guard should be assigned to it. There are k such guards in the castle, so if there are more than k opened doors, one of them is going to be left unguarded! Notice that a guard can't leave his post until the door he is assigned to is closed.

Slastyona had a suspicion that there could be uninvited guests at the evening. She knows the order in which the invited guests entered the castle, and wants you to help her check whether there was a moment when more than k doors were opened.

Input
Two integers are given in the first string: the number of guests n and the number of guards k (1 ≤ n ≤ 106, 1 ≤ k ≤ 26).

In the second string, n uppercase English letters s1s2... sn are given, where si is the entrance used by the i-th guest.

Output
Output «YES» if at least one door was unguarded during some time, and «NO» otherwise.

You can output each letter in arbitrary case (upper or lower).

Examples
inputCopy
5 1
AABBB
outputCopy
NO
inputCopy
5 1
ABABB
outputCopy
YES
Note
In the first sample case, the door A is opened right before the first guest's arrival and closed when the second guest enters the castle. The door B is opened right before the arrival of the third guest, and closed after the fifth one arrives. One guard can handle both doors, as the first one is closed before the second one is opened.

In the second sample case, the door B is opened before the second guest's arrival, but the only guard can't leave the door A unattended, as there is still one more guest that should enter the castle through this door.


    """
    
    
n, k = map(int, input().split())
s = input()
count = 0
entrCnt = {}
entrSeen = {}

for entr in s:
    if entr in entrCnt:
        entrCnt[entr] += 1
    else:
        entrCnt[entr] = 1
        entrSeen[entr] = 1

for entr in s:
    entrCnt[entr] -= 1

    if entrSeen[entr] == 1:
        count += 1

    if count > k:
        print("YES")
        break

    if entrCnt[entr] == 0:
        count -= 1
        entrSeen[entr] = 0
    else:
        print("NO")
