class MyNumbers:
    def __iter__(self):
        self.a = 753414
        return self
    
    def __next__(self):
        if self.a <= 99999999:
            x = self.a
            self.a = round(((((self.a * 3) / 2) + 1) * 1.1)/1.5)
            return x
        else:
            raise StopIteration

myclass = MyNumbers()

for item in myclass:
    print(item)