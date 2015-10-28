## Protomarket

a prototype for a marketplace

This is an early proof of concept for a global market place
based on Colored Coins, [https://github.com/OpenAssets/](Openassets) and the Lykke exchange concept, see ([Lykke Colored Coin Exchange White Paper](https://wiki.lykkex.com/colored_coin_exchange_white_paper)).

## Simplified market model

we use a very simple model of a market

* the market consists of two assets: Bitcoin and LykkeCoin, and therefore on trading pair: LKK/BTC

* clients submit requests to the server to buy or sell LKK against BTC

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

MIT License
