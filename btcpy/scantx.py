#!/usr/bin/env python3
""" simple utility to scan blockchain for an openasset and print out its script """

import bitcoin.rpc
import datetime
import binascii


from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160, b2lx

def bh(x):
    return binascii.hexlify(x)

def datestr(utime):
    dateFormat = '%Y-%m-%d'
    return datetime.datetime.fromtimestamp(int(utime)).strftime(dateFormat)

def printtx():
    proxy = bitcoin.rpc.Proxy()

    txid = lx('9a0466b49bc91007767caf478d9aa8e91ce04c9d0c0aae3023ed0f9bc7e567bb')
    vout = 0

    txin = CMutableTxIn(COutPoint(txid, vout))
    #print txin
    txes = proxy.getrawtransaction(txid)
    print txes.vout
    print '*'*20
    print 'parts of the transaction'
    print '*'*20
    for vo in txes.vout:
        for x in vo.scriptPubKey.raw_iter():
            print x

            #Yields tuples of (opcode, data, sop_idx) so that the different possible
            #PUSHDATA encodings can be accurately distinguished, as well as
            #determining the exact opcode byte indexes. (sop_idx)

            """
            (106, None, 0)
            (18, 'OA\x01\x00\x02\x80\xd6\xa3\xf8\x1b\xe0\x90\x82\xf7\xa4\xeb\x02\x00', 1)
            (118, None, 0)
            (169, None, 1)
            (20, '\x08\xcf7lN\x8e\xd01&}\xf2\xe5\xfax\xdf\xe9XxP\x8b', 2)
            (136, None, 23)
            (172, None, 24)
            (118, None, 0)
            (169, None, 1)
            (20, '4\rx\xfc\x9e\x8b7\x94)\x87\xc3/\xd0\x98\x8b\x907<L\xd1', 2)
            (136, None, 23)
            (172, None, 24)
            (118, None, 0)
            (169, None, 1)
            (20, '4\rx\xfc\x9e\x8b7\x94)\x87\xc3/\xd0\x98\x8b\x907<L\xd1', 2)
            (136, None, 23)
            (172, None, 24)
            """

def scanblock(blocknum):
    proxy = bitcoin.rpc.Proxy()
    print('*** show transaction hashes for a block ***')

    h = proxy.getblockhash(blocknum)
    block = proxy.getblock(h)

    print 'total tx %i'%len(block.vtx)
    print 'transaction hashes'
    for x in block.vtx[:10]:
        txh = b2lx(x.GetHash())
        print txh

if __name__=='__main__':
    printtx()
    #scanblock(380550)
