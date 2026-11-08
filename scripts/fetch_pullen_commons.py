#!/usr/bin/env python3
"""Save public Commons photographs and provenance for the Pullen layout check."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1] / 'sources' / 'commons-pullen'
PARAMS = dict(action='query', format='json', generator='categorymembers',
              gcmtitle='Category:Pullen Park Carousel', gcmtype='file', gcmlimit='100',
              prop='imageinfo', iiprop='url|extmetadata', iiurlwidth='1280')
API = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(PARAMS)

def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'CarouselHistoricalResearch/1.0 (public source comparison)'})
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numbers', nargs='*', type=int)
    args = parser.parse_args()
    ROOT.mkdir(exist_ok=True)
    index = ROOT / 'index.json'
    if not index.exists():
        body = fetch(API)
        data = json.loads(body)
        if 'query' not in data:
            raise ValueError(str(data)[:300])
        index.write_bytes(body)
        (ROOT / 'index.request.json').write_text(json.dumps({
            'url': API, 'retrieved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}, indent=2)+'\n')
    data = json.loads(index.read_text())
    combined = dict(data['query']['pages'])
    part = 2
    while 'continue' in data:
        next_index = ROOT / f'index-{part}.json'
        url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({**PARAMS, **data['continue']})
        if not next_index.exists():
            body = fetch(url)
            next_data = json.loads(body)
            if 'query' not in next_data:
                raise ValueError(str(next_data)[:300])
            next_index.write_bytes(body)
            next_index.with_suffix('.request.json').write_text(json.dumps({
                'url': url, 'retrieved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}, indent=2)+'\n')
        data = json.loads(next_index.read_text())
        for key, value in data['query']['pages'].items():
            combined[key] = {**combined.get(key,{}), **value}
        part += 1
    pages = list(combined.values())
    print('Indexed pages:',len(pages))
    if not args.numbers:
        return
    selected=[p for p in pages if p.get('imageinfo') and p['title'] in [f'File:Pullen Park Carousel {n:02d}.JPG' for n in args.numbers]]
    def save(p):
        info=p['imageinfo'][0]
        url=info.get('thumburl',info['url'])
        filename=p['title'].removeprefix('File:').replace(' ','-')
        dest=ROOT/filename
        try:
            body=dest.read_bytes() if dest.exists() else fetch(url)
            if not body.startswith(b'\xff\xd8'):
                raise ValueError('Not a JPEG')
            dest.write_bytes(body)
            return dict(file=filename,url=url,source_page=info['descriptionurl'],
                        bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),
                        retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='saved')
        except Exception as exc:
            return dict(file=filename,url=url,status='failed',error=str(exc))
    path=ROOT/'manifest.json'
    old={e['file']:e for e in json.loads(path.read_text())} if path.exists() else {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for item in pool.map(save,selected):
            old[item['file']]=item
            print(item['file'],item['status'])
    path.write_text(json.dumps(list(old.values()),indent=2)+'\n')

if __name__=='__main__':
    main()
