import random
import math
import sys

def gen_prime (n):
    start = 2 ** (n -1)
    stop = (2 ** n) -1

    iter = stop-start
    k = int(math.log(n, 2))
    # print (k)

    while iter > 0:
        x = random.randrange(start, stop)
        if miller_rabin(x, k) == ("Probably Prime" or "Prime"):
            return x
        else:
            iter -= 1
    
    raise Exception("No Prime Found")
    # print (start)
    # print (stop)
    # print (x)
    # print (to_binary(x))
    


def to_binary(x: int):
    '''
    @return binary form of x
    '''
    return int(bin(x)[2:])

def miller_rabin (n, k):
    '''
    n is the number we are checking
    k is the number of test should be done

    @return : string -> Composite or Prime or Probably Prime
    @complexity : O(k + log(n))
    '''

    if n <= 2:
        #we know 2, 1 (arguably) is prime and neg just dont work
        return "Prime"
    elif n % 2 == 0:
        #if even we know it is not prime
        return "Composite"
    
    #changing n-1 = 2^s . t
    s = 0
    t = n -1
    while t % 2 == 0:
        s += 1
        t /= 2
    
    #make sure it is and int sos easier to read XD
    t = int(t)
    
    # print("s:",s, "t:", to_binary(t))

    #test primality k times
    for _ in range(k):
        #pick a witness
        a = random.randrange(2, n)
        # print(a)

        # creating list using repeated squaring
        rep_sq = []
        #append the first iteration
        rep_sq.append((a**t) % n)
        for i in range(1, s + 1):
            # repeated squaring 
            rep_sq.append((rep_sq[-1]**2) % n)

        #checking
        if (rep_sq [-1] != 1):
            # a ^ n-1 mod n not equal 1
            return "Composite"
        else:
            #try finding if -1 and 1 consequently
            i = 1
            done = False
            while not done and i <= s + 1:
                if rep_sq[-i] != 1:
                    done = True
                    if rep_sq[-i] != n -1:
                        return "Composite"
                else:
                    i += 1
    return "Probably Prime"


def write_file(filename, string):
    filen = open(filename, "w")
    filen.write(string)
    filen.close()


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(gen_prime(n))


# print(miller_rabin (561, 6))
# print(15 ** 28 % 29)