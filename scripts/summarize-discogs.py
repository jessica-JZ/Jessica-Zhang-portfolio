#!/usr/bin/env python3
"""Create auditable summary tables from the filtered Discogs CSV."""

import csv
import gzip
from collections import defaultdict
from pathlib import Path


DATA_DIR = Path("data/final-project-part-one")
INPUT = DATA_DIR / "discogs-electronic-formats-1985-2024.csv.gz"
ANNUAL = DATA_DIR / "discogs-annual-style-format-counts.csv"
SHARES = DATA_DIR / "discogs-annual-style-format-shares.csv"
QUALITY = DATA_DIR / "data-quality-summary.txt"
MASTER_SENSITIVITY = DATA_DIR / "discogs-2024-master-sensitivity.csv"


release_ids = set()
release_ids_with_master = set()
release_ids_without_country = set()
formats_by_release = defaultdict(set)
styles_by_release = defaultdict(set)
by_year = defaultdict(set)
by_year_style = defaultdict(set)
by_year_style_format = defaultdict(set)
masters_by_year_style = defaultdict(set)
masters_by_year_style_format = defaultdict(set)

with gzip.open(INPUT, "rt", newline="", encoding="utf-8") as source:
    for row in csv.DictReader(source):
        release_id = row["release_id"]
        year = int(row["year"])
        style = row["style"]
        format_name = row["format"]

        release_ids.add(release_id)
        by_year[year].add(release_id)
        by_year_style[(year, style)].add(release_id)
        by_year_style_format[(year, style, format_name)].add(release_id)
        formats_by_release[release_id].add(format_name)
        styles_by_release[release_id].add(style)
        if row["master_id"] and row["master_id"] != "0":
            release_ids_with_master.add(release_id)
            master_id = row["master_id"]
            masters_by_year_style[(year, style)].add(master_id)
            masters_by_year_style_format[(year, style, format_name)].add(master_id)
        if not row["country"]:
            release_ids_without_country.add(release_id)

with ANNUAL.open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(["year", "style", "format", "distinct_releases"])
    for key in sorted(by_year_style_format):
        writer.writerow([*key, len(by_year_style_format[key])])

with SHARES.open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(
        ["year", "style", "format", "distinct_releases", "style_year_releases", "share"]
    )
    for (year, style, format_name), ids in sorted(by_year_style_format.items()):
        denominator = len(by_year_style[(year, style)])
        writer.writerow(
            [year, style, format_name, len(ids), denominator, len(ids) / denominator]
        )

with MASTER_SENSITIVITY.open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(
        ["year", "style", "format", "distinct_masters", "style_year_masters", "share"]
    )
    year = 2024
    for style in ("House", "Techno", "Ambient"):
        denominator = len(masters_by_year_style[(year, style)])
        for format_name in ("Vinyl", "CD", "File"):
            count = len(masters_by_year_style_format[(year, style, format_name)])
            writer.writerow([year, style, format_name, count, denominator, count / denominator])

with QUALITY.open("w", encoding="utf-8") as target:
    target.write(f"distinct_releases: {len(release_ids)}\n")
    target.write(f"releases_with_master_id: {len(release_ids_with_master)}\n")
    target.write(f"releases_without_master_id: {len(release_ids - release_ids_with_master)}\n")
    target.write(f"releases_without_country: {len(release_ids_without_country)}\n")
    target.write(
        f"releases_with_multiple_selected_formats: "
        f"{sum(len(values) > 1 for values in formats_by_release.values())}\n"
    )
    target.write(
        f"releases_with_multiple_selected_styles: "
        f"{sum(len(values) > 1 for values in styles_by_release.values())}\n"
    )
    target.write(f"first_year: {min(by_year)}\n")
    target.write(f"last_year: {max(by_year)}\n")
    for year in sorted(by_year):
        target.write(f"distinct_releases_{year}: {len(by_year[year])}\n")
