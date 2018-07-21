#Project 2 Ryan Cox ID# 31953949

import socket
from collections import namedtuple

Connection = namedtuple('Connection', ['socket', 'input', 'output'])

##### EXCEPTION #####

class ConnectionProtocolError(Exception):
    pass

##### HOST AND PORT #####

def read_host() -> str:
    while True:
        host = input('Host: ').strip()
        if len(host) == 0:
            print('Specify the host (Name or IP Address)')
        else:
            return host

def read_port() -> int:
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

##### CONNECTION #####

def connect(host: str, port: int) -> Connection:
    ''' takes the host and port and creates a connection '''

    echo_socket = socket.socket()
    echo_socket.connect((host, port))

    echo_socket_input = echo_socket.makefile('r')
    echo_socket_output = echo_socket.makefile('w')

    connection_tuple = Connection(socket = echo_socket, input = echo_socket_input,
                                  output = echo_socket_output)

    return connection_tuple

def AI_connect(connection: Connection) -> str:
    ''' alerts server it wants to start an AI game '''
    _write_line(connection, "AI_GAME")
    response = _read_line(connection)

    if response == 'READY':
        return response
    else:
        raise ConnectionProtocolError()

def login(connection: Connection) -> str:
    ''' gets a username and uses it to establish connection '''
    username = _username()

    _write_line(connection, "I32CFSP_HELLO " + username)

    response = _read_line(connection)

    if response.startswith("WELCOME"):
        return response
    else:
        raise ConnectionProtocolError()

def close_connection(connection: Connection):
    ''' closes the connection if something is wrong '''    
    connection.socket.close()
    connection.input.close()
    connection.output.close()
 
##### AI MOVE and Sending Move to Server #####

def AI_move(connection: Connection) -> list:
    ''' takes the AI move and splits it into the move type and column '''
    response = _read_line(connection)

    return response

def send_move(connection: Connection, move: str) -> str:
    ''' sends move to the server '''
    _write_line(connection, move)
    response = _read_line(connection)

    if response == 'OKAY':
        return response
    elif response.startswith('WINNER'):
        return response
    else:
        raise ConnectionProtocolError()
   
    
###### PRIVATE FUNCTIONS ######

def _username() -> str:
    ''' gets username input from user '''
    while True:
        user = input("Enter your username: ")

        if ' ' in user:
            print("Spaces cannot be in username. Try again")
        else:
            return user
        
def _write_line(connection: Connection, line:str) -> None:
    ''' Writes a line'''
    connection.output.write(line + '\r\n')
    connection.output.flush()

def _read_line(connection: Connection) -> str:
    ''' reads the line back from the AI'''
    return connection.input.readline()[:-1]
    
