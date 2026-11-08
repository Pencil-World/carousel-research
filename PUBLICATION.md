# Public copy and provenance

This repository contains the carousel research archive and the supplied carousel photograph. Unrelated CTF projects and files are outside its scope.

The local research reports are retained, with links and commands made portable. The original report is named **RESEARCH.md**; **README.md** is the repository landing page. The original local archive has not been replaced.

Some public catalogue item responses embedded recursive administrative and account objects unrelated to the research. The published JSON retains the item identifiers, descriptions, dates, collection names, dimensions, photograph credits, and public image references needed to review the findings. Account, permission, insurance, appraisal-administration, and other unrelated internal objects were omitted. Descriptions and the source scans were not rewritten to alter the evidence.

The public versions of the download scripts apply the same catalogue filter to new item responses. The filter is in [scripts/public_catalogue.py](scripts/public_catalogue.py); [scripts/prepare_public_repository.py](scripts/prepare_public_repository.py) records the export procedure.

- [Main source manifest](sources/download-manifest.json): `sha256` verifies the published file. When a file was curated, `original_sha256` and `original_bytes` retain the original response's provenance.
- [Commons photograph manifest](sources/commons-pullen/manifest.json): source pages, public preview URLs, retrieval dates, and hashes for the Q6 photographic sequence; attribution is retained [alongside the files](sources/commons-pullen/README.md).
- [Original manifests](provenance/): preserve the original retrieval metadata and response hashes. They do not contain the omitted response bodies.
- [Publication transformations](provenance/publication-transforms.json): lists changed research files with their original and published hashes.
- [Published file inventory](provenance/published-files.json): verifies the files in this snapshot, except the inventory itself and Git's internal files.

Dates in catalogue accession identifiers do not necessarily indicate the date when a drawing or photograph was created. Failed downloads remain recorded as failures; an unavailable or empty response is not evidence.

Source publications, photographs, drawings, and website material retain their original attribution and rights. No blanket license is applied to third-party material. Source URLs and credits are retained for review.
