class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_map={}

        for word in strs:
            sorted_word="".join(sorted(word))  #sorted会 打散    join代表粘回去   ""说明没有空隙
            
            if sorted_word in big_map:
                big_map[sorted_word].append(word)   #set用add 大袋子，专门加进去  list有顺序append加在最后面
            else:
                big_map[sorted_word]=[word]
    

        return list(big_map.values()) #因为leetcode要求返回的是list 所以 要用list打包成一个列表盒子 big_map.values()只是一个视图

    

        
    
