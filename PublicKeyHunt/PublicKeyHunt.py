"""
Usage :
 > python PublicKeyHunt.py 
 
@author: ccinet
P2PKH,P2SH
"""
from bitcoinlib.services.services import Service
import argparse
import sys

def HuntPKey(oService, cPAddress):
    oTransactions=oService.gettransactions(cPAddress)
    for tx in oTransactions:
        for oInputs in tx.inputs:#tx.outputs:
            if oInputs.address == cPAddress:
                for oPKey in oInputs.keys:
                    if oPKey.public_hex:
                        return oPKey.public_hex

def main():

    parser = argparse.ArgumentParser(description='Found Public Key of the Public Address')
    parser.add_argument('sPAddress', type=str, nargs='?', default=1,
                        help='A required Public Address argument')
    
    if len(sys.argv)==1:
        parser.print_help()
        return
    args = parser.parse_args()

    service = Service()
    sPkey=HuntPKey(service, args.sPAddress)
    if sPkey:
        print("Public Key of the Public Address: ",args.sPAddress," :: ",sPkey)
    else:
        print("Not Public Key found of Public Address: ",args.sPAddress)

if __name__ == "__main__":
    main()

# For Donation: 1DvdiYvRr7pzHsYRJiXYdroQNZUqKxLAzf        