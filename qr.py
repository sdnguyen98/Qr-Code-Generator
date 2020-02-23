import qrcode
import hmac
import base64
import struct
import string
import hashlib
import time


def hotp(secret, x):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", x)
    otp = hmac.new(key, msg, hashlib.sha1).digest()
    o = otp[19] & 15
    otp = (struct.unpack(">I", otp[o:o+4])[0] & 0x7fffffff) % 1000000
    return otp

def totp(secret):
    x =int((time.time())//30)
    return hotp(secret, x)

def main():
    fix =str(0)
    secret ="JBSWY3DPEHPK3PXP"
    otplink1='otpauth://totp/CS370:'
    otplink2='?secret=JBSWY3DPEHPK3PXP&issuer=CS370'
    email = input("Enter your Gmail : \nexample - bob@gmail.com \n")
    user = otplink1+email+otplink2
    vexit = 0
    while vexit == 0:
        option = int(input("Enter 1 --generate-qr\nEnter 2 --get-otp\nEnter 3 to exit\n"))
        if option == 1:
            qr = qrcode.make(user)
            qr.show('myQR.png')
        elif option == 2:
#this helps keep the leading zero
            otp = str(totp(secret))
            z = str(otp)
            if len(z) == 5:
                z =str(fix+z)
            if len(z) == 4:
                z =str(fix+fix+z)
    #this is for the displaying of the OTP
            emptyspace = "                   "
            lempty = len(emptyspace)
            message = "OTP is "
            news = "#" + emptyspace + message + z + emptyspace + "#"
            lnew = len(news)
            edge = "# "
            mid = "# "
            for i in range (int(lnew/2 - 1)):
                edge += "# "
                mid += "  "
            edge += "#"
            mid += "#"
            print(edge)
            print(mid)
            print(news)
            print(mid)
            print(edge)

        elif option == 3:
            vexit =1

if __name__== '__main__':
    main()

