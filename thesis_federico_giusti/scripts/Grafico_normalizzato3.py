import matplotlib.pyplot as plt

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

# === Normalizzazione [0,1] ===
def normalize(values):
    min_v, max_v = min(values), max(values)
    return [(v - min_v) / (max_v - min_v) if max_v != min_v else 0 for v in values]

# === Calcolo valori aggregati ===
policies = [p[0] for p in data["TEXT GENERATION"]]  # tutte le politiche (uguali per i task)
agg_emissions = {p: [] for p in policies}
agg_errors = {p: [] for p in policies}

for task, task_data in data.items():
    policies_t, emissions, errors = zip(*task_data)
    emissions_norm = normalize(emissions)
    errors_norm = normalize(errors)

    for i, pol in enumerate(policies_t):
        agg_emissions[pol].append(emissions_norm[i])
        agg_errors[pol].append(errors_norm[i])

# Media sui 3 task
emissions_final = [sum(agg_emissions[p]) / len(agg_emissions[p]) for p in policies]
errors_final = [sum(agg_errors[p]) / len(agg_errors[p]) for p in policies]

# === Grafico unico ===
plt.figure(figsize=(12, 8))
colors = plt.cm.tab10.colors  # palette di 10 colori

for i, pol in enumerate(policies):
    plt.scatter(emissions_final[i], errors_final[i],
                color=colors[i % len(colors)], s=120,
                edgecolor="black", linewidth=0.7, marker="o", label=pol)

plt.xlabel("Emissioni normalizzate")
plt.ylabel("Errore medio normalizzato")
plt.title("Confronto politiche aggregate normalizzato (Emissioni ed Errore in [0,1])")
plt.grid(True, linestyle="--", alpha=0.6)

# Legenda sotto
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=5, frameon=True)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()