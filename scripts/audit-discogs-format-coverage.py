#!/usr/bin/env python3
"""Audit selected-format coverage against all formats in a Discogs release dump."""

import argparse
import csv
import gzip
import xml.etree.ElementTree as ET
from collections import Counter


STYLES = {"House", "Techno", "Ambient"}
YEARS = {2022, 2023, 2024}
SELECTED_FORMATS = {"Vinyl", "CD", "File"}


def texts(parent, path):
    return {
        node.text.strip()
        for node in parent.findall(path)
        if node.text and node.text.strip()
    }


def audit(input_path, output_path):
    counts = Counter()
    with gzip.open(input_path, "rb") as source:
        context = ET.iterparse(source, events=("start", "end"))
        _, root = next(context)
        for event, release in context:
            if event != "end" or release.tag != "release":
                continue
            if "Electronic" not in texts(release, "./genres/genre"):
                release.clear()
                root.clear()
                continue
            year_text = (release.findtext("released") or "").strip()[:4]
            if not year_text.isdigit() or int(year_text) not in YEARS:
                release.clear()
                root.clear()
                continue
            year = int(year_text)
            styles = texts(release, "./styles/style") & STYLES
            formats = {
                (node.get("name") or "").strip()
                for node in release.findall("./formats/format")
            }
            for style in styles:
                counts[(year, style, "all")] += 1
                if formats & SELECTED_FORMATS:
                    counts[(year, style, "selected")] += 1
                if "Cassette" in formats:
                    counts[(year, style, "cassette")] += 1
            release.clear()
            root.clear()

    with open(output_path, "w", newline="", encoding="utf-8") as target:
        writer = csv.writer(target)
        writer.writerow(
            [
                "year",
                "style",
                "all_format_releases",
                "selected_format_releases",
                "selected_format_coverage",
                "cassette_releases",
                "cassette_share",
            ]
        )
        for style in ("House", "Techno", "Ambient"):
            for year in sorted(YEARS):
                total = counts[(year, style, "all")]
                selected = counts[(year, style, "selected")]
                cassette = counts[(year, style, "cassette")]
                writer.writerow(
                    [
                        year,
                        style,
                        total,
                        selected,
                        selected / total,
                        cassette,
                        cassette / total,
                    ]
                )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to the Discogs releases.xml.gz dump")
    parser.add_argument("output", help="Path for the coverage CSV")
    args = parser.parse_args()
    audit(args.input, args.output)


if __name__ == "__main__":
    main()
