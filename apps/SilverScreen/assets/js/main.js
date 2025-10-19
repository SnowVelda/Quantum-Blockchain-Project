document.addEventListener('DOMContentLoaded', () => {
    const carouselContainer = document.querySelector('.carousel-container');

    const thumbnails = [
        { title: 'Thumbnail 1', image: 'assets/images/thumb1.jpg' },
        { title: 'Thumbnail 2', image: 'assets/images/thumb2.jpg' },
        { title: 'Thumbnail 3', image: 'assets/images/thumb3.jpg' },
        { title: 'Thumbnail 4', image: 'assets/images/thumb4.jpg' },
    ];

    function loadThumbnails() {
        thumbnails.forEach(thumb => {
            const thumbItem = document.createElement('img');
            thumbItem.src = thumb.image;
            thumbItem.alt = thumb.title;
            thumbItem.classList.add('carousel-item');
            carouselContainer.appendChild(thumbItem);
        });
    }

    loadThumbnails();

    // Basic interactivity for hero buttons (placeholders)
    const playButton = document.querySelector('.hero button:nth-of-type(1)');
    const moreInfoButton = document.querySelector('.hero button:nth-of-type(2)');

    if (playButton) {
        playButton.addEventListener('click', () => {
            alert('Playing movie/show!');
        });
    }

    if (moreInfoButton) {
        moreInfoButton.addEventListener('click', () => {
            alert('More info coming soon!');
        });
    }
});