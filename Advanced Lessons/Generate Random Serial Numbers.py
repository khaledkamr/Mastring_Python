# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# --------------------------------------------------------

import string
import random

def generateSerial(count):

    allChar = string.ascii_letters + string.digits
    charCount = len(allChar)
    serial = ""

    while count > 0:
        rand = random.randint(0, charCount-1)
        randomChar = allChar[rand]
        serial += randomChar
        count -= 1
    
    return serial

print(generateSerial(10))