| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# Digital files took the lead. Vinyl releases remained. {#the-final-data-story}

*House, Techno, and Ambient in the Discogs catalog, 1985–2024*

When digital-file versions overtook vinyl versions in these Discogs records, did vinyl disappear? The answer is more complicated: files moved ahead in House, Techno, and Ambient, but vinyl versions continued. The three views below reveal that change one step at a time.

Each line counts **cataloged release versions**, not albums sold or people listening. A vinyl edition and a download of the same album count as two versions. Discogs labels the download format `File`; I call it “digital file” here. The format tag describes the release medium, not how the music was recorded or mastered.

## 1. Start with vinyl: decline is not disappearance

![Vinyl release-version counts for House, Techno, and Ambient from 1985 to 2024 on the same scale. Vinyl continues through 2024 in all three styles.](assets/final-project-part-three/story-frame-1.svg)

[Open the vinyl chart at full size](assets/final-project-part-three/story-frame-1.svg).

House fell from 11,121 Vinyl versions at its 1996 peak to 3,022 in 2024. Vinyl also remains above zero in Techno and Ambient. “Remained” does not mean “held steady.”

## 2. Add files: a new leader, not a replacement

![The same House, Techno, and Ambient panels and axes now compare File in gray with Vinyl in blue. File counts are higher in each style by 2024.](assets/final-project-part-three/story-frame-2.svg)

[Open the two-format chart at full size](assets/final-project-part-three/story-frame-2.svg).

By 2024, File outnumbered Vinyl in each style: House had 8,428 File versions versus 3,022 Vinyl; Techno, 10,877 versus 3,442; Ambient, 7,418 versus 2,515. The gray lines lead, while the blue lines continue.

## 3. Mark the crossover: when did files move ahead?

![The same comparison with the first File-over-Vinyl year marked: 2008 for House and Techno, and 2003 for Ambient. The Vinyl lines continue through 2024.](assets/final-project-part-three/story-frame-3.svg)

[Open the annotated chart at full size](assets/final-project-part-three/story-frame-3.svg). [View the original Tableau export](assets/final-project-part-three/final-chart-tableau.png).

File first exceeded Vinyl in 2008 for House and Techno, and in 2003 for Ambient. These are crossover years in the filtered Discogs catalog, not dates when listeners switched formats. These selected styles do not represent electronic music as a whole. The distinction matters for listeners and collectors: a format can lose the lead without disappearing from release catalogs.

## What the chart can—and cannot—show

To read this evidence, start with what the lines count. I filtered the [December 2025 Discogs release dump](https://data.discogs.com/) to records dated 1985–2024, tagged `Electronic` and at least one of House, Techno, or Ambient, and issued in Vinyl, CD, or File. The lines count distinct release IDs within each style and format. A release can have more than one format tag, so these counts do not add up to a 100% whole. The [data documentation](data/final-project-part-one/README.md) records the full filters and exclusions.

Discogs is a community-built catalog, and its coverage may differ across formats and years. The comparison excludes releases tagged only with other formats. Among all 2024 Ambient releases tagged Electronic in this snapshot, 76.9% had Vinyl, CD, or File and 13.3% had Cassette; those groups can overlap. The chart is therefore not a full account of Ambient's physical releases. Physical editions may also be more likely to be cataloged than digital-only editions; I have not measured that possible bias.

The first File-tagged records in this filtered sample appear in 1993. That is not the date of the first digital music release. The downward lines after 2020 describe this December 2025 snapshot; later catalog entries can change recent-year counts. These data cannot establish sales, listening, format preference, or sound quality.

# Behind the story: changes made since Part II

In Part I, I compared Vinyl, CD, and File and tested sketches using format shares, release counts, and a master-level check. Part II narrowed the reader-facing question to whether vinyl disappeared after files took the lead. I built a three-frame Tableau storyboard, then used three full interviews and two focused critiques to test its wording and visual sequence. This page now unfolds the comparison in three stages before the methods and design process.

The title states the two-part result, and the first view shows Vinyl alone before readers compare it with File. House's decline from its 1996 peak appears beside that view so “remained” does not sound like “held steady.” The definition of a release version appears before the charts, where readers need it.

The [Part II storyboard](final-project-part-two#storyboard) tested three progressive Tableau views. For this scrolling page, I used three exported story frames based on the same processed data. Their scales, panel order, and colors stay fixed; the second adds File, and the third adds crossover annotations. Each has a full-size link because labels become small when a wide chart is scaled down.

I moved the Ambient cassette context below the main finding, into the limitations paragraph, because the two-format lines do not cover every Ambient record. I also kept the three styles as supporting examples rather than making Ambient's earlier crossover the central claim.

## The audience

I wrote for electronic-music listeners who use digital access but still encounter vinyl editions through DJs, record shops, or label releases. They may know House, Techno, and Ambient without knowing Discogs's database fields. The story therefore defines a release version above the chart: a vinyl edition and a download of one album count as separate versions. It also says early that a format tag is not evidence about recording technology, sales, or listening.

Part II supplied three full interviews and two focused classmate critiques. Across the full interviews, readers understood the main format shift, but “vinyl remained” sounded too vague when House vinyl counts had fallen substantially. Two readers hesitated over “release version.” The focused critiques raised line contrast and label size. I treated these five responses as feedback on the page, not as a representative sample of all electronic-music listeners. I did not conduct another interview round for this final page.

## Final design decisions

The final page uses a familiar line-chart comparison revealed in three stages. Vinyl is blue and File is warm gray, with the format names repeated in the text. Direct 2024 counts and crossover annotations point to the evidence without making readers reconstruct it. The y-axis starts at zero and has the same scale in every panel and frame. I avoided a 100% stacked chart because one Discogs release can have more than one format tag. The story and process live together on GitHub Pages under the course template.

## References

- Discogs, [monthly data dumps](https://data.discogs.com/), `discogs_20251201_releases.xml.gz` release snapshot. Discogs states that the dump is CC0 No Rights Reserved. The [Part I data section](final-project-part-one#data) records the snapshot, filtering steps, and limitations.
- Discogs, [Database Guidelines 6: Format](https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format), for format tags.
- Berinato, Scott. [*Good Charts: The HBR Guide to Making Smarter, More Persuasive Data Visualizations*](https://store.hbr.org/product/good-charts-the-hbr-guide-to-making-smarter-more-persuasive-data-visualizations/15005). Harvard Business Review Press, 2016, Chapter 7, “Persuasion or Manipulation? The Blurred Edge of Truth.” I used its distinction between visual emphasis and an unsupported conclusion.
- [GitHub repository](https://github.com/jessica-JZ/Jessica-Zhang-portfolio), [data preparation documentation](data/final-project-part-one/README.md), and [processed release records](https://github.com/jessica-JZ/Jessica-Zhang-portfolio/blob/main/data/final-project-part-one/discogs-electronic-formats-1985-2024.csv.gz).
- The three story frames were generated from the processed Discogs release records; the linked original chart is a Tableau export from the same records. This page uses no third-party photographs, album covers, or logos. [Part II](final-project-part-two#storyboard) shows the comparison in three Tableau stages.

## AI acknowledgements

I chose the topic, made the original Tableau chart, decided which feedback to use, and remain responsible for the final interpretation. I used ChatGPT to check the Discogs processing workflow, help generate the three SVG story frames from the processed data, and revise this story and write-up. The displayed counts and crossover years were checked against the processed data. A separate simulated target-audience critique informed early design thinking; it was not one of the five human feedback sources. ChatGPT did not generate or alter participants' comments.

# Final thoughts

I began with a wider format story that included CD, percentages, and a separate master-level view. Feedback on Part I and interviews in Part II helped me narrow the public story to File and Vinyl; the other measures remain in the data and methods pages. The release-version lines show coexistence in the catalog, but they cannot explain why people choose vinyl or how many copies sold. I would test this finished page with readers if I had another round; the feedback reported here came from Part II.
