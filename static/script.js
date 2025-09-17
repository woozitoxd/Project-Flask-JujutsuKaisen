document.addEventListener('DOMContentLoaded', function () {
    console.log("Entró al script correctamente");
    // Variables de navegación
    const hamburgerMenu = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    const overlay = document.getElementById('overlay');

    // Variables de secciones
    const characterSection = document.getElementById('character-section');
    const videosSection = document.getElementById('videos-section');
    const characterCard = document.getElementById('character-card');
    const videosCard = document.getElementById('videos-card');
    const characterDetail = document.getElementById('character-detail');
    const navCharacters = document.getElementById('nav-characters');
    const navVideos = document.getElementById('nav-videos');
    const closeDetailButton = document.querySelector('.close-detail');
    const navHome = document.getElementById('nav-home');

    navHome.addEventListener('click', () => {
        // Ocultar secciones visibles
        characterSection.style.display = 'none';
        videosSection.style.display = 'none';
        // Cerrar cualquier panel abierto
        characterDetail.style.transform = 'translateX(100%)';
        document.body.classList.remove('overflow-hidden');
        // Hacer scroll al inicio de la página
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Toggle menú móvil
    hamburgerMenu.addEventListener('click', function () {
        this.classList.toggle('open');
        mobileMenu.classList.toggle('open');
        overlay.classList.toggle('active');
        document.body.classList.toggle('overflow-hidden');
    });

    overlay.addEventListener('click', closeMobileMenu);

    document.querySelectorAll('.mobile-nav-item').forEach(item => {
        item.addEventListener('click', function () {
            const target = this.getAttribute('data-target');
            toggleSection(target);
            closeMobileMenu();
        });
    });

    // Eventos de navegación
    characterCard.addEventListener('click', () => toggleSection('characters'));
    videosCard.addEventListener('click', () => toggleSection('videos'));
    navCharacters.addEventListener('click', () => toggleSection('characters'));
    navVideos.addEventListener('click', () => toggleSection('videos'));

    // Mostrar detalles de personaje
    // Abrir
    document.querySelectorAll('.character-card').forEach(card => {
        card.addEventListener('click', function () {
            const characterId = this.getAttribute('data-character');
            loadCharacterDetails(characterId);
            characterDetail.style.transform = 'translateX(0)';
            document.body.classList.add('overflow-hidden');
        });
    });

    // Cerrar
    closeDetailButton.addEventListener('click', function () {
        characterDetail.style.transform = 'translateX(100%)';
        document.body.classList.remove('overflow-hidden');
    });


    // ======================
    // Funciones auxiliares
    // ======================

    function closeMobileMenu() {
        hamburgerMenu.classList.remove('open');
        mobileMenu.classList.remove('open');
        overlay.classList.remove('active');
        document.body.classList.remove('overflow-hidden');
    }

    function toggleSection(target) {
        const sections = { characters: characterSection, videos: videosSection };
        Object.values(sections).forEach(sec => sec.style.display = 'none');
        if (sections[target]) {
            sections[target].style.display = 'block';
            window.scrollTo({ top: sections[target].offsetTop - 80, behavior: 'smooth' });
        }
    }

    function loadCharacterDetails(characterId) {
        characterDetail.style.transform = 'translateX(0)';
        const character = characterData[characterId];
        if (!character) {
            alert('Personaje no encontrado');
            return;
        }

        document.querySelector('.character-name').textContent = character.name;
        document.querySelector('.character-age').textContent = character.age;
        document.querySelector('.character-type').textContent = character.type;
        document.querySelector('.character-grade').textContent = character.grade;
        document.querySelector('.character-affiliation').textContent = character.affiliation;
        document.querySelector('.character-technique').textContent = character.technique;
        document.querySelector('.character-detail-img').src = character.image;
        document.querySelector('.character-detail-img').alt = character.name;

        // Biografía
        const bioContainer = document.querySelector('.bio-container');
        bioContainer.innerHTML = '';
        character.bio.forEach(paragraph => {
            const p = document.createElement('p');
            p.className = 'character-bio mb-4';
            p.textContent = paragraph;
            bioContainer.appendChild(p);
        });


        // Momentos
        const momentsContainer = document.querySelector('.character-moments');
        momentsContainer.innerHTML = '';
        character.moments.forEach(moment => {
            const li = document.createElement('li');
            li.className = 'flex items-start';
            li.innerHTML = `<span class="text-purple-400 mr-3"><i class="fas fa-star"></i></span><span>${moment}</span>`;
            momentsContainer.appendChild(li);
        });
    }


});
