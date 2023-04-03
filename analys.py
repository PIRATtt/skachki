import os
import json
pylint = os.popen("""
sudo pylint app.py  --const-rgx='[a-z\_][a-z0-9\_]{2,30}$'
""").read()
result_code=float(pylint.split('\n')[-3].split()[6].split('/')[0])
if result_code < 5.5:
    print("Error code!")

os.system('sudo bandit -iii -lll -q -r ./skachki/ -o bandit.json -f json')
with open('bandit.json', 'r', encoding="utf-8") as f:
    res = json.load(f)
if res['results']:
    raise RuntimeError('Error security!')
