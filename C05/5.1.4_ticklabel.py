import matplotlib.pyplot as plt
import numpy as np

from calendar import month_name,day_name
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()

ax = fig.add_axes([0.2,0.2,0.7,0.7])

x = np.arange(1,8,1)
y = 2*x

ax.plot(x,y,ls="-",lw=2,color="orange",marker="o",ms=20,mfc="c",mec="c")

# RMB ticklabel
ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))
# dayName ticklabel
plt.xticks(x, day_name[0:7],rotation=20)

ax.set_xlim(0, 8)
ax.set_ylim(0, 18)

plt.show()
