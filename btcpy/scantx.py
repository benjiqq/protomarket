#!/usr/bin/env python3
""" utiliies to scan blockchain for openasset tx
see https://github.com/OpenAssets/open-assets-protocol"""

import bitcoin.rpc
import datetime
import binascii

from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160, b2lx

import datetime

def datestr(utime):
    dateFormat = '%Y-%m-%d'
    return datetime.datetime.fromtimestamp(int(utime)).strftime(dateFormat)

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
    for vo in txes.vout[:]:
        for x in vo.scriptPubKey.raw_iter():
            print x

            """
            # example tx with op_return
            #tuples of (opcode, data, sop_idx) so that the different possible
            #PUSHDATA encodings can be accurately distinguished, as well as
            #determining the exact opcode byte indexes. (sop_idx)

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

def printallTx(tx):
    for vo in tx.vout[:]:
        for y in vo.scriptPubKey.raw_iter():
            print y

def printTxOPR(tx):
    for vo in tx.vout[:]:
        for y in vo.scriptPubKey.raw_iter():
            op, data, _ = y
            if op == 18:
                print y

def hasOPR(tx):
    """ check whether tx has op_return """
    for vo in tx.vout[:]:
        got_OPRETURN = False
        for y in vo.scriptPubKey.raw_iter():
            op = y[0]
            if op==18:
                got_OPRETURN = True
                return True


def printblock(blocknum,f=None):
    proxy = bitcoin.rpc.Proxy()

    h = proxy.getblockhash(blocknum)
    block = proxy.getblock(h)

    for tx in block.vtx[:]:
        if hasOPR(tx):
            txid = b2lx(tx.GetHash())
            print txid
            printallTx(tx)

            #printallTx(tx)

def scanblock(blocknum,f=None):
    """ scan all tx in a block for op_return """
    proxy = bitcoin.rpc.Proxy()

    h = proxy.getblockhash(blocknum)
    block = proxy.getblock(h)

    num_opr = 0
    for tx in block.vtx[:]:

        if hasOPR(tx):
            txid = b2lx(tx.GetHash())
            printTxOPR(tx)
            num_opr +=1

    if num_opr > 0:
        s = '%i  %s  total tx: %i  num opr %i'%(blocknum, datestr(block.nTime), len(block.vtx),num_opr)
        print s
        if f: f.write(s + '\n')
    else:
        print blocknum
    #print 'total opr',num_opr

def scanall():
    """ scan blockain for op_return """
    start = 380051 #265459
    for bl in range(start,380551):
        try:
            scanblock(bl,f)
        except:
            print 'failure scanning block'
    f.close()

if __name__=='__main__':
    block = 380550
    #printblock(block)
    scanblock(block)
