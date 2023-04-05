import os
import json
pylint = os.popen('pylint app.py').read()
res_code = float(pylint.split('\n')[-3].split()[6].split('/')[0])

if res_code < 8:
    print('Error code')
print('\n\nNew comment!!!\n\n')
os.system('bandit -iii -lll -q -r ./skachki/ -o bandit.json -f json')
with open('bandit.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
if res['results']:
    raise RuntimeError('Error security')
