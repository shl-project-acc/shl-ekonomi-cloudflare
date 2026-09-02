"""
All-in-One Instant Indexing Script for shlproject.com
Integrates:
1. IndexNow API (Bing, Yandex, Naver, Seznam) - Immediate Submission
2. Google Indexing API (Googlebot) - If service_account.json is provided
"""

import os
import sys
import json
import requests
import xml.etree.ElementTree as ET

SITE_HOST = "shlproject.com"
INDEXNOW_KEY = "e03e7d3fa47d4869910d65b78f4b0df1"
INDEXNOW_KEY_LOCATION = f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt"
SITEMAP_URL = f"https://{SITE_HOST}/sitemap-0.xml"

def get_urls_from_sitemap():
    print(f"[*] Mengambil daftar URL dari sitemap: {SITEMAP_URL} ...")
    try:
        resp = requests.get(SITEMAP_URL, timeout=15)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        # Parse XML namespaces
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [elem.text.strip() for elem in root.findall('.//ns:loc', namespaces)]
        print(f"[✓] Berhasil menemukan {len(urls)} URL dari sitemap.")
        return urls
    except Exception as e:
        print(f"[!] Gagal mengambil sitemap: {e}")
        # Fallback to local default canonical post list
        return [
            f"https://{SITE_HOST}/",
            f"https://{SITE_HOST}/post/manajemen/Cara-Sederhana-Memahami-Manajemen-Risiko-Bagi-Pemula/",
            f"https://{SITE_HOST}/post/bisnis/Panduan-Lengkap-Merancang-Strategi-Bisnis-dari-Nol-Anti-Boncos/",
            f"https://{SITE_HOST}/post/bisnis/Cara-Mengelola-Arus-Kas-Usaha-agar-Bisnis-Bertahan-di-Segala-Musim/",
            f"https://{SITE_HOST}/post/ekonomi/Rahasia-Memahami-Cara-Kerja-Inflasi-agar-Nilai-Uang-Tidak-Tergerus-Diam-Diam/",
            f"https://{SITE_HOST}/post/fiqh/Panduan-Lengkap-Fiqh-Muamalah-Praktis-untuk-Bisnis-Modern-yang-Berkah/",
        ]

def submit_indexnow(urls):
    print("\n" + "="*50)
    print("🚀 SUBMIT INDEXNOW (BING, YANDEX, SEZNAM, NAVER)")
    print("="*50)
    
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": urls
    }
    
    endpoints = [
        {"name": "IndexNow Standard (Bing & Global)", "url": "https://api.indexnow.org/indexnow"},
        {"name": "Microsoft Bing IndexNow", "url": "https://www.bing.com/indexnow"},
        {"name": "Yandex IndexNow", "url": "https://yandex.com/indexnow"}
    ]
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    
    for ep in endpoints:
        try:
            r = requests.post(ep["url"], json=payload, headers=headers, timeout=15)
            if r.status_code in [200, 202]:
                print(f"[✓] {ep['name']}: Berhasil dikirim! (Status: {r.status_code})")
            else:
                print(f"[!] {ep['name']}: Respon {r.status_code} - {r.text}")
        except Exception as e:
            print(f"[X] {ep['name']}: Error koneksi - {e}")

def submit_google_indexing(urls, credentials_file="service_account.json"):
    print("\n" + "="*50)
    print("🔍 SUBMIT GOOGLE INDEXING API (GOOGLEBOT)")
    print("="*50)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cred_path = os.path.join(script_dir, credentials_file)
    
    if not os.path.exists(cred_path):
        # Check parent directory as well
        cred_path_alt = os.path.join(os.path.dirname(script_dir), credentials_file)
        if os.path.exists(cred_path_alt):
            cred_path = cred_path_alt
        else:
            print(f"[!] Berkas '{credentials_file}' belum ditemukan.")
            print(f"    ℹ️ Info: Untuk Google Indexing API, masukkan file service_account.json dari Google Cloud Console ke folder 'scripts/'.")
            print(f"    ℹ️ (IndexNow untuk Bing & Yandex tetap berjalan 100% tanpa service_account.json).")
            return

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        
        SCOPES = ["https://www.googleapis.com/auth/indexing"]
        credentials = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
        service = build("indexing", "v3", credentials=credentials)
        
        for url in urls:
            content = {
                "url": url,
                "type": "URL_UPDATED"
            }
            res = service.urlNotifications().publish(body=content).execute()
            notify_time = res.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "OK")
            print(f"[✓] Googlebot notified: {url} ({notify_time})")
    except ImportError:
        print("[!] Modul google-api-python-client belum terpasang. Jalankan: pip install google-api-python-client google-auth")
    except Exception as e:
        print(f"[!] Gagal menghubungi Google Indexing API: {e}")

def main():
    print("==================================================")
    print("⚡ SHL PROJECT — ALL-IN-ONE INSTANT INDEXING TOOL")
    print("==================================================")
    
    # Check if specific URL passed as argument
    if len(sys.argv) > 1:
        target_urls = [sys.argv[1]]
        print(f"[*] Mode Single URL: {target_urls[0]}")
    else:
        target_urls = get_urls_from_sitemap()
        
    # 1. Submit IndexNow (Bing & Yandex)
    submit_indexnow(target_urls)
    
    # 2. Submit Google Indexing API
    submit_google_indexing(target_urls)
    
    print("\n" + "="*50)
    print("✅ Selesai! Seluruh sinyal indexing telah dipancarkan.")
    print("==================================================")

if __name__ == "__main__":
    main()
