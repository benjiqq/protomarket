#!/usr/bin/env python3
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
    i = 380550 #last block as of 2015-10-27
    print('*** Bitcoin numtx ***')

    h = proxy.getblockhash(i)
    #print bh(h)
    block = proxy.getblock(h)
    #print dir(block)

    #print('%s %s'%(datestr(block.nTime),len(block.vtx)))
    print ('total tx %i',len(block.vtx))
    for x in block.vtx[:]:
        #print x
        #print dir(x)
        txh = b2lx(x.GetHash())
        #print txh
        #print txh[:2]
        if txh[:2] == '9a':
            print txh
            #print dir(txh)


    txid = lx('9a0466b49bc91007767caf478d9aa8e91ce04c9d0c0aae3023ed0f9bc7e567bb')
    vout = 0

    # Create the txin structure, which includes the outpoint. The scriptSig
    # defaults to being empty.
    txin = CMutableTxIn(COutPoint(txid, vout))
    print txin

    #if not block.vtx[0].is_coinbase():

if __name__=='__main__':
    printtx()


"""
{
  "hex": "010000000254f82806406ecd282859d2ac87acdc9f5b02ab30f2bd41d412d828cdb5e5cd25020000006a473044022044beec554d32dd28d8d42536a725987da450d2109935c95e9dddd12b7ef8e3d402204ef6cbbfb633574a392c526cad01f63d07943954fb6a0f26afbaf4be66bac346012102867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246ffffffff54f82806406ecd282859d2ac87acdc9f5b02ab30f2bd41d412d828cdb5e5cd25030000006a47304402201b57f3e927804f22e115420221dd6ab9aafdd59246c4ceaf0f7a34a763039bc602200dd30d99510d6fdc63b05d95d00a628c425f53c8dd11f81b536c226780e8d6ca012102867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246ffffffff040000000000000000146a124f4101000280d6a3f81be09082f7a4eb020058020000000000001976a91408cf376c4e8ed031267df2e5fa78dfe95878508b88ac58020000000000001976a914340d78fc9e8b37942987c32fd0988b90373c4cd188ace0c36000000000001976a914340d78fc9e8b37942987c32fd0988b90373c4cd188ac00000000",
  "txid": "9a0466b49bc91007767caf478d9aa8e91ce04c9d0c0aae3023ed0f9bc7e567bb",
  "version": 1,
  "locktime": 0,
  "vin": [
    {
      "txid": "25cde5b5cd28d812d441bdf230ab025b9fdcac87acd2592828cd6e400628f854",
      "vout": 2,
      "scriptSig": {
        "asm": "3044022044beec554d32dd28d8d42536a725987da450d2109935c95e9dddd12b7ef8e3d402204ef6cbbfb633574a392c526cad01f63d07943954fb6a0f26afbaf4be66bac346[ALL] 02867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246",
        "hex": "473044022044beec554d32dd28d8d42536a725987da450d2109935c95e9dddd12b7ef8e3d402204ef6cbbfb633574a392c526cad01f63d07943954fb6a0f26afbaf4be66bac346012102867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246"
      },
      "sequence": 4294967295
    },
    {
      "txid": "25cde5b5cd28d812d441bdf230ab025b9fdcac87acd2592828cd6e400628f854",
      "vout": 3,
      "scriptSig": {
        "asm": "304402201b57f3e927804f22e115420221dd6ab9aafdd59246c4ceaf0f7a34a763039bc602200dd30d99510d6fdc63b05d95d00a628c425f53c8dd11f81b536c226780e8d6ca[ALL] 02867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246",
        "hex": "47304402201b57f3e927804f22e115420221dd6ab9aafdd59246c4ceaf0f7a34a763039bc602200dd30d99510d6fdc63b05d95d00a628c425f53c8dd11f81b536c226780e8d6ca012102867aadf0f5afd4b0e8effd40ad76c457a8437487d4a4567d8856189720b3f246"
      },
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 0.00000000,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_RETURN 4f4101000280d6a3f81be09082f7a4eb0200",
        "hex": "6a124f4101000280d6a3f81be09082f7a4eb0200",
        "type": "nulldata"
      }
    },
    {
      "value": 0.00000600,
      "n": 1,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 08cf376c4e8ed031267df2e5fa78dfe95878508b OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a91408cf376c4e8ed031267df2e5fa78dfe95878508b88ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "1oaeByY42fXh4rYTZPwYDAB2tKFBAoTth"
        ]
      }
    },
    {
      "value": 0.00000600,
      "n": 2,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 340d78fc9e8b37942987c32fd0988b90373c4cd1 OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a914340d78fc9e8b37942987c32fd0988b90373c4cd188ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "15kEH4xJm3WFDkDpvGehcekV37f8HCJXND"
        ]
      }
    },
    {
      "value": 0.06341600,
      "n": 3,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 340d78fc9e8b37942987c32fd0988b90373c4cd1 OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a914340d78fc9e8b37942987c32fd0988b90373c4cd188ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "15kEH4xJm3WFDkDpvGehcekV37f8HCJXND"
        ]
      }
    }
  ],
  "blockhash": "00000000000000000a673154b1358967caa59767d0290a4b5040ccf22b9a3238",
  "confirmations": 426,
  "time": 1445816034,
  "blocktime": 1445816034
}
"""
