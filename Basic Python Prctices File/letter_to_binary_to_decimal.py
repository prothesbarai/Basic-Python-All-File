getText = input("Enter Text : ")
# Convert Binary And Join it  ord(value) Mainly Convert Letter To ASCII Code
binary = "".join(format(ord(c), "08b") for c in getText)
decimal = int(binary, 2)
print(decimal)

# Now Decimal TO Convert Binary to ASCII
bin = bin(decimal)[2:]  # [2:] Ignore ob
eightBitConvert = bin.zfill((8 - len(bin) % 8) + len(bin) if len(bin) % 8 != 0 else len(bin))
print(eightBitConvert)
convertAscci = ''.join(chr(int(eightBitConvert[i:i+8],2)) for i in range(0,len(eightBitConvert),8))
print(convertAscci)
