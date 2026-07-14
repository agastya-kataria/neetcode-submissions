class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countA, countB = [0]*26, [0]*26

        for i in range(len(s1)):
            countA[ord(s1[i]) - ord('a')] +=1
            countB[ord(s2[i]) - ord('a')] +=1
        matches = 0
        for i in range(26):
            matches += (1 if countA[i]==countB[i] else 0)
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index  = ord(s2[r]) - ord('a')
            countB[index]+=1
            if countB[index]==countA[index]:
                matches+=1
            elif countB[index]==countA[index]+1:
                matches-=1

            index  = ord(s2[l]) - ord('a')
            countB[index]-=1
            if countB[index]==countA[index]:
                matches+=1
            elif countB[index]+1==countA[index]:
                matches-=1
            l+=1
        return matches == 26

