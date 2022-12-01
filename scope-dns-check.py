#!/bin/python

import dns.resolver
import socket

def domain2IPcheck(domainName, ipAddress, importStatus, dnsType='A'):
    '''
    Input to the function
    - domain name
    - ip address
    - dns type (A, AAAA, CNAME, MX, NS, PTR, CERT, SRV, TXT, SOA)
    
    Outputs from the function 
    - if domain name resolves to ip address
    '''

    try:
        answers = dns.resolver.resolve(domainName, dnsType)
        dnsAnswer = str(answers.response.answer[0]).split("\n")
        ipAddr_List = []

        for item in dnsAnswer: 
            ansSplit = item.split(" ")
            ipAddr = ansSplit[4]
            if (valid_ip(ipAddr)):
                ipAddr_List.append(ipAddr)
    
        for ip in ipAddr_List:
            if (ip == ipAddress):
                return True

        return False

    except:
        print("[E] - No DNS entries returned")
        return False
        
    # additonal checks if dnspython can't be installed
    #else:
    #    print(socket.gethostbyname('www.google.com'))
        

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False



# if false, then need to manually confirm domain name
if __name__ == "__main__":

    print("[i] - This should be used as a module, otherwise conducting examples...")
    result1 = domain2IPcheck('dnspython.org', '192.168.1.1')
    print("[i] - Result should be false:        " + str(result1)) # should be false

    result2 = domain2IPcheck('dnspython.org', '52.218.80.18')
    print("[i] - Probably false, maybe true:    " + str(result2)) # probably not true but the ip address is aws dynamic

    result3 = domain2IPcheck('example.com', '93.184.216.34')
    print("[i] - Result should be true:         " + str(result3)) # should be true

    result4 = domain2IPcheck('example.cloud', '8.8.8.8')
    print("[i] - Result should be error/false:  " + str(result4)) # should error
