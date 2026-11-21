class Solution(object):
    def defangIPaddr(self, address):
        result=[]
        for i in range(len(address)):
            if address[i].isdigit():
                result+=address[i]
            elif address[i] == ".":
                result.append("[.]")
        return "".join(result)
        