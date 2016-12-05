from python_hosts import Hosts, HostsEntry
# Native Native inet_pton and inet_ntop implementation for Python on Windows
# link: https://pypi.python.org/pypi/win_inet_pton
import win_inet_pton
import sys


class Block(object):
    def __init__(self):
        self.block_file = 'block.txt'
        #hosts_file = Hosts.determine_hosts_path()
        #hosts = Hosts(path=hosts_file)
        # Default os hosts filepath is already used
        self.hosts = Hosts()
    
    def __str__(self):
        return self.hosts.determine_hosts_path()
    
    def main(self):
        if len(sys.argv) == 2:
            if sys.argv[1] == 'enable':
                self.enable_block()
                print 'Websites blocked'
                return
            elif sys.argv[1] == 'disable':
                self.disable_block()
                print 'Websites unblocked'
                return
        print 'enable  - Enable blocklist\ndisable - Disable blocklist'
    
    def disable_block(self):
        with open(self.block_file, 'r') as f:
            for line in f:
                [address, name] = line.split()
                #self.hosts.remove_all_matching(address=address, name=name)
                self.hosts.remove_all_matching(address=address)
            self.hosts.write()
        
    def enable_block(self):
        self.hosts.import_file(self.block_file)
        
if __name__ == '__main__':
    Block().main()