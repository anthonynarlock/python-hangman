#Author: Spencer Ekstrom
def main():
    #import the file into a list
    f = open("all.txt", "r")
    l = list()
    for lines in f:
        l.append(f.readline())
    f.close()
    print("yes")
    #list of nono characters
    bad = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '?', '-', '_', '*', '.', '&', '\'', '/', '\\']

    #now all your words are in a file, filter them
    filtered = list()
    print("yes1")
    for word in l:
        flag = False
        for char in bad:
                if char in word:
                    flag = True
        
        if flag == False:
            filtered.append(word)

    #write all the filtered to a file
    filteredfile = open("filtered.txt", "x")
    for word in filtered:
        filteredfile.write(word)
    filteredfile.close()

if __name__ == "__main__":
    main()