def main():


    c = set(input())
    a = set(input())
    t = set(input())
    print(c & a | a & t | t & c)


if __name__ == "__main__":
    main()