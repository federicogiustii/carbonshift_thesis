import matplotlib.pyplot as plt
import numpy as np

# === DATI ===
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
        ("NAIVE CARBON", 291.655, 8.0), 
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

# Mappa epsilon per etichette sulle barre
epsilon_map = {
    "TEXT GENERATION": {
        "NAIVE ERROR (BASE 1)": 15, "NAIVE ERROR (BASE 2)": 18, "NAIVE ERROR (BASE 3)": 20,
        "CARBONSHIFT (BASE 1)": 15, "CARBONSHIFT (BASE 2)": 18, "CARBONSHIFT (BASE 3)": 20
    },
    "NAMED ENTITY RECOGNITION": {
        "NAIVE ERROR (BASE 1)": 3, "NAIVE ERROR (BASE 2)": 8, "NAIVE ERROR (BASE 3)": 9,
        "CARBONSHIFT (BASE 1)": 3, "CARBONSHIFT (BASE 2)": 8, "CARBONSHIFT (BASE 3)": 9
    },
    "QUESTION ANSWERING": {
        "NAIVE ERROR (BASE 1)": 7, "NAIVE ERROR (BASE 2)": 8, "NAIVE ERROR (BASE 3)": 12,
        "CARBONSHIFT (BASE 1)": 7, "CARBONSHIFT (BASE 2)": 8, "CARBONSHIFT (BASE 3)": 12
    }
}

# Ordine delle politiche
policies_order = [
    "CARBONSHIFT (BASE 3)", "CARBONSHIFT (BASE 2)", 
    "CARBONSHIFT (BASE 1)","NAIVE SHIFT","NAIVE ERROR (BASE 3)",
    "NAIVE ERROR (BASE 2)", "NAIVE ERROR (BASE 1)", "NAIVE CARBON", 
    "RANDOM", "BASELINE"    
]

colors = {
    "TEXT GENERATION": "#6b8e23",
    "NAMED ENTITY RECOGNITION": "#9acd32",
    "QUESTION ANSWERING": "#2e8b57"
}

# Funzione per creare grafici orizzontali
def plot_grouped_bar_horizontal(metric_index, ylabel, title):
    y = np.arange(len(policies_order))
    height = 0.25
    fig, ax = plt.subplots(figsize=(12, 8))

    for i, task in enumerate(data.keys()):
        values = []
        epsilons = []
        for policy in policies_order:
            found = next((em, err) for pol, em, err in data[task] if pol == policy)
            values.append(found[metric_index])
            epsilons.append(epsilon_map.get(task, {}).get(policy, None))
        bars = ax.barh(y + i * height, values, height, label=task, color=colors[task])
        for bar, eps in zip(bars, epsilons):
            if eps is not None:
                ax.text(bar.get_width() + max(values)*0.01, 
                        bar.get_y() + bar.get_height()/2,
                        f"ε={eps}", va='center', fontsize=8)

    ax.set_xlabel(ylabel)
    ax.set_title(title)
    ax.set_yticks(y + height)
    ax.set_yticklabels(policies_order)
    ax.legend()
    plt.tight_layout()
    plt.show()

# Grafico Emissioni Totali
plot_grouped_bar_horizontal(metric_index=0, ylabel="Emissioni totali (mgCO₂-eq)", 
                             title="Emissioni totali per politica (tutti i task)")

# Grafico Errore Medio
plot_grouped_bar_horizontal(metric_index=1, ylabel="Errore medio", 
                             title="Errore medio per politica (tutti i task)")