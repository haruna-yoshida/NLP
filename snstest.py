import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # cf. https://www.reddit.com/r/learnpython/comments/5oscmr/why_is_seaborn_commonly_imported_as_sns/

Z = np.random.random(1000)

sns.distplot(Z, kde=False)  # kdf stands for Kernel Density Estimation, which is disabled here.
plt.show()