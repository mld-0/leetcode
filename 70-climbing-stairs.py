import functools

#   On the use of a memorization wrapper on a class method (see below)
#   LINK: https://stackoverflow.com/questions/51138226/how-to-apply-a-memorize-decorator-to-an-instance-method
def memorize_wraper(f):
    cache = {}
    @functools.wraps(f)
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

class Solution:

    memorize = { 0: 0, 1: 1, 2: 2, }

    def climbStairs(self, n: int) -> int:
        #return self.climbStairs_Recursive(n)
        #return self.climbStairs_RecursiveMemorize(n)
        return self.climbStairs_RecursiveDecorator(n)
        #return self.climbStairs_Dynamic(n)


    #   runtime: TLE
    def climbStairs_Recursive(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_Recursive(n-1) + self.climbStairs_Recursive(n-2)

    #   runtime: beats 95%
    def climbStairs_RecursiveMemorize(self, n: int) -> int:
        if n in self.memorize:
            return self.memorize[n]
        result = self.climbStairs_RecursiveMemorize(n-1) + self.climbStairs_RecursiveMemorize(n-2)
        self.memorize[n] = result
        return result

    #   runtime: beats 83%
    @memorize_wraper
    def climbStairs_RecursiveDecorator(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_RecursiveDecorator(n-1) + self.climbStairs_RecursiveDecorator(n-2)

    #   runtime: beats 99%
    @functools.lru_cache()
    def climbStairs_RecursiveLRUCache(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_RecursiveLRUCache(n-1) + self.climbStairs_RecursiveLRUCache(n-2)

    #   runtime: beats 83%
    def climbStairs_Dynamic(self, n: int) -> int:
        if n < 3:
            return n
        results = [ 1, 2, ]
        for i in range(2, n):
            results.append( results[i-1] + results [i-2] )
        return results[-1]



s = Solution()

input_values = [ 2, 3, 44, ]
input_checks = [ 2, 3, 1134903170, ]

for n, check in zip(input_values, input_checks):
    result = s.climbStairs(n)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

