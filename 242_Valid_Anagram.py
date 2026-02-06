class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count={}
        #key是字母   value是次数

        #进货
        for char in s:
            if char not in count:
                count[char]=0
                count[char]=count[char]+1
            else:
                count[char]=count[char]+1
        

        #出货
        for char in t:
            if char not in count:
                return False
            else:
                count[char]=count[char]-1
        
        #检查是否为0
        for val in count.values():  #attention its plural  values
            if val!=0:
                return False
        
        return True
