class str:
    def isValid(self, s: str) -> bool:
        
        list1 = []
        dic1 = { ')':'(', ']':'[', '}':'{' }
        
        for i in s :
            
            if i in dic1.values():
                list1.append(i)

            elif i in dic1.keys() and len(list1) != 0 :
                
                if dic1[i] != list1[-1] :
                    return False
                
                elif dic1[i] == list1[-1] :
                    list1.pop()
                
            else :
                return False
                
        return len(list1) == 0 

a = str()
print(a.isValid('()[]{}'))
