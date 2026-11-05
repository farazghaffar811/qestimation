/* Qestimation — interactions & animations (vanilla JS, no dependencies) */
(function () {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Preloader */
  const pre = $('.preloader');
  if (pre) {
    const hide = () => pre.classList.add('done');
    if (document.readyState !== 'loading') setTimeout(hide, 200);
    else document.addEventListener('DOMContentLoaded', () => setTimeout(hide, 200));
    window.addEventListener('load', hide);
    setTimeout(hide, 1800);
  }

  /* Sticky header shrink + back-to-top */
  const header = $('.header');
  const toTop = $('.to-top');
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle('is-scrolled', y > 60);
    toTop && toTop.classList.toggle('show', y > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop && toTop.addEventListener('click', (e) => { e.preventDefault(); window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });

  /* Mobile nav */
  const toggle = $('.nav-toggle');
  const nav = $('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target) && !toggle.contains(e.target) && nav.classList.contains('open')) {
        nav.classList.remove('open'); toggle.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* Button ripple */
  $$('.btn').forEach((b) => b.addEventListener('click', function (e) {
    if (reduce) return;
    const r = document.createElement('span');
    const d = Math.max(this.clientWidth, this.clientHeight);
    const rect = this.getBoundingClientRect();
    r.className = 'ripple';
    r.style.width = r.style.height = d + 'px';
    r.style.left = (e.clientX - rect.left - d / 2) + 'px';
    r.style.top = (e.clientY - rect.top - d / 2) + 'px';
    this.appendChild(r);
    setTimeout(() => r.remove(), 650);
  }));

  /* Scroll reveal (staggered) */
  const revealEls = $$('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const delay = parseInt(el.dataset.delay || '0', 10);
        setTimeout(() => el.classList.add('in'), delay);
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('in'));
  }

  /* Counters */
  const counters = $$('.counter .num[data-count]');
  const animateCount = (el) => {
    const target = parseInt(el.dataset.count, 10);
    const suffix = el.dataset.suffix || '';
    const dur = 2200;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 4);
      el.firstChild.nodeValue = Math.floor(eased * target).toLocaleString();
      if (p < 1) requestAnimationFrame(step); else el.firstChild.nodeValue = target.toLocaleString();
    };
    el.firstChild.nodeValue = '0';
    if (suffix && !el.querySelector('.plus')) { const s = document.createElement('span'); s.className = 'plus'; s.textContent = suffix; el.appendChild(s); }
    if (reduce) { el.firstChild.nodeValue = target.toLocaleString(); return; }
    requestAnimationFrame(step);
  };
  if (counters.length) {
    if ('IntersectionObserver' in window) {
      const cio = new IntersectionObserver((entries) => entries.forEach((en) => { if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); } }), { threshold: 0.4 });
      counters.forEach((c) => cio.observe(c));
    } else counters.forEach(animateCount);
  }

  /* Testimonial slider */
  const slider = $('.slider');
  if (slider) {
    const slides = $$('.slide', slider);
    const dotsWrap = $('.dots');
    let i = 0, timer;
    const go = (n) => {
      slides[i].classList.remove('active');
      dotsWrap && dotsWrap.children[i].classList.remove('active');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('active');
      dotsWrap && dotsWrap.children[i].classList.add('active');
    };
    if (dotsWrap) slides.forEach((_, n) => {
      const b = document.createElement('button');
      b.setAttribute('aria-label', 'Show testimonial ' + (n + 1));
      if (n === 0) b.classList.add('active');
      b.addEventListener('click', () => { go(n); restart(); });
      dotsWrap.appendChild(b);
    });
    const restart = () => { clearInterval(timer); if (!reduce) timer = setInterval(() => go(i + 1), 6000); };
    restart();
  }

  /* Work samples tabs */
  const tabBtns = $$('.samples__nav button');
  if (tabBtns.length) {
    const panels = $$('.samples__panel');
    const activate = (id, push) => {
      tabBtns.forEach((b) => b.classList.toggle('active', b.dataset.tab === id));
      panels.forEach((p) => {
        const on = p.id === id;
        p.classList.toggle('active', on);
        if (on) { const f = p.querySelector('iframe[data-src]'); if (f && !f.src) f.src = f.dataset.src; }
      });
      if (push) history.replaceState(null, '', '#' + id);
    };
    tabBtns.forEach((b) => b.addEventListener('click', () => activate(b.dataset.tab, true)));
    const h = location.hash.slice(1);
    activate(panels.some((p) => p.id === h) ? h : tabBtns[0].dataset.tab, false);
  }

  /* Gallery lightbox */
  const gallery = $('.gallery');
  if (gallery) {
    const links = $$('a', gallery);
    const lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.innerHTML = '<button class="lb-close" aria-label="Close"><i class="fa-solid fa-xmark"></i></button><button class="lb-prev" aria-label="Previous"><i class="fa-solid fa-chevron-left"></i></button><img alt=""><button class="lb-next" aria-label="Next"><i class="fa-solid fa-chevron-right"></i></button><div class="lb-count"></div>';
    document.body.appendChild(lb);
    const img = $('img', lb), count = $('.lb-count', lb);
    let cur = 0;
    const show = (n) => {
      cur = (n + links.length) % links.length;
      img.src = links[cur].href;
      img.alt = links[cur].querySelector('img').alt;
      count.textContent = (cur + 1) + ' / ' + links.length;
    };
    const open = (n) => { show(n); lb.classList.add('open'); document.body.style.overflow = 'hidden'; };
    const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
    links.forEach((a, n) => a.addEventListener('click', (e) => { e.preventDefault(); open(n); }));
    $('.lb-close', lb).addEventListener('click', close);
    $('.lb-prev', lb).addEventListener('click', () => show(cur - 1));
    $('.lb-next', lb).addEventListener('click', () => show(cur + 1));
    lb.addEventListener('click', (e) => { if (e.target === lb) close(); });
    document.addEventListener('keydown', (e) => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(cur - 1); if (e.key === 'ArrowRight') show(cur + 1);
    });
    let sx = 0;
    lb.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', (e) => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); });
  }

  /* Concrete slab rebar estimator */
  const est = $('.estimator');
  if (est) {
    const f = (id) => parseFloat($('#' + id, est).value) || 0;
    const out = (id, v) => { $('#' + id, est).textContent = v; };
    const calc = () => {
      const L = f('es-len'), W = f('es-wid'), sp = f('es-spacing') / 100, barLen = f('es-barlen'), price = f('es-price'), wire = f('es-wire');
      if (!L || !W || !sp) { ['es-r-len', 'es-r-wid', 'es-r-total', 'es-r-bars', 'es-r-cost'].forEach((k) => out(k, '—')); return; }
      const barsAlong = Math.floor(W / sp) + 1, barsAcross = Math.floor(L / sp) + 1;
      const lenAlong = barsAlong * L, lenAcross = barsAcross * W;
      const total = lenAlong + lenAcross;
      const bars = barLen ? Math.ceil(total / barLen) : 0;
      out('es-r-len', lenAlong.toFixed(1) + ' m');
      out('es-r-wid', lenAcross.toFixed(1) + ' m');
      out('es-r-total', total.toFixed(1) + ' m (' + (total * wire).toFixed(1) + ' kg)');
      out('es-r-bars', bars ? bars + ' bars' : '—');
      out('es-r-cost', bars && price ? '$' + (bars * price).toLocaleString(undefined, { maximumFractionDigits: 2 }) : '—');
    };
    $$('input', est).forEach((i) => i.addEventListener('input', calc));
    calc();
  }

  /* Quote form */
  const form = $('#quote-form');
  if (form) {
    const msg = $('.form-msg', form);
    const fileInput = $('input[type=file]', form);
    const fileLabel = $('.file span', form);
    fileInput && fileInput.addEventListener('change', () => { fileLabel.textContent = fileInput.files.length ? Array.from(fileInput.files).map((f) => f.name).join(', ') : 'Choose PDF / DWG / images'; });
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      msg.className = 'form-msg';
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const endpoint = form.dataset.endpoint;
      const btn = $('button[type=submit]', form);
      btn.disabled = true; btn.textContent = 'Sending…';
      try {
        if (endpoint) {
          const r = await fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
          if (!r.ok) throw new Error('Request failed');
        } else {
          const d = new FormData(form);
          const body = ['Name: ' + d.get('name'), 'Phone: ' + d.get('phone'), 'Email: ' + d.get('email'), 'Subject: ' + d.get('subject'), '', d.get('message')].join('\n');
          window.location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Quote request: ' + (d.get('subject') || 'New project')) + '&body=' + encodeURIComponent(body);
        }
        msg.textContent = 'Thank you! Your request has been received. Our estimators will get back to you within one business day.';
        msg.classList.add('ok'); form.reset(); fileLabel && (fileLabel.textContent = 'Choose PDF / DWG / images');
      } catch (err) {
        msg.textContent = 'Sorry, something went wrong. Please email us directly at ' + form.dataset.email + '.';
        msg.classList.add('err');
      } finally { btn.disabled = false; btn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Get Free Quote'; }
    });
  }

  /* Parallax for hero text */
  const heroInner = $('.hero__inner');
  if (heroInner && !reduce) {
    window.addEventListener('scroll', () => {
      const y = window.scrollY; if (y < 800) { heroInner.style.transform = 'translateY(' + y * 0.25 + 'px)'; heroInner.style.opacity = 1 - y / 900; }
    }, { passive: true });
  }

  /* Current year */
  $$('.year').forEach((y) => { y.textContent = new Date().getFullYear(); });
})();
