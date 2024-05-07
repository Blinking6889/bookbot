def wc(fc):
    wc = len(fc.split())
    return wc

def lc(fc):
    lc = {}
    new_string = " ".jo
    for i in fc.split():
        lc[i] += 1
    print(lc)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(wc(file_contents))
        print(lc(file_contents))


if __name__ == "__main__":
    main()