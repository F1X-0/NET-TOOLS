#This progmarm is incomplete. I have learned all i whanted with this project
#Feel free to copy, end and use this program <3
#I have writed some ideas abaout what you can do.


#Imports -->
from commands.UDP_MESSAGE import *
from commands.MENUS import *
from commands.INFO import *
from commands.IP_API import *
from colored import fg, attr
import os, json

#Variables -->
light_blue  = fg('#19A7CE')
dark_blue   = fg('#146C94')
grey        = fg('grey_74')
reset       = attr('reset')

#Extra funtions -->
def clear():
    os.system('cls')

def COMMAND_MANAGER():
        global arguments, command
        COMMAND_LINE()
        arguments = input().split()
        command = arguments[0].lower()

def OPTION_MANAGER():
    if command == 'help':
        clear()
        MAIN_MENU()
        HELP_MENU()

    elif command == 'clear':
        clear()
        MAIN_MENU()

    elif command == 'ping':
        clear()
        MAIN_MENU()
        try:
            PING(arguments[1], arguments[2])
        except:
            ERROR_400()

    elif command == 'geoip':
        clear()
        MAIN_MENU()
        try:
            IP_GEO(arguments[1])
        except:
            ERROR_400()

    elif command == 'sping':
        clear()
        MAIN_MENU()
        try:
            SPOOFED_ICMP(arguments[1], arguments[2], arguments[3])
        except:
            ERROR_400()

    elif command == 'tping':
        clear()
        MAIN_MENU()
        try:
            PATHPING(arguments[1])
        except:
            ERROR_400()

    elif command == 'trace':
        clear()
        MAIN_MENU()
        try:
            TRACER(arguments[1])
        except:
            ERROR_400()

    elif command == 'arp':
        clear()
        MAIN_MENU()
        try:
            ARP()
        except:
            ERROR_400()

    elif command == 'dnsc':
        clear()
        MAIN_MENU()
        try:
            DNS_CACHE()
        except:
            ERROR_400()

    elif command == 'ipconfig':
        clear()
        MAIN_MENU()
        try:
            IPCONFIG()
        except:
            ERROR_400()

    elif command == 'send':
        clear()
        MAIN_MENU()
        try:
            SEND_UDP(arguments[1], arguments[2])
        except:
            ERROR_400()

    elif command == 'recive':
        clear()
        MAIN_MENU()
        try:
            print(f'{light_blue}            [*] Started listening at :{grey}', arguments[1], '\n')
            while True:
                RECIVE_UDP(arguments[1])
        except:
            ERROR_400()

    else:
         ERROR_404()


#Open config -->
with open('config/config.json', 'r') as config:
    config = json.load(config)


#Load config -->
columns = config['columns']
lines = config['lines']
title = config['title']


#Window options -->
os.system(f'mode con: cols={columns} lines={lines}')
os.system(f'title {title}')



#Defining the program -->

def main():
    clear()
    MAIN_MENU()
    while True:
        COMMAND_MANAGER()
        OPTION_MANAGER()






#Starting the program -->
if __name__ == '__main__':
    main()
