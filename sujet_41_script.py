import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

'''---------------- VOS MESURES ----------------'''
t  = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])  # temps (s)
uc = np.array([])  # tension (V) - saisir ici les valeurs mesurées

'''---------------- (ne pas modifier) ----------'''
def _modele(t, E, tau): return E * (1 - np.exp(-t / tau))
(E, tau), _ = curve_fit(_modele, t, uc, p0=[uc[-1], 40])
t_mod = np.linspace(0, t.max(), 500)

fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(t, uc, '+k', markersize=10, markeredgewidth=2, label='Mesures', zorder=4)
ax.plot(t_mod, _modele(t_mod, E, tau), 'r-', linewidth=2, label=r'Modélisation de $u_c(t)$', zorder=3)
ax.axhline(E, color='blue', label='Tension du générateur', zorder=2)
t_tan = np.linspace(0, 1.3 * tau, 100)
ax.plot(t_tan, (E / tau) * t_tan, 'g-', label="Tangente à l'origine", zorder=3)

xp, yp = 0.08 * t.max(), 0.18 * E
xl, xr = -xp, t.max() + xp
yb, yt = -0.08 * E, E + yp
ax.set_xlim(xl, xr); ax.set_ylim(yb, yt)
for sp in ax.spines.values(): sp.set_visible(False)
ax.annotate('', xy=(xr, 0), xytext=(xl, 0), arrowprops=dict(arrowstyle='->', linewidth=1.5), clip_on=False, zorder=10)
ax.annotate('', xy=(0, yt), xytext=(0, yb), arrowprops=dict(arrowstyle='->', linewidth=1.5), clip_on=False, zorder=10)
ax.set_xticks([]); ax.set_yticks([])
for x in np.arange(0, 150, 20):
    if x: ax.plot([x,x],[0,.3],'k',lw=1.5,zorder=10); ax.text(x,-.2,str(x),ha='center',va='top',fontsize=10)
    if x and x<=t.max(): ax.plot([x,x],[0,yt],'lightgray',lw=.5,zorder=1)
for y in np.arange(0, 14, 2):
    if y: ax.plot([0,2],[y,y],'k',lw=1.5,zorder=10); ax.text(-1.5,y,str(y),ha='right',va='center',fontsize=10)
    if y and y<=E: ax.plot([0,xr],[y,y],'lightgray',lw=.5,zorder=1)
ax.annotate('0',  xy=(0,0),  xytext=(-6,-6),  textcoords='offset points', ha='right',  va='top',    fontsize=10)
ax.annotate(r'$t$ (s)',    xy=(xr,0), xytext=(5,-10),  textcoords='offset points', ha='center', va='top',    fontsize=12)
ax.annotate(r'$u_c$ (V)', xy=(0,yt),  xytext=(-30,5), textcoords='offset points', ha='left',   va='bottom', fontsize=12)
ax.set_title('Évolution de la tension aux bornes du condensateur au cours du temps')
ax.legend(loc='lower right', bbox_to_anchor=(0.95, 0.32))
plt.show()
