import time

def top_words(myfile):

    start = time.time()
    file = open(myfile, 'r')
    out = open('func_top_words_out.txt', 'w')

    count = {}

    for line in file:
        for word in line.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

    sorted_list = sorted(count.items(), key=lambda x:x[1], reverse=True)

    for i in sorted_list[:10000]:
        out.write(str(i[0]))
        out.write("\n")

    end = time.time() - start
    print("Finished getting top words after: ")
    print(end)
    ender = "\n Ended after " + end + " seconds."
    out.write(ender)
    file.close()
    out.close()
