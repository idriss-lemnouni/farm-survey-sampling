from collections import defaultdict
from csv import DictReader
import json
from pathlib import Path
from random import Random
from statistics import mean, pstdev

ROOT = Path(__file__).resolve().parent


def compare(rows, size=24, trials=5000):
    groups = defaultdict(list)
    for row in rows:
        groups[row["feed"]].append(float(row["weight"]))
    population = [weight for group in groups.values() for weight in group]
    truth = mean(population)
    quotas = {key: size * len(group) / len(population) for key, group in groups.items()}
    counts = {key: int(quota) for key, quota in quotas.items()}
    remainder = size - sum(counts.values())
    for key in sorted(groups, key=lambda k: quotas[k] - counts[k], reverse=True)[:remainder]:
        counts[key] += 1
    assert sum(counts.values()) == size and all(counts.values())
    rng = Random(42)
    simple, stratified = [], []
    for _ in range(trials):
        simple.append(mean(rng.sample(population, size)))
        stratified.append(sum(len(group) / len(population) * mean(rng.sample(group, counts[key]))
                              for key, group in groups.items()))

    def scores(estimates):
        return {"bias_g": round(mean(estimates) - truth, 3),
                "sd_g": round(pstdev(estimates), 3),
                "rmse_g": round(mean((x - truth) ** 2 for x in estimates) ** 0.5, 3)}

    return {"population_size": len(population), "mean_weight_g": round(truth, 3),
            "sample_size": size, "trials": trials, "stratum_allocations": counts,
            "simple_random": scores(simple), "stratified": scores(stratified)}


if __name__ == "__main__":
    with (ROOT / "chickwts.csv").open(encoding="utf-8-sig", newline="") as stream:
        report = compare(list(DictReader(stream)))
    output = json.dumps(report, indent=2) + "\n"
    (ROOT / "results.json").write_text(output, encoding="utf-8")
    print(output, end="")
