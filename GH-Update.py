import requests
import schedule
import time
import os
from datetime import datetime

print(f"Script started successfully.[",datetime.now(),"]")

def fetch_release_links():
    owner = ''
    repo = ''
    nflie = ''
    file_path = '/web/ghnewest/index.html'

    api_url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    response = requests.get(api_url)
    print(f"Init successfully.[",datetime.now(),"]")

    if response.status_code == 200:
        release = response.json()
        print(f"Get successfully.[",datetime.now(),"]")
        if release:
            # get release
            assets = release.get('assets', [])
            if assets:
                download_url = assets[nfile].get('browser_download_url')
                timequeryforhttp = datetime.now()
                if download_url:
                    # make HTML format string
                    html_content = f'<!DOCTYPE html><html><head><title>Latest Release</title><meta charset="utf-8" /><link rel="shortcut icon" href="https://github.com/chromium/chromium/blob/main/chrome/app/theme/chromium/product_logo_24.png?raw=true"><style>h2{{font: 400 40px/1.5 Helvetica, Verdana, sans-serif;margin: 0;padding: 0;}} .ghul{{list-style-type: none;margin: 0;padding: 0;width: 100%;}} .lcul{{overflow: auto;list-style-type: none;height: 50px;left: 0;}} .linkgh {{font: 200 20px/1.5 Helvetica, Verdana, sans-serif;border-bottom: 1px solid #ccc;}} li:last-child {{border: none;}} .linklc{{height: 25px;float: left;margin-right: 0px;border-right: 1px solid #aaa;padding: 0 20px;}} .linkgh a{{text-decoration: none;color: #000;display: block;-webkit-transition: font-size 0.3s ease, background-color 0.3s ease;-moz-transition: font-size 0.3s ease, background-color 0.3s ease;-o-transition: font-size 0.3s ease, background-color 0.3s ease;-ms-transition: font-size 0.3s ease, background-color 0.3s ease;transition: font-size 0.3s ease, background-color 0.3s ease;}}li a:hover {{font-size: 30px;background: rgb(251, 235, 216);}} .bg{{background-size: cover;background-color: rgb(255, 246, 235);background-repeat:no-repeat;background-position-x:center;}} .linklc a:hover {{color: #666;}} .linklc a {{color: rgb(149,149,149);}}</style></head><body class="bg" width="100%"><div><h2>Latest Release for Ungoogled Chromium</h2><h3>UPDATED AT UTC+8 {timequeryforhttp}</h3><ul class="ghul">'
                    # html_content += f'<li class="linkgh"><a href="https://m0e.top/{download_url}" title="{download_url}">PROXY1 - Accerated link from our site</a></li>'
                    html_content += f'<li class="linkgh"><a href="https://mirror.ghproxy.com/{download_url}" title="{download_url}">PROXY2 - Accerated link from official GHPROXY.COM</a></li>'
                    html_content += f'<li class="linkgh"><a href="https://gh-proxy.com/{download_url}" title="{download_url}">PROXY3 - Accerated link from GH-PROXY.COM</a></li>'
                    html_content += f'<li class="linkgh"><a href="{download_url}" title="{download_url}">ORIGINAL</a></li>'
                    html_content += '</ul></div><hr/><ul class="lcul"><li class="linklc"><a href="https://github.com/macchrome/winchrome/">View Github original</a></li><li class="linklc"><a href="run.py">View script</a></li><li class="linklc"><a href="run.log">View Log</a></li></ul></body></html>'

                    # write to file
                    with open(file_path, 'w') as file:
                        file.write(html_content)
                    print(f"Release links fetched and stored in {file_path} successfully![",datetime.now(),"]")
                else:
                    print("No download URL found for the latest release.[",datetime.now(),"]")
            else:
                print("No assets found for the latest release.[",datetime.now(),"]")
        else:
            print("No release found for this repository.[",datetime.now(),"]")
    else:
        print("Failed to fetch latest release. Status code:", response.status_code,"[",datetime.now(),"]")

fetch_release_links()

# Run once an hour.
schedule.every().hour.do(fetch_release_links)

# Keep script running.
while True:
    schedule.run_pending()
    time.sleep(1)
