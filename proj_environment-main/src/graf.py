import matplotlib.pyplot as plt
import numpy as np

import hente_apidata
import variabler

#fig, axs = plt.subplots(1,3, figsize=(9,3), sharey=True)


#axs[2].plot(t_dager,seksten)
#fig.suptitle('solskinnstimer')

#ypoints = np.array(['t_månder', 'seksten'])

xpoints = np.array(['seksten'])
ypoints = np.array(['t_månder'])

plt.plot(ypoints, color = 'r')
plt.show()