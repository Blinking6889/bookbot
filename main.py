def wc(fc):
    wc = len(fc.split())
    return wc

def lc(fc):
    lc = []
    for i in fc.split():
        #lc[i] += 1
        lc.append(i)
    new_string = "".join(lc)
    count = 0
    for i in new_string:
        count += 1
    return(count)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(wc(file_contents))
        print(lc(file_contents))
        #print file_contents


if __name__ == "__main__":
    main()
