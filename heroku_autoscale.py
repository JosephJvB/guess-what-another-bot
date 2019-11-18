import os
import sys
import requests

# todo: get formation before patching

def main(state):
    h_key = os.getenv('HEROKU_KEY')
    h = { 'Authorization': f'Bearer {h_key}' }
    q = 1 if state == 'on' else 0
    d = { 'quantity': q }
    u = 'https://api.heroku.com/apps/jvb-spotty-auth/formation/worker'
    res = requests.patch(url=u, json=d, headers=h)
    print(f'AUTOSCALE: {state.upper()} : {res.status_code}')
    return

if __name__ == '__main__':
    if len(sys.argv) == 0:
        raise Exception('Missing "state" argument: ["off", "on"]')
    else:
        main(sys.argv[1])