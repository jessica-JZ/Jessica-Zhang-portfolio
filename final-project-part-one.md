| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Data visualization examples](https://jessica-jz.github.io/Jessica-Zhang-portfolio/dataviz-examples) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# In the Discogs Catalog, File Releases Became Dominant—but Vinyl Releases Remained

*A Discogs comparison of Vinyl, CD, and File releases in House, Techno, and Ambient, 1985–2024*

## High-level summary

File-based distribution changed how electronic music was released, but it did not eliminate physical formats. For this project, I want to examine how the mix of Vinyl, CD, and File releases changed between 1985 and 2024 within House, Techno, and Ambient. I selected these styles because they are three parts of electronic music that I am interested in exploring. They are focused case studies, not a representative sample of the entire genre.

My intended audience is music-history enthusiasts and electronic-music listeners who are curious about format changes but may not have a technical data background. In Discogs, `File` and `Vinyl` describe how a release was issued; they do not reveal whether the music was recorded, mastered, or transferred using analog or digital technology. The project will therefore tell a music-history story about changes in cataloged release formats, not about sound quality, production methods, listening habits, or sales.

### One-sentence summary

This project shows how File releases became dominant in Discogs release-version counts while vinyl releases remained present, with House, Techno, and Ambient following different paths between 1985 and 2024.

### Audience and purpose

The primary audience is music-history enthusiasts and electronic-music listeners, including collectors, who are curious about how release formats changed but may not have a technical data background. After viewing the project, they should understand four ideas: release format is different from recording technology; the main chart counts cataloged release versions rather than listeners or sales; growth in File releases can coexist with continued vinyl releases; and House, Techno, and Ambient did not follow identical format transitions.

## Story structure

### 1. The distinction: format is not recording technology

The story will open by separating two ideas that are easy to confuse. A release labeled Vinyl may have been produced from a digital master, while `File` identifies a release format rather than the method used to record the music. This distinction keeps the story focused on what the Discogs fields can actually show.

Planned visual: a simple annotated timeline that establishes the analysis window. Vinyl and CD are already present at the 1985 boundary; 1993 is the first File-tagged record in this filtered Discogs sample, not a claim about the first digital music release in history. The timeline will orient the reader rather than prove the main claim.

### 2. The transition: the format mix changes

Next, I will show the annual percentage of selected electronic release versions that include Vinyl, CD, or File. For each style and year, the denominator is the number of distinct Discogs release versions that contain at least one of those three selected formats. Releases available only on other formats, such as cassette, are outside this comparison. A release can include more than one selected format, so the percentages are overlapping attributes rather than parts of a required 100% total. The measure will be shown as a percentage as well as a count so that growth in the size of the Discogs catalog does not automatically look like growth in every format.

Planned visual: aligned lines for format share, paired with a small line chart for total cataloged releases. The lines are more accurate than a 100% stacked chart because 2,001 releases in the cleaned data have more than one selected format. The total-count chart supplies the denominator context needed to interpret the shares.

### 3. The complication: electronic styles do not move together

The project will then compare House, Techno, and Ambient. Small-multiple line charts will use the same scale and time range so the audience can compare the styles without learning a new chart form. The analysis will examine how the timing and shape of the Vinyl decline differed across the three styles rather than treating Electronic as one uniform category.

Planned visual: three aligned line charts showing the percentage of releases tagged with each selected format. Annotations will mark when File first exceeds Vinyl in the filtered data: 2003 for Ambient and 2008 for House and Techno. These are transitions within the selected Discogs records, not dates for the music industry as a whole.

### 4. The second lens: versions and works answer different questions

Before the conclusion, I will compare the release-version result with a 2024 master-level check. The first measure asks how many separately cataloged versions include a format. The second asks whether an identifiable work has at least one version in that format. Showing these views separately will make clear why Vinyl can represent a smaller share of release versions while still being available for a substantial share of works.

Planned visual: a paired-dot chart for File and Vinyl at the master level, clearly separated from the annual release-version chart. A note will explain that the percentages can overlap and that only records with a usable `master_id` are included.

### 5. The conclusion: a format shift, not a production story

The ending will show that File became the largest of the three selected format categories in release-version counts, while vinyl releases remained present in thousands of cataloged versions each year. Across 2022–2024, File appeared on 69.8%–75.2% of filtered release versions across the three styles, while Vinyl appeared on 19.8%–25.1%. This is evidence of coexistence in cataloged release formats, not evidence about sound quality, consumer preference, or whether a vinyl record was made from an analog or digital master. A second, master-level view will answer a different question: whether a cataloged work had at least one version in a format.

## Initial sketches

The storyboard and chart sketches below show how the evidence will unfold. The first maps the five-part reading sequence. The remaining sketches use preliminary results to test the planned comparisons, labels, scales, and qualifications before I build the final Tableau views.

### Sketch 1: Overall story flow

![Five-panel storyboard showing the definition, historical transition, recent summary, master-level check, and qualified conclusion](assets/final-project-part-one/storyboard.svg?v=14)

### Sketch 2: Preliminary chart refinement

I refined the second chart idea with preliminary data to test whether the proposed story is supported. Among the three selected format categories, File accounted for the largest share of filtered Discogs release versions in House, Techno, and Ambient, but the transitions did not follow identical paths. Pooling the last three complete years, 2022–2024, File appeared on 72.4% of House release versions, 75.2% of Techno release versions, and 69.8% of Ambient release versions; Vinyl appeared on 25.1%, 22.7%, and 19.8%, respectively. The three-year window reduces dependence on a single recent endpoint. For each style and year, the denominator contains distinct release versions tagged with at least one selected format: Vinyl, CD, or File.

The percentages measure whether a release version includes each format. They are not mutually exclusive: 2,001 of the 1,247,145 filtered release versions, or 0.16%, contain more than one selected format. The lines therefore should not be read as components that must add to exactly 100%, although the overlap at the release-version level is small.

![Preliminary line chart comparing Vinyl, CD, and File shares for House, Techno, and Ambient](assets/final-project-part-one/preliminary-format-share.svg?v=7)

### Sketch 3: The recent result and its denominator

This compact view will summarize the most recent complete three-year period without relying on a single endpoint. File and Vinyl are shown as separate, overlapping attributes rather than slices of one whole. The note under Ambient makes the narrower coverage visible at the moment the reader encounters that result.

![Paired-dot sketch comparing pooled 2022–2024 File and Vinyl percentages in House, Techno, and Ambient](assets/final-project-part-one/recent-format-summary.svg?v=1)

### Sketch 4: Vinyl releases remained in absolute counts

A percentage alone cannot show whether vinyl releases disappeared. This count view therefore accompanies the share chart. It shows that Discogs still contains thousands of Vinyl-tagged release versions in recent years, while avoiding a claim that the count is currently rising. The panels use the same scale so that the styles can be compared honestly.

![Small-multiple sketch of annual Vinyl-tagged release-version counts from 2015 through 2024](assets/final-project-part-one/vinyl-absolute-counts.svg?v=1)

### Sketch 5: A different unit of analysis

The master-level chart is intentionally separate because it answers a different question. Its percentages can overlap: one work may have both a File version and a Vinyl version. This view will help readers understand that File dominates the count of individual versions, while Vinyl is still available for many identifiable works in the 2024 subset.

![Paired-dot sketch showing the percentage of 2024 Discogs masters with at least one File or Vinyl version](assets/final-project-part-one/master-format-view.svg?v=1)

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

The filters were applied in that order. This audit trail shows how the source records were reduced:

| Step | Releases |
|---|---:|
| All releases in the source snapshot | 18,724,693 |
| Tagged `Electronic` | 4,813,369 |
| Excluded because the year was missing or outside 1985–2024 | 496,258 |
| Excluded because none of the three selected styles was present | 2,899,365 |
| Excluded because none of the three selected formats was present | 170,601 |
| Included distinct release versions | 1,247,145 |

The exclusion counts are sequential, so each release appears in only one exclusion row.

### Why these categories?

I chose House, Techno, and Ambient because they are three electronic styles I am interested in comparing. The project treats them as case studies rather than evidence about all electronic music. I compare Vinyl, CD, and File because they support the physical-to-file transition at the center of the story. Releases available only on other formats, including cassette, are excluded from the denominator. The results therefore describe the mix among three selected formats rather than the complete format market.

The period begins in 1985 as a consistent analytical boundary, not as a claim about the beginning of vinyl or electronic music. It ends in 2024 because that is the last complete calendar year before the December 2025 source snapshot.

### Coverage of the three selected formats

The three-format comparison does not cover every release format equally well across the styles. In 2024, Vinyl, CD, or File appeared on 97.7% of the House records and 96.0% of the Techno records in scope, but only 76.9% of the Ambient records. Cassette alone appeared on 13.3% of the 2024 Ambient records.

| Style | Releases in all formats | Releases with Vinyl, CD, or File | Selected-format coverage | Releases with Cassette |
|---|---:|---:|---:|---:|
| House | 11,998 | 11,724 | 97.7% | 142 (1.2%) |
| Techno | 15,204 | 14,597 | 96.0% | 296 (1.9%) |
| Ambient | 14,603 | 11,228 | 76.9% | 1,941 (13.3%) |

Ambient must therefore be interpreted as a comparison among Vinyl, CD, and File rather than a complete account of its physical-format history. The linked coverage file also includes 2022 and 2023.

The cleaned file retains `release_id`, `master_id`, `year`, `country`, `style`, `format`, and the original format descriptions. Style and format are multi-value fields. I created one row per release-style-format combination and kept the release ID so I can calculate distinct-release counts. Chart labels will say “releases tagged with this style” when categories overlap.

I checked record counts by year and style, missing country values, and overlapping format labels. If a single recording has several separate release versions, those versions can appear more than once in the release data. The main unit of analysis is therefore a cataloged release version. I also completed a sensitivity check using `master_id` where available.

### A second view: does a master have a File or Vinyl version?

Discogs stores different editions, regional versions, reissues, and format variants as separate release records, which can give some works more weight in the release-version chart. I therefore calculated a second view after deduplicating 2024 records by `master_id` within each style. This is not the same measure as release-version share: it asks whether a master represented in the filtered 2024 records had at least one File or Vinyl version.

| Style | Masters with a File version | Masters with a Vinyl version |
|---|---:|---:|
| House | 64.3% | 50.1% |
| Techno | 74.8% | 56.4% |
| Ambient | 65.1% | 39.6% |

These percentages overlap because one master may have both File and Vinyl release versions. The higher Vinyl percentages do not invalidate the release-version result; they reveal a different pattern. File accounts for more individual cataloged versions, while a substantial share of the identifiable works also have a Vinyl version. Only 651,067 of the 1,247,145 filtered release versions have a usable master ID, so this second view applies to a partial subset and does not replace the release-version analysis.

### What the data can and cannot show

Discogs is a community-built catalog. The data can show how release versions in its catalog are tagged by year, style, and format. It cannot directly show:

- how many people listened to or purchased a release;
- whether vinyl is more popular or has better audio quality;
- whether a Vinyl release was cut from an analog or digital master;
- whether an online recording was transferred from a vinyl record;
- why an artist or label selected a particular format; or
- whether Discogs coverage is equally complete across styles, countries, and years.

Different file formats or data rates may also be cataloged as separate release versions under Discogs guidelines. Release-version counts can therefore give works with more editions or variants more weight, and should not be interpreted as market share. Recent years may continue to receive community-contributed entries after the snapshot date; this is another reason the main summary uses a pooled 2022–2024 window rather than relying only on 2024.

These limits will appear beside the charts rather than only at the bottom of the page.

### Working data and documentation

- Official source: [Discogs Data](https://data.discogs.com/)
- Discogs field and submission guidance: [Database Guidelines 1: General Rules](https://support.discogs.com/hc/en-us/articles/360005006334-Database-Guidelines-1-General-Rules)
- Discogs format definitions: [Database Guidelines 6: Format](https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format)
- [Cleaned release-level CSV, gzip compressed](data/final-project-part-one/discogs-electronic-formats-1985-2024.csv.gz)
- [Annual counts for Tableau](data/final-project-part-one/discogs-annual-style-format-counts.csv)
- [Annual format shares for Tableau](data/final-project-part-one/discogs-annual-style-format-shares.csv)
- [2024 master-level sensitivity check](data/final-project-part-one/discogs-2024-master-sensitivity.csv)
- [2022–2024 selected-format and Cassette coverage](data/final-project-part-one/discogs-2022-2024-format-coverage.csv)
- [Data quality summary](data/final-project-part-one/data-quality-summary.txt)
- [Data processing documentation](data/final-project-part-one/README.md)
- [Extraction script](scripts/extract-discogs-electronic.py)
- [Format coverage audit script](scripts/audit-discogs-format-coverage.py)

I downloaded the December 2025 release snapshot and verified its SHA-256 checksum against Discogs' checksum file. The filtered CSV contains 1,345,791 rows representing 1,247,145 distinct release versions. The larger row count occurs because releases with several selected styles or formats are expanded into separate rows. The project README records the source snapshot, checksum, filters, grouping rules, exclusions, and row counts.

## Method and medium

The final project will be a scrolling data story published on GitHub Pages and designed as a small digital music-history exhibition rather than a dashboard. I plan to create the charts in Tableau and embed or export them for the page. The reader will move through the story in a fixed order, beginning with the meaning of the format labels before moving into the historical patterns. Limited interaction, such as a style selector or details on hover, may help readers inspect the evidence without interrupting the narrative.

The visual design will use a restrained, archive-inspired palette: neutral gray for context, one consistent color for Vinyl, and distinct colors for CD and File. A simple record motif and timeline can provide historical context, but I will avoid copyrighted album artwork, artist photographs, and logos. Labels and annotations will be placed near the data they explain. Counts, percentages, dates, the denominator, and the unit of analysis will remain visible.

### Audience testing plan

Before Part II is finalized, I will ask several people in the intended audience to view the story without additional explanation. I will use these questions to test whether the wording and charts communicate the intended distinctions:

1. What do `File` and `Vinyl` measure in this project?
2. Do you expect the three format percentages to add to exactly 100%? Why or why not?
3. What is the difference between the release-version chart and the master-level table?
4. After viewing the story, would you describe vinyl releases as disappearing, growing, or remaining present?
5. What limitation would you mention before applying the Ambient result to all of its physical formats?

## References

Discogs. “Discogs Data.” Monthly database dumps. Accessed September 19, 2026. https://data.discogs.com/

Discogs. “Database Guidelines 1: General Rules.” Accessed September 19, 2026. https://support.discogs.com/hc/en-us/articles/360005006334-Database-Guidelines-1-General-Rules

Discogs. “Database Guidelines 6: Format.” Accessed September 19, 2026. https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format

## AI acknowledgement

I used ChatGPT to help me revise the writing.
