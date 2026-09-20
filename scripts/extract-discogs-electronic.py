#!/usr/bin/env python3
"""Extract a reproducible electronic-music subset from a Discogs release dump."""

import argparse
import csv
import gzip
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


SELECTED_STYLES = {"House", "Techno", "Ambient"}
SELECTED_FORMATS = {"Vinyl", "CD", "File"}


def texts(parent, path):
    return {
        node.text.strip()
        for node in parent.findall(path)
        if node.text and node.text.strip()
    }


def release_year(release):
    value = release.findtext("released") or ""
    first_four = value.strip()[:4]
    return int(first_four) if first_four.isdigit() else None


def extract(input_path, output_path, stats_path):
    counters = Counter()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with gzip.open(input_path, "rb") as source, open(
        output_path, "w", newline="", encoding="utf-8"
    ) as target:
        writer = csv.DictWriter(
            target,
            fieldnames=[
                "release_id",
                "master_id",
                "year",
                "country",
                "style",
                "format",
                "format_description",
            ],
        )
        writer.writeheader()

        context = ET.iterparse(source, events=("start", "end"))
        _, root = next(context)
        for event, release in context:
            if event != "end":
                continue
            if release.tag != "release":
                continue

            counters["releases_read"] += 1
            genres = texts(release, "./genres/genre")
            if "Electronic" not in genres:
                release.clear()
                root.clear()
                continue
            counters["electronic_releases"] += 1

            year = release_year(release)
            if year is None or not 1985 <= year <= 2024:
                counters["excluded_year"] += 1
                release.clear()
                root.clear()
                continue

            styles = sorted(texts(release, "./styles/style") & SELECTED_STYLES)
            if not styles:
                counters["excluded_style"] += 1
                release.clear()
                root.clear()
                continue

            formats = []
            for format_node in release.findall("./formats/format"):
                name = (format_node.get("name") or "").strip()
                if name not in SELECTED_FORMATS:
                    continue
                descriptions = sorted(texts(format_node, "./descriptions/description"))
                formats.append((name, " | ".join(descriptions)))

            if not formats:
                counters["excluded_format"] += 1
                release.clear()
                root.clear()
                continue

            release_id = release.get("id", "")
            master_id = (release.findtext("master_id") or "").strip()
            country = (release.findtext("country") or "").strip()

            for style in styles:
                for format_name, format_description in formats:
                    writer.writerow(
                        {
                            "release_id": release_id,
                            "master_id": master_id,
                            "year": year,
                            "country": country,
                            "style": style,
                            "format": format_name,
                            "format_description": format_description,
                        }
                    )
                    counters["output_rows"] += 1

            counters["included_distinct_releases"] += 1
            release.clear()
            root.clear()

    with open(stats_path, "w", encoding="utf-8") as stats:
        for key in sorted(counters):
            stats.write(f"{key}: {counters[key]}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to the Discogs releases.xml.gz dump")
    parser.add_argument("output", help="Path for the filtered CSV")
    parser.add_argument("stats", help="Path for extraction counts")
    args = parser.parse_args()
    extract(args.input, args.output, args.stats)


if __name__ == "__main__":
    main()
