from typing import Dict, Self


class NumbersConverter:

    """
    All functions of converting will work only by using string type of classic numbers
    """

    def __init__(self):
        pass
    
    @classmethod
    def __validation(cls, num: str) -> bool:
        symbols = {"I", "V", "X", "L", "C", "D", "M"}
        for symbol in num:
            if symbol not in symbols:
                return False
        return True

    def from_rhyme(self: Self, num: str) -> int:

        num = num.upper()
        rhyme_context: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 100
        }

        if not self.__validation(num=num):
            raise ValueError(f" {num} isn't a rhyme symbol!")
        else:
            result: int = 0
            for elem in range(len(num)):
                if elem < len(num) - 1 and rhyme_context[num[elem]] < rhyme_context[num[elem + 1]]:
                    result += -rhyme_context[num[elem]]
                else:
                    result += rhyme_context[num[elem]]
                
            return result

