def main():
    ip4 = input("Enter an IPv4 address: ")
    ip4 = ip4.split(".")
    if len(ip4)!=4:
        print("is an invalid IPv4 address")
    else:
        check = True
        for i in ip4 :
            if int(i)<0 or int(i)>255 or len (i)!=3:
                check = False
        print("is a valid IPv4 address")
main()

