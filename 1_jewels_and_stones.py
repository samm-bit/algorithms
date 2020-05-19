# references
# https://leetcode.com/problems/jewels-and-stones
# https://wiki.python.org/moin/TimeComplexity
# https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
# http://www.whatasciicode.com/p/ascii-code-table.html

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        x='a'
        print(ord(x))
#         x = set(J)
#         count=0
#         for i in S:
#             if(i in x):
#                 count+=1
        
#         return count
    
    
# todo 
# put S in array of 52
# upper or lower case
# iterate through J and go to index where we expect to see a matching char -> if match then count++ otherise return
# return count