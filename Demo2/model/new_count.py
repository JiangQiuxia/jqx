from model.count import A

class B(A):
    def sub(self,a,b):
        return a-b

if __name__ == '__main__':
 result = B().add(2,5)
 print(result)