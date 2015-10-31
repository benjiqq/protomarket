"""
print transactions and their inputs/outputs
"""

import bitcoin.rpc
import datetime
import binascii
from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160, b2lx

def printtx(txid):
    """ print all outputs of a transaction """
    bitcoinLayer = bitcoin.rpc.Proxy()

    txid = lx(txid)
    txes = bitcoinLayer.getrawtransaction(txid)

    print '*'*20
    print 'outputs of the transaction\n(op_code, data, sop_idx)'
    print '*'*20
    for vo in txes.vout[:]:
        for x in vo.scriptPubKey.raw_iter():
            print x


def printTx():
    i = 381409 # a block with only 1 transaction in it
    #see https://blockchain.info/block-height/381340
    bitcoinLayer = bitcoin.rpc.Proxy()
    h = bitcoinLayer.getblockhash(i)
    block = bitcoinLayer.getblock(h)

    """
    =========
    a block
    =========
    Magic no 	value always 0xD9B4BEF9 	4 bytes
    Blocksize 	number of bytes following up to end of block 	4 bytes
    Blockheader 	consists of 6 items 	80 bytes
    Transaction counter 	positive integer VI = VarInt 	1 - 9 bytes
    transactions 	the (non empty) list of transactions 	<Transaction counter>-many transactions
    """
    #https://en.bitcoin.it/wiki/Block
    for tx in block.vtx[:]:
        #see https://blockchain.info/tx/81500026f314952d74742b1fa738ae4e626adb9a2a0e3a2ea65bf0b4177db378
        txid = b2lx(tx.GetHash())
        print txid
        #https://en.bitcoin.it/wiki/Transaction
        for vi in tx.vin[:]:
            print vi
            """
            the block has only the coinbase as input
            CTxIn(COutPoint(), CScript([x('e1d105'), x('2f416e74506f6f6c2f7363322f384d2f170e920a205634ce24'), CScriptOp(0xc6), x('000006190100')...<ERROR: PUSHDATA(11): truncated data>]), 0xffffffff)

            #on the wire: 01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff2603e1d105192f416e74506f6f6c2f7363322f384d2f170e920a205634ce24c60b000006190100ffffffff0100f90295000000001976a91435df7e6daa60393b0ed2474a21713a845a2212dd88ac00000000
            """

        for vo in tx.vout[:]:
            print vo
            for y in vo.scriptPubKey.raw_iter():
                print y

if __name__=='__main__':
    printTx()
