function toggleContact() {
    const contactInfo = document.getElementById('contact-info');
    const button = document.querySelector('.contact-toggle');

    if (contactInfo.classList.contains('hidden')) {
        contactInfo.classList.remove('hidden');
        button.innerHTML = '📞 Скрыть контакты';
    } else {
        contactInfo.classList.add('hidden');
        button.innerHTML = '📞 Контактная информация';
    }
}