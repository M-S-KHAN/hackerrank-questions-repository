## This is where the actual Solution resides!
def merge_the_tools(string, k):
    if k == 1:
        for i in range(len(string)):
            print(string[i])        
        return
    
    for i in range(k):
        substr = string[i*k:(i*k)+k]
        vals = ""
        for i in range(len(substr)):
            if substr[i] not in vals:
                vals += substr[i]
        print(vals)