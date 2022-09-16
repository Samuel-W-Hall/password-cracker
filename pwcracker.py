# Samuel Hall, Georgia Radu #


# Import #
import hashlib


# Use this to get a hash of password #
k = input("This is optional and will put the password you enter through the SHA-1 hash function.\nEnter password: ")
khash = hashlib.sha1(bytes(k, "utf-8")).hexdigest()
print("\nThe hash for", k, " is:", khash)



# All 2 digit numbers #
digit2 = []    
for dig in range(0, 10):
    for dig2 in range(0,10):
        num = "".join((str(dig), str(dig2)))
        digit2.append(num)

foundhash = False

# Password Input #            
pwhash = input("\n\nPlease enter the hash of the password you wish to crack: ")
print("\nNow checking for all dictionary related passwords...")



# Code for all dictionary related passwords #
with open("dictionary.txt", mode = "r", newline = "\r\n") as f:

    for line in f:
        # Initial values #
        word = line.replace("\r","")
        word = word.replace("\n","")
        poss_words = [word]
        poss_word_var = [word]
        word_prefix = []
        word_suffix = []


        # 2-digit Prefix and Suffix #
        for d in range(0, len(digit2)):
            prefix = "".join((digit2[d], word))
            suffix = "".join((word, digit2[d]))
            word_prefix.append(prefix)
            word_suffix.append(suffix)
                       
        

        # Creates list of all possible variations using specified substitution #
        def variations(word_list, letter, sub):

            for k in range(0, len(word)):
                if (word[k] == letter):
                    index = k        
                    for t in range(0, len(word_list)):
                        new_word = "".join((word_list[t][:index], sub, word_list[t][index+1:]))
                        word_list.append(new_word)


        
        variations(poss_word_var, "i", "1")
        variations(poss_word_var, "o", "0")
        variations(poss_word_var, "a", "@")
        variations(poss_word_var, "s", "5")


        # Compiles all words which we need to check the hashes of #
        def combine(word_list, start):
            for r in range(start, len(word_list)):
                poss_words.append(word_list[r])


        combine(poss_word_var, 1)
        combine(word_prefix, 0)
        combine(word_suffix, 0)

    
        # Check hashes of all possible words and print password #
        for p in range(0, len(poss_words)):
            all_hash = hashlib.sha1(bytes(poss_words[p], "utf-8")).hexdigest()
            if (all_hash == pwhash):
                print("\nThe password is:", poss_words[p])
                input()
                foundhash = True
            


if foundhash == True:
    pass
else:
    print("\nNo hash was found relating to the english dictionary.\n\nNow checking all passwords of 6 lowercase letters from the english alphabet. \n\nThis may take a while...")
    # Any password of 6 letters from lowercase english alphabet #
    passwords = []
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for u in range(0, 26):
        for v in range(0, 26):
            for w in range(0, 26):
                for x in range(0, 26):
                    for y in range(0, 26):
                        for z in range(0, 26):
                            pw = "".join((alphabet[u], alphabet[v], alphabet[w], alphabet[x], alphabet[y], alphabet[z]))
                            if (hashlib.sha1(bytes(pw, "utf-8")).hexdigest() == pwhash):
                                print("\nThe password is:", pw)
                                input()
                                foundhash = True

if foundhash == True:
    pass
else:
    print("\nThere is no password from the english dictionary, \neither with or without a 2 digit prefix,\nor with any of the following variations: \n\"i\" to \"1\", \n\"o\" to \"0\", \n\"a\" to \"@\", \n\"s\" to \"5\", \nwhich has the hash: ", pwhash)
    input()
    
                            
            
            
