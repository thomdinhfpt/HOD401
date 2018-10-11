import socket
import sys
import requests

if __name__ == '__main__':
    domain = input("Enter a domain: ")
    subdomain = []

    with open("dictionary.txt") as subs: 
        for line in subs:
            subdomain.append(line.strip())
    for sub in subdomain:
        result = sub + "." + domain
        try:
            addr = socket.gethostbyname(result)
            print(result + "\n")
        except:
            pass