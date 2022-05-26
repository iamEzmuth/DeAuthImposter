# DeAuthImposter
Best tool to deauthenticate (disconnect) everyone in wifi network you are...

TO start the tool:

$>sudo python3 deauthimposter.py [mandatrory options]

In Mandatory options you have two of them:
1) all
2) select

 if you choose "all", all devices connected to that wifi network will get disconnected but choosing "select", before running attack
 you will be asked for which device to be removed from attack list so that you can remove you own devices for deauthenticating (disconnecting)
 
$>sudo python3 deauthimposter.py all

                ||(OR)

$>sudo python3 deauthimposter.py select

Fisrt all Networks will be detected and you would be asked for which network you are in....

Then all devices in the network will be scaned and if "select" argument was gives than you will be listed with a table
of all devices (MAc-ADdress) then you would be asked to removes your devices to check mac-address of your device their its very simple
google it (-_-) :)

Atlast all devices that wrent removed will be Attcaked with deauthentication script and will get disconnect and will not be able 
to connect to that wifi till you close the script by typing "quit" and pressing Enter...


------------------------Note----------------------------

"""It took 3 hours to complete this script but may have some flaws feel free to fork and pull request"""
'''but dont pull request for changing comments till hacktoberfest'''  (-_-) (=_=)

BY: iamEZMUTH 
