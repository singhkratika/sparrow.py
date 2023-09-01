#binary ,octa and hexa program in python.
n=int(input("enter a number:"))
print("binary format:"+bin(n).replace("0b",""))
print("octal format:"+oct(n).replace("0o",""))
print("hexa-decimal format:"+hex(n).replace("0x",""))