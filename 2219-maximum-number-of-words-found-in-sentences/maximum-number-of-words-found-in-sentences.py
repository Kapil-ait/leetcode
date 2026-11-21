class Solution(object):
    def mostWordsFound(self, sentences):
        max_count = 0

        for i in sentences:
            count = 0
            for j in i:
                if j == " ":
                    count += 1
            if count + 1 > max_count:
                max_count = count + 1
        return max_count