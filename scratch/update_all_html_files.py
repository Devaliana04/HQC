import os
import json
import re

# Load 120 keywords
with open('scratch/keywords_100.txt', 'r', encoding='utf-8') as f:
    KEYWORDS_STR = f.read().strip()
KEYWORDS_LIST = [k.strip() for k in KEYWORDS_STR.split(',') if k.strip()]

DOMAIN = "https://hqconstruction.id"

# Base Organization & WebSite Schemas
ORG_SCHEMA = {
    "@type": ["Organization", "GeneralContractor", "HomeAndConstructionBusiness"],
    "@id": f"{DOMAIN}/#organization",
    "name": "HQC — High Quality Construction",
    "alternateName": ["HQC", "High Quality Construction", "HQC Construction"],
    "url": f"{DOMAIN}/",
    "logo": {
        "@type": "ImageObject",
        "@id": f"{DOMAIN}/#logo",
        "url": f"{DOMAIN}/favicon.png",
        "contentUrl": f"{DOMAIN}/favicon.png",
        "caption": "Logo HQC High Quality Construction",
        "width": 512,
        "height": 512
    },
    "image": {
        "@type": "ImageObject",
        "url": f"{DOMAIN}/assets/images/og/hqc-og-home.jpg",
        "width": 1200,
        "height": 630
    },
    "description": "Perusahaan jasa konstruksi profesional berspesialisasi dalam pembangunan vila mewah, hotel, resort, pekerjaan struktur pembesian, instalasi utilitas MEP, dan finishing arsitektur berkualitas tinggi.",
    "telephone": "+6282144267826",
    "email": "info@hqconstruction.id",
    "priceRange": "$$$",
    "address": {
        "@type": "PostalAddress",
        "addressCountry": "ID"
    },
    "contactPoint": [
        {
            "@type": "ContactPoint",
            "telephone": "+6282144267826",
            "contactType": "customer service",
            "areaServed": "ID",
            "availableLanguage": ["Indonesian", "English"]
        }
    ],
    "knowsAbout": KEYWORDS_LIST,
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Layanan Konstruksi HQC",
        "itemListElement": [
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Pembangunan Vila Eksklusif",
                    "description": "Konstruksi vila tropis modern dan private villa dengan standar mutu arsitektural tinggi."
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Konstruksi Hotel & Resort",
                    "description": "Pembangunan akomodasi pariwisata, boutique hotel, dan hospitality resort."
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Pekerjaan Struktur & Pondasi",
                    "description": "Pondasi bore pile, tulangan pembesian presisi, dan pengecoran struktur beton bertulang."
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Instalasi MEP & Utilitas",
                    "description": "Sistem perpipaan PPR/PVC sebelum pengecoran, instalasi kelistrikan conduit, dan sanitasi."
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Finishing Arsitektur & Fasad",
                    "description": "Finishing dinding lengkung, batu alam, travertin, terrazzo, dan kolam renang infinity."
                }
            }
        ]
    }
}

WEBSITE_SCHEMA = {
    "@type": "WebSite",
    "@id": f"{DOMAIN}/#website",
    "url": f"{DOMAIN}/",
    "name": "HQC High Quality Construction",
    "alternateName": ["HQC", "High Quality Construction"],
    "publisher": { "@id": f"{DOMAIN}/#organization" },
    "description": "Dokumentasi nyata perjalanan konstruksi vila dan hotel—dari detail pembesian struktur, instalasi utilitas, hingga wujud arsitektur jadi.",
    "inLanguage": "id-ID",
    "potentialAction": {
        "@type": "SearchAction",
        "target": f"{DOMAIN}/blog?q={{search_term_string}}",
        "query-input": "required name=search_term_string"
    }
}

FAVICON_BLOCK = """  <!-- Favicon & Brand Icons -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/favicon.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/favicon-512x512.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#10263F">"""

KEYWORDS_META = f'  <meta name="keywords" content="{KEYWORDS_STR}">'

print("Setup completed successfully.")
