from file import File
import json
import logging

f = File()
class FileMachine:
    def proses(self, string_to_process, buff):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                file_name = cstring[1].strip()
                print(f"Client request upload {file_name}")
                f.create_data(file_name, buff)
                return "Upload success"

            elif (command=='download'):
                file_name = cstring[1].strip()
                print(f"Client request download {file_name}")
                hasil = f.get_data(file_name, buff)
                if hasil:
                    return "Download success"

            elif (command=='list'):
                res = f.list_data()
                print("Client request file list")
                return json.dumps(res)

            else:
                return "Command not found"
        except:
            return "Error"