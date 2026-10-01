# Portfolio maintenance guide

This guide applies to the public [Jessica Zhang data visualization portfolio](https://jessica-jz.github.io/Jessica-Zhang-portfolio/).

## Protect graded work

Final project pages and charts may be revised during the current, user-requested adjustment. Once Jessica confirms the project is final, treat its prose, analysis, data, images, and charts as frozen during routine portfolio maintenance. Reopen them only for an explicit request. If a page is still being graded, keep substantive changes within the scope Jessica has authorized.

## Current site structure

- Keep the course template's theme and page layout. Home links directly to Government Debt, Critique by Design, and Final project Parts I, II, and III. The same six links appear in one navigation row on each public project page; the three final parts are siblings, not a chain of landing pages.
- Part III is the public final story. The old `/final-data-story` address redirects there, while its original Markdown remains in Git. The empty Data visualization examples page is removed and must not reappear as a placeholder.
- Supporting Markdown pages linked from a project, such as the data documentation, need a visible route back to Home and the related project pages.
- When changing a project later, update its existing page and preserve its public URL. Add a new Home and navigation link only for a real new page. Avoid duplicate public versions of the same story.

## Check the five rubric areas

1. **Public access (1.25):** Open the `github.io` home page without signing in, then confirm each page opens. Check any retained redirect, including `/final-data-story`, and remove links to deleted pages from visible navigation.
2. **Organization (2.5):** Keep the template's familiar home, About me, What I hope to learn, and Portfolio sections, along with its theme and navigation style. Give each page a clear title and logical headings, and keep the work easy to find.
3. **Content (2.5):** Remove template text and stale promises, correct typos, and keep claims, sources, and AI acknowledgements accurate. Do not invent project outcomes.
4. **Links (2.5):** Keep a visible path from every page to Home and related work. Show Final project Parts I, II, and III as parallel links on Home and in each project's navigation, without an intermediary gallery. Check internal and important external links on the published site.
5. **Images and charts (1.25):** Confirm images render and interactive charts open; keep a readable static chart when an embed fails.

## Routine for each update

1. Inspect the assignment and current public pages. Synchronize the local checkout with GitHub before editing, and preserve unrelated changes.
2. Make the smallest changes that address a visible issue. Respect the project's current edit or freeze status and keep one clear public entry for each project part.
3. Check Markdown links and local image paths, then inspect the rendered public pages after publishing. Verify the deployed commit and reload cached pages when an old navigation row persists. A successful local build or GitHub commit alone does not prove the live page works.
4. Compare the visible result with all five rubric areas. Report what was verified and what remains subjective or unverified; do not promise a score.

Use the installed `telling-stories-with-data` skill for chart-specific and portfolio guidance. Keep this guide and the skill in sync when the course requirements change.
