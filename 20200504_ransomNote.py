class Solution(object):
    '''
    This function use dictionary to find whether the letter in the megazines
    can construct the letter in ransomNote. The idea is to count the letter
    count in magazines and subtract if the same letter appear in ransomNote.
    If the number is less than 0 or the letter is not appear in magazine, then
    return False, otherwise return True
    '''
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magazineLetterDict = {}
        
        for i in magazine:
            if i != ' ':
                magazineLetterDict[i] = magazineLetterDict.get(i, 0) + 1
                
        for i in ransomNote:
            if i != ' ':
                if i in magazineLetterDict.keys():
                    magazineLetterDict[i] -= 1
                    if magazineLetterDict[i] < 0:
                        return False
                else:
                    return False
                
        return True

ransomNote = 'aa'
magazine = 'aab'

solution = Solution()
print(solution.canConstruct(ransomNote, magazine))