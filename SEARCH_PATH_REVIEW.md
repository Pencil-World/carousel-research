# Review search path, focused on Q6–Q7

Research date: 8 November 2026. This is a reproducible route to the new evidence, not a verbatim record of every unsuccessful web query. See [REVIEW.md](REVIEW.md) for the conclusions and limits.

1. Read the original `README.md`, `SEARCH_PATH.md`, `EVIDENCE_INDEX.md`, `REVIEW_HANDOFF.md`, and source manifest. Recheck the 1976 inventory's storage entry and full arrangement drawing, rather than starting from the tentative letter `g`.

2. Search the web for **Raleigh carousel drawings collections**. A [Summer 2018 city newsletter](https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR24/raleigh-register-summer-2018.pdf), page 2, points to the museum's then-current PastPerfect catalogue and mentions 281 Pullen drawings. The old catalogue address no longer worked in the research search tool.

3. Follow the city's current [Historic Resources and Museums Program Collection page](https://raleighnc.gov/parks-and-recreation/services/historic-resources-and-museums-program/historic-resources-and-1). Its **online database** link leads to [Raleigh's CatalogAccess catalogue](https://raleighhrmprogram.catalogaccess.com/). This is the official link connecting the catalogue to the city.

4. The search tool returned 403 for the catalogue, and local browser use was disabled. An ordinary public HTTP request retrieved its home page. Read the public frontend's linked search bundle; it specifies the read-only keyword endpoint `/api/search/keyword`. No authentication or write endpoint was used. The saved HTML and JavaScript files document the request fields.

5. Search **pig**, including archive and photograph records. The result has 138 records, requiring two pages at 100 records per page. Locate **PPC2018.001.095** (pig drawing 7A), **PPC2019.001.237** (1981 acorn detail), and **PPC2019.001.242** (painted pig in 1982). Open the images, not just the descriptions. The acorn and two oak leaves match the 1976 storage entry. The API data records expose the same catalogue descriptions and public image IDs.

6. Search **PPC* AND map** to locate **PPC2018.001.001**, the Spring 1976 restoration working map. Open all four public views: overall sheet, bottom key, side key, title. Separate the date of the base drawing from the dates of later annotations. Search **PPC2018* AND 9A**, **9B**, **18A**, and **4A** to compare numbered cats and rabbits with the earlier descriptions. Do not treat these identification numbers as a proven old-coordinate crosswalk.

7. Search **carousel AND estimate**, **carousel AND stripping**, and **PPC2024.002***. The last query returns **81** public restoration-project records. Read their dates and descriptions, then inspect promising scans. The most useful for Q7 is **PPC2024.002.020**, dated 31 August 1976: it explicitly names Dick Norton and $400 per animal, but dates his examination to 1971. Record that discrepancy.

8. Compare **PPC2024.002.022** (Layton's 6 December 1976 proposal), **PPC2024.002.037A–B** (Farley's 28 February 1977 fundraising letter), and **PPC2024.002.059** (Cameron's September 1977 proposal). They distinguish different dates, authors, unit costs, and combined project totals. Do not use any as proof of a 1975 amount merely because the numbers look plausible.

9. Search **carousel AND history**. This also finds **PRCR2018.008.028**, the Spring 1983 *Merry-Go-Roundup* issue. Inspect its public image list: only front, rear, and page 2 are available, not the article interior. This is a precise remaining lead, not a solved source.

10. Recheck [NCA photograph 023](https://www.carousels.org/psp/PullenPark/Pullen%20Park023.html), dated 28 May 2004, and [004](https://www.carousels.org/psp/PullenPark/Pullen%20Park004.html), dated 10 November 2006. The former captions the acorn pig as second-row; the latter shows a second-row cat that can be compared with a numbered drawing. Neither dates the pig's original return. Retain the need for an arrangement anchored on the fixed chariots.

Exact commands used for the catalogue can be rerun from the repository. These make public, read-only HTTP requests and save the response and request metadata:

```bash
python3 ./scripts/query_city_catalog.py pig raleigh-search-pig
python3 ./scripts/query_city_catalog.py pig raleigh-search-pig-page2 --skip 100
python3 ./scripts/query_city_catalog.py 'PPC* AND map' raleigh-search-pullen-map
python3 ./scripts/query_city_catalog.py 'PPC2024.002*' raleigh-search-project-2024
python3 ./scripts/fetch_city_records.py ./sources/raleigh-search-project-2024.json raleigh-project-2024
```

The catalogue returned server errors for a requested page size of 200; retrying with its working 100-record page size succeeded. The script now caps requests at 100. A public larger-image URL listed in metadata returned 403; no access controls were bypassed. The working image endpoint's scans were retained instead.

`download_sources.py` contains the precise public record and image URLs for the cited scans. Its `--only` option fetches named entries without retrying all older failed museum pages. The manifests and each search's `.request.json` companion allow a reviewer to check URLs, request bodies, retrieval times, and hashes.
