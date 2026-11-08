# Q6: lowercase or uppercase row?

Research date: 8 November 2026. Scope: choose the row only; leave the exact letter open.

**Subsequent exact-letter result:** [Q6_POSITION.md](Q6_POSITION.md) maps the acorn pig to lowercase **g** by counting from chariot IV through overlapping photographs. The row-only investigation below is retained; its statement that the exact letter remains open is superseded by that spatial proof. The first-return date remains unverified.

**Use lowercase `a-r` as the supported working choice: the center / second row.** The acorn-and-oak-leaf pig is explicitly captioned as a second-row figure in a dated National Carousel Association photograph. The historical inventory uses lowercase letters for the center row. This establishes the later row strongly; the same row at its original return by 1980 remains an inference because the photograph is from 2004.

## Evidence chain

1. **Identify the stored animal by its carving.** The [1976 National Register nomination](https://files.nc.gov/ncdcr/nr/WA0008.pdf), PDF page 7, describes the stored pig with an acorn, two oak leaves, a scalloped blanket, and damaged hind legs. Inspect the [complete rendered page](evidence/1976-source-page-07.png). These features distinguish it from the other pigs; its later paint color alone is insufficient.
2. **Bridge that animal to the restoration documentation.** The city's [pig drawing, PPC2018.001.095](https://raleighhrmprogram.catalogaccess.com/archives/18630), visibly marked **No. 7A**, shows the acorn, leaves, and scalloped blanket. The [9 September 1981 detail slide, PPC2019.001.237](https://raleighhrmprogram.catalogaccess.com/photos/12294), shows the carving and identifies 7A. Compare the saved [drawing](sources/raleigh-drawing-pig-7a.jpg) and [detail](sources/raleigh-slide-acorn-detail-1981.jpg). The identification is based on sculpted features, not on interpreting the suffix A as a row code.
3. **Establish its documented later row.** [NCA photograph 023](https://carousels.org/psp/PullenPark/Pullen%20Park023.html), credited to Rebekah Creech and dated **28 May 2004**, is captioned **“Dentzel Second Row Pig.”** Its [image](sources/nca-pullen-second-row-pig.jpg) shows the matching acorn-and-leaf ornament beside a scalloped blanket on the black-and-white pig. The brown pig visible behind it is closer to the center of the carousel. The caption and radial arrangement agree on the second / middle row.
4. **Translate the row into the historical case convention.** In the nomination, PDF page 4 begins **Center Row – Jumpers** with lowercase a, b, c, d; the sequence continues through r. PDF page 6 begins **Inner Row – Jumpers** with uppercase A, B, C, D, continuing through R on page 7. See the [center-row page](evidence/1976-source-page-04.png) and [inner-row page](evidence/1976-source-page-06.png). Consequently, a second-row / center-row pig belongs to the **lowercase `a-r`** answer set.

## New checks and exclusions

The catalogue was searched specifically for row terminology, rather than treating every pig photograph as the stored animal:

| Query | Results | Consequence |
| --- | --- | --- |
| `7A AND row` | 0 | No explicit 7A-to-row wording found by this query. |
| `carousel AND "center row"` | 7 | Includes a dated 1998 pig photograph, but visual inspection identifies a different pig. |
| `carousel AND "inner row"` | 1 | A horse photograph; does not locate 7A. |

Two additional dated photographs were inspected:

- [PPC2019.001.743](https://raleighhrmprogram.catalogaccess.com/photos/14610), slide stamped **NOV82A5**, [saved image](sources/raleigh-mounted-carousel-november-1982.jpg): the visible cream pig has elaborate straps and a different blanket. It does not supply an early placement for the acorn pig.
- [PPC2019.001.747](https://raleighhrmprogram.catalogaccess.com/photos/14617), **11 September 1998**, [saved image](sources/raleigh-center-row-pig-1998.jpg): the catalogue explicitly says center row, but the animal is again the cream pig with different trappings. It cannot independently corroborate the acorn pig's row.

These records were excluded as evidence for the stored pig, despite containing useful-sounding dates or row descriptions.

## What remains open

**The exact letter is not decided here.** No. 7A is an animal identifier; converting 7 to the seventh letter or A to an uppercase position is not a valid proof. The pre-restoration inventory already records another pig at lowercase g.

The NCA photograph proves a 2004 center-row placement. The dated restoration slides show 7A off the carousel in August 1979, an acorn detail in September 1981, and fresh paint in March 1982. They do not independently prove the question's return-by-1980 premise or exclude later movement between rows. A dated installation record or an early mounted photograph of the acorn pig would close that gap. Thus confidence is **high for the photographed later row**, and **qualified for its original insertion row**.

Fixed chariot positions are unnecessary for this case-only decision. They will matter when counting a particular lettered position.

## Reproduce the search

1. Open the [nomination PDF](sources/pullen-1976-national-register.pdf), PDF pages 4, 6, and 7. Read the row headings and stored-animal description; do not rely solely on OCR.
2. Open city records [18630](https://raleighhrmprogram.catalogaccess.com/archives/18630) and [12294](https://raleighhrmprogram.catalogaccess.com/photos/12294). Match the acorn, leaves, and blanket to the stored description and confirm the 7A label.
3. Open [NCA photograph 023](https://carousels.org/psp/PullenPark/Pullen%20Park023.html). Read both its caption and date, then inspect the carving in the image. The page without `www` responded successfully during this review.
4. Search Raleigh's public catalogue for the three queries above. The public search endpoint and payload are documented in `scripts/query_city_catalog.py`; it performs read-only searches. From the repository root, rerun:

   ```bash
   python3 scripts/query_city_catalog.py '7A AND row' raleigh-row-search-7a
   python3 scripts/query_city_catalog.py 'carousel AND "center row"' raleigh-row-search-center
   python3 scripts/query_city_catalog.py 'carousel AND "inner row"' raleigh-row-search-inner
   ```

5. Compare the saved search responses and `.request.json` files in `sources/`. Inspect photos 14610 and 14617 and exclude them from the acorn-pig inference for the reasons above. The original photo descriptions are already in [the pig-photo index](sources/raleigh-pig-photos/descriptions.json).
6. Verify the new image URLs and SHA-256 hashes in [the download manifest](sources/download-manifest.json). No archive staff were contacted and no answer was submitted.

## Focused review handoff prompt

> Review only whether the stored Pullen Park pig belongs to lowercase a-r or uppercase A-R. Read Q6_ROW.md, then independently inspect nomination PDF pages 4, 6, and 7; Raleigh drawing 18630; detail slide 12294; and NCA photograph 023 with its dated caption. Check whether the acorn, two oak leaves, and scalloped blanket identify the same carving. Verify the historical center/inner case convention. Distinguish a demonstrated 2004 row from an inferred original insertion row. Do not derive a letter from No. 7A, and do not substitute the cream pig in photos 14610 or 14617. Return: supported case, evidence, confidence, and any missing chronological link. Do not decide the exact letter or research Q7.
