#word count
def wc(fc):
    wc = len(fc.split())
    return wc

#letter count
def lc(fc):
    wl = []
    letter_dict = {}
    for i in fc.split():
        wl.append(i.lower())
    new_string = " ".join(wl)
    for i in new_string:
        #print(i)
        if i not in letter_dict:
            if i.isalpha():
                letter_dict[i] = 1
        if i in letter_dict:
            letter_dict[i] += 1
    return(letter_dict)


    
    #print(new_string)
    #unique_list = set(lc)
    
    #for i in unique_list:

    # return(len(new_string))
    #return(unique_list)

# def gen_report(wordcount, lettercount):
#     char_array = []
#     for i in lettercount:
#         char_array.append[i]
#     sorted_array = char_array.sort()
#     print(sorted_array)



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # lettercount = lc(file_contents)
        # wordcount = wc(file_contents)
        # print(gen_report(wordcount, lettercount))
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f'{wc(file_contents)} words found in the document.')
        lc_dict = lc(file_contents)
        sorted_dict = dict(sorted(lc_dict.items()))
        for i in sorted_dict:
            print(f'''The {i} character was found {lc_dict[i]} times''')
        print("--- End report ---")
        #print(lc(file_contents))

if __name__ == "__main__":
    main()
