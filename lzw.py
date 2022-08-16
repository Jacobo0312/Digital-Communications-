

def compress(uncompressed,dictionary):

    """Compress a string to a list of output symbols."""
 
    dict_size = len(dictionary)


    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed,dictionary):
    """Decompress a list of output ks to a string."""
 
    dict_size = len(dictionary)
    dictionary = {v: k for k, v in dictionary.items()}


    result = ""
    w = dictionary[compressed.pop(0)]
    
    result+=w
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result+=entry
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result
 
 


# How to use:

dictionary = {'B':0,'N':1}

input=[0, 2, 3, 1, 3, 0, 5, 4, 1, 8, 6]

decompressed = decompress(input,dictionary)

decompress=list(decompressed)

# Convert output to message format Matrix 5 x 5

count=0
message=""
for i in decompress:
    if i=='B':
        x=" BLANCO "
    else:
        x=" NEGRO  "
    if (count==4):
        count=0
        
        message+=x+"\n"
    else:
        count+=1
        message+=x


print(message)