"""Keep research fields from a city catalogue response for public sharing.

The API embeds account, permissions, administrative, and recursive internal
objects in item responses. Those objects are unrelated to this research.
"""
import json


def pick(data, fields):
    return {key: data[key] for key in fields if key in data}


def public_dictionary(data):
    if not isinstance(data, dict):
        return data
    return pick(data, ("Id", "Title", "Description"))


def public_city_record(data):
    if not isinstance(data, dict) or not isinstance(data.get("Item"), dict):
        return data
    item = data["Item"]
    result = pick(item, (
        "Id", "ItemType", "ItemId", "AlternativeItemId", "AlternativeItemName",
        "YearRangeFrom", "YearRangeTo", "Description", "CreationDate", "Title",
        "ExhibitLabel", "IsPublicAccess", "OldNumber", "CreatedDate",
        "LastModifiedDate", "CatalogDate", "NumberOfCatalogItemImages",
        "NumberOfCatalogItemAttachments", "NumberOfCatalogItemUrls",
    ))
    for key in ("Collection", "ItemName", "OtherName"):
        if key in item:
            result[key] = public_dictionary(item[key])
    dimension = item.get("CatalogItemDimension")
    if isinstance(dimension, dict):
        result["CatalogItemDimension"] = pick(dimension, (
            "UnitsId", "Circumference", "Depth", "Diameter", "Height", "Length",
            "Weight", "Width", "Count", "Details",
        ))
    photo = item.get("CatalogItemPhoto")
    if isinstance(photo, dict):
        result["CatalogItemPhoto"] = pick(photo, (
            "DimensionDetails", "Copyrights", "NegativeNumber", "FrameNumber",
            "SlideNumber", "Frame",
        ))
        for key in ("Photographer", "Studio", "ProcessingMethod", "PrintSize", "FilmSize", "OriginalCopy", "Event"):
            if key in photo:
                result["CatalogItemPhoto"][key] = public_dictionary(photo[key])
    result["Images"] = []
    for image in item.get("Images", []):
        obj = image.get("ImageObject", image)
        if not isinstance(obj, dict):
            continue
        public_image = pick(obj, (
            "Id", "Caption", "IsRestricted", "IsPublic", "ImageDetails",
            "Copyrights", "ImageSize", "NegativeNumber", "AltText",
        ))
        if "Id" in public_image:
            public_image["PublicImageUrl"] = (
                "https://raleighhrmprogram.catalogaccess.com/api/images/"
                + str(public_image["Id"])
            )
        result["Images"].append({"ImageObject": public_image})
    output = {"Item": result}
    for key in ("Title", "ChildItems", "RelatedRecords", "Attachments", "Urls"):
        if key in data:
            value = data[key]
            if isinstance(value, list):
                value = [pick(entry, ("Id", "ItemId", "Title", "Description", "Url", "URL", "Name", "FileName", "Caption"))
                         if isinstance(entry, dict) else entry for entry in value]
            output[key] = value
    output["PublicationNote"] = (
        "Research fields retained; unrelated account and administrative metadata "
        "removed. The publication manifest preserves the original response hash."
    )
    return output


def public_response_bytes(body):
    try:
        original = json.loads(body)
    except (ValueError, UnicodeError):
        return body
    transformed = public_city_record(original)
    if transformed is original:
        return body
    return (json.dumps(transformed, indent=2, ensure_ascii=False) + "\n").encode()
