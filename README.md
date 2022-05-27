# DeAuthImposter
Best tool to deauthenticate (disconnect) everyone in wifi network you want to...

## Installing dependencies
```
    sudo pip3 install -r Requirements.txt

```

## TO start the tool:
```
    sudo python3 deauthimposter.py [mandatrory options]
```

In Mandatory options you have two of them:

1) Method : This option specifies whether the script should run on all targets that
            belongs to that network or selected ones.
    1) all (Attacks all targets)
    2) select (Attacks selected targets that you specify)

2) Network Interface Name: Next you have the specify you Network Interface name 
                           primarily you wifi interface name. (you can find that name by typing ifconfig in linux systems, it would be named like wlan0,wfpl0,wls1p0 etc...)

 if you choose "all", all devices connected to that wifi network will get disconnected but choosing "select", before running attack
 you will be asked for which device to be removed from attack list so that you can remove you own devices for deauthenticating (disconnecting)
 
 ```
$>sudo python3 deauthimposter.py all wlan0
```
                ||(OR)
```
$>sudo python3 deauthimposter.py select wlan0
```
Fisrt all Networks will be detected and you would be asked for target network....

Then all devices in the network will be scanned and if "select" argument was provided than you will be listed with a table
of all devices (MAc-ADdress) that are in target network after that you would be asked to remove your devices and other devices that are not to be targeted. (finding MAC Address of you device is pretty easy google it:))

Atlast all devices that were'nt removed will be Attacked with deauthentication script and will get disconnected and will not be able 
to reconnect to that wifi network till you close the script by typing "quit" and pressing Enter...


------------------------Note----------------------------

"""It took 3 hours to complete this script but may have some flaws feel free to fork and pull request"""
'''but don't pull request for changing comments till hacktoberfest'''(=_=)

BY: iamEZMUTH 

