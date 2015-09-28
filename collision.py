from crc_algorithms import Crc
import random
import string
import time
import datetime

def main():
    string1 = ''
    string2 = "c651ceb5fa05b4195f993513d8bb5381"
    crc = Crc(width = 16, poly = 0x8005,
              reflect_in = True, xor_in = 0x0000,
              reflect_out = True, xor_out = 0x0000)
    crc1 = 'a'
    crc2 = crc.table_driven(string2)
    print datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') 
    while crc1 != crc2: 
        string1 = ''.join(random.SystemRandom().choice(string.ascii_letters + \
         string.digits) for _ in range(32))
        crc1 = crc.table_driven(string1)
 
    print datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') 
    print string1
    print string2 
    print "CRC: " + str(crc1)

if __name__ == "__main__":
    main()
