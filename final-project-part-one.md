| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Data visualization examples](https://jessica-jz.github.io/Jessica-Zhang-portfolio/dataviz-examples) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# Files Took Over, but Vinyl Remained

*Release-format changes in House, Techno, and Ambient, 1985–2024*

## High-level summary

File-based distribution changed how electronic music was released, but it did not eliminate physical formats. For this project, I want to examine how the mix of Vinyl, CD, and File releases changed between 1985 and 2024 within House, Techno, and Ambient. I chose these three styles as a focused comparison within electronic music, not as a representative sample of the entire genre.

My intended audience is people who enjoy electronic music but may not think about the difference between a release format and a recording method. In Discogs, `File` and `Vinyl` describe how a release was issued; they do not reveal whether the music was recorded, mastered, or transferred using analog or digital technology. The project will therefore tell a story about changes in cataloged release formats, not about sound quality, production methods, listening habits, or sales.

### One-sentence summary

This project shows how File releases became dominant while Vinyl remained part of the release mix, with House, Techno, and Ambient following different paths between 1985 and 2024.

### Audience and purpose

The primary audience is electronic-music listeners and collectors who are curious about how music formats change. After viewing the project, they should understand that growth in File releases can coexist with continued Vinyl releases. They should also be able to distinguish a release-format trend from a claim about popularity or about whether a recording itself is analog or digital.

## Story structure

### 1. The distinction: format is not recording technology

The story will open by separating two ideas that are easy to confuse. A release labeled Vinyl may have been produced from a digital master, while `File` identifies a release format rather than the method used to record the music. This distinction keeps the story focused on what the Discogs fields can actually show.

Planned visual: a simple annotated timeline showing when Vinyl, CD, and File releases appear in the selected data. This will orient the reader rather than prove the main claim.

### 2. The transition: the format mix changes

Next, I will show the annual share of selected electronic releases tagged Vinyl, CD, and File. For each style and year, the denominator is the number of distinct Discogs release versions that contain at least one of those three selected formats. Releases available only on other formats, such as cassette, are outside this comparison. The measure will be shown as a percentage as well as a count so that growth in the size of the Discogs catalog does not automatically look like growth in every format.

Planned visual: aligned lines for format share, paired with a small line chart for total cataloged releases. The lines are more accurate than a 100% stacked chart because 2,001 releases in the cleaned data have more than one selected format. The total-count chart supplies the denominator context needed to interpret the shares.

### 3. The complication: electronic styles do not move together

The project will then compare House, Techno, and Ambient. Small-multiple line charts will use the same scale and time range so the audience can compare the styles without learning a new chart form. The analysis will examine how the timing and shape of the Vinyl decline differed across the three styles rather than treating Electronic as one uniform category.

Planned visual: three aligned line charts showing the percentage of releases tagged Vinyl, one for each selected style. A highlighted annotation will identify the largest meaningful difference supported by the cleaned data.

### 4. The conclusion: a format shift, not a production story

The ending will show that File became the largest of the three selected format categories, while Vinyl still represented roughly 22%–26% of filtered releases across the three styles in 2024. This is evidence of coexistence in cataloged release formats, not evidence about sound quality, consumer preference, or whether a vinyl release came from an analog or digital master. I will also explain how multi-format releases and reissues affect the count.

## Initial sketches

The two sketches below show the planned order of the story and the role of each chart. The first is a structural storyboard; its lines and values are placeholders, not results. The second refines the planned comparison using preliminary data.

### Sketch 1: Overall story flow

![Storyboard sketch showing the opening distinction, timeline, paired share and count charts, style comparison, and conclusion](assets/final-project-part-one/storyboard.svg?v=8)

### Sketch 2: Preliminary chart refinement

I refined the second chart idea with preliminary data to test whether the proposed story is supported. File became the largest of the three selected format categories in House, Techno, and Ambient, but the transitions did not follow identical paths. In 2024, 25.8% of House releases, 23.6% of Techno releases, and 22.4% of Ambient releases in the filtered Discogs data were tagged Vinyl. For each style and year, the denominator contains distinct release versions tagged with at least one selected format: Vinyl, CD, or File. Because a release may carry more than one format tag, the three percentages are not parts of a mutually exclusive 100% total.

![Preliminary line chart comparing Vinyl, CD, and File shares for House, Techno, and Ambient](assets/final-project-part-one/preliminary-format-share.svg?v=5)

## Data

### Primary source

The primary source is the [Discogs monthly data dumps](https://data.discogs.com/). Discogs publishes Release, Artist, Label, and Master Release data as XML files and states on the download page that the data is available under the CC0 No Rights Reserved license. I used one dated snapshot rather than combining multiple monthly dumps because each dump is a snapshot of the database rather than a new month of releases.

The release dump contains the fields needed for this project, including release year, genre, style, format, and country. Discogs also explains that Style is required for submissions in the Electronic genre, which makes this source useful for comparing House, Techno, and Ambient. The official release dump is large: the December 2025 compressed file is listed at approximately 10.2 GB. I preserved a link to that source and created a smaller project CSV containing only the selected records and fields.

### Data preparation

I extracted records that meet all of these conditions:

- Genre includes `Electronic`.
- Release year is between 1985 and 2024.
- Style includes `House`, `Techno`, or `Ambient`.
- Format includes `Vinyl`, `CD`, or `File`.
- The year is present and valid.

The cleaned file retains `release_id`, `master_id`, `year`, `country`, `style`, `format`, and the original format descriptions. Style and format are multi-value fields. I created one row per release-style-format combination and kept the release ID so I can calculate distinct-release counts. Chart labels will say “releases tagged with this style” when categories overlap.

I checked record counts by year and style, missing country values, and overlapping format labels. A remaining analysis step is to test the effect of reissues. If a single recording has several separate release versions, those versions can appear more than once in the release data. I will use `master_id` where available for a sensitivity check and state clearly that the main unit is a cataloged release version.

### What the data can and cannot show

Discogs is a community-built catalog. The data can show how release versions in its catalog are tagged by year, style, and format. It cannot directly show:

- how many people listened to or purchased a release;
- whether vinyl is more popular or has better audio quality;
- whether a Vinyl release was cut from an analog or digital master;
- whether an online recording was transferred from a vinyl record;
- why an artist or label selected a particular format; or
- whether Discogs coverage is equally complete across styles, countries, and years.

These limits will appear beside the charts rather than only at the bottom of the page.

### Working data and documentation

- Official source: [Discogs Data](https://data.discogs.com/)
- Discogs field and submission guidance: [Database Guidelines 1: General Rules](https://support.discogs.com/hc/en-us/articles/360005006334-Database-Guidelines-1-General-Rules)
- Discogs format definitions: [Database Guidelines 6: Format](https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format)
- [Cleaned release-level CSV, gzip compressed](data/final-project-part-one/discogs-electronic-formats-1985-2024.csv.gz)
- [Annual counts for Tableau](data/final-project-part-one/discogs-annual-style-format-counts.csv)
- [Annual format shares for Tableau](data/final-project-part-one/discogs-annual-style-format-shares.csv)
- [Data quality summary](data/final-project-part-one/data-quality-summary.txt)
- [Data processing documentation](data/final-project-part-one/README.md)
- [Extraction script](scripts/extract-discogs-electronic.py)

I downloaded the December 2025 release snapshot and verified its SHA-256 checksum against Discogs' checksum file. The filtered CSV contains 1,345,791 rows representing 1,247,145 distinct release versions. The larger row count occurs because releases with several selected styles or formats are expanded into separate rows. The project README records the source snapshot, checksum, filters, grouping rules, exclusions, and row counts.

## Method and medium

The final project will be a scrolling data story published on GitHub Pages. I plan to create the charts in Tableau and embed or export them for the page. The reader will move through the story in a fixed order, with one main idea per section. Limited interaction, such as a style selector or details on hover, may help readers inspect the evidence without turning the project into a standalone dashboard.

The visual design will use a restrained palette: neutral gray for context, one consistent color for Vinyl, and distinct but quieter colors for CD and File. Labels and annotations will be placed near the data they explain. Counts, percentages, dates, and the unit of analysis will remain visible.

## References

Discogs. “Discogs Data.” Monthly database dumps. Accessed September 19, 2026. https://data.discogs.com/

Discogs. “Database Guidelines 1: General Rules.” Accessed September 19, 2026. https://support.discogs.com/hc/en-us/articles/360005006334-Database-Guidelines-1-General-Rules

Discogs. “Database Guidelines 6: Format.” Accessed September 19, 2026. https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format

## AI acknowledgement

I used ChatGPT to help me revise the writing.
