class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.loadFactor = self.loadCalc()
    
    
    
    #Calculates the load factor on the hash table
    def loadCalc(self):
        count = 0
        loadFactor = 0
        sizeofTable = len(self.slots)
        for index in range(sizeofTable):
            if self.slots[index] == None:
                count +=1
        numberOfItems = sizeofTable - count
        loadFactor = numberOfItems / sizeofTable
        return loadFactor
    #
    def resize(self):
        self.size = self.nextprime(self.size)
        count = 0  
        slots = []
        data = []
   
        while(count < len(self.slots)):
            if(self.slots[count] != None):
                slots.append(self.slots[count])
                data.append(self.data[count])
            count+=1
        self.slots = [None] * self.size
        self.data = [None] * self.size
        count = 0
   
        while(count < len(slots)):
            self.put(slots[count], data[count])
            count+=1       
   
    
    #Generates the next prime number 
    def nextprime(self, x):
        newX = x+1
        found = False
        if newX == 1:
            return 1
        elif newX == 0:
            return 0
        else:
            while not found:
                if newX % 1 == 0 and newX%newX == 0 and newX % 2 != 0 and newX % 3 != 0:
                    found == True
                    return newX
                newX = newX+1    
   
   
    
    def put(self,key,data):
    
        loadFactor = self.loadCalc()
        
        if loadFactor > 0.90:
            self.resize()
      
        hashvalue = self.hashfunction(key,len(self.slots))
      
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
    
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data 
        
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
    
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)    
        
    
        
            
        

H = HashTable()
H.put(54,"cat")
H.put(26,"dog")
H.put(22,"c at")
H.put(34,"ca t")
H.put(46,"dog ")
H.put(52,"c a t")
H.put(64,"ca  t")
H.put(86,"d o g  ")
H.put(62,"c a t  ")
H.put(14,"ca 2t")
H.put(116,"d o1g  ")
H.put(117,"do1g  ")   
H.put(44,"goat")
H.put(55,"pig")
H.put(20,"chicken")
H.put(42,"goat")
H.put(51,"pig")
H.put(24,"chicken")
print(H.slots)
print(H.data)

print(H.get(-21))
