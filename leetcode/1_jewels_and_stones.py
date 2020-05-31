# references
# https://leetcode.com/problems/jewels-and-stones
# https://wiki.python.org/moin/TimeComplexity
# https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
# http://www.whatasciicode.com/p/ascii-code-table.html

# O(1)
class SolutionOne:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # unordered and unindexed collection 
        x = set(J)
        count=0
        for i in S:
            if(i in x): # avg = O(1), worst = O(n)
                count+=1
        
        return count
    
# O(nm)    
class SolutionTwo:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        # intialise an empty array of all possible characters that could be a jewel (upper and lower case) - almost setting a dictionary
        own_dict=[None]*52
        # place jewels in empty array
        for jew in J:
            if(jew>'Z'):
                own_dict[ord(jew)-71]=jew
            else:
                own_dict[ord(jew)-65]=jew
        # iterate through stones to see if any of them match with the array of jewels
        for stone in S:
            find_jew_at_index=0
            if(stone>'Z'):
                find_jew_at_index = ord(stone)-71
            else:
                find_jew_at_index = ord(stone)-65    
            if(stone==own_dict[find_jew_at_index]):
                count+=1

        return count