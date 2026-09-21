# Discogs electronic formats dataset: processing plan

## Source snapshot

- Publisher: Discogs
- Source page: https://data.discogs.com/
- Intended file: `discogs_20251201_releases.xml.gz`
- Listed compressed size: approximately 10.2 GB
- Verified SHA-256: `43c3c22173092bf4595249f33e1f045ba5d6ce434a36b7eb6fb4efb50ee04bc1`
- License stated by publisher: CC0 No Rights Reserved
- Analysis period: release years 1985–2024

The monthly release file is a full database snapshot. Only one snapshot should be used for this project.

## Output

`discogs-electronic-formats-1985-2024.csv.gz`

The filtered file contains 1,345,791 data rows and 1,247,145 distinct Discogs release IDs. Its uncompressed size is approximately 67 MB. Summary files are also included for Tableau:

- `discogs-annual-style-format-counts.csv`
- `discogs-annual-style-format-shares.csv`
- `discogs-2024-master-sensitivity.csv`
- `discogs-2022-2024-format-coverage.csv`
- `data-quality-summary.txt`

The repository stores the detailed CSV with gzip compression. Its SHA-256 checksum is `1ff94bad0a6c5b18dfb73e7a1720b7c3b6ba20783e394963109d51271547e015`.

Columns:

| Column | Meaning |
|---|---|
| `release_id` | Discogs release identifier |
| `master_id` | Discogs master-release identifier when available |
| `year` | Stated release year |
| `country` | Discogs release country |
| `style` | One selected style: House, Techno, or Ambient |
| `format` | One grouped format: Vinyl, CD, or File |
| `format_description` | Original format description retained for checking |

## Filtering and reshaping rules

1. Keep releases whose genre list contains `Electronic`.
2. Keep years from 1985 through 2024.
3. Keep records tagged with at least one selected style: `House`, `Techno`, or `Ambient`.
4. Keep records with at least one selected format: `Vinyl`, `CD`, or `File`.
5. Expand multi-value style and format fields into release-style-format rows.
6. Preserve `release_id` so charts can use distinct release counts.
7. Do not treat style totals as mutually exclusive.
8. Record the number of excluded records and missing values after processing.

## Required checks before analysis

- Verify the downloaded file against the publisher's checksum.
- Confirm that yearly counts are plausible and investigate sudden discontinuities.
- Inspect raw format names and descriptions before grouping.
- Compare release-level counts with master-level counts to assess the effect of reissues and regional versions.
- Document all changes to the filtering or grouping rules.

## Completed quality checks

- Full source SHA-256 matched the Discogs checksum.
- Source releases read: 18,724,693.
- Releases tagged Electronic: 4,813,369.
- Included distinct release versions: 1,247,145.
- Included rows after expanding styles and formats: 1,345,791.
- Releases without a usable master ID: 596,078.
- Releases without country: 53,210.
- Releases with more than one selected format: 2,001.
- Releases with more than one selected style: 76,325.
- A 2024 sensitivity check deduplicated records by `master_id` within each style and year. The direction of the main result did not change, although only records with a usable master ID could be included.

Because formats can overlap, format percentages should be shown as separate lines or bars rather than forced into a 100% stacked chart.

## Reproduction scripts

- `scripts/extract-discogs-electronic.py` filters the official release dump.
- `scripts/summarize-discogs.py` creates the annual count and share tables.
- `scripts/plot-preliminary-results.py` creates the preliminary SVG evidence check.
- `scripts/audit-discogs-format-coverage.py` measures how much of each style is covered by the three selected formats and reports Cassette separately.

## Interpretation

The output will describe release versions cataloged by Discogs. It will not measure listeners, streams, sales, production methods, or the source of audio uploaded to the internet.
