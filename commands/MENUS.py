from colored import fg, attr
from time import sleep
import os

#os.system('mode con: cols=150 lines=40')

light_blue  = fg('#19A7CE')
dark_blue   = fg('#146C94')
grey        = fg('grey_74')
reset       = attr('reset')


def MAIN_MENU():
    print(light_blue + f'''

                                                                                                
            ███╗   ██╗███████╗████████╗              ████████╗ ██████╗  ██████╗ ██╗     ███████╗
            ████╗  ██║██╔════╝╚══██╔══╝              ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝        {dark_blue} » Made by : F1X {light_blue}
            ██╔██╗ ██║█████╗     ██║       █████╗       ██║   ██║   ██║██║   ██║██║     ███████╗        {dark_blue} » GithHub : F1X-0 {light_blue}
            ██║╚██╗██║██╔══╝     ██║       ╚════╝       ██║   ██║   ██║██║   ██║██║     ╚════██║        {dark_blue} » Use 'help' to see the commands {light_blue}
            ██║ ╚████║███████╗   ██║                    ██║   ╚██████╔╝╚██████╔╝███████╗███████║
            ╚═╝  ╚═══╝╚══════╝   ╚═╝                    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
 

            

    ''' + grey)

def COMMAND_LINE():
    print(f'\n{light_blue}            >> {grey}', end='')

def HELP_MENU():
    print(grey + f'''
    
            {light_blue}[*] Commands :{grey}

                {light_blue}>{grey} geoip   [target]                      {light_blue}|{grey}   Show geolocalitation info about the IP
                {light_blue}>{grey} ping    [target] [count]              {light_blue}|{grey}   Send an specific amount of eco ICMP
                {light_blue}>{grey} sping   [target] [source] [count]     {light_blue}|{grey}   Send an spoofed eco ICMP (Chanages the source)
                {light_blue}>{grey} tping   [target]                      {light_blue}|{grey}   Does a trace and send an eco ICMP to all
                {light_blue}>{grey} trace   [target]                      {light_blue}|{grey}   Shows all the connections your packets was sent through
                {light_blue}>{grey} send    [target] [dport]              {light_blue}|{grey}   Sends an UDP message to a target
                {light_blue}>{grey} recive  [sport]                       {light_blue}|{grey}   Start reciving the UDP messages
                {light_blue}>{grey} arp                                   {light_blue}|{grey}   Shows your arp mac entries
                {light_blue}>{grey} dnsc                                  {light_blue}|{grey}   Shows your dns cache
                {light_blue}>{grey} ipconfig                              {light_blue}|{grey}   Shows your interfaces configuration

                {light_blue}Page {grey}1{light_blue} / {grey}1
    ''')

#                {light_blue}>{grey} strace  [target]                      {light_blue}|{grey}   Same as trace but with spoofed source
#Yo can add this but only works with IPv6 (use tracert -h in cmd for help)

def ERROR_404():
    print(f'{light_blue}            [!]{grey} Command not found')

def ERROR_400():
    print(f'{light_blue}            [!]{grey} An error ocured. See help for command usage')
