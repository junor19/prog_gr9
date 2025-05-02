import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

import hente_apidata
import variabler

fig, axs = plt.subplots(1,3, figsize=(9,3), sharey=True)

axs[0].bar(seksten)
axs[1].scatter(t_månden)
axs[2].plot(t_dager,seksten)
fig.suptitle('solskinnstimer')