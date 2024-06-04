#word count
def wc(fc):
    wc = len(fc.split())
    return wc

#letter count
def lc(fc):
    lc = []
    for i in fc.split():
        lc.append(i)
    new_string = "".join(lc)
    return(len(new_string))

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(wc(file_contents))
        print(lc(file_contents))
        #print file_contents

if __name__ == "__main__":
    main()
