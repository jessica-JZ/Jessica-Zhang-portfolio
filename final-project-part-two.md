| [Home](https://jessica-jz.github.io/Jessica-Zhang-portfolio/) | [Data visualization examples](https://jessica-jz.github.io/Jessica-Zhang-portfolio/dataviz-examples) | [Visualizing Government Debt](https://jessica-jz.github.io/Jessica-Zhang-portfolio/visualizing-government-debt) | [Critique by Design](https://jessica-jz.github.io/Jessica-Zhang-portfolio/critique-by-design) | [Final project I](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-one) | [Final project II](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-two) | [Final project III](https://jessica-jz.github.io/Jessica-Zhang-portfolio/final-project-part-three) |

# Wireframes / storyboards

**Working story title:** *In the Discogs Catalog, Digital Files Took the Lead—but Vinyl Records Remained.*

## Story direction

Electronic-music listeners can encounter the same release as both a download and a 12-inch record. This project asks what that coexistence looks like in the Discogs catalog: once digital-file releases became more common, did vinyl-record releases disappear?

For listeners who still encounter both options in record shops and label catalogs, the chart provides historical context. I use annual cataloged release-version counts for House, Techno, and Ambient from 1985 through 2024. The story shows when digital files took the lead and whether vinyl records continued afterward. It does not recommend one format or compare sound quality.

One small-multiple line chart carries the story. Each panel compares digital-file and vinyl-record releases over time, and the three styles provide separate cases rather than a ranking. The evidence supports a narrow conclusion: in the Discogs catalog, digital-file dominance coexisted with continuing vinyl releases. “Continued” does not mean stable or growing. House vinyl releases, for example, fell from a peak of 11,121 in 1996 to 3,022 in 2024.

I created the high-fidelity chart in Tableau. The final reader-facing story will use Shorthand as a scroll-based presentation, while this GitHub page documents the Part II storyboard, data decisions, and user-research plan.

`File` and `Vinyl` are Discogs format tags. In the reader-facing text, I describe them as “digital file (download)” and “vinyl record.” A release version is one particular edition of a recording. For example, a vinyl edition, a Japanese CD edition, and a FLAC download of the same album count as three release versions. The tags describe the release medium, not how the audio was recorded or mastered. These counts do not measure sales, listening, popularity, or sound quality.

## Storyboard

This Part II storyboard shows the main chart in three progressive states. The first two are simplified reveal frames generated from the same data; the third is the high-fidelity Tableau endpoint. All three keep the panel order, time range, count scale, and color meaning constant. Their typography and legend treatment differ because the endpoint was produced in Tableau, so the sequence should be read as a storyboard progression rather than a literal animation.

### Story beat 1: Begin with the visual contradiction

The opening places the chart near the beginning and asks what happened to vinyl records after digital-file releases moved ahead. The definition above explains “release version” with a concrete album-edition example and clarifies that format does not describe recording or mastering technology.

### Story beat 2: Reveal the evidence in one main chart

The main visual has aligned House, Techno, and Ambient panels. Each panel shows annual numbers of cataloged Digital File and Vinyl Record release versions from 1985 through 2024. Vinyl uses blue, while Digital File uses a quiet warm gray. Direct 2024 labels reduce eye travel between the lines and legend. All panels use the same time range and count scale.

The three states below use the same real data and analytical structure. One release version is one format-specific edition, not a sale or a unique album.

#### Progressive state 1: Establish that vinyl remained

![Storyboard frame 1 of 3 showing annual Vinyl release-version counts for House, Techno, and Ambient](assets/final-project-part-two/storyboard-stage-1.svg)

The first state asks one question: did vinyl approach zero? The blue lines remain visible through 2024 in all three panels.

#### Progressive state 2: Add the format that took the lead

![Storyboard frame 2 of 3 adding annual Digital file release-version counts to the Vinyl lines](assets/final-project-part-two/storyboard-stage-2.svg)

The second state adds Digital File without changing the axes. Readers can now see both the crossover and the continued presence of vinyl rather than interpreting the change as complete replacement.

#### Progressive state 3: Annotate the crossovers

![Storyboard frame 3 of 3 annotating when Digital file first exceeded Vinyl for House, Techno, and Ambient](assets/final-project-part-two/storyboard-stage-3.svg)

The final state marks the first year Digital File exceeded Vinyl Record: 2003 for Ambient and 2008 for House and Techno. Ambient crossed five years earlier.

> Ambient context: in 2024, Vinyl, CD, or File appeared on 76.9% of the Ambient records in scope, while cassette appeared on 13.3%. The two-line chart therefore does not represent Ambient's full physical-format mix.

CD does not appear in the main chart because the central comparison is Digital File versus Vinyl Record. One release may have more than one format tag, so the two lines are separate counts rather than parts of a 100% total.

### Story beat 3: Resolve the question and define its limits

The proposed ending returns to the opening question: Digital File releases took the lead in this Discogs sample while vinyl records continued to appear in thousands of cataloged versions. It avoids claims about a vinyl revival or listener preference. The chart note names Discogs as the source and explains the unit of analysis. In the filtered data, 0.16% of release versions contain more than one selected format tag, so the categories should not be read as two parts of a 100% total. The master-level sensitivity check remains on the Part I page rather than becoming another visual chapter.

The limitations note explains that Discogs is a user-contributed collector database. Physical releases may be more likely to be cataloged than digital-only releases, so the catalog may make vinyl look more persistent than the full release market. This is a possible source of bias, not a measured correction factor.

The first File-tagged records in this filtered sample appear in 1993; that is not a claim about the first downloadable music release. The December 2025 snapshot may also receive additional community entries for recent release years. The post-2020 decline should therefore be read as a pattern in the catalog snapshot, not as proof that the broader market declined by the same amount.

In the final Shorthand story, a reader should be able to scroll through the three states, identify both formats without outside explanation, and summarize the conclusion in one sentence. Readers who want the analytical details can continue to the limitations without interrupting the main story.

### High-fidelity draft

The third frame uses my uploaded Tableau chart as the high-fidelity endpoint and adds the crossover annotation layer needed for the storyboard. The first two frames prototype the earlier reveal steps without pretending to be final Tableau exports. Across the sequence, the real data, panel order, time range, shared scale, and color meaning stay constant. The direct 2024 labels, axes, legend, crossover annotations, and source note allow the endpoint to be understood on its own.

> Part II participant instruction: please stop here after reviewing the storyboard. I will ask the interview questions before you read the process notes and research plan below.

## How Part I feedback shaped this storyboard

The comments below were made about my Part I sketches. I used them as preliminary design input for the revised Part II storyboard. They are separate from the Part II interviews described later on this page. One additional critique was framed as a simulated target-audience pretest; I use it only as design critique, not as a completed interview.

| Feedback on the Part I sketches | Change made in the Part II storyboard |
|---|---|
| The intended audience and central story were difficult to identify. | I narrowed the audience to electronic-music listeners who mainly use digital access but still encounter vinyl editions. Every frame now examines whether the rise of digital-file releases meant that vinyl records disappeared. |
| Sketch 2 was the clearest direction. | I selected one digital-file-versus-vinyl time-series figure instead of carrying five competing directions forward. |
| The sketches needed clearer legends, axes, units, and annotations. | The revised storyboard includes a claim-based title, named axes, a shared scale, 2024 labels, crossover annotations, and the Discogs source. |
| The miniature vinyl-count and total-catalog lines were difficult to interpret. | I removed both placeholders. The main chart uses annual counts to show the crossover and vinyl's continued presence. |
| The master-level comparison was difficult to understand. | I moved the master-level sensitivity check to a methods note so the main story keeps one unit of analysis. |
| Connectors between File and Vinyl dots implied a continuum or a 100% total. | I removed the connected-dot designs because the format categories can overlap. |
| The amount of detail created too much cognitive load. | I reduced the reader-facing story to one chart shown in three progressive states and moved technical detail below the main narrative. |
| “File” and “release version” were difficult for a general reader to interpret. | The chart uses “Digital File” and “Vinyl Record,” while the text defines a digital file as a download and explains release versions with a concrete album-edition example. |
| Definitions and methodology delayed the main evidence. | I shortened the definitions and placed them immediately before the storyboard, while keeping detailed limitations below the frames. |
| The title made vinyl's continued presence sound more positive than the comparison warranted. | The working title states that digital files took the lead before it says that vinyl records remained. |
| Ambient's cassette releases and Discogs's collector-community coverage could change the interpretation. | The storyboard adds an Ambient context note and a concise limitation about possible cataloging bias. |

# User research

## Target audience

The primary audience is electronic-music listeners who mainly use streaming or downloads but still encounter vinyl through DJs, record shops, or label releases. They may recognize House, Techno, and Ambient, but they are not expected to know how Discogs organizes its database.

These listeners may assume that a newer format replaces an older one. After reading the story, they should be able to explain how digital files became the dominant cataloged format while vinyl records remained present. They should also be able to use the chart as evidence without treating catalog counts as proof that vinyl became more popular.

I recruited three people with different levels of familiarity with the course: a current classmate, a former student, and a Data Science student who is not enrolled in the class. This mix let me test the story with readers who understand data visualization and with a reader outside the course. The available notes do not establish that all three participants match the primary audience, so I treat these interviews as usability tests of the story and charts rather than a representative audience sample. I describe participants only in broad terms and do not include names or other identifying information.

## Interview script

### Research goals

The protocol tests whether readers can identify the intended audience, central question, and main comparison in the revised Part II storyboard. It also tests whether readers understand the unit of analysis and the limits of the data.

### Interview procedure

Each participant viewed the revised page through the Part II participant instruction before reading the process notes or research plan. The page included story-direction text before the charts, so that framing may have influenced their interpretations. I asked the same core questions and took anonymous notes. I recorded whether each answer showed clear, partial, or incorrect understanding. I then compared repeated observations with conflicting interpretations rather than treating every suggestion as a required change.

### Questions

| Research goal | Question |
|---|---|
| Test whether the audience is apparent | Who do you think this story is for? |
| Test whether the central question is clear | In one sentence, what do you think this story is trying to explain? |
| Test the main comparison | What does the main chart want you to notice? |
| Test the main conclusion | How would you describe the change in vinyl releases over this period? What evidence led you to that answer? |
| Test the unit of analysis | What do you think “release version” means here? |
| Test the style comparison | What difference, if any, do you notice among House, Techno, and Ambient? |
| Test chart readability | Point to the year when digital-file releases first exceeded vinyl releases for Techno. |
| Test the limits | What can this data tell us, and what can it not tell us? |
| Identify friction | Where did you feel confused, uncertain, or less interested? |
| Invite redesign suggestions | What would you change first? |

## Interview findings

Three Part II interviews have been completed. Interview 1 was with a classmate enrolled in the course. Interview 2 was with someone who previously took the course. Interview 3 was with a Data Science student who is not enrolled in this course. The tables use specific paraphrases because permission to publish direct quotations has not been confirmed. The three storyboard images remain in the form the participants reviewed. The responses below are plans for Part III, not changes already applied to those images.

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
| Differences among the styles | The participant noticed that Ambient crossed around 2003, earlier than House and Techno around 2008. | Interview 3 also noticed the earlier crossover but found the emphasis distracting, so Part III should treat the timing difference as secondary. |
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

The three interviews produced the following plan. I added source and method clarifications to the Part II write-up, while the visible story changes remain decisions for Part III. None of the three storyboard images has been altered after the interviews.

| Finding | Part III decision | Reason |
|---|---|---|
| The opening takeaway was slow or ambiguous for all three participants. | Revise the title and subtitle to name both the decline and Vinyl's continued presence. | This was the clearest repeated issue. |
| State 3 uses a different visual style. | Redraw state 3 to match states 1 and 2, changing only the crossover annotation layer. | A consistent frame makes the progressive reveal easier to follow. |
| The Ambient cassette note distracted two participants. | Move the cassette detail to the limitations. | It is useful context but does not belong in the main two-format comparison. |
| The role of the three style panels was interpreted differently. | Explain that the styles are supporting cases and reduce the emphasis on Ambient being five years earlier. | The story is about a shared pattern rather than ranking genres. |
| The unit of analysis was initially unclear to one participant. | The concrete edition example remains, with a short unit note added beside the storyboard. | This adds clarity without repeating the full methods section. |
| The overlap sentence was difficult to understand. | The page now says that one release may have several format tags, so the lines are not parts of a 100% total. | The revised wording is more direct. |
| The early Digital File points and post-2020 decline raised a new data question. | The limitations now identify 1993 as the first File-tagged year in the sample and treat the recent decline only as a catalog-snapshot pattern. | The source supports those boundaries but not a causal explanation. |
| The central story and data limitations were understood. | Keep the progressive sequence, crossover years, end labels, and cautious conclusion. | These elements worked across all three interviews. |

## References

Discogs. “Discogs Data.” Monthly database dumps. https://data.discogs.com/

Discogs. “Database Guidelines 6: Format.” https://support.discogs.com/hc/en-us/articles/360005006654-Database-Guidelines-6-Format

Berinato, Scott. *Good Charts*. Chapter 7, “Persuasion or Manipulation? The Blurred Edge of Truth.”

## AI acknowledgements

I chose the topic, decided which feedback to use, created and reviewed the Tableau chart, and remain responsible for the interpretation. I used ChatGPT to help check the Discogs data-processing workflow, narrow the story, revise the writing, and organize and anonymize participant feedback. ChatGPT also helped create the first two progressive storyboard frames from the extracted data and add a draft crossover annotation layer to my uploaded Tableau chart. Separately, I used ChatGPT for a simulated target-audience critique. I did not count that simulation among the three interviews. All feedback counted as interview evidence came from human participants; ChatGPT did not generate or alter their comments.
