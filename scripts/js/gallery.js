// gallery.js
document.addEventListener('DOMContentLoaded', function () {
    const gallery = document.querySelector('.gallery-scroll');
    const prevBtn = document.querySelector('.nav-btn.prev');
    const nextBtn = document.querySelector('.nav-btn.next');
    const progressBar = document.querySelector('.progress-bar');

    // Рассчитываем ширину карточки с учетом gap
    const cardStyle = window.getComputedStyle(document.querySelector('.photo-card'));
    const gapStyle = window.getComputedStyle(gallery);
    const cardWidth = parseInt(cardStyle.width) + parseInt(gapStyle.gap);

    // Функция для прокрутки галереи
    function scrollGallery(direction) {
        const scrollAmount = cardWidth * direction;
        gallery.scrollBy({
            left: scrollAmount,
            behavior: 'smooth'
        });

        // Анимация кнопки
        const btn = direction > 0 ? nextBtn : prevBtn;
        btn.style.transform = 'scale(0.95)';
        setTimeout(() => {
            btn.style.transform = '';
        }, 150);
    }

    // Обновление прогресс-бара
    function updateProgress() {
        const scrollableWidth = gallery.scrollWidth - gallery.clientWidth;
        const scrollPosition = gallery.scrollLeft;
        const progress = (scrollPosition / scrollableWidth) * 100;
        progressBar.style.width = `${progress}%`;
    }

    // Drag & Drop для мыши
    let isDragging = false;
    let startX;
    let scrollLeft;

    gallery.addEventListener('mousedown', (e) => {
        isDragging = true;
        gallery.style.cursor = 'grabbing';
        startX = e.pageX - gallery.offsetLeft;
        scrollLeft = gallery.scrollLeft;
        gallery.style.scrollBehavior = 'auto'; // Отключаем smooth при drag
    });

    gallery.addEventListener('mouseleave', () => {
        isDragging = false;
        gallery.style.cursor = 'grab';
        gallery.style.scrollBehavior = 'smooth';
    });

    gallery.addEventListener('mouseup', () => {
        isDragging = false;
        gallery.style.cursor = 'grab';
        gallery.style.scrollBehavior = 'smooth';
    });

    gallery.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX - gallery.offsetLeft;
        const walk = (x - startX) * 2;
        gallery.scrollLeft = scrollLeft - walk;
        updateProgress();
    });

    // Touch события для мобильных устройств
    gallery.addEventListener('touchstart', (e) => {
        startX = e.touches[0].pageX - gallery.offsetLeft;
        scrollLeft = gallery.scrollLeft;
        gallery.style.scrollBehavior = 'auto';
    });

    gallery.addEventListener('touchmove', (e) => {
        const x = e.touches[0].pageX - gallery.offsetLeft;
        const walk = (x - startX);
        gallery.scrollLeft = scrollLeft - walk;
        updateProgress();
    });

    gallery.addEventListener('touchend', () => {
        gallery.style.scrollBehavior = 'smooth';
    });

    // Обработчики для кнопок
    prevBtn.addEventListener('click', () => scrollGallery(-1));
    nextBtn.addEventListener('click', () => scrollGallery(1));

    // Обновление прогресса при скролле
    gallery.addEventListener('scroll', updateProgress);

    // Инициализация прогресс-бара
    updateProgress();

    // Добавляем класс для плавного появления галереи
    setTimeout(() => {
        document.querySelector('.gallery-section').classList.add('loaded');
    }, 100);
});