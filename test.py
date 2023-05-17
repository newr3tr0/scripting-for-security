def runPortScan():
    host = "127.0.0.1"
    nm = nmap.PortScanner()
    nm.scan(host, '21-400')

    print(nm.command_line())  # Print the Nmap command line used to run the scan

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())

        for protocol in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % protocol)

            portList = nm[host][protocol].keys()
            for port in portList:
                print('port : %s\tstate : %s' % (port, nm[host][protocol][port]['state']))
