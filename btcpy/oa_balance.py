""" example to use OA parser """

from openassets import protocol
import bitcoin
import bitcoin.rpc
from bitcoin.core import b2x, lx
#import protocol.MarkerOutput as MO

txid = '9a0466b49bc91007767caf478d9aa8e91ce04c9d0c0aae3023ed0f9bc7e567bb'

proxy = bitcoin.rpc.Proxy()
txid = lx(txid)
txes = proxy.getrawtransaction(txid)

for transaction in txes.vout[:1]:
    mo_payload = protocol.MarkerOutput.parse_script(transaction.scriptPubKey)
    print (b2x(mo_payload))
    marker = protocol.MarkerOutput.deserialize_payload(mo_payload)
    print (marker)

"""
def _get_unspent_outputs(self, address, **kwargs):
    cache = self.cache_factory()
    engine = openassets.protocol.ColoringEngine(self.provider.get_transaction, cache, self.event_loop)

    unspent = yield from self.provider.list_unspent(None if address is None else [str(address)], **kwargs)

    result = []
    for item in unspent:
        output_result = yield from engine.get_output(item['outpoint'].hash, item['outpoint'].n)
        output = openassets.transactions.SpendableOutput(
            bitcoin.core.COutPoint(item['outpoint'].hash, item['outpoint'].n), output_result)
        output.confirmations = item['confirmations']
        result.append(output)

    # Commit new outputs to cache
    yield from cache.commit()
    return result
"""

#if marker_output_payload is not None:
    # Deserialize the payload as a marker output
#    marker_output = MarkerOutput.deserialize_payload(marker_output_payload)
