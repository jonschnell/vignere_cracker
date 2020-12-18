'''
@author: Jonathon Schnell

@date: 8/25/2020

@version: 1.0

'''

#key: magic

#plaintext: mr and mr sdursley of number four privet drive were proud to
#say that they were perfectly normal thank you very much they were the last 
#people youd expect to be involved in anything strange or mysterious because
#they just didnt hold with such nonsense mr dursley was the director of a 
#firm called grunning swhichmadedrill she was a big beefy man with hardly any 
#neck although he did have a very large mustache mrs dursley was thin and blonde
#and had nearly twice the usual amount of neck which came in very useful as she
#spent so much of her time craning over garden fences spying on the neighbors
#the dursley shada small son called dudley and in their opinion there was no finer
#boy anywhere the dursleys had everything they wanted but they also had a secret and the irgreatest 
#fear was that somebody would discover it they didnt think they could bear it if anyone
#found out about the pottersmrspotter was mrs dursleys sister but they hadnt met for several years in fact
#mrs dursley pretended she didnt have a sister because her sister and her good for nothing husband were
#a sundursley is has it was possible to be



import array
import numpy
import collections


if __name__ == "__main__":
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    cipher = "yrgvfyrylwdsrmaaftconexnqgrvzkhezltuvkegdevzqgdzwumyzpcftnmaiexmrqrlmeflevqdmgtvtatsaaubmtkmakjfhkgyqrkbjqlgavbeuxnqyucfqxvmeftujgunbwnhejqpmnebjunmavdatogarsgufexqqgshmemuymvteerwetjqfztnwnpwobjeuippanympeeszfgrytgkwgavtejqtqczwtafgnkdmiinxejotgntqpsscpkohsifqdxqnxsnmymsgjksbkmhkmgvyutnpcddrgczytmewarbjaumpjqdoljmvkixqretcdgkuwetgkjqmxafgrytgkwgavtitippbrwppegvftajvgmrrgviiimvteaawmlguqgnzwhzeisytiipemmkqphexgweelcnmsypgepkvveoscetolpgdtougorgvkzgudgdggzfqnlmpoeyarkitoqztnmpqimpdarybjqdazuxeeajmdgaomlraqzcgtnqdjcfxeeippitbjqixwrunowpfhkzgiayvqritmtnoeipkwnmtqtnmfgrytgksnifqvkzafhovifhkgymnzmfnuzbjqygtuahglceeizgfatlvteozidegbgetlmcdwgavtazaqyehwfkwucnpdoaeavkzkftnmapijvvfhovmfhkgeaurldqaxqvufgvaanknqgnjwwfahwwftnmratzmtemxaratzmtiayutedazuxeeauuszmtnuzbjqynifztsmvroxaghexinkegzuunliefmxafgrytgkpxmvqnjmfehklkpnzpchegaketkzdqcgcuqhkzuuszmtmnjpgdguwfroxvqfhovituyjczdcmtqaycppuxanqyoajmsobymsvwueihtgfohm"    

    
    def decrypt(ciphertext, key):
        plaintext = ""
        #how many times to multiply the key to prevent writing a complicated nested loop
        multi = len(ciphertext)/len(key)
        key *= multi+1
        
        i = 0
        while i < len(ciphertext):
            #temp is the number representation of the plaintext letter
            temp = alphabet.index(ciphertext[i:i+1]) - alphabet.index(key[i:i+1])
            #look up temp in the alphabet to get a key
            # % 26 not technically needed but good pratice
            plaintext += alphabet[temp % 26]
            i += 1
        
        return plaintext
    
    #this functions in reverse of the function above
    # % 26 is imporntant because it is possible to go over 26
    def encrypt(plaintext, key):
        ciphertext = ""
        multi = len(plaintext)/len(key)
        
        key *= multi+1
        
        i = 0
        while i < len(plaintext):
                
            temp = alphabet.index(plaintext[i:i+1]) + alphabet.index(key[i:i+1])
            ciphertext += alphabet[temp % 26]
            i += 1
        
        return ciphertext
    
    #returns a best guess for the key
    def crack(ciphertext):
        #two strings to compare to find repeats
        substring1 = ""
        substring2 = ""
        key = ""
        #array of actual distances between matching strings
        arr1 = array.array('i', [1])
        #array of possable key lengths
        arr2 = array.array('i', [1])
        #keys of length 1 do not matter
        a = 2
        #the longest match is 11 in this case
        #instead of leaving this on 1/2 cipher length i changed to longest key to decrease runtime
        while a < 12:
            #start index of first substring
            i = 0
            #start index of the second substring
            j = a - 1
            while i < len(cipher):
                substring1 = cipher[i:i+a]
                #print (substring1)
                while j < len(cipher):
                    #construct substring
                    substring2 = cipher[j:j+a]
                    if substring1 == substring2:
                        #if they have a match print the substring and the distance between matches
                        
                        arr1.append(j-i)                  
                    j += 1
                #when i incriments set j to i + the length of the match we are looking for because a match wont matter between 0 and a
                j = i+a
                i += 1
            a += 1
        
    
        #divide all the key lengths by 2->the number itself of key
        d = 0
        while d < len(arr1):
            for c in range(2, arr1[d] + 1):
                if arr1[d] % c == 0:
                    #store in a new array
                    arr2.append(c)
            
            d += 1
        
        #convert to numpy array
        arr3 = numpy.array(arr2)
        keylength = numpy.bincount(arr3).argmax()
        
        print("array of distances between all matched strings")
        print(arr1)
        print("array of divisors of all possible distances")
        print(arr2)
        #print(reduce(gcd, arr1))
        print("finding the distance with the most occorances from array 2 will give us a key length")
        #print the key length possability that ocours most
        print('key length:',keylength)
        #populate each substring with the first letter
        everynth1 = cipher[0:1]
        everynth2 = cipher[1:2]
        everynth3 = cipher[2:3]
        everynth4 = cipher[3:4]
        everynth5 = cipher[4:5]
        #split the ciphertext into 5 substrings because the key is 5 characters long and populate the substrings
        i = keylength
        while i < len(cipher):
            everynth1 += cipher[i:i+1]
            everynth2 += cipher[i+1:i+2]
            everynth3 += cipher[i+2:i+3]
            everynth4 += cipher[i+3:i+4]
            everynth5 += cipher[i+4:i+5]
            i+=keylength
        
        print("below are the 5 substrings and their most frequent letter")
        print (everynth1)
        print(collections.Counter(everynth1).most_common(1)[0])
        
        print (everynth2)
        print(collections.Counter(everynth2).most_common(1)[0])
        
        print (everynth3)
        print(collections.Counter(everynth3).most_common(1)[0])
        
        print (everynth4)
        print(collections.Counter(everynth4).most_common(1)[0])
        
        print (everynth5)
        print(collections.Counter(everynth5).most_common(1)[0])
        
        #preform a reverse shift of the most common letters to e
        shift1 = alphabet.index('q') - alphabet.index('e') % 26
        key += alphabet[shift1]
        
        shift2 = alphabet.index('e') - alphabet.index('e') % 26
        key += alphabet[shift2]
        
        shift3 = alphabet.index('g') - alphabet.index('e') % 26
        key += alphabet[shift3]
        
        shift4 = alphabet.index('m') - alphabet.index('e') % 26
        key += alphabet[shift4]
        
        shift1 = alphabet.index('g') - alphabet.index('e') % 26
        key += alphabet[shift1]
        
        print("the algorithims best guess for the key:")
        return key

    
    ###################################################################
    finalkey = "magic"
    
    print(crack(cipher))
    print("the key is probably MAGIC")
    print("plaintext:")
    print(decrypt(cipher, finalkey))
    
    print("re-encrypt and compare to the cipher text as a sanity check")
    foo = "mrandmrsdursleyofnumberfourprivetdrivewereproudtosaythattheywereperfectlynormalthankyouverymuchtheywerethelastpeopleyoudexpecttobeinvolvedinanythingstrangeormysteriousbecausetheyjustdidntholdwithsuchnonsensemrdursleywasthedirectorofafirmcalledgrunningswhichmadedrillshewasabigbeefymanwithhardlyanyneckalthoughhedidhaveaverylargemustachemrsdursleywasthinandblondeandhadnearlytwicetheusualamountofneckwhichcameinveryusefulasshespentsomuchofhertimecraningovergardenfencesspyingontheneighborsthedursleyshadasmallsoncalleddudleyandintheiropiniontherewasnofinerboyanywherethedursleyshadeverythingtheywantedbuttheyalsohadasecretandtheirgreatestfearwasthatsomebodywoulddiscoverittheydidntthinktheycouldbearitifanyonefoundoutaboutthepottersmrspotterwasmrsdursleyssisterbuttheyhadntmetforseveralyearsinfactmrsdursleypretendedshedidnthaveasisterbecausehersisterandhergoodfornothinghusbandwereasundursleyishasitwaspossibletobe"
    bar = "magic"
    print(encrypt(foo, bar))
    if encrypt(foo, bar) == cipher:
        print("sanity check passed :)")
    else:
        print("ciphertext does not match :(")
            