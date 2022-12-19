class A:

    def _init_(self):
        print("this is init A")
    def method1(self):
        print("this is method A")
        

class B(A):
    def _init_(self):
        super()._init_()
        print("this is init B")
    def method2(self):
        print("this is method B")
# class C(B,A):
#     def method3(self):
#         print("this is method 3")

objB = B()
# objB = B()
# objC = C()