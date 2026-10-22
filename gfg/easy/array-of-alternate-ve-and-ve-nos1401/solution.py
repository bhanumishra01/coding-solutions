class Solution:
    def rearrange(self, arr):
        positive = []
        negative = []

        for x in arr:
            if x >= 0:
                positive.append(x)
            else:
                negative.append(x)

        result = []
        i = 0
        j = 0

        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1

        result.extend(positive[i:])
        result.extend(negative[j:])

        arr[:]= result