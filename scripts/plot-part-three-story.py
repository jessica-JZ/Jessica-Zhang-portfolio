#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/final-project-part-one/discogs-annual-style-format-counts.csv"
DESTINATION = ROOT / "assets/final-project-part-three"
STYLES = ["House", "Techno", "Ambient"]
FORMATS = ["Vinyl", "File"]
COLORS = {"Vinyl": "#4C78A8", "File": "#635b55"}
LABELS = {"Vinyl": "Vinyl", "File": "Digital file"}

values = defaultdict(dict)
with SOURCE.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        if row["style"] in STYLES and row["format"] in FORMATS:
            values[(row["style"], row["format"])][int(row["year"])] = int(row["distinct_releases"])


def crossover_year(style):
    shared_years = sorted(set(values[(style, "Vinyl")]) & set(values[(style, "File")]))
    return next(year for year in shared_years if values[(style, "File")][year] > values[(style, "Vinyl")][year])


WIDTH, HEIGHT = 1400, 945
LEFT, RIGHT = 130, 235
TOP, PANEL_HEIGHT, GAP = 170, 180, 45
PLOT_WIDTH = WIDTH - LEFT - RIGHT
MAX_VALUE = 19000


def x_position(year):
    return LEFT + (year - 1985) / (2024 - 1985) * PLOT_WIDTH


def y_position(value, panel_top):
    return panel_top + PANEL_HEIGHT - value / MAX_VALUE * PANEL_HEIGHT


def text(x, y, content, css_class, anchor=None):
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" class="{css_class}"{anchor_attr}>{escape(content)}</text>'


def make_frame(stage):
    titles = {
        1: ("Vinyl releases fell, but did not disappear", "Annual Discogs release-version counts, 1985–2024."),
        2: ("Digital files took the lead", "The same axes show the change across three styles."),
        3: ("Digital files took the lead; vinyl continued", "First File-over-Vinyl years are marked within this Discogs sample."),
    }
    title, subtitle = titles[stage]
    visible_formats = ["Vinyl"] if stage == 1 else FORMATS
    css = '<style>text{font-family:Arial,sans-serif;fill:#262626}.eyebrow{font-size:22px;font-weight:700;letter-spacing:1.5px;fill:#6d6d6d}.title{font-size:36px;font-weight:700}.subtitle{font-size:22px;fill:#555}.panel{font-size:24px;font-weight:700}.axis{font-size:20px;fill:#666}.axis-title{font-size:20px;fill:#444}.end{font-size:21px;font-weight:700}.source{font-size:19px;fill:#666}.grid{stroke:#e6e3df;stroke-width:1}.baseline{stroke:#bdb8b3;stroke-width:1.2}.cross{stroke:#9a612f;stroke-width:1.5;stroke-dasharray:5 5}.callout{font-size:19px;font-weight:700;fill:#7a4b25}.callout-year{font-size:22px;font-weight:700;fill:#7a4b25}</style>'
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        f'<title id="title">Storyboard frame {stage} of 3: {escape(title)}</title>',
        f'<desc id="desc">Annual Discogs catalog counts for House, Techno, and Ambient release versions from 1985 through 2024.</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        css,
        text(55, 38, f"FINAL STORY FRAME {stage} OF 3", "eyebrow"),
        text(55, 78, title, "title"),
        text(55, 108, subtitle, "subtitle"),
    ]

    legend_x = 1040
    for index, format_name in enumerate(visible_formats):
        y = 55 + index * 28
        parts.append(f'<line x1="{legend_x}" y1="{y}" x2="{legend_x + 30}" y2="{y}" stroke="{COLORS[format_name]}" stroke-width="5"/>')
        parts.append(text(legend_x + 40, y + 5, LABELS[format_name], "axis"))

    for panel_index, style in enumerate(STYLES):
        panel_top = TOP + panel_index * (PANEL_HEIGHT + GAP)
        parts.append(text(55, panel_top + 8, style, "panel"))
        for tick in (0, 5000, 10000, 15000):
            y = y_position(tick, panel_top)
            css_class = "baseline" if tick == 0 else "grid"
            parts.append(f'<line x1="{LEFT}" y1="{y:.1f}" x2="{WIDTH - RIGHT}" y2="{y:.1f}" class="{css_class}"/>')
            parts.append(text(LEFT - 12, y + 5, "0" if tick == 0 else f"{tick // 1000}K", "axis", "end"))
        for year in (1985, 1995, 2005, 2015, 2024):
            x = x_position(year)
            parts.append(f'<line x1="{x:.1f}" y1="{panel_top}" x2="{x:.1f}" y2="{panel_top + PANEL_HEIGHT}" stroke="#f2f0ed"/>')
            if panel_index == len(STYLES) - 1:
                parts.append(text(f"{x:.1f}", panel_top + PANEL_HEIGHT + 24, str(year), "axis", "middle"))

        for format_name in visible_formats:
            points = " ".join(
                f'{x_position(year):.1f},{y_position(value, panel_top):.1f}'
                for year, value in sorted(values[(style, format_name)].items())
            )
            parts.append(
                f'<polyline points="{points}" fill="none" stroke="{COLORS[format_name]}" '
                'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
            )
            final_value = values[(style, format_name)][2024]
            final_y = y_position(final_value, panel_top)
            label_y = final_y + (-8 if format_name == "File" else 16)
            end_label = f'{format_name} {final_value:,}'
            parts.append(text(WIDTH - RIGHT + 14, f"{label_y:.1f}", end_label, "end"))

        if stage == 3:
            year = crossover_year(style)
            x = x_position(year)
            file_y = y_position(values[(style, "File")][year], panel_top)
            vinyl_y = y_position(values[(style, "Vinyl")][year], panel_top)
            parts.append(f'<line x1="{x:.1f}" y1="{panel_top}" x2="{x:.1f}" y2="{panel_top + PANEL_HEIGHT}" class="cross"/>')
            for y in (file_y, vinyl_y):
                parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#ffffff" stroke="#9a612f" stroke-width="3"/>')
            box_x = min(x + 12, WIDTH - RIGHT - 205)
            box_y = panel_top + 12
            parts.append(f'<rect x="{box_x:.1f}" y="{box_y:.1f}" width="195" height="52" rx="5" fill="#ffffff" fill-opacity="0.94" stroke="#c99a70"/>')
            parts.append(text(f"{box_x + 10:.1f}", f"{box_y + 19:.1f}", "File exceeds Vinyl", "callout"))
            parts.append(text(f"{box_x + 10:.1f}", f"{box_y + 42:.1f}", str(year), "callout-year"))

    parts.extend([
        text(LEFT + PLOT_WIDTH / 2, 867, "Release year", "axis-title", "middle"),
        f'<text x="24" y="470" class="axis-title" text-anchor="middle" transform="rotate(-90 24 470)">Number of cataloged release versions</text>',
        '<line x1="55" y1="895" x2="1345" y2="895" stroke="#d7d3cf"/>',
        text(55, 922, "Source: Discogs December 2025 release dump. Catalog records, not sales or listening. Formats may overlap.", "source"),
        '</svg>',
    ])
    return "\n".join(parts)


def main():
    expected_crossovers = {"House": 2008, "Techno": 2008, "Ambient": 2003}
    assert {style: crossover_year(style) for style in STYLES} == expected_crossovers
    assert max(value for series in values.values() for value in series.values()) <= MAX_VALUE
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for stage in (1, 2, 3):
        output = make_frame(stage)
        assert f"FINAL STORY FRAME {stage} OF 3" in output and "Source: Discogs" in output
        (DESTINATION / f"story-frame-{stage}.svg").write_text(output, encoding="utf-8")
    final_chart = make_frame(3).replace("Storyboard frame 3 of 3:", "Final chart:").replace(
        "FINAL STORY FRAME 3 OF 3", "DISCOGS RELEASE FORMATS, 1985–2024"
    )
    assert "3 of 3" not in final_chart and "FINAL STORY FRAME" not in final_chart
    (DESTINATION / "final-chart.svg").write_text(final_chart, encoding="utf-8")


if __name__ == "__main__":
    main()
