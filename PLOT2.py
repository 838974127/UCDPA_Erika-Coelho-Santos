#CROP PRODUCTION OF AUSTRALIA_SUM_FROM 2010 TO 2020_per_Tonne_Ha.

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

SUBJECTS = ('Rice', 'Wheat', 'Maize', 'Soybean')

y_pos = np.arange(len(SUBJECTS))
VALUE = [115.119, 21.644, 76.734, 17.841]

plt.bar(y_pos, VALUE, align='center', alpha=0.5)
plt.xticks(y_pos, SUBJECTS)
plt.ylabel('VALUE OF THE CROP PRODUCTION_TONNE_HA')
plt.title('SUBJECTS OF THE CROP PRODUCTION OF AUSTRALIA_ SUM_FROM 2010 TO 2020')

plt.show()
