"""Merge all catalog_*.py supplement files into data/products.json"""
import json
import os
import sys
import importlib.util

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT = os.path.join(PROJECT_DIR, "data", "products.json")

def load_module(path):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# Load existing products.json
with open(OUTPUT, "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_names = {p["name"].lower().strip() for p in existing}
print(f"Existing products: {len(existing)}")

# Load each supplement catalog
supplements = [
    "catalog_waves_uad.py",
    "catalog_ni_kontakt.py",
    "catalog_drums_samples.py",
    "catalog_misc.py",
    "catalog_synths2.py",
    "catalog_effects2.py",
    "catalog_generated.py",
    "catalog_final.py",
    "catalog_niche.py",
    "catalog_bulk.py",
]

added = 0
skipped = 0
by_category = {}

for fname in supplements:
    path = os.path.join(SCRIPT_DIR, fname)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {fname}")
        continue
    mod = load_module(path)
    products = mod.PRODUCTS
    print(f"\n  {fname}: {len(products)} entries")
    for p in products:
        name_key = p["name"].lower().strip()
        if name_key in existing_names:
            skipped += 1
            continue
        # Ensure required fields
        p.setdefault("featured", False)
        p.setdefault("images", [])
        p.setdefault("pros", [])
        p.setdefault("cons", [])
        p.setdefault("tags", [p["category"]])
        p.setdefault("releaseYear", 2023)
        p.setdefault("latestVersion", "")
        p.setdefault("platforms", ["Windows", "macOS"])
        p.setdefault("formats", ["VST3", "AU", "AAX"])
        existing.append(p)
        existing_names.add(name_key)
        cat = p.get("category", "unknown")
        by_category[cat] = by_category.get(cat, 0) + 1
        added += 1

print(f"\nAdded {added} new products (skipped {skipped} duplicates)")
print("By category:")
for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
    print(f"  {cat:<15} {count}")
print(f"\nTotal in products.json: {len(existing)}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Saved to {OUTPUT}")
