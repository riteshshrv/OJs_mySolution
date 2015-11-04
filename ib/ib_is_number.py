class Solution:
    # @param s, a string
    # @return, a boolean
    def isNumberWithoutE(self, s, decimalAllow = True):
        ''' Check whether s is a number not in scientific notation
        '''
        digits = "1234567890"
        
        sLen = len(s)
        if sLen == 0:               return False
        
        if s[0] == "+" or s[0] == "-":
            # Skip the sign
            s = s[1:]; sLen -= 1
            if sLen == 0:           return False
 
        
        if "." in s:
            if sLen == 1 or not decimalAllow:   return False
            
            decimalPoint = s.index(".")
            if (len(s[decimalPoint+1:])==0):
                return False
            for item in s[:decimalPoint] + s[decimalPoint+1:]:
                if not item in digits:          return False
            else:
                # All elements are digits (except one decimal point)
                return True
        else:
            for item in s:
                if not item in digits:          return False
            else:
                # All elements are digits
                return True
 
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        ''' Check whether s is a valid number.
        '''
        s = s.strip(" ")    # Remove the leading and tailing spaces
        
        if "e" in s:
            # Might be a number in scientific notation.
            divPos = s.index("e")
            return self.isNumberWithoutE(s[:divPos]) and \
                   self.isNumberWithoutE(s[divPos+1:], False)
        elif "E" in s:
            # Might be a number in scientific notation
            divPos = s.index("E")
            return self.isNumberWithoutE(s[:divPos]) and \
                   self.isNumberWithoutE(s[divPos+1:], False)
        else:
            # Might be a number not in scientific notation
            return self.isNumberWithoutE(s)

def main():
    m=Solution()
    print(m.isNumber(input()))

if __name__ == '__main__':
    main()