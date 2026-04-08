function toggleEVersionDownload() {
    const contactInfo = document.getElementById('e-version-download-messages');
    const button = document.querySelector('.e-version-download-toggle');

    if (contactInfo.classList.contains('hidden')) {
        contactInfo.classList.remove('hidden');
        button.innerHTML = '📄 Скачать резюме в электронном документе:';
    } else {
        contactInfo.classList.add('hidden');
        button.innerHTML = '📄 Скачать резюме в электронном документе ...';
    }
}