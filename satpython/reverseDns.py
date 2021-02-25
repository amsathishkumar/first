import socket

with open('list43.txt', 'r') as furls:
    urls = furls.readlines()

with open('list43_url.txt', 'w') as configuration:
    #configuration.write(f' {"URL": <30} {"Resolved IP": <16} {"Reversed DNS": <16}\n')
    configuration.write(f' {"URL": <50} {"Resolved IP": <40}\n')
    for url in urls:
        url = url.strip()
   #     DNStoIP = socket.gethostbyname(url)
        try:
            DNStoIPs = socket.gethostbyname_ex(url)
            listToStr = ','.join([str(elem) for elem in DNStoIPs[2]])
            configuration.write(f' {url: <50} {listToStr: <40}\n')
            print(url)
            print(DNStoIPs[2])
        except:
            configuration.write(f' {url: <40} {"NA": <30}\n')
        # reversed_dns = socket.gethostbyaddr(socket.gethostbyname(url))
        # reversed_dns = ""
        # if isinstance(DNStoIPs[2], list):
        #   for ipt in DNStoIPs[2]:
        #       reversed_dns = socket.gethostbyaddr(ipt)
        #       rr = reversed_dns[0]
        #       configuration.write(f' {url: <30} {ipt: <16} {rr: <16}\n')
#print( f' {url: <20} {DNStoIP: <16} {reversed_dns[0]: <16}')
#print("URL: "+url+" Resolved IP:"+DNStoIP + " Reversed DNS: "+reversed_dns[0])
