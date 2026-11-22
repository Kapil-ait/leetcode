class Solution(object):
    def checkString(self, s):
        flag = False
        for i in s:
            if i == 'b':
                flag = True
            elif i == 'a' and flag == True:
                return False

        return True