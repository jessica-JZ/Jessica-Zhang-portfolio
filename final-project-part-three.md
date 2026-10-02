| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# Digital files took the lead. Vinyl releases remained. {#the-final-data-story}

*House, Techno, and Ambient in the Discogs catalog, 1985–2024*

Read the [final Shorthand story](https://carnegiemellon.shorthandstories.com/23fdf1b6-4f4c-42d7-b816-1c06513afc1a/index.html). This page also keeps the two Tableau views and documents how I made them.

If you find electronic music online but still see vinyl editions in record shops or DJ sets, you may wonder whether one format has displaced the other. In the Discogs catalog, digital-file versions overtook vinyl versions in House, Techno, and Ambient. Did vinyl disappear? First, look at vinyl on its own. Then compare the two formats in the second Tableau chart.

Each line counts **cataloged release versions**, not albums sold or people listening. A vinyl edition and a download of the same album count as two versions. Discogs labels the download format `File`; I call it “digital file” here. The format tag describes the release medium, not how the music was recorded or mastered.

## 1. Start with vinyl

[Open the vinyl chart on Tableau Public](https://public.tableau.com/views/VinylbyStyle-Baseline/Vinylbaselinebystyle) for a larger view.

<div style="max-width: 100%; overflow-x: auto;">
<iframe title="Tableau chart of cataloged Vinyl Record versions in House, Techno, and Ambient, 1985–2024" src="https://public.tableau.com/views/VinylbyStyle-Baseline/Vinylbaselinebystyle?:showVizHome=no&amp;:embed=yes" width="100%" height="650" style="border: 0; min-width: 960px;" loading="lazy" allowfullscreen></iframe>
</div>

House fell from 11,121 Vinyl versions at its 1996 peak to 3,022 in 2024. Techno peaked at 6,510 in 1992 and counted 3,442 in 2024; Ambient reached 3,051 in 2021 and counted 2,515 in 2024. The paths differ: between 2010 and 2019, cataloged vinyl versions rose from 2,999 to 5,033 in Techno and from 641 to 2,732 in Ambient, while House was nearly flat (3,442 to 3,393). Vinyl's continued presence was not just a line hovering above zero.

**Read these as Discogs catalog counts, not market totals.** People may still add recent releases, so the 2021–2024 endpoints—including Ambient's apparent peak—may change.

## 2. Compare files and vinyl

The Tableau chart adds the medium-gray Digital File line to the blue Vinyl line. Use the **Style** list to focus on Ambient, House, or Techno, or select **(All)** to compare them side by side. Hover over a line for the count in a particular year; the visible end labels show 2024 counts. Ambient Vinyl counted 2,515 versions in 2024; its label is omitted where it would cover the line.

As you switch styles, look for the annotated first year File exceeds Vinyl: **2003 in Ambient; 2008 in House and Techno.** Ambient's 2003 counts were still relatively small: 637 File versions and 446 Vinyl versions. The takeaway is that File took the lead in the catalog, while Vinyl continued to be listed. The **(All)** view uses the same zero-based y-axis scale across the three panels; when you filter to one style, the axis may rescale. Compare the counts, not only the apparent steepness of the lines.

[Open the chart on Tableau Public](https://public.tableau.com/views/FileandVinylbyStyleInteractive/03Finalannotatedchart) for a larger view.

<div style="max-width: 100%; overflow-x: auto;">
<iframe title="Tableau chart with a Style menu for comparing cataloged Digital File and Vinyl Record versions in House, Techno, and Ambient, 1985–2024" src="https://public.tableau.com/views/FileandVinylbyStyleInteractive/03Finalannotatedchart?:showVizHome=no&amp;:embed=yes" width="100%" height="650" style="border: 0; min-width: 960px;" loading="lazy" allowfullscreen></iframe>
</div>

By **2019**, File already outnumbered Vinyl by about **3.4 to 1 in House, 3.0 to 1 in Techno, and 4.9 to 1 in Ambient**. Those ratios use a year before the recent cataloging window. The 2024 entries still show thousands of vinyl versions in each style, but their totals—and the downward turns after 2020—may change as Discogs fills in.

These are crossover years in the filtered Discogs catalog, not dates when listeners switched formats. These selected styles do not represent electronic music as a whole. For a non-interactive copy, [view the original Tableau export](assets/final-project-part-three/final-chart-tableau.png).

## What the chart can—and cannot—show

To read this evidence, start with what the lines count. I filtered the [December 2025 Discogs release dump](https://data.discogs.com/) to records dated 1985–2024, tagged `Electronic` and at least one of House, Techno, or Ambient, and issued in Vinyl, CD, or File. The lines count distinct release IDs within each style and format. CD is kept in the processed data but is not plotted here. A release can have more than one format tag, so these counts do not add up to a 100% whole. A release can also carry several style tags, so the three panels overlap and should not be added together. The [data documentation](data/final-project-part-one/README.md) records the full filters and exclusions.

Discogs is a community-built catalog, and its coverage may differ across formats and years. The comparison excludes releases tagged only with other formats. Among all 2024 Ambient releases tagged Electronic in this snapshot, 76.9% had Vinyl, CD, or File and 13.3% had Cassette; those groups can overlap. The chart is therefore not a full account of Ambient's physical releases. If physical editions are more likely to be cataloged than digital-only editions, these data would overstate Vinyl's presence relative to File. I have not measured whether that bias exists.

The first File-tagged records in this filtered sample appear in 1993. That is not the date of the first digital music release. Techno and Ambient File counts peak in 2020 in this snapshot, then decline; the data used for these charts cannot explain why. Later catalog entries can also change recent-year counts. These data cannot establish sales, listening, format preference, or sound quality.

# Behind the story: changes made since Part II

In Part I, I compared Vinyl, CD, and File and tested sketches using format shares, release counts, and a master-level check. Part II narrowed the reader-facing question to whether vinyl disappeared after files took the lead. I built a three-frame Tableau storyboard, then used three full interviews and two focused critiques to test its wording and visual sequence. Later comments on the Part III page prompted the clearer three-style vinyl comparison and the 2019 headline ratios. The published Shorthand story uses a Vinyl-only Tableau view followed by an interactive File-versus-Vinyl view; this page keeps both views beside the methods and design process.

The title states the two-part result, and the first view shows Vinyl alone before readers compare it with File. Peaks and later counts for all three styles appear beside that view so “remained” does not sound like “held steady.” The definition of a release version appears before the charts, where readers need it.

| Feedback (source) | What I changed | Where readers can see it |
| --- | --- | --- |
| “Vinyl remained” sounded too much like “held steady” (Part II interviews) | Added House's decline and the different Techno and Ambient paths | Text beside the Vinyl baseline |
| “Release version” was unclear (two Part II readers) | Defined it with one album issued as vinyl and as a download | Before the first chart |
| The File line was hard to see (focused critiques) | Changed it from light gray to a more legible medium gray | File-versus-Vinyl Tableau view |
| The finding relied too much on 2024 (Part III reader comments) | Used 2019 ratios for the main comparison and kept 2024 provisional | Comparison conclusion and methods |

The [Part II storyboard](final-project-part-two#storyboard) tested three progressive Tableau views. On this page, I published the Vinyl-only baseline as a Tableau view, then embedded a copy of my Tableau comparison with a visible Style list. Readers can isolate a style or return to all three. The linked static Tableau export preserves a non-interactive copy.

I moved the Ambient cassette context below the main finding, into the limitations paragraph, because the two-format lines do not cover every Ambient record. I also kept the three styles as supporting examples rather than making Ambient's earlier crossover the central claim.

## The audience

I wrote for electronic-music listeners who use digital access but still encounter vinyl editions through DJs, record shops, or label releases. They may know House, Techno, and Ambient without knowing Discogs's database fields. The story therefore defines a release version above the chart: a vinyl edition and a download of one album count as separate versions. It also says early that a format tag is not evidence about recording technology, sales, or listening.

Part II supplied three full interviews and two focused classmate critiques. Across the full interviews, readers understood the main format shift, but “vinyl remained” sounded too vague when House vinyl counts had fallen substantially. Two readers hesitated over “release version.” The focused critiques raised line contrast and label size. Later Part III reader comments asked for more detail on Techno and Ambient, a clearer Discogs-only caveat, and less reliance on 2024 for the headline comparison. I used those comments to revise this page; they are not a representative sample of all electronic-music listeners. I have not tested this revised version with a new reader.

## Final design decisions

The final story uses two Tableau views: a Vinyl-only introduction and a File-versus-Vinyl comparison with a visible Style list. The baseline no longer shows a redundant Style filter or one-series legend; its lines are labeled Vinyl. Vinyl is blue and File is medium gray, with the format names repeated in the text. The crossover years are annotated in the comparison chart. I use 2019 for the headline ratios and treat 2024 as provisional evidence that vinyl entries continued. In the all-styles view, the y-axis starts at zero and has the same scale in each style panel; filtering can rescale it. I avoided a 100% stacked chart because one Discogs release can have more than one format tag. Shorthand holds the reader story; this GitHub page documents the process and keeps the Tableau views available.

## References

- Discogs, [monthly data dumps](https://data.discogs.com/), `discogs_20251201_releases.xml.gz` release snapshot. Discogs states that the dump is CC0 No Rights Reserved. The [Part I data section](final-project-part-one#data) records the snapshot, filtering steps, and limitations.
- Discogs, [Database Guidelines 6: Format](https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format), for format tags.
- Berinato, Scott. [*Good Charts: The HBR Guide to Making Smarter, More Persuasive Data Visualizations*](https://store.hbr.org/product/good-charts-the-hbr-guide-to-making-smarter-more-persuasive-data-visualizations/15005). Harvard Business Review Press, 2016, Chapter 7, “Persuasion or Manipulation? The Blurred Edge of Truth.” I used its distinction between visual emphasis and an unsupported conclusion.
- [GitHub repository](https://github.com/jessica-JZ/Jessica-Zhang-portfolio), [data preparation documentation](data/final-project-part-one/README.md), and [processed release records](https://github.com/jessica-JZ/Jessica-Zhang-portfolio/blob/main/data/final-project-part-one/discogs-electronic-formats-1985-2024.csv.gz).
- Both embedded charts and the linked static export are my Tableau visualizations of the processed Discogs release records. The Shorthand cover uses a [vinyl photo by Miguel Á. Padriñán on Pexels](https://www.pexels.com/photo/close-up-photo-of-vinyl-disc-3391930/); this GitHub page uses no third-party photographs, album covers, or logos. [Part II](final-project-part-two#storyboard) shows the comparison in three Tableau stages.

## AI acknowledgements

I chose the topic, made the original Tableau chart, decided which feedback to use, and remain responsible for the final interpretation. I used ChatGPT to check the Discogs processing workflow and help revise the Shorthand story and this write-up. The displayed counts and crossover years were checked against the processed data. A separate simulated target-audience critique informed early design thinking; it was not one of the five human feedback sources. ChatGPT did not generate or alter participants' comments.

# Final thoughts

I began with a wider format story that included CD, percentages, and a separate master-level view. Feedback on Part I and interviews in Part II helped me narrow the public story to File and Vinyl; the other measures remain in the data and methods pages. The release-version lines show coexistence in the catalog, but they cannot explain why people choose vinyl or how many copies sold. The next useful check would be to ask a fresh reader to try this revised page and say whether the two Tableau views make that distinction clear.
