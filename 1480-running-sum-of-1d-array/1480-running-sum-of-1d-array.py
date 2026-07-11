class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running = 0
        answer = []

        for num in nums:
            running += num
            answer.append(running)

        return answer