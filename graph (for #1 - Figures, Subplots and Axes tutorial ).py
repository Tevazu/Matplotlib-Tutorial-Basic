import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = np.arange(2,11,2)

figure = plt.figure()
axes1 = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = figure.add_axes([0.3, 0.5, 0.2, 0.3])

axes1.plot(y,x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")

axes2.plot(x,y)
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")


plt.show()
