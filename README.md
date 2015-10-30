## Protomarket

This is an early proof of concept for the Lykke exchange marketplace, see ([Lykke Colored Coin Exchange White Paper](https://wiki.lykkex.com/colored_coin_exchange_white_paper)), based
based on Colored Coins [https://github.com/OpenAssets/](Openassets).

## Building

Install

* [https://github.com/bitcoin/bitcoin](bitcoin core)  
* [https://github.com/benjyz/python-bitcoinlib](python-bitcoin)
* [https://github.com/OpenAssets/openassets](openassets)

Try the examples in transaction_layer/examples

## Simplified market model

We develop a very simplified auction protocol so to focus on a Bitcoin <> Colored Coin swap

* we introduce a ColoredCoin for testing purposes: ProtomarketCoin (PMC)

* the market consists of two assets: Bitcoin and ProtomarketCoin, and therefore one trading pair: PMC/BTC

* clients submit requests to the server to buy or sell PMC against BTC

* the quantity of the request is fixed to 10 units

* the price has only 10 possible values: [1, ..., 10]

* if all price-slots are taken, the client receives a message to wait

## References

* Lykke Colored Coin Exchange White Paper: https://wiki.lykkex.com/colored_coin_exchange_white_paper
* Openassets protocol: https://github.com/OpenAssets/open-assets-protocol
* Colored Coins Meni Rosenfeld (2012): https://bitcoil.co.il/BitcoinX.pdf
* Ethereum Whitepaper (2013): http://vitalik.ca/ethereum.html and updated version https://github.com/ethereum/wiki/wiki/White-Paper
* Nxt Whitepaper (2014): https://wiki.nxtcrypto.org/wiki/Whitepaper:Nxt
* NuBits (September, 2014): https://nubits.com/sites/default/files/a...014-en.pdf
* Counterparty (2013): http://counterparty.io/docs/
* MasterCoin (2013): https://github.com/OmniLayer/spec
* Ripple, original papers by Ryan Fugger: http://archive.ripple-project.org/paymentrouting.pdf, http://archive.ripple-project.org/decentralizedcurrency.pdf

## License

MIT License, see https://opensource.org/licenses/MIT
