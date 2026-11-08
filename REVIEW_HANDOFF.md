Copy the following prompt into a review chat. It requests an independent audit; this file does not start another agent or contact anyone.

---

Independently audit and, where possible, finish this carousel OSINT challenge. Work in `./`. The input image is `./inputs/carousel.png`. Start by reading `README.md`, `SEARCH_PATH.md`, `EVIDENCE_INDEX.md`, and `sources/download-manifest.json`.

The original six supplied questions ask for:

1. The city containing the museum displaying the photographed pig, among its combined collections.
2. All three other carousel animals displayed with it in the 2020–2026 period.
3. The park with the greatest number of original carousel figures by the artist implied by an apparently missing original Q1.
4. The sculpture trailing, in the same row, a horse rumored to have been used to count rotations before restoration.
5. The stored pig's original reinstallation location, using the historic diagram's case-sensitive `a`–`r` or `A`–`R`, assuming the chariots stayed fixed. The question says the pig was back by 1980.
6. The 1975 estimated USD cost per animal for stripping, sanding, painting, and rebuilding.

Current findings are **Williamsburg, Virginia**; **cat, Bactrian camel, ostrich**; **Pullen Park, Raleigh**; and **lion if the intended horse is the flag-bearing lead horse**. The worldwide superlative and the rotation-counting rumor have not been independently proved. The original reinstallation letter and the 1975 amount remain **unsolved**. A later-position hypothesis, lowercase `g`, is explicitly tentative. Do not treat it as an accepted answer.

Your job is to try to falsify these findings, not rubber-stamp them. For each question, return a verdict of confirmed, supported with caveat, incorrect, or unresolved, with a direct source URL, publication/capture date where available, and a precise page/figure/object identifier.

For the museum:

- Compare the original pig's carving, paint, background cat, ostrich, column, and wall scene with the saved official images. A generic pig resemblance is insufficient.
- Check the distinction between the Abby Aldrich Rockefeller Folk Art Museum and the combined Art Museums of Colonial Williamsburg.
- Distinguish a current exhibition page, an older travel article, and the user's 2026 photograph. Do not claim continuous display for the full date interval from an older source alone.
- Locate the pictured pig's own exhibit label or catalogue record if possible. The museum cat record's qualified Cernigliaro attribution should not be silently transferred to the pig or converted into certainty of personal execution.

For Pullen and the lion:

- Check whether the 52-figure attribution actually proves the requested global ranking. Identify whether “original” means original carving, original paint, or original to the current machine.
- Read the historic inventory and inspect the NCA flag-horse photograph. Verify which animal follows in the direction of rotation. Do not infer trailing order from the numerical order of a list.
- Find an independent source connecting the counting-rotations rumor to the particular flag/lead horse. If that identity is wrong, revise the answer.

For the pig letter, give this question special scrutiny:

- Use the 17-page state nomination, its storage description, the full arrangement drawing, and later photographs.
- Match the carving itself. Do not identify a pig by its coat color alone.
- Anchor the full sequence on a fixed chariot, demonstrate the center versus inner row, and explain the letter case.
- Consider that animals could have moved during the 1970s–1980s restoration or the later re-restoration. An acorn pig photographed in 2004 does not prove where it was first put back or that it was there in 1980.
- Do not select a location simply because it held an aluminum replacement. Likewise, do not accept the tentative `g` without resolving the earlier pig recorded there.
- Prefer a dated figure register, restoration drawing, or a clearly dated photographic sequence. If the “by 1980” premise is wrong, say so with evidence.

For the price:

- Find the actual 1975 appraisal/estimate or a contemporaneous, reliable quotation. Establish the expert's identity, the date, USD amount, unit, and treatment scope.
- Do not use a later project total, an appraisal value, a fundraising target, a modern treatment quote, or a calculated total divided by figure count.
- The nomination names Dick Norton as an examining expert; it does not itself establish that he authored the specific requested unit estimate. Test that lead instead of assuming it.
- Promising remaining references: Raleigh Fine Arts Society, MSS 035, restoration project files at Olivia Raney Local History Library; the linked ArchivesSpace resource 43 (returned 403 during this run); Merry-Go-Roundup vol. 10 no. 1 (Spring 1983), indexed as a major Pullen article; Smithsonian Fried collection's Pullen reference folder, Box 26 Folder 4. Their records are leads, not evidence of an amount.
- Do not contact staff, purchase subscriptions, or submit answers to an external challenge platform without the user's explicit authorization. Use public records and any access the user has already authorized.

Use full PDF pages and primary records. The state nomination, city landmark report, and federal dossier have different PDF page numbering. The state copy has 17 pages and its plan is PDF page 14. NCA photograph 004 is dated 10 November 2006; photograph 023 is dated 28 May 2004.

Write the audit to `./REVIEW.md`. Include corrected answers, direct citations, the reasoning chain for any letter, unresolved issues, and concrete next evidence needed. Preserve original sources and do not overwrite the researcher's report merely to hide a disagreement. An honest unresolved verdict is preferable to an unsupported answer.
