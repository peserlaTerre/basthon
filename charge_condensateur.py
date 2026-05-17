import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ─────────────────────────────────────────────
#  VOS MESURES  (t en secondes, uC en volts)
# ─────────────────────────────────────────────
t  = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])   # ← modifiez ici
uC = np.array([0, 3.16, 5.18, 6.32, 7.04, 7.47, 7.73, 7.89, 7.98, 8.03, 8.06])   # ← modifiez ici

# ─────────────────────────────────────────────
#  MODÉLISATION  uC(t) = E · (1 − exp(−t/τ))
# ─────────────────────────────────────────────
def modele(t, E, tau):
    return E * (1 - np.exp(-t / tau))

popt, _ = curve_fit(modele, t, uC, p0=[max(uC)*1.1, t[-1]/5])
E, tau = popt

print(f"uC(t) = {E:.3f} × (1 − exp(−t / {tau:.3f}))")
print(f"  E = {E:.3f} V    τ = {tau:.3f} s")

# ─────────────────────────────────────────────
#  TRACÉ
# ─────────────────────────────────────────────
t_plot = np.linspace(0, max(t) * 1.1, 500)

plt.figure(figsize=(8, 5))
plt.scatter(t, uC, color="crimson", zorder=5, label="Mesures")
plt.plot(t_plot, modele(t_plot, E, tau), color="steelblue", linewidth=2,
         label=f"Modèle : {E:.3f}·(1−exp(−t/{tau:.3f}))")
plt.xlabel("t (s)")
plt.ylabel("uC (V)")
plt.title("Charge d'un condensateur — uC = f(t)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
