import os
import glob
import re
import json

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
DOMAIN = "https://hqc-high-quality-construction.vercel.app"

# Bali villa keywords (120+ targeted keywords)
BALI_KEYWORDS = (
    "hqc bali, hqc high quality construction bali, jual vila bali, penjualan vila bali, "
    "investasi vila bali, beli vila bali, properti vila bali, villa development bali, developer vila bali, "
    "investasi properti bali, rancang bangun vila bali, villa turnkey project bali, jasa pembangunan vila bali, "
    "kontraktor vila bali, bangun vila bali, kontraktor private villa bali, kontraktor luxury villa bali, "
    "jasa renovasi vila bali, kontraktor vila canggu, kontraktor vila seminyak, kontraktor vila uluwatu, "
    "kontraktor vila ubud, kontraktor vila sanur, kontraktor vila pererenan, kontraktor vila tabanan, "
    "jasa pembangunan hotel bali, kontraktor hotel bali, konstruksi resort bali, boutique hotel contractor bali, "
    "eco resort contractor bali, hospitality construction bali, villa and resort builder bali, kontraktor bali, "
    "perusahaan konstruksi bali, jasa kontraktor bali, general contractor bali, pemborong bali, kontraktor profesional bali, "
    "pekerjaan struktur bangunan bali, struktur tahan gempa vila bali, pembesian pondasi vila bali, "
    "pengecoran beton bertulang bali, pondasi bore pile bali, pondasi cakar ayam, footing foundation bali, "
    "balok dan kolom struktur, sloof gantung beton, retaining wall dinding penahan tanah bali, "
    "uji kuat tekan beton bali, rebar installation bali, instalasi mep bali, mechanical electrical plumbing bali, "
    "instalasi pipa air bersih bali, jalur pipa air kotor vila, instalasi pipa sebelum cor beton, "
    "pemipaan ppr air panas bali, pemipaan pvc berkualitas, instalasi pipa pex, sistem sanitasi vila septic tank, "
    "instalasi stp sewage treatment bali, jalur kabel konduit listrik, panel listrik lvmdb, "
    "grounding sistem penangkal petir bali, pekerjaan dinding bata ringan hebel, plesteran dan acian halus, "
    "perancah scaffolding bali, rangka fasad baja ringan, fasad arsitektural lengkung bali, dinding ekspos terkurasi, "
    "secondary skin fasad vila, insulasi dinding bangunan, partisi kedap suara, waterproofing membrane dak beton bali, "
    "waterproofing polyurethane, pemasangan kusen aluminium bali, pintu kaca sliding panoramik, "
    "finishing arsitektur tropis bali, lantai semen ekspos teraso, batu alam travertin marmer mewah, "
    "decking kayu ulin kolam renang, konstruksi kolam renang infinity bali, swimming pool builder bali, "
    "waterproofing kolam renang vila, sistem sirkulasi kolam overflow, lanskap tropis vila bali, "
    "lighting arsitektur eksterior, plafon gypsum drop ceiling, cat dinding tahan cuaca tropis bali, "
    "dokumentasi progres konstruksi bali, pengawasan berkala proyek bali, rab pembangunan vila bali, "
    "rencana anggaran biaya vila bali, gambar kerja ded arsitektur, time schedule kurva s, "
    "laporan mingguan proyek bali, inspeksi mutu bahan konstruksi bali, quality control konstruksi bali, "
    "spesifikasi teknis bangunan bali, konsultasi proyek konstruksi bali, bali luxury villa builder, blueprint to built bali"
)

html_files = [
    'index.html',
    'tentang.html',
    'produk.html',
    'portofolio.html',
    'blog.html',
    'blog/blog.html',
    'blog/tahapan-pembangunan-vila.html',
    'blog/instalasi-pipa-sebelum-pengecoran.html',
    'blog/cara-memilih-kontraktor-vila.html',
    'kontak.html',
    'kebijakan-privasi.html',
    '404.html'
]

page_titles_desc = {
    'index.html': (
        'HQC Bali | Kontraktor Pembangunan & Penjualan Vila Mewah Bali',
        'HQC Bali adalah kontraktor terpercaya spesialis rancang bangun dan penjualan vila mewah, hotel, serta resort di Canggu, Seminyak, Uluwatu, dan Ubud Bali.'
    ),
    'tentang.html': (
        'Tentang HQC Bali | Filosofi Konstruksi & Spesialis Vila Mewah Bali',
        'Kenali HQC Bali, studio kontraktor terdepan di Bali yang mengedepankan transparansi tahapan struktur, integritas bahan, dan standar estetika arsitektur tropis.'
    ),
    'produk.html': (
        'Layanan & Solusi Konstruksi Vila Bali | HQC Bali',
        'Layanan komprehensif pembangunan vila privat, hotel butik, pekerjaan struktur bertulang tahan gempa, instalasi utilitas MEP, dan finishing arsitektur di Bali.'
    ),
    'portofolio.html': (
        'Galeri Progres Lapangan & Konstruksi Vila Bali | HQC Bali',
        'Dokumentasi nyata tahapan pembangunan vila di Bali: pembesian plat, jalur MEP tertanam, rangka fasad, plesteran dinding lengkung, hingga infinity pool.'
    ),
    'blog.html': (
        'Catatan Konstruksi & Panduan Investasi Vila Bali | HQC Bali',
        'Edukasi teknis, tips memilih kontraktor vila Bali, tahapan pembangunan, dan panduan investasi properti vila di Bali dari para ahli HQC.'
    ),
    'blog/blog.html': (
        'Catatan Konstruksi & Panduan Investasi Vila Bali | HQC Bali',
        'Edukasi teknis, tips memilih kontraktor vila Bali, tahapan pembangunan, dan panduan investasi properti vila di Bali dari para ahli HQC.'
    ),
    'blog/tahapan-pembangunan-vila.html': (
        'Tahapan Pembangunan Vila Bali: Dari Struktur Hingga Finishing | HQC Bali',
        'Panduan lengkap alur kerja pembangunan vila eksklusif di Bali untuk mencegah pembengkakan anggaran dan memastikan kualitas struktur tahan lama.'
    ),
    'blog/instalasi-pipa-sebelum-pengecoran.html': (
        'Koordinasi Jalur Pipa Sebelum Pengecoran Beton Plat Vila | HQC Bali',
        'Pentingnya integrasi sistem plumbing MEP sebelum cor beton di proyek vila Bali guna menghindari kebocoran dan menjaga integritas tulangan struktural.'
    ),
    'blog/cara-memilih-kontraktor-vila.html': (
        'Cara Memilih Kontraktor Vila Terpercaya di Bali | HQC Bali',
        'Kriteria krusial evaluasi rekanan konstruksi, kelengkapan RAB, time schedule kurva S, dan pengawasan berkala sebelum membangun vila di Bali.'
    ),
    'kontak.html': (
        'Hubungi HQC Bali | Konsultasi Proyek Vila & Hotel Bali',
        'Konsultasikan rencana pembangunan atau renovasi vila mewah Anda di Bali langsung dengan tim insinyur dan arsitek profesional HQC via WhatsApp.'
    ),
    'kebijakan-privasi.html': (
        'Kebijakan Privasi | HQC Bali High Quality Construction',
        'Kebijakan privasi dan komitmen perlindungan data klien serta pengunjung situs resmi HQC Bali High Quality Construction.'
    ),
    '404.html': (
        'Halaman Tidak Ditemukan (404) | HQC Bali',
        'Halaman yang Anda tuju tidak ditemukan atau telah berpindah. Kembali ke beranda HQC Bali untuk menjelajahi proyek konstruksi vila kami.'
    )
}

print(f"Updating {len(html_files)} HTML files with Bali Villa Keywords & WhatsApp Open Graph...")

for hf in html_files:
    fp = os.path.join(workspace, hf.replace('/', os.sep))
    if not os.path.exists(fp):
        continue

    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    title, desc = page_titles_desc.get(hf, page_titles_desc['index.html'])
    
    # Calculate canonical url
    if hf == 'index.html':
        canon_url = f"{DOMAIN}/"
    elif hf.endswith('.html'):
        clean_path = hf.replace('.html', '')
        if clean_path == 'blog/blog':
            clean_path = 'blog'
        canon_url = f"{DOMAIN}/{clean_path}"

    # 1. Update Title
    c = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', c, flags=re.DOTALL)

    # 2. Update Description
    c = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']>',
               f'<meta name="description" content="{desc}">', c, flags=re.DOTALL | re.IGNORECASE)

    # 3. Update Keywords with BALI_KEYWORDS
    c = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']>',
               f'<meta name="keywords" content="{BALI_KEYWORDS}">', c, flags=re.DOTALL | re.IGNORECASE)

    # 4. Update Canonical
    c = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']>',
               f'<link rel="canonical" href="{canon_url}">', c, flags=re.DOTALL | re.IGNORECASE)

    # 5. Open Graph Meta Tags (strictly configured for WhatsApp link preview thumbnail)
    # WhatsApp requires og:image with JPG or PNG, 1200x630, type image/jpeg
    og_block = f'''  <!-- Open Graph / WhatsApp / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="HQC Bali — High Quality Construction">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon_url}">
  <meta property="og:image" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">
  <meta property="og:image:secure_url" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="HQC Bali - Kontraktor Pembangunan & Penjualan Vila Mewah Bali">
  <meta property="og:locale" content="id_ID">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@hqconstruction">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{DOMAIN}/assets/images/og/hqc-og-home.jpg">'''

    # Replace existing OG and Twitter block
    og_pattern = r'<!-- Open Graph / Facebook & WhatsApp -->[\s\S]*?<!-- Favicon'
    if re.search(og_pattern, c):
        c = re.sub(og_pattern, og_block + '\n\n  <!-- Favicon', c, count=1)
    else:
        # Fallback regex
        alt_og_pattern = r'<meta property="og:type"[\s\S]*?<meta name="twitter:image" content=".*?">'
        c = re.sub(alt_og_pattern, og_block, c, count=1)

    # 6. Synchronize domain in JSON-LD schemas
    c = c.replace('https://hqconstruction.id', DOMAIN)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"  [UPDATED] {hf}")

# Update sitemap.xml
sitemap_path = os.path.join(workspace, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sm = f.read()
sm = sm.replace('https://hqconstruction.id', DOMAIN)
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sm)
print("  [UPDATED] sitemap.xml with Vercel domain.")

# Update robots.txt
robots_path = os.path.join(workspace, 'robots.txt')
with open(robots_path, 'r', encoding='utf-8') as f:
    rb = f.read()
rb = rb.replace('https://hqconstruction.id', DOMAIN)
if 'Allow: /hqc-og-home.jpg' not in rb:
    rb = rb.replace('Allow: /assets/images/', 'Allow: /assets/images/\nAllow: /hqc-og-home.jpg')
with open(robots_path, 'w', encoding='utf-8') as f:
    f.write(rb)
print("  [UPDATED] robots.txt with Vercel domain and OG image access.")

print("\nAll SEO & WhatsApp Open Graph updates completed successfully!")
