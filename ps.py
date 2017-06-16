# -*- coding: utf-8 -*-  
#additional 
from ftplib import FTP
import ftplib
import os  
import socket  
import sys
import os.path
  
HOST = 'rabbit.lan'
PORT = 5021 
DIRN = 'Local'  
FILE = None  
METHOD = None

def main():  
    if not len(sys.argv) == 3  :
        print 'Wrong Argument!'
        return
    FILE = sys.argv[2]
    METHOD = sys.argv[1]

    try:  
        f = FTP()
        f.connect(HOST,PORT)  
    except (socket.error, socket.gaierror):  
        print 'ERROR:cannot find " %s"' % HOST  
        return  
    print '***Connected to host "%s"' % HOST  
  
    try:  
        f.login()  
    except ftplib.error_perm:  
        print 'ERROR: cannot login anonymously'  
        f.quit()  
        return  
    print '*** Logged in as "anonymously"'  
    try:  
        f.cwd(DIRN)  
    except ftplib.error_perm:  
        print 'ERRORL cannot CD to "%s"' % DIRN  
        f.quit()  
        return  
    print '*** Changed to "%s" folder' % DIRN  
    if METHOD == 'get' :
        try:  
            f.retrbinary('RETR %s' % FILE, open(FILE.decode('gbk'), 'wb').write)  
        except ftplib.error_perm:  
            print 'ERROR: cannot read file "%s"' % FILE  
            os.unlink(FILE)  
        else:  
            print '*** Downloaded "%s" to CWD' % FILE  
    elif METHOD == 'put':
        FileHandler = open(FILE.decode('gbk'),'rb')
        try :
            f.storbinary('STOR %s' % os.path.split(FILE)[1].decode('gbk').encode('utf-8'), FileHandler)
            FileHandler.close()
        except ftplib.error_perm :
            print 'Error upload "%s" ' % FILE.decode('gbk')
        else :
            print '***Upload "%s" Succeed' % FILE.decode('gbk')
    else :
        pass	
    f.quit()  
    return  
  
if __name__ == '__main__':  
    main()