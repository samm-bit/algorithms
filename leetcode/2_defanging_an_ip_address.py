# references
# https://leetcode.com/problems/defanging-an-ip-address/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ('[.]'.join((str(i) for i in address.split('.'))))
        
        
