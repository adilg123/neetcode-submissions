class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        sMap = {}
        for s in strs:
        
            sortedString = "".join(sorted(s))

            #act: [cat,tac,act]

            if sortedString in sMap:
                sMap[sortedString].append(s)#add to current value list

            else:
                sMap[sortedString] = [s]
            
        return list(sMap.values())



