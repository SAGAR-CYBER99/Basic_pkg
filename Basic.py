# Termux basic pakage install
#(copyright)
#Author Sh
#▣𝗴𝗶𝘁𝗵𝘂𝗯.𝗰𝗼𝗺/𝗦𝗔𝗚𝗔𝗥-𝗖𝗬𝗕𝗘𝗥𝟵𝟵
import time
import sys
import os 
import signal

def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.006)


def handler(signum, frame):
    res = input("\n\033[1;92mCtrl-c was pressed. Do you really want to exit? (y/n): ")
    if res == 'y':
    	delay_print('\n\033[1;92mExiting...\n\n')
    	time.sleep(1)
    	exit()

signal.signal(signal.SIGINT, handler)

os.system('clear')
delay_print('''\033[1;92m                                                                                    
                              ,,                                                    
`7MM"""Yp,                    RS              `7MM"""Mq.`7MMF' `YMM' .g8"""bgd      
  MM    Yb                                      MM   `MM. MM   .M' .dP'     `M      
  MM    dP  ,6"Yb.  ,pP"Ybd `7MM  ,p6"bo        MM   ,M9  MM .d"   dM'       `      
  MM"""bg. 8)   MM  8I   `"   MM 6M'  OO        \033[1;97mMMmmdM9   MMMMM.   MM               
  MM    `Y  ,pm9MM  `YMMMa.   MM 8M             MM        MM  VMA  MM.    `7MMF'    
  MM    ,9 8M   MM  L.   I8   MM YM.    ,       MM        MM   `MM.`Mb.     MM      
.JMMmmmd9  `Moo9^Yo.M9mmmP' .JMML.YMbmd'      .JMML.    .JMML.   MMb.`"bmmmdPY     
                                                                 Created By Md S4G4R  ©

[❔] Choose an option:

\033[1;97m[01] Install manually
[02] Install all basic package
[03] Join Fb group 
[04] About 
[00] Exit
''')

main = input(" \033[1;92m╚══[🐼] \033[1;90m Choose option\033[1;91m:\033[1;97m ")

if main == '01' or main == '1':
	while True:
		os.system('clear')
		delay_print('''\033[91m
   _____ ___ ___ __  __ _   ___  __  ___  _   ___ _  __   _   ___ ___ 
  |_   _| __| _ \  \/  | | | \ \/ / | _ \/_\ / __| |/ /  /_\ / __| __|
    | | | _||   / |\/| | |_| |>  <  |  _/ _ \ (__| ' <  / _ \ (_ | _| \033[1;97m
    |_| |___|_|_\_|  |_|\___//_/\_\ |_|/_/ \_\___|_|\_\/_/ \_\___|___|
                                             \033[1;97mCreated By \033[1;57mMd S4G4R

[?] Choose Any Package:

\033[1;97m[01] inxi
[02] python2
[03] python3
[04] curl
[05] perl
[06] ngrok
[07] nodejs
[08] figlet
[09] ruby
[10] php
[11] o-editor
[12] termux-api
[13] netcat
[14] zip
[15] unzip
[16] fish
[17] cmatrix
[18] tor
[19] tar
[20] wget
[21] mpv
[22] openssh
[23] openssl
[24] clang
[25] nmap
[26] w3m
[27] dnsutils-static
[28] dnsutils
[29] coreutils
[30] python2-static
[31] vim-python
[32] python2-six
[33] python-static
[34] vim
[35] tree
[36] youtubedr
[37] proot
[38] proot-distro
[39] openjdk-17
[40] unrar
[41] golang-doc
[42] golang
[43] cowsay
[44] wireshark-gtk
[45] x11-repo
[46] root-repo
[47] unstable-repo
[48] inetutils
[49] lf
[50] findomain
[51] jp2a
[95] Back
[00] Exit''')

		pall = input('\n\n═[🐼] \033[1;90m Basic PKG \033[1;91m:\033[1;97m  ')
		if pall == '01' or pall == '1':
			delay_print('\n\033[1;92minxi is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install inxi -y')
			delay_print('\n\033[1;92minxi is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '02' or pall == '2':
			delay_print('\n\033[1;92mpython2 is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install python2 -y')
			delay_print('\n\033[1;92mpython2 is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '03' or pall == '3':
			delay_print('\n\033[1;92mpython3 is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install python3 -y')
			delay_print('\n\033[1;92mpython3 is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '04' or pall == '4':
			delay_print('\n\033[1;92mcurl is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install curl -y')
			delay_print('\n\033[1;92mcurl is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '05' or pall == '5':
			delay_print('\n\033[1;92mperl is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install perl -y')
			delay_print('\n\033[1;92mperl is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '06' or pall == '6':
			delay_print('\n\033[1;92mngrok is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install nodejs -y;npm install ngrok -g')
			delay_print('\n\033[1;92mngrok is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '07' or pall == '7':
			delay_print('\n\033[1;92mnodejs is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install nodejs -y')
			delay_print('\n\033[1;92mnodejs is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '08' or pall == '8':
			delay_print('\n\033[1;92mfiglet is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install figlet -y')
			delay_print('\n\033[1;92mfiglet is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '09' or pall == '9':
			delay_print('\n\033[1;92mruby is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install ruby -y')
			delay_print('\n\033[1;92mruby is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '10':
			delay_print('\n\033[1;92mphp is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install php -y')
			delay_print('\n\033[1;92mphp is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '11':
			delay_print('\n\033[1;92mo-editor is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install o-editor -y')
			delay_print('\n\033[1;92mo-editor is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '12':
			delay_print('\n\033[1;92mtermux-api is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install termux-api -y')
			delay_print('\n\033[1;92mtermux-api is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '13':
			delay_print('\n\033[1;92mnetcat is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install netcat -y')
			delay_print('\n\033[1;92mnetcat is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '14':
			delay_print('\n\033[1;92mzip is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install zip -y')
			delay_print('\n\033[1;92mzip is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '15':
			delay_print('\n\033[1;92munzip is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install unzip -y')
			delay_print('\n\033[1;92munzip is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '16':
			delay_print('\n\033[1;92mfish is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install fish -y')
			delay_print('\n\033[1;92mfish is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '17':
			delay_print('\n\033[1;92mcmatrix is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install cmatrix -y')
			delay_print('\n\033[1;92mcmatrix is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '18':
			delay_print('\n\033[1;92mtor is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install tor -y')
			delay_print('\n\033[1;92mtor is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '19':
			delay_print('\n\033[1;92mtar is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install tar -y')
			delay_print('\n\033[1;92mtar is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '20':
			delay_print('\n\033[1;92mwget is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install wget -y')
			delay_print('\n\033[1;92mwget is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '21':
			delay_print('\n\033[1;92mmpv is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install mpv -y')
			delay_print('\n\033[1;92mmpv is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '22':
			delay_print('\n\033[1;92mopenssh is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install openssh -y')
			delay_print('\n\033[1;92mopenssh is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '23':
			delay_print('\n\033[1;92mopenssl is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install openssl -y')
			delay_print('\n\033[1;92mopenssl is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '24':
			delay_print('\n\033[1;92mclang is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install clang -y')
			delay_print('\n\033[1;92mclang is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '25':
			delay_print('\n\033[1;92mnmap is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install nmap -y')
			delay_print('\n\033[1;92mnmap is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '26':
			delay_print('\n\033[1;92mw3m is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install w3m -y')
			delay_print('\n\033[1;92mw3m is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '27':
			delay_print('\n\033[1;92mdnsutils-static is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install dnsutils-static -y')
			delay_print('\n\033[1;92mdnsutils-static is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '28':
			delay_print('\n\033[1;92mdnsutils is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install dnsutils -y')
			delay_print('\n\033[1;92mdnsutils is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '29':
			delay_print('\n\033[1;92mcoreutils is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install coreutils -y')
			delay_print('\n\033[1;92mcoreutils is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '30':
			delay_print('\n\033[1;92mpython2-static is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install python2-static -y')
			delay_print('\n\033[1;92mpython2-static is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '31':
			delay_print('\n\033[1;92mvim-python is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install vim-python -y')
			delay_print('\n\033[1;92mvim-python is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '32':
			delay_print('\n\033[1;92mpython2-six is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install python2-six -y')
			delay_print('\n\033[1;92mpython2-six is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '33':
			delay_print('\n\033[1;92mpython-static is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install python-static -y')
			delay_print('\n\033[1;92mpython-static is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '34':
			delay_print('\n\033[1;92mvim is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install vim -y')
			delay_print('\n\033[1;92mvim is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '35':
			delay_print('\n\033[1;92mtree is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install tree -y')
			delay_print('\n\033[1;92mtree is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '36':
			delay_print('\n\033[1;92myoutubedr is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install youtubedr -y')
			delay_print('\n\033[1;92myoutubedr is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '37':
			delay_print('\n\033[1;92mproot is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install proot -y')
			delay_print('\n\033[1;92mproot is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '38':
			delay_print('\n\033[1;92mproot-distro is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install proot-distro -y')
			delay_print('\n\033[1;92mproot-distro is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '39':
			delay_print('\n\033[1;92mopenjdk-17 is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install openjdk-17 -y')
			delay_print('\n\033[1;92mopenjdk-17 is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '40':
			delay_print('\n\033[1;92munrar is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install unrar -y')
			delay_print('\n\033[1;92munrar is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '41':
			delay_print('\n\033[1;92mgolang-doc is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install golang-doc -y')
			delay_print('\n\033[1;92mgolang-doc is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '42':
			delay_print('\n\033[1;92mgolang is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install golang -y')
			delay_print('\n\033[1;92mgolang is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '43':
			delay_print('\n\033[1;92mcowsay is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install cowsay -y')
			delay_print('\n\033[1;92mcowsay is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '44':
			delay_print('\n\033[1;92mwireshark-gtk is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install x11-repo -y;apt install wireshark-gtk -y')
			delay_print('\n\033[1;92mwireshark-gtk is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '45':
			delay_print('\n\033[1;92mx11-repo is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install x11-repo -y')
			delay_print('\n\033[1;92mx11-repo is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '46':
			delay_print('\n\033[1;92mroot-repo is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install root-repo -y')
			delay_print('\n\033[1;92mroot-repo is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '47':
			delay_print('\n\033[1;92munstable-repo is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install unstable-repo -y')
			delay_print('\n\033[1;92munstable-repo is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '48':
			delay_print('\n\033[1;92minetutils is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install inetutils -y')
			delay_print('\n\033[1;92minetutils is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '49':
			delay_print('\n\033[1;92mlf is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install lf -y')
			delay_print('\n\033[1;92mlf is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '50':
			delay_print('\n\033[1;92mfindomain is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install findomain -y')
			delay_print('\n\033[1;92mfindomain is installed in your termux\n')
			time.sleep(1.5)
		elif pall == '51':
			delay_print('\n\033[1;92mjp2a is installing...\n\n')
			os.system('apt update -y;apt upgrade -y;apt install jp2a -y')
			delay_print('\n\033[1;92mjp2a is installed in your termux\n')
			time.sleep(1.5)

		elif pall == '95':
			delay_print('\033[1;92mComing back')
			os.system('sleep 1.0')
			os.system('python basicx.py')
			break
		elif pall == '0' or pall == '00':
			delay_print('\n\033[1;92mExiting...\n\n')
			os.system('sleep 1.0')
			exit()
		elif pall == 'q' or pall == 'Q':
			delay_print('\n\033[1;92mExiting...\n\n')
			os.system('sleep 1.0')
			exit()
		else:
			delay_print('\n\033[1;92mInvalid input\n')
			os.system('sleep 1.0')

elif main == '02' or main == '2':
	delay_print('\033[1;92mOk, all basic packages are installing in your termux, it might be take some time')
	os.system('apt update -y')
	os.system('apt upgrade -y')
	os.system('apt install root-repo unstable-repo x11-repo inxi python2 python curl perl nodejs figlet php ruby o-editor termux-api zip unzip fish cmatrix tor tar wget mpv jp2a openssh openssl clang nmap w3m dnsutils-static dnsutils coreutils python2-static python-static vim tree youtubedr proot proot-distro openjdk-17 unrar golang cowsay inetutils lf findomain jp2a -y')
	os.system('npm install ngrok -g')

elif main== '03' or main == '3':
    os.system('xdg-open https://m.facebook.com/groups/786815129769934/?ref=share&mibextid=NSMWBT')
    os.system('sleep 1.0')
    os.system('python basicx.py')
    
elif main == '04' or main == '4':
	os.system('clear')
	delay_print('''\033[31;1md888888b  .d88b.   .d88b.  db      .d8888.       .d8b.  d8888b.  .d88b.  db    db d888888b      
`~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP      d8' `8b 88  `8D .8P  Y8. 88    88 `~~88~~'      
   88    88    88 88    88 88      `8bo.        88ooo88 88oooY' 88    88 88    88    88 \033[31m        
   88    88    88 88    88 88        `Y8b.      88~~~88 88~~~b. 88    88 88    88    88\033[36;1m         
   88    `8b  d8' `8b  d8' 88booo. db   8D      88   88 88   8D `8b  d8' 88b  d88    88         
   YP     `Y88P'   `Y88P'  Y88888P `8888Y'      YP   YP Y8888P'  `Y88P'  ~Y8888P'    YP         
                                                               \033[0mCreated By Md S4G4R  ©''')
	delay_print("""\n\n\033[1;92mHello Guys I'm Md sagar, And I've created this tool for those who is beginner termux user and they have no any idea which type package we need to install in my termux or which not. \nGuys you can install total 51 basic packages in your termux that too just in one click and you have an option to install required basic packages manually. I hope This tool will help you a lot And Please Give Us feedback of this tool on github page,\n\nGuys you can also connect with us on Social media group,social media link is given below""")

	while True:
		delay_print('\n\033[1;92m[##] Select an option:\n\n[95] Back\n[00] Exit\n')
		ask = input('\n═[🐼] \033[1;90m Basic PKG \033[1;91m:\033[1;97m : ')
		if ask == '95':
			delay_print('\n\033[1;92mComing Back\n')
			time.sleep(1.0)
			os.system('python basicx.py')
			break
		elif ask == '0' or ask == '00' or ask == 'q' or ask == 'Q':
			delay_print('\n\033[1;92mExiting...\n\n')
			time.sleep(1.0)
			exit()
		else:
			delay_print('\n\033[1;92mInvalid Input\n')
			time.sleep(0.5)


elif main == '00' or main == '0' or main == 'q' or main == 'Q':
	delay_print('\n\033[1;92mExiting...\n\n')
	os.system('sleep 1.0')
	exit()

else:
	delay_print('\n\033[1;92mInvalid Input\n')
	os.system('sleep 1.0')
	os.system('python basicx.py')
