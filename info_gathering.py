import nmap
import sys
import pprint
import time

nm_scan = nmap.PortScanner()
print('\nRunning...\n')
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-O')

pprint.pprint(nm_scanner)

host_status = 'the host is ' + nm_scanner['scan'][sys.argv[1]]['status']['state'] + '.\n'
port_open = ' the port 80 is ' + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state'] + '.\n'
method_scan = 'method of scanning is: ' + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + '.\n'
#guessed_os = 'there is a %s percent chance that the hose is running %s'%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][[sys.argv[1]]['osmatch'][0]['name'])

with open('%s.txt'%sys.argv[1],'w') as f:
    f.write(host_status + port_open + method_scan)
    f.write("\nReport Generated " + time.strftime('%Y-%m-d_%H:%M:%S GMT',time.gmtime()))

print('\nFinished...')