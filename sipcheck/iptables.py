# -*- coding: utf-8 -*-
'''
    Wrapper for use iptables an block IPs
'''
import logging
import os

class IPTables(object):
    ''' IPTables wrapper '''
    dbconn = None

    def __init__(self, dbconn):
        ''' Constructor '''
        self.dbconn = dbconn
        self.logger = logging.getLogger(__name__)

    def block(self, ipaddress):
        ''' Set an IP adress as blocked an blocks with iptables '''
        self.logger.debug('Blocking %s IP address' % ipaddress)
        self.dbconn.block(ipaddress)
        os.system ("iptables -A INPUT -s %s -j DROP" % ipaddress)
        return True

    def unblock(self, ipaddress):
        ''' Unset an IP as bloked an release iptables block '''
        self.logger.debug('Unblocking %s IP address' % ipaddress)
        self.dbconn.block(ipaddress)
        os.system ("iptables -D INPUT -s %s -j DROP" % ipaddress)
        return True

