document.addEventListener('DOMContentLoaded', function() {
    // Toggle the mobile menu
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('header nav ul');

    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('open');
        });
    }

    // Show a confirmation before logging out
    const logoutLink = document.querySelector('a[href$="logout/"]');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            if (!confirm("Are you sure you want to log out?")) {
                event.preventDefault();
            }
        });
    }

    // AJAX for dynamically loading articles (if you plan to use it)
    const loadMoreButton = document.querySelector('#load-more');
    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', function() {
            const url = this.dataset.url;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const articlesContainer = document.querySelector('#articles');
                    data.articles.forEach(article => {
                        const articleElement = document.createElement('li');
                        articleElement.innerHTML = `<a href="${article.url}">${article.title}</a>`;
                        articlesContainer.appendChild(articleElement);
                    });
                })
                .catch(error => console.error('Error loading more articles:', error));
        });
    }
});