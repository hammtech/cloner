import re # pour utiliser la fonction regex
from pprint import pprint

import json
from typing import Dict, Tuple, Any

ip_count = {}
data = {}

with open("./access.log", "r") as f: # ouvrir le fichier .log en mode "read" en le nommant f.
        log = f.readlines() # lire chaque ligne dans f
        for l in log: # boucle for
                regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[\w.+] \".+\" (\d{1,3}) '
                ip, status = re.findall(regex, l)[0]

                if ip not in ip_count:
                        ip_count[ip] = {}

                if status in ip_count[ip]:
                        ip_count[ip][status] += 1
                else:
                        ip_count[ip][status] = 1

        with open("ip_status.json", "w") as file:
                json.dump(ip_count, file, indent=2)





