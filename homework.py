from utils import NumbersConverter as Num 
# from_rhyme(rhyme_number) <- single method


def main():
    print(Num.__doc__)

    while True:

        data = str(input())

        if not data:    # Enter or CTRL+C to break
            break
        
        print(Num.from_rhyme(self=Num, num=data))


if __name__ == "__main__":
    main()