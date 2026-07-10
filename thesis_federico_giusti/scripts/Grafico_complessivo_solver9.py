import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# === DATI (aggiornati) ===
data = {
    "TEXT GENERATION": [
        ("BASELINE", 1575.0, 13.0),
        ("RANDOM", 1153.337, 17.4),
        ("NAIVE CARBON", 1108.345, 18.0),
        ("NAIVE ERROR (BASE 1)", 1383.335, 15.0),
        ("NAIVE ERROR (BASE 2)", 1148.339, 17.4857),
        ("NAIVE ERROR (BASE 3)", 1176.671, 17.1714),
        ("NAIVE SHIFT", 1140.0, 13.0),
        ("CARBONSHIFT (BASE 1)", 994.167, 15.0),
        ("CARBONSHIFT (BASE 2)", 776.667, 18.0),
        ("CARBONSHIFT (BASE 3)", 637.777, 20.0),
    ],
    "NAMED ENTITY RECOGNITION": [
        ("BASELINE", 291.655, 3.0),
        ("RANDOM", 276.661, 6.5429),
        ("NAIVE CARBON", 291.655, 8.0),  # aggiornato
        ("NAIVE ERROR (BASE 1)", 291.655, 3.1429),
        ("NAIVE ERROR (BASE 2)", 279.993, 5.9143),
        ("NAIVE ERROR (BASE 3)", 278.327, 6.5143),
        ("NAIVE SHIFT", 213.198, 3.0),
        ("CARBONSHIFT (BASE 1)", 213.198, 3.0),
        ("CARBONSHIFT (BASE 2)", 177.224, 7.9714),
        ("CARBONSHIFT (BASE 3)", 170.552, 9.0),
    ],
    "QUESTION ANSWERING": [
        ("BASELINE", 758.345, 7.0),
        ("RANDOM", 436.671, 9.4857),
        ("NAIVE CARBON", 350.0, 8.0),
        ("NAIVE ERROR (BASE 1)", 741.678, 7.1714),
        ("NAIVE ERROR (BASE 2)", 628.342, 7.9714),
        ("NAIVE ERROR (BASE 3)", 458.338, 9.1714),
        ("NAIVE SHIFT", 541.660, 7.0),
        ("CARBONSHIFT (BASE 1)", 541.660, 7.0),
        ("CARBONSHIFT (BASE 2)", 250.005, 8.0),
        ("CARBONSHIFT (BASE 3)", 148.333, 12.0),
    ]
}

# Ordine e colori coerenti in legenda
policies_order = [
    "BASELINE", "RANDOM", "NAIVE CARBON",
    "NAIVE ERROR (BASE 1)", "NAIVE ERROR (BASE 2)", "NAIVE ERROR (BASE 3)",
    "NAIVE SHIFT", "CARBONSHIFT (BASE 1)", "CARBONSHIFT (BASE 2)", "CARBONSHIFT (BASE 3)"
]

color_map = {
    "BASELINE": "#1f77b4",                 # blu
    "RANDOM": "#7f7f7f",                   # grigio
    "NAIVE CARBON": "#ff7f0e",             # arancio
    "NAIVE ERROR (BASE 1)": "#aec7e8",     # azzurro chiaro
    "NAIVE ERROR (BASE 2)": "#9467bd",     # viola
    "NAIVE ERROR (BASE 3)": "#17becf",     # turchese
    "NAIVE SHIFT": "#e377c2",              # rosa
    "CARBONSHIFT (BASE 1)": "#bcbd22",     # giallo-verde
    "CARBONSHIFT (BASE 2)": "#2ca02c",     # verde
    "CARBONSHIFT (BASE 3)": "#8c564b",     # marrone
}

# --- figura e assi ---
fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=False)
fig.suptitle("Confronto delle politiche per ciascun task - emissioni di carbonio ed errore medio", fontsize=14, y=0.98)

# spazio per la legenda sotto
fig.subplots_adjust(left=0.06, right=0.98, top=0.88, bottom=0.23, wspace=0.25)

for ax, (task, task_data) in zip(axes, data.items()):
    # scatter: pallini con bordo nero
    for policy, emission, err in task_data:
        ax.scatter(
            emission, err,
            s=80, marker='o',
            facecolor=color_map[policy],
            edgecolors='black', linewidths=0.8, zorder=3
        )

    # griglia (major+minor)
    ax.minorticks_on()
    ax.grid(True, which='major', linestyle='--', alpha=0.35)
    ax.grid(True, which='minor', linestyle=':', alpha=0.20)

    ax.set_title(task.upper(), fontsize=13, pad=10)
    ax.set_xlabel("Intensità di carbonio (gCO₂-eq)")
    ax.set_ylabel("Errore medio (%)")

# --- legenda globale centrata in basso (non tagliata) ---
handles = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=color_map[p], markeredgecolor='black',
           markersize=8, linewidth=0, label=p)
    for p in policies_order
]
fig.legend(handles=handles, loc='lower center', ncol=5, frameon=True)

# Mostra o salva
# plt.savefig("grafico_tradeoff_scatter.png", dpi=200)
plt.show()