

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
    print(dictionary)
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

dictionary = {' ':0,'P':1,'H':2,'Z':3,'G':4,'R':5,'A':6,'L':7,'T':8,'J':9,'B':10,'N':11,'D':12}

compressed = compress("PAPA GARLAND HAD A HAT AND A JAZZ BAND",dictionary)
print(compressed)

