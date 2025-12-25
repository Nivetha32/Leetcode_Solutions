class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ye, mo, d = date.split('-')
        return f"{bin(int(ye))[2:]}-{bin(int(mo))[2:]}-{bin(int(d))[2:]}"

