from sip import *
import sip

def run_proxy():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    logging.basicConfig(filename='proxy.log')
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    sip.recordroute = recordroute
    sip.topvia = topvia
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    print("Proxy server started at <%s:%s>" % (ipaddress, PORT))
    server.serve_forever()

if __name__ == "__main__":
    print("Please type START to start proxy server or END to end program.")
    choice = input()
    while (choice != 'END'):
        if(choice == 'START'):
            run_proxy()
            break
        else:
            print("Incorrect input.")
            choice = input()
