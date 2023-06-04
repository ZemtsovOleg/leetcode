class Solution():
    def fizzBuzz(self, n: int) -> list[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1, n+1):
            if (not i % 3) and (not i % 5):
                lst.append('FizzBuzz')
            elif not i % 3:
                lst.append('Fizz')
            elif not i % 5:
                lst.append('Buzz')
            else:
                lst.append(str(i))
        return lst


s = Solution()
print(s.fizzBuzz(15))
