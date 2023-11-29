def hammingWeight(n):
    # Convert to number to avoid working with strings
        if not isinstance(n, (bytes, bytearray)):
            # If string, convert directly without needing to convert from bin to dec
            if type(n) == str:
                n = int(n)
            # If int convert to binary
            else:
                n = bin(int(n))[2:]
                n = int(n)
                
        oneCount = 0
        for i in range(32):
            if n%10 == 1:
                oneCount+=1
            n //= 10
        return oneCount
        
print(hammingWeight('01100000101000'))
