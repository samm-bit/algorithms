class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ('[.]'.join((str(i) for i in address.split('.'))))
        
        