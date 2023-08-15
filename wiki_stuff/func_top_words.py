import time

#takes a file name and an integer, returns nothing
#it returns nothing, to save on memeory usage it outputs everything into a text file, I didn't want to pass an object since that would get large fast
def top_words(myfile, top):

    start = time.time()
    file = open(myfile, 'r')
    out = open('func_top_words_out.txt', 'w')

    #count is a dictionary that has given words as keys and the amount of times that word has appeared as a value.
    count = {}

    for line in file:
        for word in line.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

    #This line sorts the dictionary by items in reverse, so basically the word with the highest number to the word with the lowest.
    sorted_list = sorted(count.items(), key=lambda x:x[1], reverse=True)

    #top will limit the list to only the top X words. I was intending to get the top 10,000 words, and then find the related words of just those. 
    for i in sorted_list[:top]:
        out.write(str(i[0]))
        out.write("\n")

    end = time.time() - start
    print("Finished getting top words after: ")
    print(end)
    ender = "\n Ended after " + end + " seconds."
    out.write(ender)
    file.close()
    out.close()
