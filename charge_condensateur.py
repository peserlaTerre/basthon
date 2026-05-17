import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ─────────────────────────────────────────────
#  VOS MESURES  (t en secondes, uC en volts)
# ─────────────────────────────────────────────
t  = np.array([...])   # ← modifiez ici
uC = np.array([...])   # ← modifiez ici

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
