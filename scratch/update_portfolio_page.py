import os
import re

workspace = r"c:\Users\LENOVO\Downloads\HQC-High Quality Construction"
portofolio_path = os.path.join(workspace, "portofolio.html")

with open(portofolio_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the 10 rich architectural showcase cards
portfolio_grid_html = '''    <!-- Architectural Project Showcase Section -->
    <section class="hqc-section hqc-section--paper" id="proyek-lapangan">
      <div class="container">
        <!-- Section Header -->
        <div class="text-center max-w-700 mx-auto mb-5">
          <span class="hqc-eyebrow hqc-eyebrow--dark">BUKTI NYATA KEAHLIAN LAPANGAN</span>
          <h2 class="display-6 fw-bold text-navy mb-3">Galeri Tahapan Konstruksi Vila & Properti Bali</h2>
          <div class="hqc-line-blue mx-auto mb-3"></div>
          <p class="text-slate">Jelajahi dokumentasi nyata dari setiap lapis pekerjaan konstruksi HQC di Bali—mulai dari pondasi struktur tahan gempa, instalasi utilitas tertanam, hingga finishing arsitektural tropis mewah. Klik foto untuk melihat detail spesifikasi teknis.</p>
        </div>

        <!-- Filter Tabs -->
        <div class="d-flex flex-wrap gap-2 justify-content-center mb-5" role="tablist">
          <button type="button" class="hqc-filter-btn active" data-filter="all">Semua Tahapan (10)</button>
          <button type="button" class="hqc-filter-btn" data-filter="struktur">Struktur & Pembesian</button>
          <button type="button" class="hqc-filter-btn" data-filter="utilitas">Utilitas (MEP)</button>
          <button type="button" class="hqc-filter-btn" data-filter="dinding">Rangka & Dinding</button>
          <button type="button" class="hqc-filter-btn" data-filter="finishing">Finishing Arsitektur</button>
          <button type="button" class="hqc-filter-btn" data-filter="eksterior">Eksterior & Kolam</button>
        </div>

        <!-- Architectural Showcase Grid (Wide Aspect Ratio Cards) -->
        <div class="hqc-portfolio-grid" id="portfolioGallery">
          <!-- Item 01: Struktur Pembesian Plat -->
          <article class="hqc-portfolio-card" data-category="struktur"
            data-title="Pembesian Plat Lantai & Jalur Pipa Terintegrasi"
            data-phase="FASE 01 • STRUKTUR TAHAN GEMPA"
            data-location="📍 Canggu, Bali"
            data-img="/assets/images/portfolio/hqc-struktur-pembesian-instalasi-pipa-01.webp"
            data-desc="Dokumentasi penataan tulangan plat lantai dua lapis dengan perletakan saluran pipa gravitasi terukur. Kawat bendrat diikat ganda guna menjamin tulangan tidak bergeser selama pemadatan vibrator beton."
            data-specs="Besi Ulir D16/D19 SNI | Pipa PVC AW Rucika | Mutu Beton K-350 | Spacer Beton Tahu 3cm">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 01 • STRUKTUR</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-struktur-pembesian-instalasi-pipa-01.webp" alt="Pembesian Plat Lantai dan Jalur Pipa Terintegrasi HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Canggu, Bali • Proyek Vila Mewah</div>
              <h3 class="hqc-portfolio-card__title">Pembesian Plat Lantai & Jalur Pipa Terintegrasi</h3>
              <p class="hqc-portfolio-card__desc">Pemasangan besi tulangan plat dua lapis berstandar gempa dengan koordinasi pipa utilitas tertanam sebelum pengecoran.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Besi Ulir D16 SNI</span>
                <span class="hqc-portfolio-card__spec-pill">Beton K-350</span>
                <span class="hqc-portfolio-card__spec-pill">Plumbing AW</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 02: Bekisting & Sudut Lebar Struktur -->
          <article class="hqc-portfolio-card" data-category="struktur"
            data-title="Bentangan Balok Utama & Bekisting Presisi"
            data-phase="FASE 02 • STRUKTUR SLAB"
            data-location="📍 Pererenan, Bali"
            data-img="/assets/images/portfolio/hqc-area-struktur-pipa-02.webp"
            data-desc="Tampak sudut lebar bentangan balok utama dan plat lantai zona basah vila. Kemiringan pipa pembuangan diuji waterpass presisi untuk menjamin aliran air gravitasi tanpa resiko sumbatan di kemudian hari."
            data-specs="Balok Induk 30x60 | Phenolic Film 18mm | Waterpass Digital | Garansi Struktur 10 Tahun">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 02 • STRUKTUR</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-area-struktur-pipa-02.webp" alt="Bentangan Balok Utama dan Bekisting Presisi HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Pererenan, Bali • Vila Komersial</div>
              <h3 class="hqc-portfolio-card__title">Bentangan Balok Utama & Bekisting Presisi</h3>
              <p class="hqc-portfolio-card__desc">Inspeksi sudut bentang balok penopang lantai atas dengan penahan bekisting baja kokoh anti lendutan.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Balok 30x60</span>
                <span class="hqc-portfolio-card__spec-pill">Phenolic 18mm</span>
                <span class="hqc-portfolio-card__spec-pill">Anti Lendut</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 03: Rangka Struktur Depan Bertingkat -->
          <article class="hqc-portfolio-card" data-category="struktur"
            data-title="Kerangka Bertingkat Kolom & Balcon Cantilever"
            data-phase="FASE 03 • STRUKTUR BERTINGKAT"
            data-location="📍 Uluwatu, Bali"
            data-img="/assets/images/portfolio/hqc-struktur-depan-bangunan-03.webp"
            data-desc="Wujud progres fisik struktur bangunan vila tepi tebing Uluwatu. Mengkombinasikan kolom beton penopang masif dengan overhang balkon kantilever yang menghadap pemandangan samudera lepas."
            data-specs="Kolom K-400 | Balcon Cantilever 2.5m | Tulangan Ekstra Negatif | Pondasi Bore Pile">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 03 • STRUKTUR BERTINGKAT</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-struktur-depan-bangunan-03.webp" alt="Kerangka Bertingkat Kolom dan Balcon Cantilever HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Uluwatu, Bali • Cliffside Luxury Villa</div>
              <h3 class="hqc-portfolio-card__title">Kerangka Bertingkat Kolom & Balcon Cantilever</h3>
              <p class="hqc-portfolio-card__desc">Struktur bertingkat modern dengan bukaan void tinggi dan balkon gantung aman teruji perhitungan insinyur sipil.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Cantilever 2.5m</span>
                <span class="hqc-portfolio-card__spec-pill">Bore Pile 12m</span>
                <span class="hqc-portfolio-card__spec-pill">Struktur Gempa</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 04: Utilitas MEP -->
          <article class="hqc-portfolio-card" data-category="utilitas"
            data-title="Jaringan Plumbing MEP & Konduit Elektrikal"
            data-phase="FASE 04 • UTILITAS (MEP)"
            data-location="📍 Seminyak, Bali"
            data-img="/assets/images/portfolio/hqc-jaringan-pipa-pembesian-04.webp"
            data-desc="Detail penataan jalur pipa air bersih panas/dingin dan konduit elektrikal tahan api tertanam rapi di dalam balok plat. Setiap sambungan diuji tekanan air (pressure test 10 bar) selama 24 jam sebelum pengecoran."
            data-specs="Pipa PPR Westpex | Uji Tekan 10 Bar | Pipa Conduit Clipsal | Solvent Cement Standar">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 04 • MEP</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-jaringan-pipa-pembesian-04.webp" alt="Jaringan Plumbing MEP dan Konduit Elektrikal HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Seminyak, Bali • Boutique Resort</div>
              <h3 class="hqc-portfolio-card__title">Jaringan Plumbing MEP & Konduit Elektrikal</h3>
              <p class="hqc-portfolio-card__desc">Instalasi sanitasi modern bebas bocor dengan pipa PPR air panas dan pengujian hidrostatik ketat sebelum ditutup beton.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">PPR Air Panas</span>
                <span class="hqc-portfolio-card__spec-pill">Uji Tekan 10 Bar</span>
                <span class="hqc-portfolio-card__spec-pill">Zero Leakage</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 05: Pembesian Detail Kawat Bendrat -->
          <article class="hqc-portfolio-card" data-category="struktur"
            data-title="Ikatan Tulangan Besi & Selimut Beton Decking"
            data-phase="FASE 05 • PEMBESIAN DETAIL"
            data-location="📍 Ubud, Bali"
            data-img="/assets/images/portfolio/hqc-pembesian-struktur-05.webp"
            data-desc="Detail kerapian ikatan kawat bendrat pada perjumpaan kolom-balok. Pemasangan beton decking silinder menjaga jarak selimut beton 3.5 cm dari bekisting, melindungi tulangan dari kelembaban iklim tropis Bali."
            data-specs="Kawat Bendrat Ganda | Selimut Beton 3.5cm | Sengkang Pembagi 100mm | Anti Korosi Tropis">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 05 • DETAIL PEMBESIAN</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-pembesian-struktur-05.webp" alt="Ikatan Tulangan Besi dan Selimut Beton Decking HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Ubud, Bali • Eco Luxury Villa</div>
              <h3 class="hqc-portfolio-card__title">Ikatan Tulangan Besi & Selimut Beton Decking</h3>
              <p class="hqc-portfolio-card__desc">Pengerjaan pembesian manual oleh tukang besi bersertifikasi untuk memastikan kekuatan daktilitas gempa maksimal.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Besi D19 SNI</span>
                <span class="hqc-portfolio-card__spec-pill">Decking 3.5cm</span>
                <span class="hqc-portfolio-card__spec-pill">Daktilitas Gempa</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 06: Rangka Fasad Baja Ringan -->
          <article class="hqc-portfolio-card" data-category="dinding"
            data-title="Rangka Fasad Baja Ringan & Struktur Sekunder"
            data-phase="FASE 06 • RANGKA FASAD"
            data-location="📍 Canggu, Bali"
            data-img="/assets/images/portfolio/hqc-pekerjaan-rangka-fasad-06.webp"
            data-desc="Pemasangan rangka fasad hollow galvanis anti karat untuk pembentukan bidang secondary skin arsitektural. Penggunaan scaffolding terstandar menjamin keselamatan kerja dan kelurusan bidang fasad vertikal."
            data-specs="Hollow Galvanis 4x4 / 4x2 | Scaffolding Tubular K3 | Dynabolt Stainless Steel | Tahan Angin Laut">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 06 • RANGKA FASAD</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-pekerjaan-rangka-fasad-06.webp" alt="Rangka Fasad Baja Ringan dan Struktur Sekunder HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Canggu, Bali • Modern Tropical Villa</div>
              <h3 class="hqc-portfolio-card__title">Rangka Fasad Baja Ringan & Struktur Sekunder</h3>
              <p class="hqc-portfolio-card__desc">Rangka penopang fasad arsitektur modern tahan korosi udara laut dengan penguncian dynabolt baja tahan karat.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Galvanis Anti Karat</span>
                <span class="hqc-portfolio-card__spec-pill">Standar K3</span>
                <span class="hqc-portfolio-card__spec-pill">Tahan Angin Laut</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 07: Dinding Bata Ringan Presisi & Perancah -->
          <article class="hqc-portfolio-card" data-category="dinding"
            data-title="Dinding Bata Ringan Hebel & Perancah Keselamatan"
            data-phase="FASE 07 • DINDING PRESISI"
            data-location="📍 Sanur, Bali"
            data-img="/assets/images/portfolio/hqc-pekerjaan-dinding-scaffolding-07.webp"
            data-desc="Pasangan dinding bata ringan Hebel dengan perekat semen mortar instan bermutu tinggi. Dinding berdiri tegak lurus sempurna berkat kontrol lot benang laser sebelum pekerjaan plesteran luar dimulai."
            data-specs="Bata Ringan Hebel 10cm | Mortar Instan MU-380 | Kolom Praktis 12m2 | Laser Alignment">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 07 • DINDING HEBEL</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-pekerjaan-dinding-scaffolding-07.webp" alt="Dinding Bata Ringan Hebel dan Perancah Keselamatan HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Sanur, Bali • Private Residence</div>
              <h3 class="hqc-portfolio-card__title">Dinding Bata Ringan Hebel & Perancah Keselamatan</h3>
              <p class="hqc-portfolio-card__desc">Dinding kedap suara berbobot ringan yang meredam rambatan panas matahari tropis secara efektif ke dalam ruangan.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Hebel Presisi</span>
                <span class="hqc-portfolio-card__spec-pill">Insulasi Suhu</span>
                <span class="hqc-portfolio-card__spec-pill">Kedap Suara</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 08: Finishing Plesteran Acian Lengkung -->
          <article class="hqc-portfolio-card" data-category="finishing"
            data-title="Finishing Acian Halus & Bukaan Lengkung Estetik"
            data-phase="FASE 08 • FINISHING ARSITEKTUR"
            data-location="📍 Seminyak, Bali"
            data-img="/assets/images/portfolio/hqc-finishing-plester-dinding-08.webp"
            data-desc="Pengerjaan tangan terampil plesteran semen acian pada koridor berarsitektur lengkung mediterania tropis. Menghasilkan permukaan dinding halus bebas retak rambut dengan kelengkungan simetris sempurna."
            data-specs="Acian Instan MU-200 | Profil Lengkung Khusus | Semen Anti Retak Rambut | Basecoat Tahan Cuaca">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 08 • FINISHING</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-finishing-plester-dinding-08.webp" alt="Finishing Acian Halus dan Bukaan Lengkung Estetik HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Seminyak, Bali • Mediterranean Tropical Villa</div>
              <h3 class="hqc-portfolio-card__title">Finishing Acian Halus & Bukaan Lengkung Estetik</h3>
              <p class="hqc-portfolio-card__desc">Detail arsitektural lengkung organik yang membutuhkan keahlian plesteran tingkat tinggi khas villa eksklusif Bali.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Dinding Lengkung</span>
                <span class="hqc-portfolio-card__spec-pill">Bebas Retak Rambut</span>
                <span class="hqc-portfolio-card__spec-pill">Sentuhan Mewah</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 09: Eksterior Infinity Pool & Dek Kayu -->
          <article class="hqc-portfolio-card" data-category="eksterior"
            data-title="Infinity Pool Vila & Dek Kayu Ulin Tepi Kolam"
            data-phase="FASE 09 • EKSTERIOR & KOLAM"
            data-location="📍 Bingin, Uluwatu, Bali"
            data-img="/assets/images/portfolio/hqc-progres-eksterior-kolam-09.webp"
            data-desc="Penyelesaian area kolam renang infinity vila dengan sirkulasi overflow. Dilapisi waterproofing polyurethane ganda dan dikelilingi decking kayu ulin Kalimantan yang tahan terhadap air berkaporit dan sengatan matahari."
            data-specs="Waterproofing Polyurethane | Decking Ulin Asli Kelas 1 | Mosaik Kuda Laut | Pompa Hayward USA">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 09 • INFINITY POOL</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-progres-eksterior-kolam-09.webp" alt="Infinity Pool Vila dan Dek Kayu Ulin HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Bingin, Uluwatu, Bali • Luxury Sea-View Villa</div>
              <h3 class="hqc-portfolio-card__title">Infinity Pool Vila & Dek Kayu Ulin Tepi Kolam</h3>
              <p class="hqc-portfolio-card__desc">Pembangunan fasilitas kolam renang vila eksklusif dengan sistem filtrasi air kristal dan pencahayaan malam dramatis.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Infinity Pool</span>
                <span class="hqc-portfolio-card__spec-pill">Kayu Ulin Asli</span>
                <span class="hqc-portfolio-card__spec-pill">Anti Bocor</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>

          <!-- Item 10: Fasad Arsitektur Jadi & Koridor Mewah -->
          <article class="hqc-portfolio-card" data-category="eksterior"
            data-title="Wujud Jadi Fasad Lengkung & Pasangan Travertin"
            data-phase="FASE 10 • HASIL JADI ARSITEKTUR"
            data-location="📍 Canggu, Bali"
            data-img="/assets/images/portfolio/hqc-progres-fasad-bangunan-10.webp"
            data-desc="Hasil akhir koridor beratap lengkung dengan balutan batu alam travertin dan lantai teraso halus. Bukti dedikasi HQC dalam mengubah gambar desain arsitek menjadi wujud nyata bernilai investasi tinggi di Bali."
            data-specs="Batu Alam Travertin | Lantai Teraso Cor | Cat Tahan Cuaca Jotun | Nilai Investasi Tinggi">
            <div class="hqc-portfolio-card__img-wrap">
              <span class="hqc-portfolio-card__badge">FASE 10 • HASIL JADI</span>
              <span class="hqc-portfolio-card__zoom-hint" title="Perbesar Foto">🔍</span>
              <img src="/assets/images/portfolio/hqc-progres-fasad-bangunan-10.webp" alt="Wujud Jadi Fasad Lengkung dan Pasangan Travertin HQC Bali" width="600" height="375" loading="lazy">
            </div>
            <div class="hqc-portfolio-card__body">
              <div class="hqc-portfolio-card__location">📍 Canggu, Bali • Finished Architectural Villa</div>
              <h3 class="hqc-portfolio-card__title">Wujud Jadi Fasad Lengkung & Pasangan Travertin</h3>
              <p class="hqc-portfolio-card__desc">Realisasi bangunan vila tropis mewah yang siap huni atau disewakan dengan tingkat okupansi dan ROI optimal.</p>
              <div class="hqc-portfolio-card__specs">
                <span class="hqc-portfolio-card__spec-pill">Batu Travertin</span>
                <span class="hqc-portfolio-card__spec-pill">Lantai Teraso</span>
                <span class="hqc-portfolio-card__spec-pill">High ROI Bali</span>
              </div>
              <button type="button" class="hqc-portfolio-card__btn">
                <span>🔍 Lihat Foto & Spesifikasi Detail</span>
              </button>
            </div>
          </article>
        </div>

        <!-- Interactive Lightbox Modal (Zoom & Full Detail Viewer) -->
        <div class="modal fade" id="hqcPortfolioModal" tabindex="-1" aria-labelledby="lightboxTitle" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered hqc-lightbox-dialog">
            <div class="modal-content hqc-lightbox-content">
              <div class="modal-header hqc-lightbox-header d-flex justify-content-between align-items-center">
                <div class="d-flex align-items-center gap-2">
                  <span class="badge bg-primary bg-opacity-25 text-primary px-3 py-1 rounded-pill small" id="lightboxPhase">FASE PROYEK</span>
                  <span class="small text-muted" id="lightboxCounter">1 dari 10</span>
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button>
              </div>
              <div class="modal-body hqc-lightbox-body">
                <!-- Large Image Viewer with Prev/Next Navigation -->
                <div class="hqc-lightbox-img-wrap">
                  <button type="button" class="hqc-lightbox-nav-btn hqc-lightbox-nav-btn--prev" id="lightboxPrev" aria-label="Foto Sebelumnya" title="Sebelumnya (Panah Kiri)">‹</button>
                  <img id="lightboxImg" src="" alt="Detail Pekerjaan Lapangan HQC Bali" class="img-fluid">
                  <button type="button" class="hqc-lightbox-nav-btn hqc-lightbox-nav-btn--next" id="lightboxNext" aria-label="Foto Berikutnya" title="Berikutnya (Panah Kanan)">›</button>
                </div>
                <!-- Technical Info & Specs -->
                <div class="hqc-lightbox-info">
                  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-2">
                    <h3 class="h4 fw-bold text-navy mb-0" id="lightboxTitle">Judul Proyek</h3>
                    <span class="badge bg-info text-dark" id="lightboxLocation">📍 Lokasi Proyek</span>
                  </div>
                  <p class="text-slate mb-3" id="lightboxDesc">Deskripsi detail spesifikasi teknis dan pekerjaan di lapangan.</p>
                  <div class="mb-4">
                    <strong class="d-block small text-navy text-uppercase mb-2">Spesifikasi Material & Metode Konstruksi:</strong>
                    <div id="lightboxSpecs" class="d-flex flex-wrap gap-1"></div>
                  </div>
                  <div class="d-flex flex-wrap justify-content-between align-items-center pt-3 border-top border-light gap-3">
                    <span class="small text-muted">Ingin membangun vila dengan standar mutu seperti ini di Bali?</span>
                    <a href="https://wa.me/6282144267826?text=Halo%20HQC%20Bali%2C%20saya%20tertarik%20dengan%20progres%20konstruksi%20dan%20ingin%20konsultasi%20proyek%20vila."
                      target="_blank" rel="noopener noreferrer" class="hqc-btn hqc-btn--primary">
                      <span>Konsultasi Proyek via WhatsApp ↗</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>'''

# Replace from `<!-- Interactive Circular Orbit Section -->` to the end of the section
pattern = r'<!-- Interactive Circular Orbit Section -->[\s\S]*?</section>'
if re.search(pattern, content):
    new_content = re.sub(pattern, portfolio_grid_html, content, count=1)
    with open(portofolio_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced circular orbit section with modern architectural cards and lightbox in portofolio.html!")
else:
    print("Warning: Pattern not found in portofolio.html, searching fallback...")
    alt_pattern = r'<section class="hqc-section hqc-section--paper">[\s\S]*?</section>'
    new_content = re.sub(alt_pattern, portfolio_grid_html, content, count=1)
    with open(portofolio_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fallback replace completed.")
