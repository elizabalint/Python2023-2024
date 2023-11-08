# 1. Write a Python class that simulates a Stack. The class should implement
# methods like push, pop, peek (the last two methods should return None if no 
# element is present in the stack).

class Stack:
        def __init__(self):
                self.stack = {}
                self.size = 0

        def push(self,elem):
                self.stack[self.size] = elem
                self.size += 1
        def pop(self):
                if self.size == 0:
                        return None
                self.size -= 1
                sterge = self.stack[self.size]
                del self.stack[self.size]
                return sterge

        def peek(self):
                if self.size == 0:
                        return None
                return self.stack[self.size -1]
        def afis(self):
            if self.size == 0: 
                print(None)
            else:
                for i in range(self.size - 1, -1, -1):
                    print(self.stack[i])
        
stiva = Stack()
stiva.push(3)
stiva.push(12)
stiva.push(5)
stiva.push(9)
stiva.push(10)
stiva.push(0)
stiva.push(45)
stiva.push(56)

print(stiva.peek())
print(stiva.pop())
print(stiva.peek())
stiva.afis()

# 2. Write a Python class that simulates a Queue. The class should implement 
# methods like push, pop, peek (the last two methods should return None if no 
# element is present in the queue).

class Queue:
    def __init__(self):
        self.queue = {}
        self.size = 0
        self.prim = 0

    def push(self, elem):
        self.queue[self.size] = elem
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        sterge = self.queue[self.prim]
        del self.queue[self.prim]
        self.prim += 1
        return sterge 

    def peek(self):
        if self.size == 0:
            return None
        return self.queue[self.prim]

    def afis(self):
        if self.size == 0: 
            print(None)
        else:
            for i in range(self.prim,self.size):
                print(self.queue[i])

coada = Queue()
coada.push(3)
coada.push(12)
coada.push(5)
coada.push(9)
coada.push(10)
coada.push(0)
coada.push(45)
coada.push(56)
print(coada.peek()) 
print(coada.pop()) 
print(coada.peek()) 
coada.afis() 

# 3. Write a Python class that simulates a matrix of size NxM, with N and M 
# provided at initialization. The class should provide methods to access 
# elements (get and set methods) and some methematical functions such as 
# transpose, matrix multiplication and a method that allows iterating through 
# all elements form a matrix an apply a transformation over them (via a lambda 
# function).

class Matrix:
    def __init__ (self, m, n):
        self.m = m
        self.n = n
        self.mat = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(0)
            self.mat.append(row)
    def get_elem(self, i, j):
        if 0 <= i <= self.m and 0<= j <= self.n:
            return self.mat[i][j]
        else: 
            raise ValueError("in afara matricei")
    def set(self, i, j, val):
        if 0 <= i <= self.n and 0 <= j <= self.m:
            self.mat[i][j] = val
        else:
            raise ValueError("in afara matricei")
    def transpusa(self):
        transpus = []
        for i in range(self.n):
            r = []
            for j in range(self.m):
                r.append(self.mat[j][i])
            transpus.append(r)
        return transpus
    
    def multip(self, mat2):
        if self.m != mat2.n:
            return None
        multiplicare = []
        for i in range(self.m):
            r = []
            for j in range(mat2.n):
                produs = 0
                for k in range(self.m):
                    produs += self.mat[i][k] * mat2.get_elem(k,j)
                r.append(produs)
            multiplicare.append(r)
        return multiplicare
    
    def transf(self, function):
        transf_lambda =  []
        for i in range(self.m):
            r = []
            for j in range(self.n):
                transf = function(self.mat[i][j])
                r.append(transf)
            transf_lambda.append(r)
        return transf_lambda
        
    def print_mat(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.mat[i][j], end=" ")
            print()
        
mat1 = Matrix(2, 3)
mat1.set(0, 0, 1)
mat1.set(0, 1, 2)
mat1.set(0, 2, 3)
mat1.set(1, 0, 4)
mat1.set(1, 1, 5)
mat1.set(1, 2, 6)

mat2 = Matrix(3, 2)
mat2.set(0, 0, 7)
mat2.set(0, 1, 8)
mat2.set(1, 0, 9)
mat2.set(1, 1, 10)
mat2.set(2, 0, 11)
mat2.set(2, 1, 12)

print("Mat1:")
mat1.print_mat()

print("Mat2:")
mat2.print_mat()

inmultire = mat1.multip(mat2)
print("Inmultire")
print(inmultire)

transpusa = mat1.transpusa()
print("Transpusa:")
print(transpusa)


transformare = mat1.transf(lambda x: x * 2)
print("Transformare")
print(transformare)
