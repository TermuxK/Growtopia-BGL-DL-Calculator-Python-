import time

bgl = 100
onebgl = 1
worldlock = 100

print("Script will end when you done using it after 5 seconds.")
time.sleep(2)
print("Write a Number")
dl_asked = int(input("[]: "))
print("-----------------------------------")
print(bgl*dl_asked," DLs.")
print(onebgl*dl_asked," BGLs.")
print("-----------------------------------")
time.sleep(5)