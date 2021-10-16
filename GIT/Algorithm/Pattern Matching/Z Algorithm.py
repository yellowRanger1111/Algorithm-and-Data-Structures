#by Owen Austin 30039096
import sys

def z_algo (string):
    #array for z values
    z_array = [0]*len(string)

    #base case
    i = 0
    while i+1 < len(string) and string[i] == string[1 + i]:
            z_array[1] += 1
            i+=1

    try:
        for i in range(z_array[1]):
            z_array[2+i] = z_array[1+i] -1
    
    except IndexError:
        return z_array
    
    # aacababaca
    # z[1] = 1
    
    else :
        left = 0
        right = 0

        index_now = z_array[1] + 2 #we know 1 after basecase must be 0

        
        while index_now < len(string):
            #case 2
            
            if(index_now < right):
                #inside a z box
                #case where less than
                if(z_array[index_now - left] + index_now < right):
                    #print("case less than")
                    z_array[index_now] = z_array[index_now - left]
                elif (z_array[index_now - left] + index_now > right):
                    # print("case more than")
                    z_array[index_now] = right - index_now
                else :  #equal to
                    # print("case equal")
                    i = 0
                    z_array[index_now] = right - index_now

                    while (right + 1 + i < len(string) and string [right + 1 + i] == string [right - index_now + 1 + i]):
                        z_array[index_now] += 1
                        i+= 1
                    left = index_now
                    right = index_now + z_array[index_now] -1


            #case 1
            elif(string [index_now] == string [0]):
                # print("case iterate")
                z_array[index_now] += 1
                i = 1
                while( i+index_now < len(string) and string[index_now + i] == string[i]):
                        z_array[index_now] += 1
                        i+=1
                left = index_now
                right = index_now + z_array[index_now] - 1

            # aaabaaaacd
            #     4
            # 012345678
            
            # print("right: ", right)
            # print("left : ", left)
            # print(z_array)

            index_now +=1
        
        return z_array

def check_patter_matching (pat, string):
    allstr= pat+"$"+string
    newstr= ""

    # print("Changing Whole")

    for i in range(len(pat)+ len(string) + 1):
        if(ord(allstr[i]) in range(97,123)):
            newstr += "1"
        else:
            newstr += allstr[i]

    # print("start z", newstr)

    z = z_algo(newstr)

    # print("end z", z)

    outcome = []

    # print("change pat")
    pat_now = change(pat)


    # print("start checking")

    for i in range(len(z)):
        if(z[i] == len(pat_now)):

            # print(i, pat_now, allstr[i: i+len(pat_now)], change(allstr[i: i+len(pat_now)]))

            if(pat_now == change(allstr[i: i+len(pat_now)])):
                outcome.append(i - len(pat_now))
    
    # print ("end checking")

    return outcome

def change (pat):
    used = []
    num_now = 0
    pat_chg = ""


    #process pat
    for i in pat:
        if(ord(i) in range(97,123)):
            add = True
            for letters in range(len(used)):
                if used[letters] == i:
                    pat_chg += str(letters)
                    add = False
                    break
            
            if( add ):
                used.append(i)
                pat_chg += str(num_now)
                num_now += 1
        else:
            pat_chg += i
    
    return pat_chg

def readFiles(tfn, pfn):
    txtFile = open(tfn, 'r')
    text = txtFile.read()
    txtFile.close()

    patFile = open(pfn, "r")
    pat = patFile.read()
    patFile.close

    return text, pat

def writeFile (data, fn):
    file = open(fn, 'w+')
    for item in data:
        file.write(str(item))
        file.write("\n")
    file.close()
    


if __name__ == "__main__":
    txtFileName = sys.argv[1]
    patFileName = sys.argv[2]

    txt, pat = readFiles(txtFileName, patFileName)

    a = check_patter_matching(pat , txt)
    writeFile(a,'output_parameter_matching.txt')




