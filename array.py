#hello world - this is an implementation of dynamic array.

class Array:
    
    def __init__(self, capacity):
    	self.array = []

    def print_array(self):
        print self.array

    def get_size(self):
    	return len(self.array)

    def is_empty(self):
        for i in range(len(self.array)):
            if self.array[i] is not None:
                return False
        return True

    # ACCESS #

    def get_at(self, index):
    	if len(self.array) > index:
    	    return self.array[index] # O(1) - indexing
	else:
	    return "This array does not have an index %s" % index
    
    def replace(self, item, index):
    	self.array[index] = item # O(1) - access and replace


    # INSERT #
    
    def insert(self, item, index):
        self.array.append(None) # O(N) - insert in the middle somewhere
        for i, e in reversed(list(enumerate(self.array))):
            if i == index-1:
                break
            self.array[i] = self.array[i-1]
        self.array[index] = item

    def push(self, item):
        self.array.append(item) # Amortized O(1) - insert at the tail                        

    def prepend(self, item):
    	self.insert(item, 0) # O(N) - insert at head

    # DELETE #

    def pop(self):
        return self.array.pop()    # O(1) - pop last item    
            
    def delete(self, index):
        self.array[index] = None
        for i in range(index+1, len(self.array)): # O(N) - delete at index
            self.array[i-1] = self.array[i]
        self.array.pop()

    def remove(self, item):
        index = self.find(item)
        self.delete(index) # O(N) - delete an item

    # LINEAR SEARCHING #

    def find(self, item):
        if item in self.array: # O(N) - searching
            return self.array.index(item)


    # RESIZING #

    def resize(self, new_cap):
        extend = new_cap - len(self.array)
        for i in range(1, extend+1):
            self.array.append(None)


