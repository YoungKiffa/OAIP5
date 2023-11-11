def main():


    sas = int(input())
    tsvet = [input() for i in range(sas)]
    vse = int(input())
    for i in range(vse):
        print(tsvet[i % sas])


if __name__ == "__main__":
    main()