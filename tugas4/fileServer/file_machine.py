from file import File
import json
import logging

class FileMachine:
    def proses(self, string_to_process, buff):
        f = File()
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("Upload file from client")
                file_name = cstring[1].strip()
                logging.warning(file_name)
                logging.warning(buff)
                f.create_data(file_name, buff)
                return json.dumps("File uploaded")

            elif (command=='list'):
                logging.warning("Get list of file in server")
                hasil = f.list_data()
                logging.warning(hasil)
                return json.dumps(hasil)

            elif (command=='download'):
                logging.warning("Download file from server")
                file_name = cstring[1].strip()
                hasil = f.get_data(file_name, buff)
                return json.dumps(hasil)
            else:
                return "Command not found"
        except:
            return "Error"