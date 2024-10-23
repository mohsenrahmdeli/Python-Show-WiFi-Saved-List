import subprocess

command_one = "netsh wlan show profiles"
var = "All Usr Profile"
file_obj = open("req.txt", "w")

a = subprocess.check_output(command_one.split(" ")).decode("utf-8").split('\n')
a = [i for i in a if "All User Profile" in i]

for i in a:
    try:
        t = i.split(':')[1].replace('\n', '')
        t = t.strip()
        
        result = subprocess.check_output(['netsh', 'wlan' , 'show' , 'profiles' , t , 'key=clear']).decode('utf-8').split('\n')
        result = [b for b in result if "Key Content" in b]
        
        end = str(result).split("Key Content")[1].strip()
        
        file_obj.write(t+end+'\n')
        print(t,end)
    except:
        None
file_obj.close()
