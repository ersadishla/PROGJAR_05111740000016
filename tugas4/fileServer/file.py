import shelve
import uuid
from datetime import datetime
import os


class File:
    def __init__(self):
        self.data = shelve.open('db/file.dat')

    def is_exist(self,fileName=None):
        timestamp = datetime.now()
        for i in self.data.keys():
            if(self.data[i]['fileName'].lower()==fileName.lower()):
                temp = self.data[i]
                temp['lastModified'] = timestamp
                self.data[i] = temp
                return True
        return False

    def create_data(self,fileName=None,buff=None):
        if (fileName is None or buff is None):
            return False

        timestamp = datetime.now()

        get_size = buff.recv(4)
        file_size = int.from_bytes(get_size,byteorder='big')

        with open(fileName, 'wb+') as file_recv:
            recv_size = 0
            while recv_size < file_size:
                byte_n = buff.recv(32)
                recv_size += len(byte_n)
                if not byte_n:
                    break
                file_recv.write(byte_n)
        file_recv.close()

        duplicate = False
        for i in self.data.keys():
            try:    
                if(self.data[i]['fileName'].lower()==fileName.lower()):
                    temp = self.data[i]
                    temp['lastModified'] = str(timestamp)
                    self.data[i] = temp
                    duplicate = True
            except:
                duplicate = False
        if not duplicate:
            id=str(uuid.uuid4())
            data = dict(id=id,fileName=fileName,lastModified=str(timestamp))
            self.data[id]=data
        return True
        
    def get_data(self,fileName=None,buff=None):
        if (fileName is None or buff is None):
            return False

        for i in self.data.keys():
            if (self.data[i]['fileName'].lower()==fileName.lower()):
                size = os.path.getsize(fileName)
                val = size.to_bytes(4,byteorder='big')
                buff.send(val)
                with open(fileName, 'rb') as file_to_send:
                    for byte in file_to_send:
                        buff.sendall(byte)
                file_to_send.close()
                return "File Downloaded"

        size = 0
        val = size.to_bytes(4,byteorder='big')
        buff.send(val)
        return "No Such File"
    
    def list_data(self):
        k = [{'fileName':self.data[i]['fileName'],'lastModified':self.data[i]['lastModified']} for i in self.data.keys()]
        return k

if __name__ == "__main__":
    f = File()
    print(f.list_data())
