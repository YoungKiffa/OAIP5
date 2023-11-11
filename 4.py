def main():


    sas = []
    while True:
        sys = int(input())
        if sys == 0:
            break
        sas.append(sys)
    fyf = [sys for sys in sas if sys % len(sas) == 0]
    print(fyf)


if __name__ == "__main__":
    main()