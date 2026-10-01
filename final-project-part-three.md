| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Data visualization examples](https://jessica-jz.github.io/Jessica-Zhang-portfolio/dataviz-examples) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# The final data story

My [published final data story](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-data-story) asks what happened to vinyl-record releases after digital-file releases became more common in the Discogs catalog. The [GitHub repository](https://github.com/jessica-JZ/Jessica-Zhang-portfolio) contains the page, data summaries, chart source, and earlier project work. [Part I](final-project-part-one) records the question, source, filtering, and initial sketches; [Part II](final-project-part-two) shows the storyboard and reader feedback. This page explains what changed for the final version.

Part II named Shorthand as the planned publishing platform. I published the final scrolling sequence on GitHub Pages instead, where the story, source notes, and process pages can link directly to one another.

# Changes made since Part II

I changed the opening to state the result sooner: digital files took the lead, and vinyl releases continued. The first section now names House's decline from 11,121 Vinyl versions at its 1996 peak to 3,022 in 2024. This keeps “continued” from sounding like “unchanged.” The definition of a release version appears before the charts, where readers need it.

The [final story](final-data-story) keeps the three-stage reveal from Part II, but all three frames now use the same layout, axes, panel order, and type treatment. I redrew the third frame from the same annual summary as the first two, adding only the crossover layer. I darkened the File line, enlarged chart labels, and shortened the 2024 end labels for reading at page width. The earlier Tableau export remains visible in the [Part II storyboard](final-project-part-two#progressive-state-3-annotate-the-crossovers); it was the high-fidelity draft, while the consistent frames are the final story presentation. The [chart-generation script](scripts/plot-part-two-storyboard.py) and [annual counts](data/final-project-part-one/discogs-annual-style-format-counts.csv) make the final redraw traceable.

I moved the detailed Ambient cassette context below the story's main sequence. It is still in the final story's “How to read this evidence” section because the two-format comparison covers only 76.9% of the 2024 Ambient records in scope. I also kept the three style panels as supporting cases rather than making Ambient's earlier crossover the central claim. The first File-over-Vinyl years remain marked: 2003 for Ambient and 2008 for House and Techno.

## The audience

I wrote for electronic-music listeners who use digital access but still encounter vinyl editions through DJs, record shops, or label releases. They may know House, Techno, and Ambient without knowing Discogs's database fields. The story therefore defines a release version near the first chart: a vinyl edition and a download of one album count as separate versions. It also says early that a format tag is not evidence about recording technology, sales, or listening.

Part II supplied three full interviews and two focused classmate critiques. Across the full interviews, readers understood the main format shift, but the phrase “vinyl remained” sounded too vague or too positive when House vinyl counts had fallen substantially. Two readers hesitated over “release version.” A reader also noticed that the third chart frame looked different from the first two. The focused critiques raised line contrast and label size. I treated these five responses as feedback on the page, not as a representative sample of all electronic-music listeners. I did not conduct another interview round for this final page.

## Final design decisions

One chart, revealed in stages, lets the reader keep the same scales while asking a new question at each step. Vinyl is blue throughout; File is dark gray, with its meaning repeated in labels and prose. Direct 2024 counts reduce the need to move between a line and a legend. I kept the y-axis anchored at zero and the scale identical across panels so the differences are not exaggerated. I avoided a 100% stacked chart because one Discogs release can have more than one format tag.

## References

- Discogs, [monthly data dumps](https://data.discogs.com/), December 2025 release snapshot. The [Part I data section](final-project-part-one#data) records the snapshot, filtering steps, and limitations.
- Discogs, [Database Guidelines 6: Format](https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format), for format tags.
- Berinato, Scott. *Good Charts*, Chapter 7, “Persuasion or Manipulation? The Blurred Edge of Truth,” informed the distinction between a persuasive visual emphasis and an unsupported conclusion.
- [Data preparation documentation](data/final-project-part-one/README.md), [annual counts](data/final-project-part-one/discogs-annual-style-format-counts.csv), and [final chart-generation script](scripts/plot-part-two-storyboard.py).
- All three final SVG charts use the project's Discogs summary. The final story uses no third-party photographs, album covers, or logos. The original Tableau export is retained on [Part II](final-project-part-two#progressive-state-3-annotate-the-crossovers).

## AI acknowledgements

I chose the topic, decided which feedback to use, and remain responsible for the interpretation. I used ChatGPT to check the Discogs processing workflow, revise the story and this write-up, organize and anonymize Part II feedback, and generate the final three SVG frames from the previously extracted summary. I created and reviewed the original Tableau chart in Part II. A separate simulated target-audience critique informed early design thinking but was not counted among the five human feedback sources. ChatGPT did not generate or alter participants' comments.

# Final thoughts

The most useful design lesson was how much the unit of analysis changes the claim. Release-version counts can show that formats coexist in this catalog. They cannot explain why people choose vinyl, whether one format sounds better, or how many copies sold. Putting those limits beside the evidence made the ending more precise. The final page has been checked as a published page, but it has not had a new audience test after the Part II feedback.
