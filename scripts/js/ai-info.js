function toggleAiInfo() {
    const contactInfo = document.getElementById('ai-info-messages');
    const button = document.querySelector('.ai-info-toggle');

    if (contactInfo.classList.contains('hidden')) {
        contactInfo.classList.remove('hidden');
        button.innerHTML = '֎ Об использовании AI:';
    } else {
        contactInfo.classList.add('hidden');
        button.innerHTML = '֎ Об использовании AI ...';
    }
}