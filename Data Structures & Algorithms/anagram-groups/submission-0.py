class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_angm = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in grp_angm.keys():
                grp_angm[sorted_s].append(s)
            else:
                grp_angm[sorted_s] = [s]
        
        return list(grp_angm.values())