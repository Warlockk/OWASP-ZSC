#!/usr/bin/env python
'''
OWASP ZSC | ZCR Shellcoder
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project
https://github.com/Ali-Razmjoo/OWASP-ZSC
http://api.z3r0d4y.com/
https://groups.google.com/d/forum/owasp-zsc [ owasp-zsc[at]googlegroups[dot]com ]
'''
import binascii
import random
import string
from core.compatible import version
_version = version()

def encode(f):
    base64_arr = ''
    val_name = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    data = ''
    if _version is 2:
        data = val_name + ' = "' + str(binascii.b2a_base64(f)).replace('\n','') +'";'

    if _version is 3:
        data = val_name + ' = "' + str(binascii.b2a_base64(f).replace('\n','').encode('latin-1')).decode('latin-1') +'"'

    var_b64 = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    var_str = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    var_data = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    func_name = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    func_argv = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(50))
    f = '''
%s
function %s(%s) {
    var %s = %s.toString();
    var %s = window.atob(%s)
    return %s;
}
%s = %s;
eval(%s(%s));'''%(data,func_name,func_argv,var_b64,func_argv,var_str,var_b64,var_str,var_data,val_name,func_name,var_data)
    return f

def start(content):
    return str(str('/*\n')+str(content.replace('*/','*_/'))+str('\n*/') + str(encode(content))+str('\n'))
