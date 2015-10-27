import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class ImageDithering:
    def count(self, dithered, screen):
        allpixels=''.join(screen)
        c=0
        for i in allpixels:
        	if i in dithered:
        		c+=1
        
        return c

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\"") + str(",") + str("{"))
	for i in range(len(p1)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str("\"") + str(p1[i]) + str("\""))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = ImageDithering()
	startTime = time.clock()
	answer = obj.count(p0, p1)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p2))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p2
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True
tests_disabled = False


# ----- test 0 -----
disabled = False
p0 = "BW"
p1 = ("AAAAAAAA","ABWBWBWA","AWBWBWBA","ABWBWBWA","AWBWBWBA","AAAAAAAA")
p2 = 24
all_right = (disabled or KawigiEdit_RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = "BW"
p1 = ("BBBBBBBB","BBWBWBWB","BWBWBWBB","BBWBWBWB","BWBWBWBB","BBBBBBBB")
p2 = 48
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = "ACEGIKMOQSUWY"
p1 = ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX","ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX","ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX","ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX","ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX","ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX")
p2 = 150
all_right = (disabled or KawigiEdit_RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = "CA"
p1 = ("BBBBBBB","BBBBBBB","BBBBBBB")
p2 = 0
all_right = (disabled or KawigiEdit_RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = "DCBA"
p1 = ("ACBD",)
p2 = 4
all_right = (disabled or KawigiEdit_RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

if (all_right):
	if (tests_disabled):
		print(str("You're a stud (but some test cases were disabled)!"))
	else:
		print(str("You're a stud (at least on given cases)!"))
	
else:
	print(str("Some of the test cases had errors."))

# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!