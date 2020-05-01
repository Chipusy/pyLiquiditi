# pyLiquiditi
Python lib for working with <a href="https://liquiditi.io">Liquiditi.io</a> API

## Install:
- Clone this repo to your local machine using `https://github.com/Chipusy/pyLiquiditi`
## Usage:
```python
from Liquiditi import API

api = API(token='**********************************')

# currencies list and balances
api.currency_list()

# retrieve order
api.order_get(order_id='*************')

# order list by status (optional)
api.order_list(status='expired')

# order creating
api.order_create(
    from_currency='btc',
    to_currency='lbtc',
    address = 'VJLJ5pYxVs9exe7zxq1MNbBeq7ZC1kGWT9psRQUD3k1f2Wdk9bffSKgVxbMhvtnGH4adscaRCRW1nGN6')
)

````
## Documentation
- <a href="https://api.liquiditi.io/v1/docs/">Liquiditi.io API Documentation</a>
