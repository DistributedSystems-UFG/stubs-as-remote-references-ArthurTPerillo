import pickle
from client import *
from dbclient import *
from constRPC import *

c2 = Client(PORTC2)
data = c2.recvAny()
dbC2 = pickle.loads(data)
dbC2.appendData('Client 2')
print(dbC2.getValue())
