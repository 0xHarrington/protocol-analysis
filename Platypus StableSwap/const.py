#!/usr/bin/env python
'''
Constants used for the Platypus stableswap protocol calculations that are independent of the user.
'''


# protocol-level constants
MAX_SUPPLY = 3 * 10**8                # 300,000,000
LIQUIDITY_MINING_ALLOCATION = 0.4     # 40% of above

BASE_POOL_ALLOCATION = .3
BOOSTING_POOL_ALLOCATION = .5
AVAX_PTP_POOL = .2

HOURLY_STAKED_PTP_vePTP_YIELD = 0.014

# market-level constants

CIRCULATING_MARKET_CAP = 10 ** 7      # assume 10MM MC for now
TVL_TO_CMC_RATIO = 5                  # TVL 5x the size of token CMC (curve's TVL is >12x)
TVL = TVL_TO_CMC_RATIO * CIRCULATING_MARKET_CAP

PERCENT_COINS_CIRCULATING = .035 + .035 + LIQUIDITY_MINING_ALLOCATION
PTP_PRICE = CIRCULATING_MARKET_CAP / (MAX_SUPPLY * PERCENT_COINS_CIRCULATING)
FDMC = PTP_PRICE * MAX_SUPPLY

PERCENT_PTP_STAKED = .4
GLOBAL_PTP_STAKED = MAX_SUPPLY * PERCENT_COINS_CIRCULATING * PERCENT_PTP_STAKED
