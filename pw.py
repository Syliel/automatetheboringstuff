#!/usr/bin/env python3
#pw.py - An insecure password locker program

import sys, pyperclip, json

DB = "database.json"

def load_from_db():
    with open(DB, 'r') as f:
        content = f.read()
    return json.loads(content)


def save_db(db):
    with open(DB, 'w') as f:
        f.write(json.dumps(db))


def main():
    passwords = load_from_db()
    if len(sys.argv) <2:
        print('Usage: python pw.py [account] - copy account password')
        sys.exit()

    account = sys.argv[1]   #First command line arg is the account name

    if account in passwords:
        pyperclip.copy(passwords[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
        passwords[account] = input("Please enter password: ")
        save_db(passwords)



if __name__ == '__main__':
    main()
