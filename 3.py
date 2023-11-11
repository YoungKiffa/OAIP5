def main():


    xax = input()
    cac = set('0123456789')
    cyc = set(xax)
    e = cac - cyc
    print(e)


if __name__ == "__main__":
    main()