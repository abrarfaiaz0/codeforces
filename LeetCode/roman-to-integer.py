class Solution:
    def romanToInt(self, s: str) -> int:
        rtoi={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
        roman = input()
        val = rtoi[roman[len(roman)-1]]
        integer = rtoi[roman[len(roman)-1]]
        for i in reversed(range(len(roman)-1)):
            integer  
            if int(rtoi[roman[i]]) >= val:
                integer += int(rtoi[roman[i]])
                val = int(rtoi[roman[i]])
            else:
                integer -= int(rtoi[roman[i]])
                val = int(rtoi[roman[i]])
        return integer