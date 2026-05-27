#!/usr/bin/env python3
"""Ping IndexNow after deployment to notify search engines of updated URLs."""
import os, urllib.request, json, sys

def main():
    key = os.environ.get('INDEXNOW_KEY') or open('.env.local').readlines()
    if not key:
        # Try reading from .env.local
        for line in open('.env.local'):
            if line.startswith('INDEXNOW_KEY='):
                key = line.split('=', 1)[1].strip()
                break
    
    if not key:
        print('ERROR: INDEXNOW_KEY not found')
        sys.exit(1)
    
    host = 'audiosoftwarehub.online'
    sitemap_url = f"https://{host}/sitemap.xml"
    
    # Bing IndexNow endpoint
    ping_url = f"https://www.bing.com/indexnow?url={sitemap_url}&key={key}"
    
    try:
        req = urllib.request.Request(ping_url)
        resp = urllib.request.urlopen(req, timeout=10)
        print(f"OK: IndexNow pinged successfully (HTTP {resp.status})")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
