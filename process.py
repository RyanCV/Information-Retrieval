# -*- coding: UTF-8 -*-

# -*- coding: UTF-8 -*-
#-----------------------------------------------------------
# PPython(PHP and Python).
#   (2012-15 http://code.google.com/p/ppython/)
#
# License: http://www.apache.org/licenses/LICENSE-2.0
#-----------------------------------------------------------

import sys
import time
import threading
import socket

import php_python

#the min size of message package
REQUEST_MIN_LEN = 10
TIMEOUT = 180

pc_dict = {}        
global_env = {} 

# find position of c in bytes
# pos: the start position
def index(bytes, c, pos=0):
    for i in range(len(bytes)):
        if (i <= pos):
            continue
        if bytes[i] == c:
            return i
            break
    else:
        return -1


# encode parameters from python to php
def z_encode(p):
    if p == None:                               #python None to PHP NULL
        return "N;"
    elif isinstance(p, int):                    #python int to PHP int
        return "i:%d;" % p
    elif isinstance(p, str):                    #python String to PHP String
        p_bytes = p.encode(php_python.CHARSET);
        ret = 's:%d:"' % len(p_bytes)
        ret = ret.encode(php_python.CHARSET)
        ret = ret + p_bytes + '";'.encode(php_python.CHARSET)
        #ret = str(ret, php_python.CHARSET)
        ret = str(ret)
        return ret
    elif isinstance(p, bool):                   #python boolean to PHP boolean
        b=1 if p else 0
        return 'b:%d;' % b
    elif isinstance(p, float):                  #python float to PHP float
        return 'd:%r;' % p
    elif isinstance(p, list) or isinstance(p, tuple):        #python list,tuple to PHP array with int indice
        s=''
        for pos,i in enumerate(p):
            s+=z_encode(pos)
            s+=z_encode(i)
        return "a:%d:{%s}" % (len(p),s)
    elif isinstance(p, dict):                   #python dictionary to PHP array with string indice
        s=''
        for key in p:
            s+=z_encode(key)
            s+=z_encode(p[key])
        return "a:%d:{%s}" % (len(p),s)
    else:                                       #Other types in python to PHP NULL
        return "N;"

#decode php parameters from string to python
def z_decode(p):
    if p[0]==chr(0x4e):                      #NULL 0x4e-'N'
        return None,p[2:]
    elif p[0]==chr(0x62):                    #bool 0x62-'b'
        if p[2] == chr(0x30):                # 0x30-'0'
            return False,p[4:]
        else:
            return True,p[4:]
    elif p[0]==chr(0x69):                    #int  0x69-'i'
        i = index(p, chr(0x3b), 1)           # 0x3b-';'
        return int(p[2:i]),p[i+1:]
    elif p[0]==chr(0x64):                    #double 0x64-'d'
        i = index(p, chr(0x3b), 1)           # 0x3b-';'
        return float(p[2:i]),p[i+1:]
    elif p[0]==chr(0x73):                    #string 0x73-'s'
        len_end = index(p, chr(0x3a), 2)     # 0x3a-':'
        str_len = int(p[2:len_end])
        end = len_end + 1 + str_len + 2
        v = p[(len_end + 2) : (len_end + 2 + str_len)]
        #return str(v, php_python.CHARSET), p[end+1:]
        return v.encode(php_python.CHARSET), p[end+1:]
    elif p[0]==chr(0x61):                    #array 0x61-'a'
        list_=[]       #array
        dict_={}       #dictionary
        flag=True      #true-tuple false-dictionary
        second = index(p, chr(0x3a), 2)      # 0x3a-":"
        num = int(p[2:second])  #number of elements
        pp = p[second+2:]       #all elements
        for i in range(num):
            key,pp=z_decode(pp)  #key decode
            if (i == 0): 
                if (not isinstance(key, int)) or (key != 0):
                    flag = False            
            val,pp=z_decode(pp)  
            list_.append(val)
            dict_[key]=val
        return (list_, pp[2:]) if flag else (dict_, pp[2:])
    else:
        return p,''


def parse_php_req(p):
    while p:
        v,p=z_decode(p)         
        params = v

    modul_func = params[0]        
    pos = modul_func.find("::")
    modul = modul_func[:pos]    
    func = modul_func[pos+2:]   
    return modul, func, params[1:]   
    

class ProcessThread(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self._socket = socket

    def run(self):        
        try:  
            self._socket.settimeout(TIMEOUT)                 
            firstbuf = self._socket.recv(16 * 1024)          
            if len(firstbuf) < REQUEST_MIN_LEN:               
                print 'error message,less than minimum length:',firstbuf
                self._socket.close()
                return

            firstComma = index(firstbuf, chr(0x2c))              
            print firstbuf
            totalLen = int(firstbuf[0:firstComma])
            print 'message length:',totalLen
            reqMsg = firstbuf[firstComma+1:]
            print 'reqMsg:',reqMsg
            while (len(reqMsg) < totalLen):    
                reqMsg = reqMsg + self._socket.recv(16 * 1024)
        except Exception,e:  
            print 'getMessage error',str(e)
            self._socket.close()
            return
        modul, func, params = parse_php_req(reqMsg)
        print 'module:',modul,'func:',func,'parmas:',params

        if (modul not in pc_dict):  
            try:
                callMod = __import__ (modul)    
                pc_dict[modul] = callMod   
            except Exception,e:
                print 'module not exist:',modul
                self._socket.sendall(("F" + "module '%s' is not exist!" % modul).encode(php_python.CHARSET)) 
                self._socket.close()
                return
        else:
            callMod = pc_dict[modul]

        try:
            callMethod = getattr(callMod, func)
        except Exception,e:
            print 'function not exist:',func
            self._socket.sendall(("F" + "function '%s()' is not exist!" % func).encode(php_python.CHARSET)) #异常
            self._socket.close()
            return
        try: 
            params = ','.join([repr(x) for x in params])         
            compStr = "import %s\nret=%s(%s)" % (modul, modul+'.'+func, params)
            rpFunc = compile(compStr, "", "exec")
            
            if func not in global_env: 
                global_env[func] = rpFunc   
            local_env = {}
            exec (rpFunc, global_env, local_env)    
        except Exception,e:  
            print 'call python error:',str(e)
            errType, errMsg, traceback = sys.exc_info()
            self._socket.sendall(("F%s" % errMsg).encode(php_python.CHARSET)) 
            self._socket.close()
            return
        rspStr = z_encode(local_env['ret'])

        try:  
            rspStr = "S" + rspStr
            self._socket.sendall(rspStr.encode(php_python.CHARSET))
        except Exception,e:
            print 'send message error:',str(e)
            errType, errMsg, traceback = sys.exc_info()
            self._socket.sendall(("F%s" % errMsg).encode(php_python.CHARSET)) 
        finally:
            self._socket.close()
            return