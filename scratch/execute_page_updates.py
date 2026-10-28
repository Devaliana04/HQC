import os
import json
import re

def run_updates():
    root = os.getcwd()
    
    with open('scratch/keywords_100.txt', 'r', encoding='utf-8') as f:
        keywords_str = f.read().strip()
    keywords_list = [k.strip() for k in keywords_str.split(',') if k.strip()]
    
    DOMAIN = "https://hqconstruction.id"
    
    org_schema = {
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
        "knowsAbout": keywords_list,
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

    website_schema = {
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

    pages_info = {
        'index.html': {
            'path': '/',
            'title': 'HQC High Quality Construction | Jasa Konstruksi & Pembangunan Vila Hotel',
            'desc': 'Kenali proses pembangunan vila dan hotel bersama HQC melalui dokumentasi nyata pekerjaan struktur pembesian, instalasi utilitas, rangka dinding, dan finishing arsitektur.',
            'type': 'website',
            'breadcrumbs': None
        },
        'tentang.html': {
            'path': '/tentang',
            'title': 'Tentang HQC — High Quality Construction | Profil & Standar Mutu',
            'desc': 'Profil perusahaan konstruksi HQC, dedikasi dokumentasi transparan, standar mutu struktur dan komitmen pengerjaan vila dan hotel bernilai arsitektural tinggi.',
            'type': 'website',
            'breadcrumbs': [('Beranda', '/'), ('Tentang HQC', '/tentang')]
        },
        'produk.html': {
            'path': '/produk',
            'title': 'Solusi & Layanan Konstruksi Vila Hotel | HQC Construction',
            'desc': 'Solusi konstruksi terpadu: pembangunan vila eksklusif, konstruksi hotel resort, pekerjaan struktur pondasi, instalasi pipa MEP, dan finishing arsitektural.',
            'type': 'website',
            'breadcrumbs': [('Beranda', '/'), ('Produk & Layanan', '/produk')]
        },
        'portofolio.html': {
            'path': '/portofolio',
            'title': 'Portofolio & Dokumentasi Progres Konstruksi | HQC',
            'desc': 'Jelajahi galeri bulat interaktif dokumentasi progres konstruksi vila dan hotel: pekerjaan pembesian, jalur pipa, perancah dinding, hingga fasad arsitektur.',
            'type': 'website',
            'breadcrumbs': [('Beranda', '/'), ('Portofolio Progres', '/portofolio')]
        },
        'blog.html': {
            'path': '/blog',
            'title': 'Catatan Konstruksi HQC — Wawasan & Edukasi Proyek Vila Hotel',
            'desc': 'Kumpulan artikel dan panduan teknis konstruksi: tahapan bangun vila, koordinasi pipa sebelum cor, serta panduan memilih kontraktor terpercaya.',
            'type': 'blog',
            'breadcrumbs': [('Beranda', '/'), ('Jurnal Konstruksi', '/blog')]
        },
        'blog/tahapan-pembangunan-vila.html': {
            'path': '/blog/tahapan-pembangunan-vila',
            'title': 'Tahapan Pembangunan Vila: Dari Struktur Hingga Finishing | HQC',
            'desc': 'Panduan komprehensif fase konstruksi vila: pondasi struktur, instalasi utilitas pipa sebelum pengecoran, pekerjaan dinding, dan finishing arsitektur.',
            'type': 'article',
            'breadcrumbs': [('Beranda', '/'), ('Jurnal', '/blog'), ('Tahapan Pembangunan Vila', '/blog/tahapan-pembangunan-vila')]
        },
        'blog/instalasi-pipa-sebelum-pengecoran.html': {
            'path': '/blog/instalasi-pipa-sebelum-pengecoran',
            'title': 'Pentingnya Koordinasi Jalur Pipa Sebelum Pengecoran | HQC',
            'desc': 'Penjelasan teknis pentingnya perencanaan dan pemasangan jalur pipa MEP di antara tulangan besi sebelum pengecoran plat beton struktur bangunan.',
            'type': 'article',
            'breadcrumbs': [('Beranda', '/'), ('Jurnal', '/blog'), ('Instalasi Pipa Sebelum Cor', '/blog/instalasi-pipa-sebelum-pengecoran')]
        },
        'blog/cara-memilih-kontraktor-vila.html': {
            'path': '/blog/cara-memilih-kontraktor-vila',
            'title': 'Panduan Memilih Kontraktor Vila Terpercaya & Profesional | HQC',
            'desc': 'Langkah evaluasi dan kriteria esensial dalam memilih kontraktor pembangunan vila: verifikasi dokumentasi lapangan, kejelasan kontrak, dan transparansi mutu.',
            'type': 'article',
            'breadcrumbs': [('Beranda', '/'), ('Jurnal', '/blog'), ('Cara Memilih Kontraktor', '/blog/cara-memilih-kontraktor-vila')]
        },
        'kontak.html': {
            'path': '/kontak',
            'title': 'Kontak & Konsultasi Proyek Vila Hotel | HQC Construction',
            'desc': 'Hubungi tim HQC High Quality Construction melalui WhatsApp resmi +62 821-4426-7826 untuk konsultasi perencanaan pembangunan vila atau hotel.',
            'type': 'website',
            'breadcrumbs': [('Beranda', '/'), ('Kontak', '/kontak')]
        },
        'kebijakan-privasi.html': {
            'path': '/kebijakan-privasi',
            'title': 'Kebijakan Privasi — HQC High Quality Construction',
            'desc': 'Kebijakan privasi dan ketentuan perlindungan data komunikasi bagi pengunjung website HQC High Quality Construction.',
            'type': 'website',
            'breadcrumbs': [('Beranda', '/'), ('Kebijakan Privasi', '/kebijakan-privasi')]
        },
        '404.html': {
            'path': '/404',
            'title': '404 — Halaman Tidak Ditemukan | HQC High Quality Construction',
            'desc': 'Halaman yang Anda tuju tidak ditemukan pada website resmi HQC High Quality Construction.',
            'type': 'website',
            'breadcrumbs': None
        }
    }

    for file_rel, meta in pages_info.items():
        file_path = os.path.join(root, file_rel.replace('/', os.sep))
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        canonical_url = f"{DOMAIN}{meta['path']}" if meta['path'] != '/' else f"{DOMAIN}/"
        
        # Build JSON-LD graph for this page
        graph = [org_schema, website_schema]
        
        webpage_node = {
            "@type": "WebPage" if meta['type'] != 'article' else "ItemPage",
            "@id": f"{canonical_url}#webpage",
            "url": canonical_url,
            "name": meta['title'],
            "description": meta['desc'],
            "isPartOf": { "@id": f"{DOMAIN}/#website" },
            "about": { "@id": f"{DOMAIN}/#organization" },
            "inLanguage": "id-ID",
            "keywords": keywords_list[:30]
        }
        
        if meta['breadcrumbs']:
            webpage_node["breadcrumb"] = { "@id": f"{canonical_url}#breadcrumb" }
            bc_node = {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "name": b[0],
                        "item": f"{DOMAIN}{b[1]}" if b[1] != '/' else f"{DOMAIN}/"
                    }
                    for i, b in enumerate(meta['breadcrumbs'])
                ]
            }
            graph.append(bc_node)
            
        # Page specific schema nodes
        if file_rel == 'produk.html':
            services_node = {
                "@type": "ItemList",
                "@id": f"{canonical_url}#services-list",
                "name": "Daftar Layanan Konstruksi HQC",
                "itemListElement": [
                    {
                        "@type": "Service",
                        "name": "Pembangunan Vila Eksklusif",
                        "serviceType": "Villa Construction",
                        "provider": { "@id": f"{DOMAIN}/#organization" },
                        "areaServed": "ID"
                    },
                    {
                        "@type": "Service",
                        "name": "Konstruksi Hotel & Resort",
                        "serviceType": "Hospitality Construction",
                        "provider": { "@id": f"{DOMAIN}/#organization" },
                        "areaServed": "ID"
                    },
                    {
                        "@type": "Service",
                        "name": "Pekerjaan Struktur & Pondasi",
                        "serviceType": "Structural Engineering & Foundation",
                        "provider": { "@id": f"{DOMAIN}/#organization" },
                        "areaServed": "ID"
                    },
                    {
                        "@type": "Service",
                        "name": "Instalasi MEP & Utilitas",
                        "serviceType": "Mechanical Electrical Plumbing",
                        "provider": { "@id": f"{DOMAIN}/#organization" },
                        "areaServed": "ID"
                    },
                    {
                        "@type": "Service",
                        "name": "Finishing Arsitektur & Fasad",
                        "serviceType": "Architectural Finishing & Facade",
                        "provider": { "@id": f"{DOMAIN}/#organization" },
                        "areaServed": "ID"
                    }
                ]
            }
            graph.append(services_node)
            
        if file_rel == 'portofolio.html':
            portfolio_node = {
                "@type": "CollectionPage",
                "@id": f"{canonical_url}#portfolio",
                "name": "Portofolio Dokumentasi Progres Konstruksi HQC",
                "description": "Dokumentasi visual nyata tahapan pekerjaan struktur pembesian, instalasi pipa utilitas, perancah dinding, dan progres finishing fasad.",
                "publisher": { "@id": f"{DOMAIN}/#organization" }
            }
            graph.append(portfolio_node)
            
        if meta['type'] == 'article':
            article_node = {
                "@type": "BlogPosting",
                "@id": f"{canonical_url}#article",
                "headline": meta['title'],
                "description": meta['desc'],
                "image": f"{DOMAIN}/assets/images/og/hqc-og-home.jpg",
                "datePublished": "2026-10-29T08:00:00+07:00",
                "dateModified": "2026-10-29T08:00:00+07:00",
                "inLanguage": "id-ID",
                "author": {
                    "@type": "Organization",
                    "@id": f"{DOMAIN}/#organization",
                    "name": "Tim Editorial Konstruksi HQC"
                },
                "publisher": { "@id": f"{DOMAIN}/#organization" },
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": canonical_url
                },
                "keywords": keywords_list[:30]
            }
            graph.append(article_node)
            
        graph.append(webpage_node)
        
        full_jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)
        
        # Build complete new head block
        new_head_meta = f"""  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta['title']}</title>
  <meta name="description" content="{meta['desc']}">
  <meta name="keywords" content="{keywords_str}">
  <meta name="author" content="HQC — High Quality Construction">
  <link rel="canonical" href="{canonical_url}">
  {"<meta name='robots' content='noindex, follow'>" if file_rel == "404.html" else "<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'>"}

  <!-- Open Graph / Facebook & WhatsApp -->
  <meta property="og:type" content="{meta['type']}">
  <meta property="og:site_name" content="HQC High Quality Construction">
  <meta property="og:title" content="{meta['title']}">
  <meta property="og:description" content="{meta['desc']}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">
  <meta property="og:image:secure_url" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="HQC High Quality Construction — Dokumentasi Progres Konstruksi">
  <meta property="og:locale" content="id_ID">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@hqconstruction">
  <meta name="twitter:title" content="{meta['title']}">
  <meta name="twitter:description" content="{meta['desc']}">
  <meta name="twitter:image" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">

  <!-- Favicon & Brand Icons for Google Search & Browsers -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/favicon.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/favicon-512x512.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#10263F">
  <meta name="msapplication-TileColor" content="#10263F">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="/assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="/assets/css/main.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
{full_jsonld}
  </script>"""

        # Replace existing <head>...</head>
        content = re.sub(r'<head>.*?</head>', f'<head>\n{new_head_meta}\n</head>', content, flags=re.DOTALL)
        
        # Also clean up internal links in body:
        # Replace href="/tentang/" with href="/tentang"
        # Replace href="/produk/" with href="/produk"
        # Replace href="/portofolio/" with href="/portofolio"
        # Replace href="/blog/" with href="/blog"
        # Replace href="/kontak/" with href="/kontak"
        # Replace href="/kebijakan-privasi/" with href="/kebijakan-privasi"
        content = content.replace('href="/tentang/"', 'href="/tentang"')
        content = content.replace('href="/produk/"', 'href="/produk"')
        content = content.replace('href="/portofolio/"', 'href="/portofolio"')
        content = content.replace('href="/blog/"', 'href="/blog"')
        content = content.replace('href="/kontak/"', 'href="/kontak"')
        content = content.replace('href="/kebijakan-privasi/"', 'href="/kebijakan-privasi"')
        content = content.replace('href="/blog/tahapan-pembangunan-vila/"', 'href="/blog/tahapan-pembangunan-vila"')
        content = content.replace('href="/blog/instalasi-pipa-sebelum-pengecoran/"', 'href="/blog/instalasi-pipa-sebelum-pengecoran"')
        content = content.replace('href="/blog/cara-memilih-kontraktor-vila/"', 'href="/blog/cara-memilih-kontraktor-vila"')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {file_rel} successfully.")

    print("All pages successfully updated with complete meta, 120 keywords, and interconnected JSON-LD schemas!")

if __name__ == '__main__':
    run_updates()
