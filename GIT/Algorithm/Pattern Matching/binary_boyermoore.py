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

                    while (right + i + 1< len(string) and string [right + 1 + i] == string [right - index_now + i]):
                        z_array[index_now] += 1
                        i+= 1
                    left = index_now
                    right = index_now + z_array[index_now] - 1


            #case 1
            elif(string [index_now] == string [0]):
                # print("case iterate")
                z_array[index_now] += 1
                i = 1
                while( i+index_now < len(string) and string[index_now + i] == string[i]):
                        z_array[index_now] += 1
                        i+=1
                left = index_now
                right = index_now + z_array[index_now] -1
            
            # print("right: ", right)
            # print("left : ", left)
            # print(z_array)

            index_now +=1
        
        return z_array

def boyer_moore(pat, string):
    bc = bad_character(pat)
    gs = good_suffix(pat)
    mp = match_prefix(pat)
    # print(bc, "\n", gs, "\n", mp)

    outcome = []
    m = len(pat)
    index_now = 0
    
    while index_now  + m-1 < len(string):
        sbc = 0
        sgs = 0 

        # print(outcome)
        # print(index_now)
        
        #print("index now", index_now)

        for i in range(m-1, -1, -1):
            if string[index_now + i] != pat[i]:
                # print(i)
                
                sbc =  i - bc[int(string[index_now + i])][i]
                
                if gs[i + 1] == 0:
                    # print('mp')
                    sgs = m - mp[i+1]
                else:
                    # print("gs")
                    sgs = m - gs[i+1] - 1

                index_now += max(sbc, sgs)
                # print (sbc, sgs)
                break

        
        if(sbc == 0 and sgs == 0):
            outcome.append(index_now)
            index_now += 1
        
    return outcome

def match_prefix(pat):
    z_suf = z_algo(pat[::-1])[::-1]
    outcome = [0]
    for i in z_suf:
        outcome.append(max(i, outcome[-1]))
    outcome[-1] = len(pat)
    return outcome[::-1]

def bad_character(pat):
    outcome = ([],[])
    
    for i in range(len(pat)):
        outcome[1].append(-1)
        outcome[0].append(-1)


    for i in range(1,len(pat)):
        if int(pat[i-1]) == 0:
            outcome[0][i] = i-1
            outcome[1][i] = outcome[1][i-1]
        else:
            outcome[1][i] = i-1
            outcome[0][i] = outcome[0][i-1]


    
    if outcome[1][len(pat)-1] != len(pat)-1:
        outcome[1][len(pat)-1] = outcome[1][len(pat)-1]
    
    elif outcome[0][len(pat)-1] != len(pat)-1:
        outcome[0][len(pat)-1] = outcome[1][len(pat)-1]
    
    return outcome

def good_suffix(pat):
    gs = [0] * (len(pat)+1)
    z = z_algo(pat[::-1])[::-1]

    for i in range(len(pat)-1):
        if(z[i] >= 0):
            j = len(pat) - z[i] 
            gs[j] = i 

    return gs

def readFiles(tfn, pfn):
    txtFile = open(tfn, 'r')
    text = txtFile.read()
    txtFile.close()

    patFile = open(pfn, "r")
    pat = patFile.read()
    patFile.close()

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

    a = boyer_moore(pat , txt)
    print(len(a))
    writeFile(a,'output_binary_boyermoore.txt')

