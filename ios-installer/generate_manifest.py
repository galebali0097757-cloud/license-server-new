#!/usr/bin/env python3
"""Create a manifest for an already signed and properly provisioned iOS IPA."""
import argparse
import pathlib
import plistlib
from urllib.parse import urlsplit

def https_url(s):
    url = urlsplit(s)
    if url.scheme != "https" or not url.netloc or url.username or url.password:
        raise argparse.ArgumentTypeError("An HTTPS URL without credentials is required")
    return s

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ipa-url",required=True,type=https_url)
    p.add_argument("--bundle-id",required=True)
    p.add_argument("--version",required=True)
    p.add_argument("--title",required=True)
    p.add_argument("--out",default="manifest.plist")
    a=p.parse_args()
    if not all(map(str.strip,(a.bundle_id,a.version,a.title))):
        p.error("bundle-id, version and title may not be empty")
    doc={"items":[{"assets":[{"kind":"software-package","url":a.ipa_url}],
          "metadata":{"bundle-identifier":a.bundle_id,"bundle-version":a.version,
                      "kind":"software","title":a.title}}]}
    pathlib.Path(a.out).write_bytes(plistlib.dumps(doc))
    print("Saved",a.out,"(signature not validated)")
if __name__=="__main__":
    main()
