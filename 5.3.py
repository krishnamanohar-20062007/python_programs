#5.3 Visualize time-series data and customize axis labels and date formats.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
#simulate time-series data
date_rng=pd.date_range(start='2025-4-01',end='2025-4-15',freq='D')
data=np.random.randn(len(date_rng))

fig,axs=plt.subplots(figsize=(10,6))
axs.plot(date_rng,data,marker='o',linestyle='--',color='blue')
#label axis and use custom date format
axs.set_xlabel("Date")
axs.set_ylabel("Measurment")
axs.set_title("Time series visualization")
axs.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
