// Clean URL Enforcer - immediately hide .html and /index from address bar on all environments
(function() {
  try {
    var p = window.location.pathname;
    if (p.endsWith('.html')) {
      var clean = p.replace(/\.html$/, '');
      if (clean.endsWith('/index')) clean = clean.replace(/\/index$/, '');
      window.history.replaceState(null, '', (clean || '/') + window.location.search + window.location.hash);
    }
  } catch (e) {}
})();

document.addEventListener('DOMContentLoaded', () => {
  // Universal clean link handler: ensure clicking any link never shows .html
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (!a || !a.href || a.target === '_blank') return;
    try {
      const u = new URL(a.href, window.location.origin);
      if (u.origin === window.location.origin && u.pathname.endsWith('.html')) {
        const cleanPath = u.pathname.replace(/\.html$/, '');
        a.href = cleanPath + (cleanPath.endsWith('/') ? '' : '/') + u.search + u.hash;
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

  // Circular items active ring styling
  const circleButtons = document.querySelectorAll('.hqc-portfolio-circle');
  circleButtons.forEach(circle => {
    circle.addEventListener('click', () => {
      circleButtons.forEach(c => c.classList.remove('active'));
      circle.classList.add('active');
    });
  });

  // URL Hash auto-open for portfolio details e.g. /portofolio/#detail-struktur-01
  if (window.location.hash) {
    const targetElement = document.querySelector(window.location.hash);
    if (targetElement && targetElement.classList.contains('collapse')) {
      const bsCollapse = new bootstrap.Collapse(targetElement, { toggle: true });
      setTimeout(() => {
        targetElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 350);
    }
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
