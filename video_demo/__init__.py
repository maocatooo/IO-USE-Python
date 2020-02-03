

class testClose():

    def __init__(self):
        print("Q333")

    def close(self):
        print('Q666666')

    def __enter__(self):
        print("Q4444")

    def __exit__(self,*args,**kwargs):
        print('Q55555')
        self.close()
        pass

print("Q1")
with testClose() as t:
    print("Q22")
    pass
print("Q7777777")