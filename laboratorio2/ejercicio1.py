# Gráficas log(n), (log(n)))^2, log(log(n)), n^3 + log(n)^3
# Librerías
import numpy as np
import matplotlib.pyplot as plt
# Datos
n = np.arange(1, 100)
log_n = np.log(n)
log_log_n = np.log(log_n)
log_log_log_n = np.log(log_log_n)
n_3 = n**3
log_n_3 = np.log(n_3)
log_log_n_3 = np.log(log_n_3)
# Gráficas
# log(n)
plt.plot(n, log_n, label='log(n)')
plt.legend()
plt.show()
# (log(n))^2
plt.plot(n, log_log_n, label='(log(n))^2')
plt.legend()
plt.show()
# log(log(n))
plt.plot(n, log_log_log_n, label='log(log(n))')
plt.legend()
plt.show()
# n^3 + log(n)^3
plt.plot(n, n_3, label='n^3 + log(n)^3')
plt.legend()
plt.show()

