class Solution:
    def fizzBuzz(self, n):
        return [(("Fizz"*(i%3<1)+"Buzz"*(i%5<1)) or str(i)) for i in range(1,n+1)]