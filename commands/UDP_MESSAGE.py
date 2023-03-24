import socket
from colored import fg, attr

light_blue  = fg('#19A7CE')
dark_blue   = fg('#146C94')
grey        = fg('grey_74')
reset       = attr('reset')

def SEND_UDP(target, port):

    port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f'{light_blue}            [*] Sending message to : {grey}{target}:{port} \n')

    message =  input(f'{light_blue}                 > Message :{grey} ').encode()

    sock.sendto(message, (target, port))
    sock.close()


def RECIVE_UDP(port):

    port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))

    message, source = sock.recvfrom(1024)

    message = str(message)
    message = message.replace("b", "")
    message = message.replace("'", "")

    source = str(source)
    source = source.replace("(", "")
    source = source.replace(")", "")
    source = source.replace("'", "")
    source = source.replace(",", "")


    print(f'{light_blue}                 > Message :{grey} {message} \n {light_blue}                  Source  :{grey} {source}\n')



