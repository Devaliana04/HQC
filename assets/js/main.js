// Clean URL Enforcer - immediately hide .html from browser address bar
(function() {
  try {
    var p = window.location.pathname;
    if (p.endsWith('.html')) {
      var clean = p.replace(/\.html$/, '');
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
            const cleanBase = path.replace(/\/$/, '');
            window.location.href = cleanBase + '.html' + u.search;
          }
        }
      }
    } catch (err) {}
  });

  // 1. Navbar Scroll Detection
  const navbar = document.querySelector('.hqc-navbar');
  if (navbar && !navbar.classList.contains('hqc-navbar-solid')) {
    const handleScroll = () => {
      if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  // 2. Floating Action Controls: Scroll Up & Down Buttons
  const btnScrollUp = document.getElementById('hqcScrollUp');
  const btnScrollDown = document.getElementById('hqcScrollDown');

  if (btnScrollUp) {
    btnScrollUp.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  if (btnScrollDown) {
    btnScrollDown.addEventListener('click', () => {
      window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' });
    });
  }

  // Dynamic visibility for up button
  const toggleScrollButtons = () => {
    if (btnScrollUp) {
      if (window.scrollY > 240) {
        btnScrollUp.style.opacity = '1';
        btnScrollUp.style.pointerEvents = 'auto';
        btnScrollUp.style.transform = 'translateY(0)';
      } else {
        btnScrollUp.style.opacity = '0';
        btnScrollUp.style.pointerEvents = 'none';
        btnScrollUp.style.transform = 'translateY(10px)';
      }
    }
  };
  window.addEventListener('scroll', toggleScrollButtons, { passive: true });
  toggleScrollButtons();

  // 3. Portfolio Filtering & Inline Circle Detail Expansion
  const filterButtons = document.querySelectorAll('[data-filter]');
  const portfolioItems = document.querySelectorAll('[data-category]');

  if (filterButtons.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterVal = btn.getAttribute('data-filter');
        portfolioItems.forEach(item => {
          const itemCat = item.getAttribute('data-category');
          if (filterVal === 'all' || itemCat === filterVal) {
            item.style.display = '';
            item.style.opacity = '1';
          } else {
            item.style.display = 'none';
            item.style.opacity = '0';
          }
        });
      });
    });
  }

  // 3. Portfolio Lightbox Controller
  const lightboxModal = document.getElementById('hqcPortfolioModal');
  if (lightboxModal) {
    let currentItemIndex = 0;
    const cards = Array.from(document.querySelectorAll('.hqc-portfolio-card'));
    
    const updateModalContent = (index) => {
      if (index < 0) index = cards.length - 1;
      if (index >= cards.length) index = 0;
      currentItemIndex = index;

      const card = cards[currentItemIndex];
      if (!card) return;

      const title = card.getAttribute('data-title') || '';
      const phase = card.getAttribute('data-phase') || '';
      const location = card.getAttribute('data-location') || 'Bali';
      const imgSrc = card.getAttribute('data-img') || '';
      const desc = card.getAttribute('data-desc') || '';
      const specs = (card.getAttribute('data-specs') || '').split('|');

      const modalImg = document.getElementById('lightboxImg');
      const modalTitle = document.getElementById('lightboxTitle');
      const modalPhase = document.getElementById('lightboxPhase');
      const modalLocation = document.getElementById('lightboxLocation');
      const modalDesc = document.getElementById('lightboxDesc');
      const modalSpecs = document.getElementById('lightboxSpecs');
      const modalCounter = document.getElementById('lightboxCounter');

      if (modalImg) modalImg.src = imgSrc;
      if (modalTitle) modalTitle.textContent = title;
      if (modalPhase) modalPhase.textContent = phase;
      if (modalLocation) modalLocation.textContent = location;
      if (modalDesc) modalDesc.textContent = desc;
      if (modalCounter) modalCounter.textContent = `${currentItemIndex + 1} dari ${cards.length}`;

      if (modalSpecs) {
        modalSpecs.innerHTML = '';
        specs.forEach(s => {
          if (s.trim()) {
            const pill = document.createElement('span');
            pill.className = 'hqc-portfolio-card__spec-pill me-1 mb-1';
            pill.textContent = s.trim();
            modalSpecs.appendChild(pill);
          }
        });
      }
    };

    cards.forEach((card, idx) => {
      card.addEventListener('click', (e) => {
        updateModalContent(idx);
        const bsModal = bootstrap.Modal.getOrCreateInstance(lightboxModal);
        bsModal.show();
      });
    });

    const prevBtn = document.getElementById('lightboxPrev');
    const nextBtn = document.getElementById('lightboxNext');
    if (prevBtn) {
      prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        updateModalContent(currentItemIndex - 1);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        updateModalContent(currentItemIndex + 1);
      });
    }

    document.addEventListener('keydown', (e) => {
      if (!lightboxModal.classList.contains('show')) return;
      if (e.key === 'ArrowLeft') {
        updateModalContent(currentItemIndex - 1);
      } else if (e.key === 'ArrowRight') {
        updateModalContent(currentItemIndex + 1);
      }
    });
  }

  // 4. Contact Form to WhatsApp Message Composer
  const contactForm = document.getElementById('hqcContactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const nama = document.getElementById('contactNama')?.value.trim() || 'Sahabat HQC';
      const jenisProyek = document.getElementById('contactJenis')?.value || 'Konstruksi Vila / Hotel';
      const lokasi = document.getElementById('contactLokasi')?.value.trim() || '-';
      const pesan = document.getElementById('contactPesan')?.value.trim() || 'Saya ingin berkonsultasi mengenai perencanaan dan pelaksanaan konstruksi.';

      const textMessage = `Halo HQC (High Quality Construction),\n\nSaya ingin konsultasi proyek:\n- Nama: ${nama}\n- Jenis Proyek: ${jenisProyek}\n- Rencana Lokasi: ${lokasi}\n- Deskripsi Kebutuhan: ${pesan}\n\nMohon info tahapan konsultasi dan penjadwalan diskusi. Terima kasih.`;
      
      const waUrl = `https://wa.me/6282144267826?text=${encodeURIComponent(textMessage)}`;
      window.open(waUrl, '_blank', 'noopener,noreferrer');
    });
  }
});
