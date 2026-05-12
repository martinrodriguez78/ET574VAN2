def hello():
    print("Hello, World!")
def helloNo(n): 
    for i in range(n-1):
        hello()
helloNo(4) 