import mechanize
import socks
import socket
import random

nrLike = 0
URL = 'Url of the server'
PAYLOAD = 'PHP request'

while True:
    try:
        nrOdAddress = 0
        with open("proxy.txt", "r") as f:
            adressessArray = f.read().splitlines()

        with open("proxy.txt", "r") as f:
            lines = f.readlines()

        nrOfAddress = random.randint(0, len(adressessArray) - 1)

        print("Trying next Proxy")
        with open("proxy.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != adressessArray[nrOfAddress]:
                    f.write(line)

        PROXY = adressessArray[nrOfAddress].split(':')[0]
        PORT = adressessArray[nrOfAddress].split(':')[1]

        print(adressessArray[nrOfAddress])

        def create_connection(address, timeout=1, source_address=None):
            sock = socks.socksocket()
            sock.connect(address)
            print("Proxy connected...")
            return sock

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(PROXY), int(PORT))

        # patch the socket module
        socket.socket = socks.socksocket
        socket.create_connection = create_connection

        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent',
                               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        #'vote_type=vote_file_minus'
        br = browser.open(URL, PAYLOAD).read()
        print(br)
    except:
        print("Proxy is not working!")