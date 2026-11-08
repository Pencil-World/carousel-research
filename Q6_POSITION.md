# Q6: exact position of the stored pig

Research date: 8 November 2026. **Answer under the question's fixed-chariot assumption: lowercase `g`.**

A new series of overlapping photographs supplies the missing link between the restored acorn pig and the historical lettered plan. The letter comes from counting positions from a chariot, independently of the animal's restoration label 7A.

## 1. Identify the animal

The [1976 nomination](https://files.nc.gov/ncdcr/nr/WA0008.pdf), PDF page 7, describes the stored pig with an acorn, two oak leaves, a scalloped blanket, and damaged hind legs. The city's [drawing 18630](https://raleighhrmprogram.catalogaccess.com/archives/18630), marked No. 7A, and [detail slide 12294](https://raleighhrmprogram.catalogaccess.com/photos/12294) show that carving. [NCA photograph 023](https://carousels.org/psp/PullenPark/Pullen%20Park023.html), dated 28 May 2004, shows the matching black-and-white animal and captions it as a second-row pig. See [the identity and row comparison](Q6_ROW.md).

## 2. Fix the starting point on the plan

The historical diagram is **PDF page 14** of the nomination. Inspect the [complete saved plan](evidence/1976-source-page-14.png). Outer positions use Roman numerals; center positions use lowercase letters. The center positions are staggered between adjacent outer positions, so the chariot does not count as an extra center-row position.

The inventory, PDF page 3, identifies outer **IV** as a three-seat chariot, **V** as the giraffe with a Greek-key strap motif, **VI** as a horse with a lion-head ornament, **VII** as the tiger, and **VIII** as another horse.

[Commons photograph 25](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_25.JPG) shows the chariot on the left, the Greek-key giraffe on the right, and a brown center-row rabbit between them. The distinctive giraffe anchors this as chariot **IV**, rather than the opposite chariot XIII. Photos [07](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_07.JPG) and [06](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_06.JPG) give additional views of that pair.

On the historical plan the center-row gap between IV and V is **d**. This establishes the starting coordinate and the counting direction.

## 3. Trace the overlapping sequence

Read photographs **25 → 24 → 23 → 22**, following the direction the animals face. The adjacent outer animals and neighboring jumper figures overlap between the views.

| Center position on historical plan | Between outer positions | Center-row figure visible | Photograph |
| --- | --- | --- | --- |
| **d** | IV chariot / V Greek-key giraffe | Brown rabbit with tall ears and draped blanket | [25](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_25.JPG) / [saved](sources/commons-pullen/Pullen-Park-Carousel-25.JPG) |
| **e** | V giraffe / VI horse | Peach horse, black mane, green trappings | [24](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_24.JPG) / [saved](sources/commons-pullen/Pullen-Park-Carousel-24.JPG) |
| **f** | VI horse / VII tiger | Dark brown horse, scalloped blanket, forelegs raised | [23](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_23.JPG) / [saved](sources/commons-pullen/Pullen-Park-Carousel-23.JPG) |
| **g** | VII tiger / VIII horse | **Black-and-white acorn-and-oak-leaf pig** | [22](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_22.JPG) / [saved](sources/commons-pullen/Pullen-Park-Carousel-22.JPG) |

[Photo 21](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_21.JPG) provides a further check: the following center-row horse occupies **h**, between outer VIII and IX.

```text
Outer:   IV chariot     V giraffe      VI horse      VII tiger      VIII horse
Center:           d rabbit       e horse       f horse        g ACORN PIG
```

The inventory on PDF pages 4–5 also places the large-eared rabbit at d and horses at e and f, corroborating the sequence. The acorn pig's demonstrated gap between outer VII and VIII is **lowercase g** on the plan.

## 4. Distinguish the result from earlier assumptions

- **7A is an animal identifier.** It identifies the carving; it does not generate the answer letter. The photo sequence supplies g independently.
- **The earlier g inventory entry describes another pig.** This proof maps the later animal into a historical coordinate. It does not claim the acorn pig was already at g in 1976 or reconstruct every restoration-era animal movement.
- **The cream pig is a different carving.** [Photo 31](https://commons.wikimedia.org/wiki/File:Pullen_Park_Carousel_31.JPG) places that pig on the opposite side between the lion and flag horse. It is not substituted for the acorn pig.
- **Uppercase G belongs to the inner row.** The matching acorn pig is in the center row, giving lowercase g.

**Confidence:** high for lowercase g as the mapped position requested under the explicit fixed-chariot assumption. The new photographic count resolves the earlier spatial uncertainty.

**Date limitation:** these photographs are from **21 September 2012**. NCA shows the same carving as a center-row animal in 2004. Neither proves when the pig was first returned, nor excludes a temporary earlier position. The question's “by 1980” premise remains unverified. This chronological limitation is separate from the demonstrated position on the historical coordinate system.

## Reproducible search path

1. Read nomination PDF pages 3–7 and 14. Locate both chariots, the Greek-key giraffe V, the center-row labels, and the stored pig description. Check the actual images, not just OCR.
2. Search `"Pullen Park" carousel "pig" chariot`. This surfaced [the Commons category](https://commons.wikimedia.org/wiki/Category:Pullen_Park_Carousel) and the numbered photograph series.
3. Inspect photos 25, 24, 23, and 22 in that order, then 21 as a check. Compare adjacent animals, poles, and radial gaps. Do not assume filename numbers themselves are carousel positions.
4. Compare the acorn pig in photo 22 with city drawing 18630, detail 12294, and NCA 023. This keeps the proof tied to the stored animal.
5. Public Commons metadata and exact request URLs are saved in [index.json](sources/commons-pullen/index.json), [index.request.json](sources/commons-pullen/index.request.json), and their continuation [index-2.json](sources/commons-pullen/index-2.json) / [request](sources/commons-pullen/index-2.request.json). The initial response lists 69 files but supplies only the first 50 image-information records; the continuation completes that metadata.
6. To retrieve the focal previews, run from the repository root:

   ```bash
   python3 scripts/fetch_pullen_commons.py --numbers 6 7 21 22 23 24 25 31
   ```

7. Verify the JPEGs against [manifest.json](sources/commons-pullen/manifest.json). Photographer **Hudacko**, date **21 September 2012**, license **CC BY-SA 3.0**. The 1280-pixel Commons previews are preserved unchanged after download; see [attribution](sources/commons-pullen/README.md).

**Metadata caution:** many pages in this series repeat an incorrect generic reindeer description. Animal identifications here come from the photographs, not those copied descriptions. No archive staff were contacted and no challenge answer was submitted.

## Review handoff prompt

> Audit the proposed answer lowercase g for Q6. Independently inspect nomination PDF pages 3–7 and 14; Raleigh drawing 18630 and detail 12294; NCA 023; and Commons photos 25, 24, 23, 22, with 21 and 31 as checks. Identify the acorn-and-two-oak-leaf stored pig. Anchor chariot IV using Greek-key giraffe V and distinguish it from XIII. Trace the center row without skipping a position: d rabbit, e horse, f horse, g acorn pig. Check the stagger between outer Roman-numeral and center lowercase positions. Do not derive g from 7A, identify the stored pig from the older g entry, or trust the Commons pages' generic reindeer captions. State whether g follows under the question's fixed-chariot assumption. Assess the return-by-1980 premise separately from the later spatial mapping. Return a verdict, concrete supporting/conflicting evidence, and any remaining ambiguity. Do not research Q7.
