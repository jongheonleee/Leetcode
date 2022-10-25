class MyHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key: int, val: int) -> None:
        self.map[key] = val


    def get(self, key: int) -> int:
        if key in self.map:
            if self.map[key] != None:
                return self.map[key]
            
        return -1

    
    def remove(self, key: int) -> None:
        if key in self.map:
            self.map[key] = None
            del key
            return None

        
        
