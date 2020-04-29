class FirstUnique(object):
    '''
    Using dictionary to record the occurance of each element. Using list to 
    return the first unique element
    '''
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.list = nums
        self.map = {}
        
        for i in nums:
            self.map[i] = self.map.get(i,0) + 1

    def showFirstUnique(self):
        """
        :rtype: int
        """
        
        while(self.list != [] and self.map[self.list[0]] > 1):
            self.list.pop(0)
            
        if self.list == []:
            return -1
        
        return self.list[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        self.map[value] = self.map.get(value,0) + 1
            
        if self.map[value] == 1:
            self.list.append(value)

solution =  FirstUnique([2,3,5])
print(solution.showFirstUnique())
print(solution.add(5))
print(solution.showFirstUnique())
print(solution.add(2))
print(solution.showFirstUnique())
print(solution.add(3))
print(solution.showFirstUnique())