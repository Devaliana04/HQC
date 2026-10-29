import os

def update_blog_internal_links():
    root = os.getcwd()

    # -------------------------------------------------------------
    # 1. Update Article 1: tahapan-pembangunan-vila
    # -------------------------------------------------------------
    a1_files = [
        os.path.join(root, 'blog', 'tahapan-pembangunan-vila', 'index.html'),
        os.path.join(root, 'blog', 'tahapan-pembangunan-vila.html')
    ]

    for fpath in a1_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        # Contextual link in intro
        c = c.replace(
            "sejak pekerjaan galian pertama dimulai.",
            'sejak pekerjaan galian pertama dimulai. Memahami seluruh rangkaian ini sama krusialnya dengan <a href="/blog/cara-memilih-kontraktor-vila/" class="text-primary fw-medium text-decoration-underline">mengetahui hal yang perlu disiapkan sebelum berkonsultasi dengan kontraktor vila</a>.'
        )

        # Contextual link in Section 1
        c = c.replace(
            "mencegah penurunan bangunan (settlement) di kemudian hari.",
            'mencegah penurunan bangunan (settlement) di kemudian hari. Rincian sistem pembesian dan daya dukung pondasi dapat Anda pelajari di halaman <a href="/produk/" class="text-primary fw-medium text-decoration-underline">Layanan Pekerjaan Struktur &amp; Pondasi HQC</a>.'
        )

        # Contextual link in Section 2
        c = c.replace(
            "agar besi tidak terpapar udara lembap yang dapat memicu karat.",
            'agar besi tidak terpapar udara lembap yang dapat memicu karat. Anda dapat menyaksikan dokumentasi fotografi aktual perakitan besi tulangan ini di <a href="/portofolio/" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Progres Lapangan HQC</a>.'
        )

        # Contextual link in Section 3
        c = c.replace(
            "harus dipasang dan diuji tekan sebelum semen beton dituangkan.",
            'harus dipasang dan diuji tekan sebelum semen beton dituangkan. Ulasan mendalam mengenai risiko pembobokan dan protokol uji tekan dapat dibaca pada artikel <a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="text-primary fw-medium text-decoration-underline">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran</a>.'
        )

        # Contextual link in Section 4
        c = c.replace(
            "menggunakan perancah scaffolding bersertifikasi keselamatan.",
            'menggunakan perancah scaffolding bersertifikasi keselamatan. Kerapian pekerjaan pasangan dinding dan ketelitian struktur ini adalah bagian dari <a href="/tentang/" class="text-primary fw-medium text-decoration-underline">standar mutu terverifikasi Blueprint to Built HQC</a>.'
        )

        # Contextual link in Section 5
        c = c.replace(
            "Tahap puncak adalah finishing arsitektur:",
            'Tahap puncak adalah finishing arsitektur pada <a href="/produk/" class="text-primary fw-medium text-decoration-underline">Layanan Pembangunan Vila Eksklusif</a>:'
        )

        # Add Related Articles Block before closing CTA card
        related_block_1 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-info bg-opacity-10 text-dark mb-2">MEP &amp; PLUMBING</span>
                        <h4 class="h6 fw-bold"><a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="text-navy text-decoration-none">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran?</a></h4>
                        <p class="small text-muted mb-0">Ulasan teknis mengapa membobok beton yang mengeras berisiko memotong tulangan struktur utama.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-warning bg-opacity-25 text-dark mb-2">PANDUAN KONTRAKTOR</span>
                        <h4 class="h6 fw-bold"><a href="/blog/cara-memilih-kontraktor-vila/" class="text-navy text-decoration-none">Hal yang Perlu Disiapkan Sebelum Berkonsultasi dengan Kontraktor</a></h4>
                        <p class="small text-muted mb-0">Daftar cek dokumen tapak lahan, DED gambar kerja, dan estimasi anggaran kontinjensi.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/cara-memilih-kontraktor-vila/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Jelajahi bukti nyata dan layanan konstruksi HQC:</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/portofolio/" class="btn btn-sm btn-outline-primary">Lihat Galeri Portofolio &rarr;</a>
                    <a href="/produk/" class="btn btn-sm btn-primary">Solusi &amp; Layanan HQC &rarr;</a>
                    <a href="/kontak/" class="btn btn-sm btn-outline-secondary">Halaman Kontak &rarr;</a>
                  </div>
                </div>
              </div>

"""
        if 'hqc-related-articles' not in c:
            c = c.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_block_1 + '<div class="card bg-light border p-4 my-5 rounded-4">')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated internal links in: {fpath}")

    # -------------------------------------------------------------
    # 2. Update Article 2: instalasi-pipa-sebelum-pengecoran
    # -------------------------------------------------------------
    a2_files = [
        os.path.join(root, 'blog', 'instalasi-pipa-sebelum-pengecoran', 'index.html'),
        os.path.join(root, 'blog', 'instalasi-pipa-sebelum-pengecoran.html')
    ]

    for fpath in a2_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        # Contextual link in intro
        c = c.replace(
            "hampir mustahil diperbaiki tanpa membongkar keramik mewah.",
            'hampir mustahil diperbaiki tanpa membongkar keramik mewah. Hal inilah yang mendasari mengapa koordinasi utilitas merupakan pilar sentral dalam <a href="/blog/tahapan-pembangunan-vila/" class="text-primary fw-medium text-decoration-underline">tahapan menyeluruh pembangunan vila dari struktur hingga finishing</a>.'
        )

        # Contextual link in Section 1
        c = c.replace(
            "plat lantai berisiko mengalami lendutan berlebih hingga retak tembus.",
            'plat lantai berisiko mengalami lendutan berlebih hingga retak tembus. Saksikan langsung kerapian rangkaian besi tulangan balok kami di <a href="/portofolio/" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Pekerjaan Struktur HQC</a>.'
        )

        # Contextual link in Section 2
        c = c.replace(
            "saat ribuan kilogram adukan beton basah dituangkan dari concrete pump.",
            'saat ribuan kilogram adukan beton basah dituangkan dari concrete pump. Sistem plumbing berstandar hospitality ini merupakan bagian dari <a href="/produk/" class="text-primary fw-medium text-decoration-underline">Layanan Instalasi MEP &amp; Utilitas HQC</a>.'
        )

        # Contextual link in Section 3
        c = c.replace(
            "barulah berita acara pengecoran disetujui.",
            'barulah berita acara pengecoran disetujui. Memverifikasi SOP pengujian seperti ini di awal adalah salah satu langkah bijak yang kami rangkum dalam <a href="/blog/cara-memilih-kontraktor-vila/" class="text-primary fw-medium text-decoration-underline">panduan memilih kontraktor vila profesional</a>.'
        )

        # Add Related Articles Block before closing CTA card
        related_block_2 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-primary bg-opacity-10 text-primary mb-2">TAHAPAN KONSTRUKSI</span>
                        <h4 class="h6 fw-bold"><a href="/blog/tahapan-pembangunan-vila/" class="text-navy text-decoration-none">Tahapan Pembangunan Vila: Dari Struktur Hingga Finishing</a></h4>
                        <p class="small text-muted mb-0">Panduan lengkap alur kerja konstruksi vila dari penyelidikan tanah hingga area kolam renang infinity.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/tahapan-pembangunan-vila/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-warning bg-opacity-25 text-dark mb-2">PANDUAN KONTRAKTOR</span>
                        <h4 class="h6 fw-bold"><a href="/blog/cara-memilih-kontraktor-vila/" class="text-navy text-decoration-none">Hal yang Perlu Disiapkan Sebelum Berkonsultasi dengan Kontraktor</a></h4>
                        <p class="small text-muted mb-0">Kriteria evaluasi kontraktor berintegritas dan cara menyusun anggaran cadangan proyek.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/cara-memilih-kontraktor-vila/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Pelajari spesifikasi MEP dan standar kami:</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/produk/" class="btn btn-sm btn-primary">Solusi Utilitas MEP HQC &rarr;</a>
                    <a href="/portofolio/" class="btn btn-sm btn-outline-primary">Lihat Foto Progres &rarr;</a>
                    <a href="/tentang/" class="btn btn-sm btn-outline-secondary">Standar Kualitas HQC &rarr;</a>
                  </div>
                </div>
              </div>

"""
        if 'hqc-related-articles' not in c:
            c = c.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_block_2 + '<div class="card bg-light border p-4 my-5 rounded-4">')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated internal links in: {fpath}")

    # -------------------------------------------------------------
    # 3. Update Article 3: cara-memilih-kontraktor-vila
    # -------------------------------------------------------------
    a3_files = [
        os.path.join(root, 'blog', 'cara-memilih-kontraktor-vila', 'index.html'),
        os.path.join(root, 'blog', 'cara-memilih-kontraktor-vila.html')
    ]

    for fpath in a3_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        # Contextual link in intro
        c = c.replace(
            "dibutuhkan tim perencana.",
            'dibutuhkan tim perencana. Memahami <a href="/blog/tahapan-pembangunan-vila/" class="text-primary fw-medium text-decoration-underline">alur tahapan pembangunan vila dari pondasi hingga finishing</a> akan memberi Anda gambaran menyeluruh tentang setiap fase yang akan dihadapi.'
        )

        # Contextual link in Section 1
        c = c.replace(
            "jalur akses mobil molen ready-mix.",
            'jalur akses mobil molen ready-mix. Pembahasan mengenai pondasi lereng dan beban tanah ini kami ulas di <a href="/produk/" class="text-primary fw-medium text-decoration-underline">Layanan Pekerjaan Struktur &amp; Pondasi HQC</a>.'
        )

        # Contextual link in Section 2
        c = c.replace(
            "denah struktur pembesian, dan denah MEP plumbing.",
            'denah struktur pembesian, dan denah MEP plumbing. Koordinasi gambar MEP sangat penting untuk mencegah masalah kebocoran fatal, sebagaimana dibahas di artikel <a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="text-primary fw-medium text-decoration-underline">mengapa jalur pipa harus direncanakan matang sebelum pengecoran</a>.'
        )

        # Contextual link in Section 4
        c = c.replace(
            "metode pengujian mutu yang mereka terapkan di lapangan.",
            'metode pengujian mutu yang mereka terapkan di lapangan. Di HQC, seluruh bukti pekerjaan terbuka dan dapat Anda verifikasi di <a href="/portofolio/" class="text-primary fw-medium text-decoration-underline">Galeri Portofolio Dokumentasi Lapangan</a> serta halaman <a href="/tentang/" class="text-primary fw-medium text-decoration-underline">Tentang HQC</a>.'
        )

        # Contextual link in Section 4 (Consultation)
        c = c.replace(
            "pilihan material yang masuk akal tanpa mengorbankan kekuatan struktural.",
            'pilihan material yang masuk akal tanpa mengorbankan kekuatan struktural. Anda dapat mempelajari rincian paket pengerjaan di <a href="/produk/" class="text-primary fw-medium text-decoration-underline">Layanan Pembangunan Vila &amp; Hotel HQC</a>.'
        )

        # Add Related Articles Block before closing CTA card
        related_block_3 = """              <!-- Related Internal Links & Articles -->
              <div class="hqc-related-articles my-5 pt-4 border-top">
                <h3 class="h5 fw-bold text-navy mb-4">Artikel Terkait &amp; Referensi Konstruksi:</h3>
                <div class="row g-4">
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-primary bg-opacity-10 text-primary mb-2">TAHAPAN KONSTRUKSI</span>
                        <h4 class="h6 fw-bold"><a href="/blog/tahapan-pembangunan-vila/" class="text-navy text-decoration-none">Tahapan Pembangunan Vila: Dari Struktur Hingga Finishing</a></h4>
                        <p class="small text-muted mb-0">Edukasi komprehensif alur kerja pembangunan vila eksklusif untuk mencegah pembengkakan anggaran.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/tahapan-pembangunan-vila/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="p-4 rounded-3 border bg-light h-100 d-flex flex-column justify-content-between">
                      <div>
                        <span class="badge bg-info bg-opacity-10 text-dark mb-2">MEP &amp; PLUMBING</span>
                        <h4 class="h6 fw-bold"><a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="text-navy text-decoration-none">Mengapa Jalur Pipa Harus Direncanakan Matang Sebelum Pengecoran?</a></h4>
                        <p class="small text-muted mb-0">Pentingnya koordinasi antara gambar arsitektur dan sistem plumbing tertanam sebelum cor plat.</p>
                      </div>
                      <div class="mt-3">
                        <a href="/blog/instalasi-pipa-sebelum-pengecoran/" class="small fw-semibold text-primary">Baca Selengkapnya &rarr;</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-3 rounded-3 bg-white border d-flex flex-wrap justify-content-between align-items-center gap-2">
                  <span class="small text-muted">Siap mendiskusikan rencana proyek vila Anda?</span>
                  <div class="d-flex flex-wrap gap-2">
                    <a href="/kontak/" class="btn btn-sm btn-primary">Konsultasi ke Tim HQC &rarr;</a>
                    <a href="/portofolio/" class="btn btn-sm btn-outline-primary">Lihat Galeri Proyek &rarr;</a>
                    <a href="/tentang/" class="btn btn-sm btn-outline-secondary">Profil Perusahaan &rarr;</a>
                  </div>
                </div>
              </div>

"""
        if 'hqc-related-articles' not in c:
            c = c.replace('<div class="card bg-light border p-4 my-5 rounded-4">', related_block_3 + '<div class="card bg-light border p-4 my-5 rounded-4">')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated internal links in: {fpath}")

    # -------------------------------------------------------------
    # 4. Update Blog Hub: blog/index.html & blog.html
    # -------------------------------------------------------------
    b_files = [
        os.path.join(root, 'blog', 'index.html'),
        os.path.join(root, 'blog.html')
    ]

    for fpath in b_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        hub_internal_strip = """    <!-- Internal Links Quick Navigation Strip -->
    <div class="bg-light border-top border-bottom py-3 mb-5">
      <div class="container d-flex flex-wrap justify-content-between align-items-center gap-3">
        <div class="small text-navy fw-semibold">
          <span class="text-sand me-1">#</span> Topik &amp; Layanan Terkait:
        </div>
        <div class="d-flex flex-wrap gap-2 small">
          <a href="/produk/" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Pembangunan Vila Eksklusif</a>
          <a href="/produk/" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Pekerjaan Struktur &amp; MEP</a>
          <a href="/portofolio/" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Galeri Progres Lapangan</a>
          <a href="/tentang/" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Standar Kualitas HQC</a>
          <a href="/kontak/" class="badge bg-white text-navy border text-decoration-none py-2 px-3">Konsultasi Rencana Proyek</a>
        </div>
      </div>
    </div>
"""
        if 'Topik &amp; Layanan Terkait' not in c:
            c = c.replace('<!-- Blog Listing Section -->\n    <section class="hqc-section hqc-section--paper">', '<!-- Blog Listing Section -->\n' + hub_internal_strip + '    <section class="hqc-section hqc-section--paper">')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated internal links in: {fpath}")

    print("\nAll blog articles and hub successfully enriched with contextual internal links!")

if __name__ == '__main__':
    update_blog_internal_links()
