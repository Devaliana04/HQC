import os
import shutil
import re

def execute_cleanup():
    root = os.getcwd()
    print("Starting cleanup...")
    
    # 1. Remove public/ folder completely (eliminates duplicate sitemap.xml, robots.txt, etc.)
    public_dir = os.path.join(root, 'public')
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print("Removed public/ directory (ONLY 1 sitemap.xml now exists at root).")
        
    # 2. Delete all folder index files and redundant directories
    redundant_dirs = [
        'tentang',
        'produk',
        'portofolio',
        'kontak',
        'kebijakan-privasi',
        os.path.join('blog', 'tahapan-pembangunan-vila'),
        os.path.join('blog', 'instalasi-pipa-sebelum-pengecoran'),
        os.path.join('blog', 'cara-memilih-kontraktor-vila'),
    ]
    
    for d in redundant_dirs:
        p = os.path.join(root, d)
        if os.path.exists(p):
            shutil.rmtree(p)
            print(f"Deleted redundant folder: {d}")
            
    # Remove blog/index.html if exists (we have blog.html at root)
    blog_index = os.path.join(root, 'blog', 'index.html')
    if os.path.exists(blog_index):
        os.remove(blog_index)
        print("Deleted blog/index.html")

    # 3. List of primary pages
    pages = [
        'index.html',
        'tentang.html',
        'produk.html',
        'portofolio.html',
        'blog.html',
        os.path.join('blog', 'tahapan-pembangunan-vila.html'),
        os.path.join('blog', 'instalasi-pipa-sebelum-pengecoran.html'),
        os.path.join('blog', 'cara-memilih-kontraktor-vila.html'),
        'kontak.html',
        'kebijakan-privasi.html',
        '404.html'
    ]
    
    clean_enforcer_script = """  <!-- Clean URL Enforcer: Hide .html from browser address bar immediately -->
  <script>
    (function() {
      try {
        var p = window.location.pathname;
        if (p.endsWith('.html')) {
          var clean = p.replace(/\\.html$/, '');
          window.history.replaceState(null, '', (clean || '/') + window.location.search + window.location.hash);
        }
      } catch (e) {}
    })();
  </script>"""

    # 4. Standardize links in all HTML files
    link_replacements = [
        ('href="/tentang/"', 'href="/tentang"'),
        ('href="/produk/"', 'href="/produk"'),
        ('href="/portofolio/"', 'href="/portofolio"'),
        ('href="/blog/"', 'href="/blog"'),
        ('href="/kontak/"', 'href="/kontak"'),
        ('href="/kebijakan-privasi/"', 'href="/kebijakan-privasi"'),
        ('href="/blog/tahapan-pembangunan-vila/"', 'href="/blog/tahapan-pembangunan-vila"'),
        ('href="/blog/instalasi-pipa-sebelum-pengecoran/"', 'href="/blog/instalasi-pipa-sebelum-pengecoran"'),
        ('href="/blog/cara-memilih-kontraktor-vila/"', 'href="/blog/cara-memilih-kontraktor-vila"'),
    ]

    for p in pages:
        p_full = os.path.join(root, p)
        if not os.path.exists(p_full):
            print(f"Warning: {p} not found!")
            continue
        with open(p_full, 'r', encoding='utf-8') as f:
            c = f.read()
            
        for old_l, new_l in link_replacements:
            c = c.replace(old_l, new_l)
            
        # Ensure clean enforcer script is present
        if '<!-- Clean URL Enforcer' not in c:
            c = c.replace('<head>', '<head>\n' + clean_enforcer_script)
            
        with open(p_full, 'w', encoding='utf-8') as f:
            f.write(c)

    # -------------------------------------------------------------
    # 5. Add rich contextual internal links in the 3 blog articles
    # -------------------------------------------------------------
    
    # --- Article 1: tahapan-pembangunan-vila.html ---
    a1_path = os.path.join(root, 'blog', 'tahapan-pembangunan-vila.html')
    with open(a1_path, 'r', encoding='utf-8') as f:
        c1 = f.read()

    c1 = c1.replace(
        "sejak pekerjaan galian pertama dimulai.",
        'sejak pekerjaan galian pertama dimulai. Memahami alur kerja ini sama pentingnya dengan <a href="/blog/cara-memilih-kontraktor-vila" class="text-primary fw-medium text-decoration-underline">menyiapkan dokumen dan kriteria sebelum memilih kontraktor vila</a>.'
    )
    c1 = c1.replace(
        "mencegah penurunan bangunan (settlement) di kemudian hari.",
        'mencegah penurunan bangunan (settlement) di kemudian hari. Pelajari lebih lanjut keteknikan pondasi dan pembesian kami pada <a href="/produk" class="text-primary fw-medium text-decoration-underline">Layanan Pekerjaan Struktur &amp; Pondasi HQC</a>.'
    )
    c1 = c1.replace(
        "agar besi tidak terpapar udara lembap yang dapat memicu karat.",
        'agar besi tidak terpapar udara lembap yang dapat memicu karat. Dokumentasi fotografi aktual tulangan balok ini dapat Anda verifikasi di <a href="/portofolio" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Progres Lapangan HQC</a>.'
    )
    c1 = c1.replace(
        "harus dipasang dan diuji tekan sebelum semen beton dituangkan.",
        'harus dipasang dan diuji tekan sebelum semen beton dituangkan. Baca ulasan mendalam mengenai risiko pembobokan plat beton pada artikel <a href="/blog/instalasi-pipa-sebelum-pengecoran" class="text-primary fw-medium text-decoration-underline">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran</a>.'
    )
    c1 = c1.replace(
        "menggunakan perancah scaffolding bersertifikasi keselamatan.",
        'menggunakan perancah scaffolding bersertifikasi keselamatan. Kerapian dinding dan ketelitian struktur ini adalah bagian dari <a href="/tentang" class="text-primary fw-medium text-decoration-underline">standar mutu Blueprint to Built HQC</a>.'
    )
    c1 = c1.replace(
        "Tahap puncak adalah finishing arsitektur:",
        'Tahap puncak adalah finishing arsitektur pada <a href="/produk" class="text-primary fw-medium text-decoration-underline">Layanan Pembangunan Vila Eksklusif HQC</a>:'
    )

    related_card_1 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-info bg-opacity-10 text-dark mb-2">MEP &amp; PLUMBING</span>
                        <h4 class="h6 fw-bold"><a href="/blog/instalasi-pipa-sebelum-pengecoran" class="text-navy text-decoration-none">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran?</a></h4>
                        <p class="small text-muted mb-0">Ulasan teknis mengapa membobok beton yang mengeras berisiko memotong tulangan struktur utama.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/instalasi-pipa-sebelum-pengecoran" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-warning bg-opacity-25 text-dark mb-2">PANDUAN KONTRAKTOR</span>
                        <h4 class="h6 fw-bold"><a href="/blog/cara-memilih-kontraktor-vila" class="text-navy text-decoration-none">Hal yang Perlu Disiapkan Sebelum Berkonsultasi dengan Kontraktor</a></h4>
                        <p class="small text-muted mb-0">Daftar cek dokumen tapak lahan, DED gambar kerja, dan estimasi anggaran kontinjensi.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/cara-memilih-kontraktor-vila" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Jelajahi bukti nyata dan layanan konstruksi HQC:</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/portofolio" class="btn btn-sm btn-outline-primary">Lihat Galeri Portofolio &rarr;</a>
                    <a href="/produk" class="btn btn-sm btn-primary">Solusi &amp; Layanan HQC &rarr;</a>
                    <a href="/kontak" class="btn btn-sm btn-outline-secondary">Halaman Kontak &rarr;</a>
                  </div>
                </div>
              </div>

"""
    if 'hqc-related-articles' not in c1:
        c1 = c1.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_card_1 + '<div class="card bg-light border p-4 my-5 rounded-4">')
        
    with open(a1_path, 'w', encoding='utf-8') as f:
        f.write(c1)
    print("Updated Article 1 internal links.")

    # --- Article 2: instalasi-pipa-sebelum-pengecoran.html ---
    a2_path = os.path.join(root, 'blog', 'instalasi-pipa-sebelum-pengecoran.html')
    with open(a2_path, 'r', encoding='utf-8') as f:
        c2 = f.read()

    c2 = c2.replace(
        "hampir mustahil diperbaiki tanpa membongkar keramik mewah.",
        'hampir mustahil diperbaiki tanpa membongkar keramik mewah. Hal inilah yang mendasari mengapa koordinasi utilitas merupakan pilar sentral dalam <a href="/blog/tahapan-pembangunan-vila" class="text-primary fw-medium text-decoration-underline">tahapan menyeluruh pembangunan vila dari struktur hingga finishing</a>.'
    )
    c2 = c2.replace(
        "plat lantai berisiko mengalami lendutan berlebih hingga retak tembus.",
        'plat lantai berisiko mengalami lendutan berlebih hingga retak tembus. Saksikan langsung kerapian rangkaian besi tulangan balok kami di <a href="/portofolio" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Pekerjaan Struktur HQC</a>.'
    )
    c2 = c2.replace(
        "saat ribuan kilogram adukan beton basah dituangkan dari concrete pump.",
        'saat ribuan kilogram adukan beton basah dituangkan dari concrete pump. Sistem plumbing berstandar hospitality ini merupakan bagian dari <a href="/produk" class="text-primary fw-medium text-decoration-underline">Layanan Instalasi MEP &amp; Utilitas HQC</a>.'
    )
    c2 = c2.replace(
        "barulah berita acara pengecoran disetujui.",
        'barulah berita acara pengecoran disetujui. Memverifikasi SOP pengujian seperti ini di awal adalah salah satu langkah bijak yang kami rangkum dalam <a href="/blog/cara-memilih-kontraktor-vila" class="text-primary fw-medium text-decoration-underline">panduan memilih kontraktor vila profesional</a>.'
    )

    related_card_2 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-primary bg-opacity-10 text-primary mb-2">TAHAPAN KONSTRUKSI</span>
                        <h4 class="h6 fw-bold"><a href="/blog/tahapan-pembangunan-vila" class="text-navy text-decoration-none">Tahapan Pembangunan Vila: Dari Struktur Hingga Finishing</a></h4>
                        <p class="small text-muted mb-0">Panduan lengkap alur kerja konstruksi vila dari penyelidikan tanah hingga area kolam renang infinity.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/tahapan-pembangunan-vila" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-warning bg-opacity-25 text-dark mb-2">PANDUAN KONTRAKTOR</span>
                        <h4 class="h6 fw-bold"><a href="/blog/cara-memilih-kontraktor-vila" class="text-navy text-decoration-none">Hal yang Perlu Disiapkan Sebelum Berkonsultasi dengan Kontraktor</a></h4>
                        <p class="small text-muted mb-0">Kriteria evaluasi kontraktor berintegritas dan cara menyusun anggaran cadangan proyek.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/cara-memilih-kontraktor-vila" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Pelajari spesifikasi MEP dan standar kami:</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/produk" class="btn btn-sm btn-primary">Solusi Utilitas MEP HQC &rarr;</a>
                    <a href="/portofolio" class="btn btn-sm btn-outline-primary">Lihat Foto Progres &rarr;</a>
                    <a href="/tentang" class="btn btn-sm btn-outline-secondary">Standar Kualitas HQC &rarr;</a>
                  </div>
                </div>
              </div>

"""
    if 'hqc-related-articles' not in c2:
        c2 = c2.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_card_2 + '<div class="card bg-light border p-4 my-5 rounded-4">')

    with open(a2_path, 'w', encoding='utf-8') as f:
        f.write(c2)
    print("Updated Article 2 internal links.")

    # --- Article 3: cara-memilih-kontraktor-vila.html ---
    a3_path = os.path.join(root, 'blog', 'cara-memilih-kontraktor-vila.html')
    with open(a3_path, 'r', encoding='utf-8') as f:
        c3 = f.read()

    c3 = c3.replace(
        "dibutuhkan tim perencana.",
        'dibutuhkan tim perencana. Memahami <a href="/blog/tahapan-pembangunan-vila" class="text-primary fw-medium text-decoration-underline">alur tahapan pembangunan vila dari pondasi hingga finishing</a> akan memberi Anda gambaran menyeluruh tentang setiap fase yang akan dihadapi.'
    )
    c3 = c3.replace(
        "jalur akses mobil molen ready-mix.",
        'jalur akses mobil molen ready-mix. Pembahasan mengenai pondasi lereng dan beban tanah ini kami ulas di <a href="/produk" class="text-primary fw-medium text-decoration-underline">Layanan Pekerjaan Struktur &amp; Pondasi HQC</a>.'
    )
    c3 = c3.replace(
        "denah struktur pembesian, dan denah MEP plumbing.",
        'denah struktur pembesian, dan denah MEP plumbing. Koordinasi gambar MEP sangat penting untuk mencegah masalah kebocoran fatal, sebagaimana dibahas di artikel <a href="/blog/instalasi-pipa-sebelum-pengecoran" class="text-primary fw-medium text-decoration-underline">mengapa jalur pipa harus direncanakan matang sebelum pengecoran</a>.'
    )
    c3 = c3.replace(
        "metode pengujian mutu yang mereka terapkan di lapangan.",
        'metode pengujian mutu yang mereka terapkan di lapangan. Di HQC, seluruh bukti pekerjaan terbuka dan dapat Anda verifikasi di <a href="/portofolio" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Dokumentasi Lapangan</a> serta halaman <a href="/tentang" class="text-primary fw-medium text-decoration-underline">Tentang HQC</a>.'
    )
    c3 = c3.replace(
        "pilihan material yang masuk akal tanpa mengorbankan kekuatan struktural.",
        'pilihan material yang masuk akal tanpa mengorbankan kekuatan struktural. Anda dapat mempelajari rincian paket pengerjaan di <a href="/produk" class="text-primary fw-medium text-decoration-underline">Layanan Pembangunan Vila &amp; Hotel HQC</a>.'
    )

    related_card_3 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-primary bg-opacity-10 text-primary mb-2">TAHAPAN KONSTRUKSI</span>
                        <h4 class="h6 fw-bold"><a href="/blog/tahapan-pembangunan-vila" class="text-navy text-decoration-none">Tahapan Pembangunan Vila: Dari Struktur Hingga Finishing</a></h4>
                        <p class="small text-muted mb-0">Edukasi komprehensif alur kerja pembangunan vila eksklusif untuk mencegah pembengkakan anggaran.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/tahapan-pembangunan-vila" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-info bg-opacity-10 text-dark mb-2">MEP &amp; PLUMBING</span>
                        <h4 class="h6 fw-bold"><a href="/blog/instalasi-pipa-sebelum-pengecoran" class="text-navy text-decoration-none">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran?</a></h4>
                        <p class="small text-muted mb-0">Pentingnya koordinasi antara gambar arsitektur dan sistem plumbing tertanam sebelum cor plat.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/instalasi-pipa-sebelum-pengecoran" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Siap mendiskusikan rencana proyek vila Anda?</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/kontak" class="btn btn-sm btn-primary">Konsultasi ke Tim HQC &rarr;</a>
                    <a href="/portofolio" class="btn btn-sm btn-outline-primary">Lihat Galeri Proyek &rarr;</a>
                    <a href="/tentang" class="btn btn-sm btn-outline-secondary">Profil Perusahaan &rarr;</a>
                  </div>
                </div>
              </div>

"""
    if 'hqc-related-articles' not in c3:
        c3 = c3.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_card_3 + '<div class="card bg-light border p-4 my-5 rounded-4">')

    with open(a3_path, 'w', encoding='utf-8') as f:
        f.write(c3)
    print("Updated Article 3 internal links.")

    # --- Blog Hub: blog.html ---
    b_path = os.path.join(root, 'blog.html')
    with open(b_path, 'r', encoding='utf-8') as f:
        cb = f.read()

    hub_internal_strip = """    <!-- Internal Links Quick Navigation Strip -->
    <div class="bg-light border-top border-bottom py-3 mb-5">
      <div class="container d-flex flex-wrap justify-content-between align-items-center gap-3">
        <div class="small text-navy fw-semibold">
          <span class="text-sand me-1">#</span> Topik &amp; Layanan Terkait:
        </div>
        <div class="d-flex flex-wrap gap-2 small">
          <a href="/produk" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Pembangunan Vila Eksklusif</a>
          <a href="/produk" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Pekerjaan Struktur &amp; MEP</a>
          <a href="/portofolio" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Galeri Progres Lapangan</a>
          <a href="/tentang" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Standar Kualitas HQC</a>
          <a href="/kontak" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Konsultasi Rencana Proyek</a>
        </div>
      </div>
    </div>
"""
    if 'Topik &amp; Layanan Terkait' not in cb:
        cb = cb.replace('<!-- Blog Listing Section -->\n    <section class="hqc-section hqc-section--paper">', '<!-- Blog Listing Section -->\n' + hub_internal_strip + '    <section class="hqc-section hqc-section--paper">')

    with open(b_path, 'w', encoding='utf-8') as f:
        f.write(cb)
    print("Updated Blog Hub internal links.")

    # -------------------------------------------------------------
    # 6. Update assets/js/main.js with Localhost/Live Server Bridge
    # -------------------------------------------------------------
    js_path = os.path.join(root, 'assets', 'js', 'main.js')
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    bridge_code = """// Clean URL Enforcer - immediately hide .html from browser address bar
(function() {
  try {
    var p = window.location.pathname;
    if (p.endsWith('.html')) {
      var clean = p.replace(/\\.html$/, '');
      window.history.replaceState(null, '', (clean || '/') + window.location.search + window.location.hash);
    }
  } catch (e) {}
})();

document.addEventListener('DOMContentLoaded', () => {
  // Live Server & Localhost Clean URL Bridge: prevents 'Cannot GET /page' on simple local dev servers
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (!a || !a.href || a.target === '_blank') return;
    try {
      const u = new URL(a.href, window.location.origin);
      if (u.origin === window.location.origin && !u.hash) {
        const isLocal = window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost';
        if (isLocal) {
          let path = u.pathname;
          if (path !== '/' && !path.endsWith('.html')) {
            e.preventDefault();
            const cleanBase = path.replace(/\\/$/, '');
            window.location.href = cleanBase + '.html' + u.search;
          }
        }
      }
    } catch (err) {}
  });
"""
    # Replace the top of main.js up to DOMContentLoaded
    js = re.sub(r'// Clean URL Enforcer.*?\n(?=  // 1\. Navbar Scroll Detection)', bridge_code + '\n', js, flags=re.DOTALL)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated assets/js/main.js with clean URL local server bridge.")

if __name__ == '__main__':
    execute_cleanup()
