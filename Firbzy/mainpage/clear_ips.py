templist = []
listIPs = []
with open("log_ip.txt", "r") as logread:
    listIPs = logread.readlines()
for element in listIPs:
    if element not in templist:
        templist.append(element)
# print(listIPs)
# print(templist)
with open("log_ip.txt", "w") as logwrite:
    logwrite.writelines(templist)