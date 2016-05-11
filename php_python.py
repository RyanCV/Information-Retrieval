# -*- coding: UTF-8 -*-

import time
import signal
import sys
import socket
import os
import process
import utils


LISTEN_PORT = 21230     
CHARSET = "utf-8"      

#build connect between php and pyhon
if __name__ == '__main__':

    print ("- PHP-Python Connection")
    print ("- Time: %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.bind(('', LISTEN_PORT))  
    sock.listen(5)  

    print ("Listen port: %d" % LISTEN_PORT)
    print ("charset: %s" % CHARSET)
    print ("Server startup...")
    
    utils.init_all_data()
    print ("Data Loaded!")
    

    while 1:
        connection,address = sock.accept()  

        try:
            process.ProcessThread(connection).start()
        except:
            pass
