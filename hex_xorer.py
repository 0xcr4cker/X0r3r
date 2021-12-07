print('''
################################################################
#              An algorithm to XOR two strings                 #
#                    Made by @unknownamd                       #
#                      Hope it works!                          #
#   You can Check the results using this online tool:          #
#        https://codebeautify.org/xor-calculator               #
#                                                              #
################################################################
''')


def hexer():
    pt  = input("insert a plain text: ")
    lnpt = len(pt)
    key = input("insert a key with length of %s: " % lnpt)
    if len(key) != len(pt):
        print("Please insert a key with the same length of the Plain Text.. ")
        exit()
    ptArr = []
    keyArr= []
    for p in pt:
        var = ''.join(hex(ord(p)))
        ptArr.append(var)
    print("Your PlainText after hexing: ", ptArr)
    for k in key:
        var2 = ''.join(hex(ord(k)))
        keyArr.append(var2)
    print("Your key after hexing:       ",keyArr)
    print("----------------------------------------")

    Xored = []

    for i in range(len(ptArr)):
        hexx = int(ptArr[i], 16) ^ int(keyArr[i], 16)
        Xored.append(hexx)
    print("XOR XOR XORed... : ", Xored)




hexer()
