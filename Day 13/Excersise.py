# write a python program to translate a msg into secret lang. Use the rules below

# coding :
# if the word contains atleast 3 chars, remove the first letter and append it at the end 
# now append 3 random chars at the starting and the end
# else:
# simply reverse the string

# decoding:
# if the word contains less than 3 chars, reverse it
# else:
# remove 3 random chars from start and end. Now remove the last letter and append it to the start

import random as r
import string

# our random function

def random_char():
    return ''.join(r.choices(string.ascii_letters, k = 3))


# Encoding

def encode(msg):
        words = msg.split()
        encoded_words = []

        for word in words:
            
            if len(word) >= 3:
                result = word[1:] + word[0]
            
                secret = random_char() + result + random_char()
                encoded_words.append(secret)

            else:
                encoded_words.append(word[::-1])
        return ' '.join(encoded_words)


# Decoding

def decode(msg):
        words = msg.split()
        decode_words = []
        for word in words:
            if len(word) < 3:
                decode_words.append(word[::-1]) 

            else:
                result = word[3:-3]

                if not result:
                    raise ValueError("Invalid encoded message!!")

                decoded = result[-1] + result[:-1]
                decode_words.append(decoded)
        return ' '.join(decode_words)




choice = input("\nWhat you wanted to do (Coding / Decoding)? :- ").strip()
ans = choice.capitalize()

if ans == 'Coding':

    # Coding

    msg = input("Enter your message :- ").strip()
    print("Encoded message is :-",encode(msg))


# decoding

elif ans == 'Decoding' :

    msg = input("Enter your secret message :- ").strip()
    try :
        print("Decoded message is :-",decode(msg))
    except ValueError as e:
        print(e)
         


