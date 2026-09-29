| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Data visualization examples](https://jessica-jz.github.io/Jessica-Zhang-portfolio/dataviz-examples) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# Wireframes / storyboards

**Working story title:** *In the Discogs Catalog, Digital Files Took the Lead—but Vinyl Records Remained.*

## Story direction

My Part I sketches explored several questions about release formats. When I presented them together, the main story was difficult to identify. In this Part II revision, every section answers one question: when digital-file releases took the lead in the Discogs catalog, did Vinyl releases disappear?

The guiding idea is that format change is not always a simple replacement story. I use annual counts of cataloged release versions because one measure can show both parts of the story: when the Digital File line moved above Vinyl and whether Vinyl later fell to zero. House, Techno, and Ambient appear as three cases within the same visual rather than as three separate stories.

The current design centers on one small-multiple line chart. Within each style panel, the comparison is Digital File versus Vinyl across time. The reader is not being asked to rank the three styles. Progressive states and annotations show when Digital File overtook Vinyl and whether Vinyl later approached zero. The intended conclusion is narrow: digital-file dominance and the continued presence of Vinyl releases can occur at the same time in a catalog.

In the source data, `Vinyl` and `File` are Discogs format labels. The Tableau chart labels them “Vinyl Record” and “Digital File.” Here, Digital File means a downloadable file release. A release version is one particular edition of a recording. For example, a vinyl edition, a Japanese CD edition, and a FLAC download of the same album count as three release versions. These labels describe release formats, not how the audio was recorded or mastered. The project does not measure listening, sales, or sound quality.

## Storyboard

This Part II storyboard shows one final chart across three progressive visual states. Together, they document a single visual changing one layer at a time. Around the chart, the story follows three beats: setup, evidence, and resolution.

### Story beat 1: Begin with the visual contradiction

The opening places the main chart near the beginning and asks what happened to Vinyl after Digital File releases moved ahead. The definition above explains “release version” with a concrete album-edition example and clarifies that format does not describe recording or mastering technology.

**Storyboard beat:** a short question followed by the first state of the main chart. The short definitions sit close to the evidence instead of delaying it.

### Story beat 2: Reveal the evidence in one main chart

The hero visual is one figure with aligned House, Techno, and Ambient panels. Each panel shows annual numbers of cataloged Digital File and Vinyl release versions from 1985 through 2024. Vinyl uses blue, while Digital File uses a quiet warm gray. Direct 2024 labels reduce eye travel between the lines and legend. The x-axis reads “Release year,” and the y-axis reads “Number of cataloged release versions.” All panels and progressive states use the same time range and count scale.

The three states below show the actual progressive walkthrough. They use the same real data, 1985–2024 time range, and count scale so that only the intended story layer changes.

#### Progressive state 1: Establish that Vinyl remained

![Storyboard frame 1 of 3 showing annual Vinyl release-version counts for House, Techno, and Ambient](assets/final-project-part-two/storyboard-stage-1.svg)

The first state asks one question: did Vinyl approach zero? The blue lines remain visible through 2024 in all three panels.

#### Progressive state 2: Add the format that took the lead

![Storyboard frame 2 of 3 adding annual Digital file release-version counts to the Vinyl lines](assets/final-project-part-two/storyboard-stage-2.svg)

The second state adds Digital File without changing the axes. Readers can now see both the crossover and the continued presence of Vinyl rather than interpreting the change as complete replacement.

#### Progressive state 3: Annotate the crossovers

![Storyboard frame 3 of 3 annotating when Digital file first exceeded Vinyl for House, Techno, and Ambient](assets/final-project-part-two/storyboard-stage-3.svg)

The final state marks the first year Digital File exceeded Vinyl: 2003 for Ambient and 2008 for House and Techno. The repeated annotation also makes the main difference among the three panels explicit: Ambient crossed five years earlier.

> Ambient context: in 2024, Vinyl, CD, or File appeared on 76.9% of the Ambient records in scope, while cassette appeared on 13.3%. The two-line chart therefore does not represent Ambient's full physical-format mix.

CD does not appear in the main chart because the central comparison is Digital File versus Vinyl. The chart does not connect the two values at a given year because the categories can overlap and do not form two ends of a 100% scale. The Ambient context note keeps that limitation visible without adding another chart.

**Storyboard structure:** consistent axes and colors make the sequence one visual explanation rather than three separate analyses.

### Story beat 3: Resolve the question and define its limits

The proposed ending returns to the opening question: Digital File releases took the lead in this Discogs sample while Vinyl releases continued to appear in thousands of cataloged versions. It avoids claims about a vinyl revival or listener preference. The chart note names Discogs as the source and explains the unit of analysis. In the filtered data, 0.16% of release versions contain more than one selected format tag, so the categories should not be read as two parts of a 100% total. The master-level sensitivity check remains on the Part I page rather than becoming another visual chapter.

The limitations note explains that Discogs is a user-contributed collector database. Physical releases may be more likely to be cataloged than digital-only releases, so the catalog may make Vinyl look more persistent than the full release market. This is a possible source of bias, not a measured correction factor.

**Scenario of use:** a reader should be able to scroll through the three states, identify the two formats without outside explanation, and summarize the conclusion in one sentence. A methods-minded reader can then continue to the limitations without interrupting the main story.

### High-fidelity draft

The third frame uses my uploaded Tableau chart as the high-fidelity base and adds only the crossover annotation layer needed for the storyboard. It uses the real Discogs data and a shared count scale. Its claim-based title limits the conclusion to the Discogs catalog, while the direct 2024 labels, axes, legend, crossover annotations, and source note allow the chart to be understood on its own.

> Part II participant instruction: please stop here after reviewing the storyboard. I will ask the interview questions before you read the process notes and research plan below.

## How Part I feedback shaped this storyboard

The comments below were made about my Part I sketches. I used them as preliminary design input for the revised Part II storyboard. They are separate from the Part II interviews described later on this page. One additional critique was framed as a simulated target-audience pretest; I use it only as design critique, not as a completed interview.

| Feedback on the Part I sketches | Change made in the Part II storyboard |
|---|---|
| The intended audience and central story were difficult to identify. | I defined the audience as electronic-music listeners who mainly use digital access but still encounter vinyl editions. Every story beat now asks whether the rise of File releases meant that Vinyl releases disappeared. |
| Sketch 2 was the clearest direction. | I selected one File-versus-Vinyl time-series figure as the main visual instead of carrying five competing directions forward. |
| The sketches needed clearer legends, axes, units, and annotations. | The revised storyboard uses direct line labels, named axes, a shared scale, crossover annotations, a caption, and the Discogs source. |
| The miniature Vinyl-count and total-catalog lines were difficult to interpret. | I removed both placeholders. The main chart uses annual counts to show the crossover and Vinyl's continued presence. |
| The master-level comparison was difficult to understand. | I moved the master-level sensitivity check to a methods note so the main story keeps one unit of analysis. |
| Connectors between File and Vinyl dots implied a continuum or a 100% total. | I removed the connected-dot designs because the format categories can overlap. |
| The amount of detail created too much cognitive load. | I reduced the reader-facing story to one chart shown in three progressive states and moved technical detail below the main narrative. |
| “File” and “release version” were difficult for a general reader to interpret. | The Tableau chart uses the reader-facing labels “Digital File” and “Vinyl Record,” and the definition above explains “release version” with a concrete album-edition example. |
| Definitions and methodology delayed the main evidence. | I shortened the definitions and placed them immediately before the storyboard, while keeping the detailed limitations below the frames. |
| The title made Vinyl's continued presence sound more positive than the comparison warranted. | The working title now states that Digital files overtook Vinyl before stating that Vinyl did not disappear. |
| Ambient's cassette releases and Discogs's collector-community coverage could change the interpretation. | The storyboard adds an Ambient context note and a concise limitation about possible cataloging bias. |

# User research

## Target audience

The primary audience is electronic-music listeners who usually access music through streaming or downloads but still see DJs, record shops, and labels release music on vinyl. A reader may recognize House, Techno, and Ambient and wonder why a new track can be available as both a download and a 12-inch record. The reader is not expected to know how Discogs organizes its database.

These listeners may carry a simple story of technological change: a newer format arrives and the older one disappears. Electronic music makes that expectation worth examining because digital files and vinyl records can both remain visible to the same listener. After reading the story, the audience should understand why “Digital releases became dominant” and “Vinyl releases remained” are not contradictory claims. They should be able to point to the two lines in the main chart as evidence and explain why the chart does not prove that vinyl became more popular.

For the Part II interviews, I will recruit at least three people who have not helped design the revised storyboard. I will try to include electronic-music listeners who mainly use streaming or downloads, because they are closest to the intended audience. A participant does not need to be enrolled in this course. I may also include one data-visualization classmate to check whether the chart can be read without additional explanation. I will describe participants only in broad terms and will not record names or other identifying information on this page.

## Interview script

### Research goals

The protocol tests whether readers can identify the intended audience, central question, and main comparison in the revised Part II storyboard. It also tests whether readers understand the unit of analysis and the limits of the data.

### Interview procedure

Each participant will view the revised storyboard before I explain the intended conclusion. I will ask the same core questions and take anonymous notes. For each question, I will record whether the answer showed clear, partial, or incorrect understanding and capture an exact quotation when the participant agrees. After the interviews, I will compare repeated observations with conflicting interpretations rather than treating every suggestion as a required change.

### Questions

| Research goal | Question |
|---|---|
| Test whether the audience is apparent | Who do you think this story is for? |
| Test whether the central question is clear | In one sentence, what do you think this story is trying to explain? |
| Test the main comparison | What does the main chart want you to notice? |
| Test the main conclusion | How would you describe the change in Vinyl releases over this period? What evidence led you to that answer? |
| Test the unit of analysis | What do you think “release version” means here? |
| Test the style comparison | What difference, if any, do you notice among House, Techno, and Ambient? |
| Test chart readability | Point to the year when Digital File releases first exceeded Vinyl releases for Techno. |
| Test the limits | What can this data tell us, and what can it not tell us? |
| Identify friction | Where did you feel confused, uncertain, or less interested? |
| Invite redesign suggestions | What would you change first? |

## Interview findings

Three Part II interviews have been completed. Interview 1 was with a classmate enrolled in the course. Interview 2 was with someone who previously took the course. Interview 3 was submitted as an anonymous written review; no further participant description was provided. The tables paraphrase the feedback because permission to publish direct quotations has not been confirmed. I have kept the storyboard in the form the participants reviewed. The responses below are plans for Part III, not changes already made to the Part II draft.

| Interview 1 observation | What I learned | Possible Part III response |
|---|---|---|
| The central storyline and three progressive states were easy to follow. | The reveal sequence answers the main question without adding separate charts. | Keep the current sequence. |
| The phrase “Vinyl Records Remained” was ambiguous. | The title should say what remained and identify the endpoint. | Test a more specific title that states that Discogs still contained thousands of Vinyl release versions in 2024. |
| The Ambient cassette percentages interrupted the main File-versus-Vinyl comparison. | The context is useful, but it may belong with the limitations. | Consider moving the cassette detail below the main visual sequence. |
| The role of House, Techno, and Ambient was unclear, especially when Ambient was highlighted as crossing five years earlier. | The panels may need to read more clearly as three supporting cases rather than a genre ranking. | Consider clarifying the role of the panels and reducing the emphasis on the five-year difference. |
| The restrained conclusion and Discogs collector-bias note made the claim more credible. | The limits help prevent catalog counts from being read as popularity, sales, or listening behavior. | Keep the cautious conclusion and bias note. |

### Interview 2

| Question area | Interview 2 observation | Possible Part III response |
|---|---|---|
| Intended audience | The story appeared to be for readers interested in music formats, Discogs data, or changes in release formats over time. | No change planned at this stage. |
| Main story | The participant understood that Digital File releases became more common in the Discogs catalog while Vinyl releases did not disappear. | Keep the central story. |
| Main chart takeaway | The participant focused on the crossover and Vinyl's continued presence afterward. | Keep the progressive reveal and crossover annotations. |
| Evidence about Vinyl | The blue Vinyl line continues through 2024 in all three panels and never falls to zero. | Keep the common time range and end labels. |
| Meaning of “release version” | The participant understood it as a format-specific edition rather than a unique song or album, but was initially unsure whether the counts represented albums, sales, or editions. | Consider placing the definition closer to the chart. |
| Differences among the styles | The participant noticed that Ambient crossed around 2003, earlier than House and Techno around 2008. | Use Interview 3 to test whether this comparison is clear without distracting from the shared pattern. |
| Techno crossover | The participant correctly identified approximately 2008. | Keep the annotation. |
| Limits of the data | The participant understood that the chart shows Discogs catalog patterns, not sales, listener preferences, streaming behavior, or a broad Vinyl revival. | Keep the current limitations. |
| Main uncertainty | The unit of analysis took some effort to understand even though the definition helped. | Test whether a shorter, more prominent unit note would help. |
| First suggested change | Add a short subtitle under the title that states the conclusion more directly. | Consider the subtitle after comparing all three interviews. |

### Interview 3

| Question area | Interview 3 observation | Possible Part III response |
|---|---|---|
| Main story | The participant understood the story as Digital File releases overtaking Vinyl while both formats continued to appear in the Discogs catalog. | Keep the central story and the progression. |
| First visual impressions | The warm crossover annotations drew attention first. The sharp House Vinyl decline and the post-2020 Digital File decline were also prominent. | Make sure the annotations do not overpower the trends they explain. |
| Progressive states | The first two states built the comparison clearly, but the third state looked like a different chart because its type, labels, legend, and panel styling changed. | Rebuild the third state in the same visual style as the first two, then add only the crossover layer. |
| Crossover meaning | The participant correctly understood the crossover as the first year Digital File release versions exceeded Vinyl, rather than a measure of sales or listening. | Keep the crossover explanation and data limits. |
| Unexplained data patterns | The post-2020 Digital File decline and the first Digital File points around 1993 raised questions about data completeness and retrospective cataloging. | Investigate these patterns before Part III and add a data-coverage note if the source supports one. |
| Ambient context | The CD and cassette percentages felt disconnected from a chart showing only Digital File and Vinyl. | Move this detail to the limitations or explain its purpose more directly. |
| Wording about overlapping formats | The sentence about not connecting values at a given year was hard to interpret. | Rewrite the overlap note in plainer language. |
| Meaning of “remained” | The title communicated persistence, but it could understate the large decline in House Vinyl release versions. | Revise the title or nearby text so persistence does not obscure the decline. |
| Interview method | The text before the storyboard explained the intended conclusion and the earlier Ambient crossover, which may have influenced the participant's answers. | In future testing, show the visual before the explanatory text. |
| First suggested change | The participant would first redraw state 3 to match states 1 and 2 while changing only the annotation layer. | Adopt this change in Part III. |

### Patterns across the three interviews

All three participants understood the main claim: Digital File release versions overtook Vinyl in the Discogs catalog, while Vinyl continued through 2024. They also understood that the chart does not measure sales, listening, or popularity. The progressive reveal and cautious limits worked well.

The opening wording needs revision. Interview 1 found “remained” ambiguous, Interview 2 wanted a faster statement of the takeaway, and Interview 3 thought the wording could understate the decline in House Vinyl releases. The Ambient cassette note distracted Interviews 1 and 3. Interviews 1 and 3 also questioned the emphasis placed on Ambient's earlier crossover, while Interview 2 interpreted the timing difference correctly. Interview 3 alone raised the visual discontinuity in state 3 and the unexplained early and post-2020 Digital File patterns. Interview 2 needed more help with the unit of analysis, while Interview 3 found the existing edition example sufficient.

# Identified changes for Part III

The three interviews produced the following plan. None of these changes has been applied to the Part II storyboard.

| Finding | Part III decision | Reason |
|---|---|---|
| The opening takeaway was slow or ambiguous for all three participants. | Revise the title and subtitle to name both the decline and Vinyl's continued presence. | This was the clearest repeated issue. |
| State 3 uses a different visual style. | Redraw state 3 to match states 1 and 2, changing only the crossover annotation layer. | A consistent frame makes the progressive reveal easier to follow. |
| The Ambient cassette note distracted two participants. | Move the cassette detail to the limitations. | It is useful context but does not belong in the main two-format comparison. |
| The role of the three style panels was interpreted differently. | Explain that the styles are supporting cases and reduce the emphasis on Ambient being five years earlier. | The story is about a shared pattern rather than ranking genres. |
| The unit of analysis was initially unclear to one participant. | Keep the concrete edition example and add a short unit note near the chart. | This adds clarity without repeating the full methods section. |
| The overlap sentence was difficult to understand. | Rewrite it to say that one release may have more than one format tag, so the lines are not parts of a 100% total. | The current wording is more technical than necessary. |
| The early Digital File points and post-2020 decline raised a new data question. | Check the source and extraction before deciding whether to add a coverage limitation. | I should not explain the pattern without evidence. |
| The central story and data limitations were understood. | Keep the progressive sequence, crossover years, end labels, and cautious conclusion. | These elements worked across all three interviews. |

## References

Discogs. “Discogs Data.” Monthly database dumps. https://data.discogs.com/

Discogs. “Database Guidelines 6: Format.” https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format

Berinato, Scott. *Good Charts*. Chapter 7, “Persuasion or Manipulation? The Blurred Edge of Truth.”

## AI acknowledgements

I used ChatGPT to critique my initial project direction, which helped me narrow the topic to one central story and one main chart. I also used it for a simulated target-audience critique, to revise and polish the writing, to organize and anonymize the peer feedback I collected, to create the first two progressive storyboard frames from the same extracted Discogs data, and to add a draft crossover annotation layer to my uploaded Tableau chart. The simulated critique is labeled separately and is not counted as an interview. The feedback counted as interviews came from human participants. ChatGPT helped organize and anonymize it but did not generate the feedback.
