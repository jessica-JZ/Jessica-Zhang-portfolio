#!/usr/bin/env python3
import csv
from collections import defaultdict
from html import escape


source = "data/final-project-part-one/discogs-annual-style-format-shares.csv"
destination = "assets/final-project-part-one/preliminary-format-share.svg"
styles = ["House", "Techno", "Ambient"]
formats = ["Vinyl", "CD", "File"]
colors = {"Vinyl": "#7656A8", "CD": "#6F91A8", "File": "#C56D2D"}
values = defaultdict(dict)

with open(source, newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        values[(row["style"], row["format"])][int(row["year"])] = float(row["share"])

width, height = 1200, 1160
left, right = 110, 50
top = 175
panel_height = 235
gap = 55
plot_width = width - left - right


def x_position(year):
    return left + (year - 1985) / (2024 - 1985) * plot_width


def y_position(share, panel_top):
    return panel_top + panel_height - share * panel_height


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
    '<rect width="100%" height="100%" fill="#ffffff"/>',
    '<style>text{font-family:Arial,sans-serif;fill:#252525}.title{font-size:31px;font-weight:700}.subtitle{font-size:18px;fill:#555}.panel{font-size:21px;font-weight:700}.tick{font-size:14px;fill:#666}.note{font-size:14px;fill:#555}.grid{stroke:#ddd9d0;stroke-width:1}</style>',
    '<text x="70" y="58" class="title">Files became dominant, but vinyl remained present</text>',
    '<text x="70" y="91" class="subtitle">Share among filtered Discogs releases with Vinyl, CD, or File, 1985–2024</text>',
]

legend_x = 760
for index, format_name in enumerate(formats):
    x = legend_x + index * 125
    parts.append(f'<line x1="{x}" y1="126" x2="{x+28}" y2="126" stroke="{colors[format_name]}" stroke-width="5"/>')
    parts.append(f'<text x="{x+36}" y="132" class="tick">{escape(format_name)}</text>')

for panel_index, style in enumerate(styles):
    panel_top = top + panel_index * (panel_height + gap)
    parts.append(f'<text x="70" y="{panel_top-18}" class="panel">{escape(style)}</text>')
    for percentage in (0, 0.25, 0.5, 0.75, 1.0):
        y = y_position(percentage, panel_top)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{left-18}" y="{y+5:.1f}" text-anchor="end" class="tick">{int(percentage*100)}%</text>')
    for year in (1985, 1995, 2005, 2015, 2024):
        x = x_position(year)
        parts.append(f'<line x1="{x:.1f}" y1="{panel_top}" x2="{x:.1f}" y2="{panel_top+panel_height}" stroke="#f1efe9"/>')
        if panel_index == len(styles) - 1:
            parts.append(f'<text x="{x:.1f}" y="{panel_top+panel_height+25}" text-anchor="middle" class="tick">{year}</text>')
    for format_name in formats:
        points = []
        for year in range(1985, 2025):
            share = values[(style, format_name)].get(year, 0.0)
            points.append(f'{x_position(year):.1f},{y_position(share, panel_top):.1f}')
        point_string = " ".join(points)
        parts.append(
            f'<polyline points="{point_string}" fill="none" stroke="{colors[format_name]}" '
            'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
        )

parts.append('<text x="630" y="1055" text-anchor="middle" class="subtitle">Release year</text>')
parts.append('<text x="28" y="585" text-anchor="middle" transform="rotate(-90 28 585)" class="subtitle">Share of filtered releases tagged with each format</text>')
parts.append('<line x1="70" y1="1090" x2="1150" y2="1090" stroke="#ddd9d0" stroke-width="1"/>')
parts.append('<text x="70" y="1125" class="note">Source: Discogs December 2025 release dump. Denominator: distinct releases tagged Vinyl, CD, or File.</text>')
parts.append('<text x="70" y="1148" class="note">Styles and formats can overlap; these are catalog records, not sales or listening data.</text>')
parts.append('</svg>')

with open(destination, "w", encoding="utf-8") as target:
    target.write("\n".join(parts))
