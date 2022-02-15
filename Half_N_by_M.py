# We are given two value that is N and M.  N is halved M-1 time and remaining is our output
class solution:
    def __init__(self):
        self.number = int(input("Enter the number "))
        self.M = int(input("Enter how many times "))

    def ans(self):
        while self.M > 1:
            self.number /= 2
            self.M -= 1

    def printoutput(self):
        print(int(self.number))


s1 = solution()
s1.ans()
s1.printoutput()
