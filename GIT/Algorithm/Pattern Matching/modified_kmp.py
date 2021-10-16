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

                    while (right + i + 1  < len(string) and string [right + 1 + i] == string [right - index_now + i]):
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

def get_sp(pat):
    z = z_algo(pat)
    z[0] = len(pat) -1

    print(z)

    m = len(pat)
    out = []
    for i in range(m):
        out.append(0)
    

    for j in range(m-1, 0, -1):
        i = j + z[j] - 1
        out[i] = z[j]
    
    return out

def kmp (pat, string):
    sp = get_sp(pat)

    output = []
    m = len(pat)
    # print("m:", m)
    index_now = 0

    while index_now + m-1 < len(string):
        shift = 0
        print("index :", index_now)
        #check from left to right
        for i in range(0,m):
            if string[index_now + i] != pat[i]:
                
                shift = max(i-1 - sp[i-1], 1)
                print(i)
                print (shift)
                index_now+= shift
                break
        
        if(shift == 0):
            output.append(index_now)
            index_now += 1
    
    return output

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

    a = kmp(pat , txt)
    writeFile(a,'output_kmp.txt')