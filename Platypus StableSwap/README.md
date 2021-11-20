# Platypus Finance
### StableSwap protocol on Avalanche

----

Graphing Emissions given bankroll and PTP staked. Generate an interactive 3D plot with matplotlib using `emissions_rate.py`.

```bash
git clone https://github.com/MattAHarrington/protocol-analysis.git
pip install -r requirements.txt
cd Platypus\ StableSwap
python emissions_rate.py
```

Change your strategy parameters using `strategy_const.py`, or vary the assumptions about the market using `const.py`.

```bash
code strategy_const.py const.py
```

You can also use the jupyter notebook for easier interaction.

```bash
jupyter notebook PlatypusFinance.ipynb
```
