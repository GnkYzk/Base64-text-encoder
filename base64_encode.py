# get string's letters 1 by 1
# turn them into binary
# get binary codes next to each other into one string(extend with 0's from right
# if not divisible by 6)
# split that binary code 6 by 6
# get those 6 char strings' value
# assign according base64 characters 
#  extend with ='s if the encoded text is not divisible by 3
# return

char64= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def dectobin(n):
    binary = bin(ord(n))
    return "0" +binary[2:]# 2: removes the 0x start of the binary representation

def bintodec(n):
    return char64[int(n,2)]

def main(s):
    binnum= map(dectobin,s)
    x = "".join(binnum)
    
    y = len(x)%6
    if y !=0:
        for i in range(6-y):
            x += "0" 
    
    nlist=[]
    index=0
    for j in range(0,int(len(x)/6)):
        nlist.append(x[index:index+6])
        index += 6 #splists the binary string 6 by 6
    
    result = map(bintodec,nlist)
    b64= "".join(result)
    
    if len(b64)%3 != 0:
        for i in range (3-len(b64)%3):
            b64 += "=" 
            
    return b64


yourtext = input("Enter your text: ")
main(yourtext)


    


    