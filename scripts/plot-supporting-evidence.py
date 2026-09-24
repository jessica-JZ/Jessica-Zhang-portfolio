#!/usr/bin/env python3
"""Create supporting SVG sketches for the electronic-format story."""

import csv
from collections import defaultdict
from pathlib import Path


DATA = Path("data/final-project-part-one")
ASSETS = Path("assets/final-project-part-one")
STYLES = ["House", "Techno", "Ambient"]
COLORS = {"Vinyl": "#7656A8", "CD": "#6F91A8", "File": "#C56D2D"}


def svg_start(width, height, title, description):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{title}</title>',
        f'<desc id="desc">{description}</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:Arial,sans-serif;fill:#252525}.title{font-size:32px;font-weight:700}.subtitle{font-size:18px;fill:#555}.label{font-size:17px}.small{font-size:14px;fill:#666}.style{font-size:21px;font-weight:700}.grid{stroke:#ddd9d0;stroke-width:1}.axis{stroke:#918d84;stroke-width:1.5}.noteBox{fill:#fff8dc;stroke:#d6bc55;stroke-width:1.5}</style>',
    ]


def write_svg(path, parts):
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def load_annual():
    rows = []
    with (DATA / "discogs-annual-style-format-shares.csv").open(
        newline="", encoding="utf-8"
    ) as source:
        for row in csv.DictReader(source):
            row["year"] = int(row["year"])
            row["distinct_releases"] = int(row["distinct_releases"])
            row["style_year_releases"] = int(row["style_year_releases"])
            row["share"] = float(row["share"])
            rows.append(row)
    return rows


def plot_recent_summary(rows):
    numerators = defaultdict(int)
    denominators = {}
    for row in rows:
        if row["year"] not in (2022, 2023, 2024):
            continue
        key = (row["style"], row["format"])
        numerators[key] += row["distinct_releases"]
        denominators[(row["style"], row["year"])] = row["style_year_releases"]

    shares = {}
    for style in STYLES:
        denominator = sum(denominators[(style, year)] for year in (2022, 2023, 2024))
        for format_name in ("Vinyl", "File"):
            shares[(style, format_name)] = numerators[(style, format_name)] / denominator

    width, height = 1200, 690
    left, right = 235, 1100
    parts = svg_start(
        width,
        height,
        "File led the selected release-version categories in 2022–2024",
        "A paired-dot comparison shows pooled File and Vinyl percentages for House, Techno, and Ambient, with a coverage warning for Ambient.",
    )
    parts += [
        '<text x="70" y="58" class="title" style="font-size:29px">Across 2022–2024, File led in all three styles</text>',
        '<text x="70" y="91" class="subtitle">Pooled percentage of filtered Discogs release versions that include each format</text>',
    ]
    for tick in (0, 25, 50, 75, 100):
        x = left + (right - left) * tick / 100
        parts.append(f'<line x1="{x:.1f}" y1="150" x2="{x:.1f}" y2="525" class="grid"/>')
        parts.append(f'<text x="{x:.1f}" y="548" text-anchor="middle" class="small">{tick}%</text>')

    for index, style in enumerate(STYLES):
        y = 210 + index * 135
        parts.append(f'<text x="70" y="{y+6}" class="style">{style}</text>')
        vinyl = shares[(style, "Vinyl")] * 100
        file_share = shares[(style, "File")] * 100
        xv = left + (right - left) * vinyl / 100
        xf = left + (right - left) * file_share / 100
        parts.append(f'<line x1="{xv:.1f}" y1="{y}" x2="{xf:.1f}" y2="{y}" stroke="#d8d4cb" stroke-width="5"/>')
        parts.append(f'<circle cx="{xv:.1f}" cy="{y}" r="10" fill="{COLORS["Vinyl"]}"/>')
        parts.append(f'<circle cx="{xf:.1f}" cy="{y}" r="10" fill="{COLORS["File"]}"/>')
        parts.append(f'<text x="{xv:.1f}" y="{y-18}" text-anchor="middle" class="label" fill="{COLORS["Vinyl"]}">Vinyl {vinyl:.1f}%</text>')
        parts.append(f'<text x="{xf:.1f}" y="{y-18}" text-anchor="middle" class="label" fill="{COLORS["File"]}">File {file_share:.1f}%</text>')

    parts += [
        '<rect x="70" y="575" width="1060" height="78" rx="8" class="noteBox"/>',
        '<text x="92" y="605" class="label">Scope warning: Vinyl, CD, or File cover 76.9% of 2024 Ambient records;</text>',
        '<text x="92" y="632" class="small">Cassette alone appears on 13.3%. This is not a complete account of Ambient’s physical-format history.</text>',
    ]
    write_svg(ASSETS / "recent-format-summary.svg", parts)


def plot_vinyl_counts(rows):
    counts = defaultdict(int)
    for row in rows:
        if row["format"] == "Vinyl" and 2015 <= row["year"] <= 2024:
            counts[(row["style"], row["year"])] = row["distinct_releases"]

    width, height = 1200, 850
    left, right = 120, 1140
    plot_width = right - left
    panel_height = 155
    max_count = 5500
    parts = svg_start(
        width,
        height,
        "Vinyl releases remained present in thousands of cataloged versions",
        "Three aligned line charts show annual Vinyl release-version counts for House, Techno, and Ambient from 2015 through 2024.",
    )
    parts += [
        '<text x="70" y="58" class="title" style="font-size:27px">Vinyl releases remained present in thousands of cataloged versions</text>',
        '<text x="70" y="91" class="subtitle">Distinct Vinyl-tagged Discogs release versions, 2015–2024</text>',
    ]

    def x_pos(year):
        return left + (year - 2015) / 9 * plot_width

    for index, style in enumerate(STYLES):
        top = 155 + index * 215
        bottom = top + panel_height
        parts.append(f'<text x="70" y="{top-20}" class="style">{style}</text>')
        for value in (0, 2500, 5000):
            y = bottom - value / max_count * panel_height
            parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" class="grid"/>')
            parts.append(f'<text x="{left-18}" y="{y+5:.1f}" text-anchor="end" class="small">{value:,}</text>')
        points = []
        for year in range(2015, 2025):
            x = x_pos(year)
            y = bottom - counts[(style, year)] / max_count * panel_height
            points.append(f"{x:.1f},{y:.1f}")
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{COLORS["Vinyl"]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
        last_y = bottom - counts[(style, 2024)] / max_count * panel_height
        parts.append(f'<circle cx="{x_pos(2024):.1f}" cy="{last_y:.1f}" r="6" fill="{COLORS["Vinyl"]}"/>')
        parts.append(f'<text x="{x_pos(2024)-8:.1f}" y="{last_y-12:.1f}" text-anchor="end" class="label">2024: {counts[(style, 2024)]:,}</text>')
        if index == 2:
            for year in (2015, 2018, 2021, 2024):
                parts.append(f'<text x="{x_pos(year):.1f}" y="{bottom+28}" text-anchor="middle" class="small">{year}</text>')

    parts += [
        '<text x="630" y="805" text-anchor="middle" class="subtitle">Release year</text>',
        '<text x="70" y="833" class="small">Counts are catalog records, not sales. Recent counts are flat or declining rather than steadily increasing.</text>',
    ]
    write_svg(ASSETS / "vinyl-absolute-counts.svg", parts)


def plot_master_view():
    values = defaultdict(dict)
    with (DATA / "discogs-2024-master-sensitivity.csv").open(
        newline="", encoding="utf-8"
    ) as source:
        for row in csv.DictReader(source):
            values[row["style"]][row["format"]] = float(row["share"]) * 100

    width, height = 1200, 690
    left, right = 250, 1100
    parts = svg_start(
        width,
        height,
        "A substantial share of identifiable masters also had a Vinyl version",
        "A paired-dot comparison shows the percentage of identifiable masters represented by a 2024 File or Vinyl release version.",
    )
    parts += [
        '<text x="70" y="58" class="title" style="font-size:28px">Many identifiable works also had a Vinyl version</text>',
        '<text x="70" y="91" class="subtitle">Masters represented by a filtered 2024 release version; formats can overlap</text>',
    ]
    for tick in (0, 25, 50, 75, 100):
        x = left + (right - left) * tick / 100
        parts.append(f'<line x1="{x:.1f}" y1="150" x2="{x:.1f}" y2="515" class="grid"/>')
        parts.append(f'<text x="{x:.1f}" y="540" text-anchor="middle" class="small">{tick}%</text>')

    for index, style in enumerate(STYLES):
        y = 210 + index * 130
        parts.append(f'<text x="70" y="{y+6}" class="style">{style}</text>')
        vinyl = values[style]["Vinyl"]
        file_share = values[style]["File"]
        xv = left + (right - left) * vinyl / 100
        xf = left + (right - left) * file_share / 100
        parts.append(f'<line x1="{xv:.1f}" y1="{y}" x2="{xf:.1f}" y2="{y}" stroke="#d8d4cb" stroke-width="5"/>')
        parts.append(f'<circle cx="{xv:.1f}" cy="{y}" r="10" fill="{COLORS["Vinyl"]}"/>')
        parts.append(f'<circle cx="{xf:.1f}" cy="{y}" r="10" fill="{COLORS["File"]}"/>')
        parts.append(f'<text x="{xv:.1f}" y="{y-18}" text-anchor="middle" class="label">Vinyl {vinyl:.1f}%</text>')
        parts.append(f'<text x="{xf:.1f}" y="{y-18}" text-anchor="middle" class="label">File {file_share:.1f}%</text>')

    parts += [
        '<rect x="70" y="575" width="1060" height="78" rx="8" class="noteBox"/>',
        '<text x="92" y="606" class="label">This is a second unit of analysis, not a replacement for the release-version chart.</text>',
        '<text x="92" y="633" class="small">Only records with a usable master ID are included. One master may have both File and Vinyl versions.</text>',
    ]
    write_svg(ASSETS / "master-format-view.svg", parts)


def plot_storyboard():
    width, height = 1200, 1880
    parts = svg_start(
        width,
        height,
        "Five-part storyboard for an electronic music format history",
        "Five stacked panels distinguish format from recording technology, show annual change, summarize recent years and counts, compare masters, and close with scope limits.",
    )
    parts += [
        '<rect width="100%" height="100%" fill="#f7f5f0"/>',
        '<text x="70" y="70" class="title">Music-history story sketch</text>',
        '<text x="70" y="106" class="subtitle">Five steps, with each chart answering one question</text>',
    ]
    panels = [(145, 255), (430, 300), (760, 300), (1090, 300), (1420, 360)]
    for y, h in panels:
        parts.append(f'<rect x="60" y="{y}" width="1080" height="{h}" rx="12" fill="#fff" stroke="#c9c5bb" stroke-width="2"/>')

    parts += [
        '<text x="95" y="198" class="small">1 · DEFINE THE TERMS</text>',
        '<text x="95" y="255" class="title">Release format is not recording technology</text>',
        '<text x="95" y="300" class="subtitle">A Vinyl release may use a digital master; File describes how a release was issued.</text>',
        '<line x1="680" y1="365" x2="1070" y2="365" class="axis"/>',
        '<circle cx="700" cy="365" r="6" fill="#918d84"/><circle cx="880" cy="365" r="6" fill="#C56D2D"/><circle cx="1060" cy="365" r="6" fill="#918d84"/>',
        '<text x="700" y="388" text-anchor="middle" class="small">1985: study begins</text>',
        '<text x="880" y="388" text-anchor="middle" class="small">1993: File in sample</text>',
        '<text x="1060" y="388" text-anchor="middle" class="small">2024</text>',

        '<text x="95" y="485" class="small">2 · SHOW THE HISTORICAL CHANGE</text>',
        '<text x="95" y="532" class="style">Annual percentage of release versions that include each format</text>',
        '<line x1="115" y1="680" x2="795" y2="680" class="axis"/>',
        '<path d="M115 565 C270 590 390 645 520 660 S690 650 795 640" fill="none" stroke="#7656A8" stroke-width="7"/>',
        '<path d="M115 650 C280 615 390 570 520 600 S690 660 795 674" fill="none" stroke="#6F91A8" stroke-width="7"/>',
        '<path d="M115 680 C320 680 430 660 535 625 S670 565 795 550" fill="none" stroke="#C56D2D" stroke-width="7"/>',
        '<text x="115" y="710" class="small">1985</text><text x="755" y="710" class="small">2024</text>',
        '<rect x="850" y="565" width="210" height="115" fill="#fafafa" stroke="#ddd9d0"/>',
        '<path d="M875 660 C920 650 955 620 1035 585" fill="none" stroke="#918d84" stroke-width="5"/>',
        '<text x="850" y="550" class="small">Pair share with total catalog counts</text>',

        '<text x="95" y="815" class="small">3 · SUMMARIZE THE RECENT STATE</text>',
        '<text x="95" y="862" class="style">2022–2024 pooled comparison plus Vinyl counts</text>',
        '<text x="95" y="905" class="subtitle">File: 69.8%–75.2% · Vinyl: 19.8%–25.1%</text>',
        '<line x1="120" y1="980" x2="540" y2="980" stroke="#d8d4cb" stroke-width="6"/>',
        '<circle cx="225" cy="980" r="11" fill="#7656A8"/><circle cx="435" cy="980" r="11" fill="#C56D2D"/>',
        '<rect x="650" y="900" width="410" height="120" fill="#fafafa" stroke="#ddd9d0"/>',
        '<path d="M680 980 L730 950 L780 960 L830 940 L880 955 L930 950 L1015 970" fill="none" stroke="#7656A8" stroke-width="6"/>',
        '<text x="650" y="890" class="small">Vinyl releases remain in thousands of cataloged versions</text>',

        '<text x="95" y="1145" class="small">4 · CHANGE THE UNIT OF ANALYSIS</text>',
        '<text x="95" y="1192" class="style">Does an identifiable master have a File or Vinyl version?</text>',
        '<text x="95" y="1235" class="subtitle">Separate paired dots; never place these values on the release-version axis.</text>',
        '<line x1="230" y1="1320" x2="1000" y2="1320" stroke="#d8d4cb" stroke-width="6"/>',
        '<circle cx="610" cy="1320" r="12" fill="#7656A8"/><circle cx="820" cy="1320" r="12" fill="#C56D2D"/>',
        '<text x="610" y="1293" text-anchor="middle" class="label">Vinyl version</text>',
        '<text x="820" y="1293" text-anchor="middle" class="label">File version</text>',

        '<text x="95" y="1475" class="small">5 · CLOSE WITH SCOPE AND LIMITS</text>',
        '<text x="95" y="1522" class="style">A catalog history with an incomplete view of Ambient formats</text>',
        '<rect x="95" y="1560" width="970" height="84" rx="8" class="noteBox"/>',
        '<text x="118" y="1594" class="label">Ambient: selected formats cover 76.9% of 2024 records; Cassette appears on 13.3%.</text>',
        '<text x="118" y="1623" class="small">Discogs records do not measure sales, listening, sound quality, or analog versus digital mastering.</text>',
        '<text x="95" y="1695" class="subtitle">Audience takeaway</text>',
        '<text x="95" y="1735" class="style">File versions became dominant in the catalog, while vinyl releases remained visible.</text>',
    ]
    write_svg(ASSETS / "storyboard.svg", parts)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    rows = load_annual()
    plot_recent_summary(rows)
    plot_vinyl_counts(rows)
    plot_master_view()
    plot_storyboard()


if __name__ == "__main__":
    main()
