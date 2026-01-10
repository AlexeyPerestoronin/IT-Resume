function toggleHrInfo() {
    const contactInfo = document.getElementById('hr-info-messages');
    const button = document.querySelector('.hr-info-toggle');

    if (contactInfo.classList.contains('hidden')) {
        contactInfo.classList.remove('hidden');
        button.innerHTML = 'Информация для HR:';
    } else {
        contactInfo.classList.add('hidden');
        button.innerHTML = '❤️ Информация для HR ...';
    }
}