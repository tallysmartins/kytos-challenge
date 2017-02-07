#!python

import sys
import struct

from enum import Enum 


######################### Message Classes ########################

class Type(Enum):
    OPFT_HELLO = 0
    OPFT_ERROR = 1
    OPFT_ECHOREQUEST = 2
    OPFT_ECHOREPLY = 3
    OPFT_VENDOR = 4


class Message():
    """Base OpenFlow Message Class

    Every message contains a Header, this
    is the basic Message where all other
    messages inherit from.
    """
    _version = None
    _type = None
    _size = None
    _xid = None
    _raw = None
    _body = None 

    def __init__(self, msg):
        """Constructor

        Args:
            msg(binary string): The raw message in binary format
            (e.g.: '\x00\x01\x00\x02\x00\x00\x00\x03'
        """
        self._raw = msg
        self.parse_header()
        self.parse_body()

    def parse_header(self):
        """Extract the header from the raw message"""
        msg_content = struct.unpack('bbhI', self._raw)
        self._version = msg_content[0]  
        self._type = msg_content[1]
        self._size = msg_content[2]
        self._xid = msg_content[3]

    def parse_body(self):
        """Extract the body from the raw message, each kind of message must
        implement this method
        """
        self._body = None

    def __str__(self):
        return """
            Protocol Version: {}\n
            Message Type: {}\n
            Size: {}(bytes)\n
            xid: {}\n
            Is valid: {}\n
            Body: {}
            """.format(
                hex(self._version), hex(self._type), 
                hex(self._size), hex(self._xid), self.is_valid(),
                self._body)
        

    def is_valid(self):
        """ Check wheter the message bytes match the kind of message being
        processed""" 
        return True


class Hello(Message):
    def __init__(self, msg):
        super().__init__(msg)

    def is_valid(self):
        return hex(self._size) == '0x800'


######################### Parser ########################
def get_msg_type(data):
    msg_type = data[1]
    return Type(msg_type)

def parse():
    try:
        data = open(sys.argv[1], 'rb').read()
    except FileNotFoundError:
        print("Could not find file `%s`" % sys.argv[1])
        exit()

    msg_type = get_msg_type(data)

    msg = None
    if(msg_type.name == 'OPFT_HELLO'):
        msg = Hello(data)
    else:
        msg = msg_type.name + " : Type not supported"

    print("="*60)
    print(msg)
    print("="*60)

def verify_args():
    if(len(sys.argv) != 2):
        print(
        """
        To use the OpenFlow Parser you must specify the file
        containing the message data, as shown below:

        $ python openflow_parser.py <message-file.dat>
        """)
        exit()

if __name__ == "__main__":
    verify_args()
    parse()
    
