class arr(object):
    def singleNumber(self, nums):

        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

a = arr()
print(a.singleNumber([4,1,2,1,2]))
