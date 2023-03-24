import os
from colored import fg, attr

light_blue  = fg('#19A7CE')
dark_blue   = fg('#146C94')
grey        = fg('grey_74')
reset       = attr('reset')

def PING(target, count):
    command = f'ping {target} -n {count} > output/PING_RESULT.txt'
    print(f'{light_blue}            [*] STARTING{grey}')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/PING_RESULT.txt')
    result = open('output/PING_RESULT.txt', 'r')
    result = result.readlines()
    result = result[-4], result[-3], result[-1]
    result = str(result)
    result = result.split()
    packets_sended = result[4]
    packets_sended = packets_sended.replace(',', "")
    packets_recived = result[7]
    packets_recived = packets_recived.replace(',', "")
    packets_losted = result[10]
    packets_losted = packets_losted.replace("\\n", "")
    packets_losted = packets_losted.replace("'", "")
    packets_losted = packets_losted.replace(",", "")
    packets_losted_percent = result[12]
    packets_losted_percent = packets_losted_percent.replace("(", "")
    ms = result[23]
    ms = ms.replace("\\n", "")
    ms = ms.replace("'", "")
    ms = ms.replace(")", "")
    
    print(f'{light_blue}            [*] Sending{grey} {count}{light_blue} ICMP to {grey}{target} \n')
    print(f'{light_blue}                > Packets sended    :{grey} {packets_sended}')
    print(f'{light_blue}                > Packets recived   :{grey} {packets_recived}')
    print(f'{light_blue}                > Packets losted    :{grey} {packets_losted}')
    print(f'{light_blue}                > Packets losted %  :{grey} {packets_losted_percent}')
    print(f'{light_blue}                > Average ms        :{grey} {ms}' )



#def NETSTAT():
#    command = f'netstat -noa > output/!!POR HACER!!'
#    print(f'{light_blue}            [*] STARTING{grey}')
#    os.system(command)
#    print(f'{light_blue}            [*] Saved on :{grey} output/!!POR HACER!!')

def ARP():
    command = f'arp -a > output/ARP_ENTRIES.txt'
    print(f'{light_blue}            [*] STARTING{grey}')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/ARP_ENTRIES.txt')
    result = open('output/ARP_ENTRIES.txt', 'r')
    for line in result:
            line.strip()
            print(f'{light_blue}                {grey} {line}', end="")
    print()

def DNS_CACHE():
    command = f'ipconfig -displaydns > output/DNS_CACHE.txt'
    print(f'{light_blue}            [*] STARTING{grey}')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/DNS_CACHE.txt')

def IPCONFIG():
    command = f'ipconfig -all > output/IPCONFIG_RESULT.txt'
    print(f'{light_blue}            [*] STARTING{grey}')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/IPCONFIG_RESULT.txt')
    

def TRACER(target):
    command = f'tracert {target} > output/TRACE_RESULT.txt'
    print(f'{light_blue}            [*] STARTING{grey} Can take a few seconds')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/TRACE_RESULT.txt')

def PATHPING(target):
    command = f'pathping {target} > output/TPING_RESULT.txt'
    print(f'{light_blue}            [*] STARTING{grey} Can take a few seconds')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/TPING_RESULT.txt')

def SPOOFED_ICMP(target, source, count):
    command = f'ping {target} -S {source} -n {count} > output/SPING_RESULT.txt'
    print(f'{light_blue}            [*] STARTING{grey}')
    os.system(command)
    print(f'{light_blue}            [*] Saved on :{grey} output/SPING_RESULT.txt')

#Procesar dataos https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html