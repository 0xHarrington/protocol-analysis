#!/usr/bin/env python
'''
Constants describing user strategy for the Platypus stableswap protocol calculations
'''

import numpy as np

# Number of incremental values to consider between min and max range
N_STEPS = 20

# Minimum and maximum USD you'd consider allocating to Platypus
STABLES_MIN = 10**4
STABLES_MAX = 10**5
stable_deposit_range = np.arange(STABLES_MIN, STABLES_MAX,
                                 (STABLES_MAX - STABLES_MIN) / N_STEPS)


# Allocating some percent of bankroll to market-buying PTP for staking
MIN_BANKROLL_PROPORTION_FOR_PTP = 0.01
MAX_BANKROLL_PROPORTION_FOR_PTP = 0.1
ptp_market_buy_bankroll_proportion = np.arange(MIN_BANKROLL_PROPORTION_FOR_PTP,
                                            MAX_BANKROLL_PROPORTION_FOR_PTP,
                                            MAX_BANKROLL_PROPORTION_FOR_PTP / N_STEPS)

# Assume staking for a day
HOURS_SPENT_STAKING = 24
