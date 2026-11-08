#!/usr/bin/env python3
"""Save the public research sources and their hashes for later review."""
import concurrent.futures
import argparse
import datetime
import hashlib
import json
import pathlib
import urllib.request
from public_catalogue import public_response_bytes

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
    "raleigh-cat-18a-drawing.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/32631",
    "nca-pullen-rabbits-010.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park010.jpg",
    "nca-pullen-horse-rabbit-007.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park007.jpg",
    "nca-pullen-jumpers-organ-009.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park009.jpg",
    "nca-pullen-cats-032.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park032.jpg",
    "nca-pullen-inner-cat-039.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park039.jpg",
    "raleigh-cat-9a-drawing.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/50582",
    "raleigh-cat-9b-drawing.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/33108",
    "raleigh-rabbit-4a-drawing.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/46075",
    "raleigh-mgr-1983-front.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/44982",
    "raleigh-mgr-1983-reverse.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/44983",
    "raleigh-mgr-1983-title.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/44984",
    "raleigh-mgr-1983-record.json": "https://raleighhrmprogram.catalogaccess.com/api/items/20325",
    "raleigh-mgr-1983-images.json": "https://raleighhrmprogram.catalogaccess.com/api/items/20325/images",
    "raleigh-restoration-map-large.jpg": "https://s3.amazonaws.com/ppwebassets/release/30527/67308602-ad16-4c1e-8bb1-c28804623723_lg.JPG",
    "raleigh-catalog-display-settings.json": "https://raleighhrmprogram.catalogaccess.com/api/appearance/common/settings",
    "raleigh-standing-horse-1-romance.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/40759",
    "raleigh-standing-metal-horse-1.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/41822",
    "pullen-interpretive-story-data.json": "https://www.arcgis.com/sharing/rest/content/items/f69cf8565252453f971333c4510ac146/data?f=json",
    "raleigh-arrangement-map-outer-key.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/46647",
    "raleigh-arrangement-map-jumper-key.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/46648",
    "raleigh-arrangement-map-title.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/46649",
    "raleigh-arrangement-map-images.json": "https://raleighhrmprogram.catalogaccess.com/api/items/17285/images",
    "raleigh-spotlight-1978-page-4.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98808",
    "raleigh-restoration-arrangement-map.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/46646",
    "raleigh-restoration-arrangement-map-record.json": "https://raleighhrmprogram.catalogaccess.com/api/items/17285",
    "raleigh-spotlight-1978-page-4-5.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98809",
    "raleigh-letter-farley-1976-05-17.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98176",
    "raleigh-progress-report-1976-08-31.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98180",
    "raleigh-layton-proposal-1976-12-06.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98184",
    "raleigh-fundraising-letter-1977-02-28.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98401",
    "raleigh-funding-memo-1977-03-04.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98405",
    "raleigh-cost-estimate-1977-04-15.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/98415",
    "raleigh-spotlight-1978-images.json": "https://raleighhrmprogram.catalogaccess.com/api/items/35024/images",
    "wake-fine-arts-finding-aid.html": "https://libraryarchives.wakegov.com/repositories/2/resources/43",
    "raleigh-drawing-pig-7a.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/50167",
    "raleigh-drawing-pig-7b-saddle.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/36653",
    "raleigh-drawing-pig-16a.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/50087",
    "raleigh-drawing-pig-16b.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/35636",
    "raleigh-slide-pig-7a-1979.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/29835",
    "raleigh-slide-acorn-detail-1981.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/27469",
    "raleigh-slide-pig-7a-1982.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/28987",
    "raleigh-slide-pig-7b-1981.jpg": "https://raleighhrmprogram.catalogaccess.com/api/images/27503",
    "raleigh-item-18630.json": "https://raleighhrmprogram.catalogaccess.com/api/items/18630",
    "raleigh-item-18634.json": "https://raleighhrmprogram.catalogaccess.com/api/items/18634",
    "raleigh-item-20734.json": "https://raleighhrmprogram.catalogaccess.com/api/items/20734",
    "raleigh-item-20738.json": "https://raleighhrmprogram.catalogaccess.com/api/items/20738",
    "raleigh-item-12294.json": "https://raleighhrmprogram.catalogaccess.com/api/items/12294",
    "raleigh-item-12287.json": "https://raleighhrmprogram.catalogaccess.com/api/items/12287",
    "raleigh-item-12299.json": "https://raleighhrmprogram.catalogaccess.com/api/items/12299",
    "raleigh-item-12312.json": "https://raleighhrmprogram.catalogaccess.com/api/items/12312",
    "raleigh-hrm-item-details.js": "https://raleighhrmprogram.catalogaccess.com/bundles/item-details?v=SJloGrEw6Y9Owj0-a-rINkPsglf73W1mCp1eAsZZqIw1",
    "raleigh-archive-18630-view.html": "https://raleighhrmprogram.catalogaccess.com/Items/ArchiveDetails/18630",
    "raleigh-photo-12287-view.html": "https://raleighhrmprogram.catalogaccess.com/Items/PhotoDetails/12287",
    "raleigh-archive-18634-view.html": "https://raleighhrmprogram.catalogaccess.com/Items/ArchiveDetails/18634",
    "raleigh-hrm-catalog-libs.js": "https://raleighhrmprogram.catalogaccess.com/bundles/libs?v=6o9Wg1d5gDZBvDyUg5tmLKD0qdh0chxWTa4AvV5oX3g1",
    "raleigh-hrm-keyword-search.js": "https://raleighhrmprogram.catalogaccess.com/bundles/multitype-keyword-search?v=1f3G_xcEsWalQkwYEvuKxAmeeqzw-_CgKVOyYMrCZ_81",
    "raleigh-hrm-search-view.html": "https://raleighhrmprogram.catalogaccess.com/Search/ItemsView",
    "raleigh-hrm-catalog-app.js": "https://raleighhrmprogram.catalogaccess.com/bundles/app?v=RZ0tJpVmTO8XUg65dgeQ5LvXWsm2TjSZZ7b7oBQuhtk1",
    "raleigh-register-summer-2018.pdf": "https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR24/raleigh-register-summer-2018.pdf",
    "raleigh-hrm-catalog-home.html": "https://raleighhrmprogram.catalogaccess.com/",
    "raleigh-hrm-collections.html": "https://raleighnc.gov/parks-and-recreation/services/historic-resources-and-museums-program/historic-resources-and-1",
    "raleigh-fine-arts-2015-newsletter.html": "https://archive.constantcontact.com/fs142/1102316631685/archive/1122369945080.html",
    "nca-pullen-004-caption.html": "https://www.carousels.org/psp/PullenPark/Pullen%20Park004.html",
    "nca-pullen-022-caption.html": "https://www.carousels.org/psp/PullenPark/Pullen%20Park022.html",
    "nca-pullen-023-caption.html": "https://www.carousels.org/psp/PullenPark/Pullen%20Park023.html",
    "nca-pullen-census.html": "https://carousels.org/USACensus/census.pl?NCANo=150",
    "wake-fine-arts-catalog.html": "https://catalog.wake.gov/Record/778096",
    "technician-1977-04-06.pdf": "https://ocr.lib.ncsu.edu/ocr/te/technician-v57n76-1977-04-06/technician-v57n76-1977-04-06.pdf",
    "pullen-nara-76001344.pdf": "https://nara-media.s3.amazonaws.com/electronic-records/rg-079/NPS_NC/76001344.pdf",
    "nca-pullen-second-row-horse-017.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park017.jpg",
    "nca-pullen-second-row-horse-020.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park020.jpg",
    "nca-pullen-second-row-horse-034.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park034.jpg",
    "nca-pullen-horses-cat-view.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park038.jpg",
    "nca-pullen-mule.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park018.jpg",
    "williamsburg-tourism-carousel-display.png": "https://assets.simpleviewinc.com/simpleview/image/upload/c_limit%2Cq_75%2Cw_1200/v1/crm/williamsburgva/Listings-43-18-_BEDB09EA-F0CB-ED50-CF5BA5FEF21371A0-bedb072ce4a742a_bedb4f34-edc5-353d-3bad9280d9287330.png",
    "nca-guide-004-restoration.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide004.pdf",
    "nca-guide-005-publicity.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide005.pdf",
    "nca-guide-006-operation.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide006.pdf",
    "nca-guide-015-fundraising.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide015.pdf",
    "nca-guide-016-fundraising.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide016.pdf",
    "nca-guide-017-fundraising.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide017.pdf",
    "nca-pullen-tiger.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park025.jpg",
    "nca-pullen-chariot-and-giraffe.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park041.jpg",
    "nca-pullen-chariot.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park013.jpg",
    "nca-pullen-lion.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park027.jpg",
    "carousel-news-2019-spring.pdf": "https://carouselhistory.com/wp-content/uploads/2019/05/Carousel-News-Spring-2019-Vol-35-No1.pdf",
    "american-roads-2016.html": "https://americanroads.net/art_spring2016.htm",
    "nca-guide-008-pullen-restoration-news.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide008.pdf",
    "nca-pullen-flag-horse-and-lion.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park004.jpg",
    "nca-pullen-two-pigs.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park022.jpg",
    "nca-pullen-second-row-pig.jpg": "https://carousels.org/psp/PullenPark/Pullen%20Park023.jpg",
    "williamsburg-camel.jpg": "https://cwf20siteprodstg.blob.core.windows.net/prod/images/Sidewalks_to_Rooftops-_Outdoor_Folk_Art_4.width-500.jpg",
    "williamsburg-cat.jpg": "https://cwf20siteprodstg.blob.core.windows.net/prod/images/Sidewalks_to_Rooftops-_Outdoor_Folk_Art_1.width-500.jpg",
    "nca-guide-003-promotion-restoration.pdf": "https://carousels.org/CRG/NCA_Carousel_Resource_Guide003.pdf",
    "nca-pullen-photo-index.html": "https://www.carousels.org/psp/PullenPark/",
    "pullen-1976-national-register.pdf": "https://files.nc.gov/ncdcr/nr/WA0008.pdf",
    "pullen-city-landmark-report.pdf": "https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR10/CarouselAtPullenPark_LandmarkOrdinanceAndReport.pdf",
    "williamsburg-sidewalks-to-rooftops.html": "https://www.colonialwilliamsburg.org/discover/historic-area/art-museums-of-colonial-williamsburg/exhibitions/sidewalks-to-rooftops-outdoor-folk-art/",
    "williamsburg-collections.html": "https://emuseum.colonialwilliamsburg.org/groups",
    "williamsburg-exhibit-family.jpg": "https://cwf20siteprodstg.blob.core.windows.net/prod/images/carnival-folk-art-family.format-jpeg.width-2000.jpg",
    "williamsburg-carousel-cat.html": "https://emuseum.colonialwilliamsburg.org/objects/58638/carousel-figure-cat",
}


def fetch(item):
    name, url = item
    destination = ROOT / "sources" / name
    if destination.exists():
        body = destination.read_bytes()
        return {"file": name, "url": url, "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body), "status": "already saved"}
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (public historical research)"})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            body = public_response_bytes(response.read())
            if not body:
                raise ValueError("Empty response; no source content retrieved")
            destination.write_bytes(body)
            return {"file": name, "url": url, "final_url": response.url, "content_type": response.headers.get("Content-Type"), "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body), "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "saved"}
    except Exception as exc:
        return {"file": name, "url": url, "status": "failed", "error": str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", choices=list(SOURCES), help="Fetch only these named sources")
    args = parser.parse_args()
    (ROOT / "sources").mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        selected = ((name, SOURCES[name]) for name in args.only) if args.only else SOURCES.items()
        entries = list(pool.map(fetch, selected))
    manifest = ROOT / "sources" / "download-manifest.json"
    old_entries = json.loads(manifest.read_text()) if manifest.exists() else []
    old_by_file = {entry["file"]: entry for entry in old_entries}
    for entry in entries:
        if entry["status"] == "already saved" and entry["file"] in old_by_file:
            entry = old_by_file[entry["file"]]
        old_by_file[entry["file"]] = entry
    manifest.write_text(json.dumps(list(old_by_file.values()), indent=2) + "\n")
    for entry in entries:
        print(entry["file"], entry["status"], entry.get("bytes", entry.get("error")))


if __name__ == "__main__":
    main()
