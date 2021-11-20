#!/usr/bin/env python
'''
Calculating the emissions from deposits in Platypus stable accounts
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, EngFormatter, PercentFormatter
from strategy_const import *
from const import *


def boosted_pool_emission_rate(your_stable_deposit, vePTP_held, other_deposit_weights):
    ''' proportion of boosted pool emissions your deposits and vePTP earn
    '''
    your_boosted_pool_weight = np.sqrt(your_stable_deposit * vePTP_held)
    return your_boosted_pool_weight / other_deposit_weights


def base_pool_emission_rate(your_stable_deposit, other_stable_deposits):
    ''' proportion of base pool emissions your deposits earn
    '''
    total_deposits = other_stable_deposits + your_stable_deposit
    return your_stable_deposit / total_deposits


# define function with vectorize decorator for extensibility
@np.vectorize
def total_emissions_rate(stable_bankroll,
                         ptp_marketbuy_proportion):
    '''
    :stable_bankroll:             total USD value of the stables you'd invest in the Platypus protocol
    :ptp_marketbuy_proportion:    proportion of stable_bankroll you'd use to marketbuy PTP for staking to vePTP

    returns the number of PTP tokens you'd rececive given defined constants earlier in the notebook.
    '''
    n_PTP = (stable_bankroll * ptp_marketbuy_proportion) / PTP_PRICE
    n_vePTP = HOURS_SPENT_STAKING * HOURLY_STAKED_PTP_vePTP_YIELD * n_PTP
    stable_deposit = stable_bankroll * (1 - ptp_marketbuy_proportion)

    # calculating lower bound on total deposit weights:
    #     assume all other deposits are from one wallet with all other staked PTP
    #     and it's been staking as long as you have
    total_deposit_weights = GLOBAL_PTP_STAKED * HOURLY_STAKED_PTP_vePTP_YIELD * HOURS_SPENT_STAKING

    boosted = boosted_pool_emission_rate(stable_deposit, n_vePTP, total_deposit_weights)
    base = base_pool_emission_rate(stable_deposit, TVL - stable_deposit)

    return (BOOSTING_POOL_ALLOCATION * boosted) + (BASE_POOL_ALLOCATION * base)


def plot_2d_returns(stable_bankroll, ptp_proportion, returns_array, as_percents = True):
    """Use matplotlib to plot the slope of returns across different bankroll strategies
    """

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(18,9))
    manifold = ax.plot_surface(stable_bankroll, ptp_proportion, returns_array,
            cmap=cm.plasma, linewidth=0.5, antialiased=False)

    # labels, titles, and axes
    ax.set_title(f"Monthly Strategy Emissions given PTP staking for {round(HOURS_SPENT_STAKING / 24)} Days")
    ax.xaxis.set_major_formatter(EngFormatter(unit="$", places=1, sep="\N{THIN SPACE}"))
    ax.set_xlabel("Strategy Bankroll")
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=1))
    ax.set_ylabel("Percent Market-Bought and Staked")
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.zaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=4))
    ax.set_zlabel("Percent of Emissions for Strategy")

    # colorbar for scale
    fig.colorbar(manifold, shrink=0.5, aspect=5, format=PercentFormatter(xmax=1, decimals=4))

    plt.show()


def main():
    print(f"Emissions calculations consider PTP/USD: ${round(PTP_PRICE, 3)}\n" +
              f"Reflecting a FDMC of \t${round(FDMC / 10**6)}MM " +
              f"({round(PERCENT_COINS_CIRCULATING * 100)}% of coins available)\n" +
              f"and implying TVL of \t${round(TVL / 10**6)}MM " +
              f"(Mcap/TVL: {round(1 / TVL_TO_CMC_RATIO, 4)})\n" +
              f"with {round(GLOBAL_PTP_STAKED / 10**6, 2)}MM PTP staked for vePTP ({round(PERCENT_PTP_STAKED * 100)}%)")

    # Create the mesh and calculate return rates
    stable_bankroll, ptp_proportion = np.meshgrid(stable_deposit_range, ptp_market_buy_bankroll_proportion)
    returns = total_emissions_rate(stable_bankroll, ptp_proportion)

    # plotting time
    plot_2d_returns(stable_bankroll, ptp_proportion, returns)


if __name__ == '__main__':
    main()
