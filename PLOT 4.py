#SUBJECTS OF THE CROP PRODUCTION OF BRAZIL_SUM_from 2010 to 2020.

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

SUBJECTS = ('Rice', 'Wheat', 'Maize', 'Soybean')
y_pos = np.arange(len(SUBJECTS))
VALUE = [40.319,27.888,60.807,33.993]

plt.bar(y_pos, VALUE, align='center', alpha=0.5)
plt.xticks(y_pos, SUBJECTS)
plt.ylabel('VALUE OF THE CROP PRODUCTION OF BRAZIL')
plt.title('SUBJECTS OF THE CROP PRODUCTION OF BRAZIL_SUM_from 2010 to 2020')

plt.show()