import requests
from colored import fg, attr

#https://hackertarget.com/ip-tools/
#https://ip-api.com/

#You can add more tools with this APIs -->
#https://api.hackertarget.com/dnslookup/?q=google.com
#https://api.hackertarget.com/httpheaders/?q=http://www.google.com
#https://api.hackertarget.com/pagelinks/?q=websitetotest.com
#https://api.hackertarget.com/reversedns/?q=8.8.8.8

light_blue  = fg('#19A7CE')
dark_blue   = fg('#146C94')
grey        = fg('grey_74')
reset       = attr('reset')

def IP_GEO(target):
    r = requests.get(f'http://ip-api.com/json/{target}')
    list = r.json()


    print(light_blue + '            [*] Query :', grey + list['query'], '\n' )



    if list['status'] == 'success' :

        print(light_blue + '                >', grey + 'Status :', list['status'])
        print(light_blue + '                >', grey + 'Country :', list['country'])
        print(light_blue + '                >', grey + 'City :', list['city'])
        print(light_blue + '                >', grey + 'Cordenades : ', 'Lat', list['lat'], 'Lon',list['lon'])
        print(light_blue + '                >', grey + 'Timezone :', list['timezone'])
        print(light_blue + '                >', grey + 'Internet service provider : ', list['isp'])


    elif list['status'] == 'fail':
        print(light_blue + '                [!]', grey + ' Status', list['status'])


    else:
        print(light_blue + '                [!]', grey + ' Status unknown')
