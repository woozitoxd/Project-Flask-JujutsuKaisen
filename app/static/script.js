document.addEventListener('DOMContentLoaded', function () {
    console.log("Entró al script correctamente");

    // Fetch de personajes
    fetch('/api/characters')
        .then(res => res.json())
        .then(data => {
            window.characterData = {};
            const container = document.querySelector('#character-section .grid');
            container.innerHTML = '';

            data.forEach(character => {
                window.characterData[character.id] = character;

                const card = document.createElement('div');
                card.className = 'character-card rounded-lg overflow-hidden cursor-pointer';
                card.setAttribute('data-character', character.id);

                card.innerHTML = `
                    <div class="overflow-hidden">
                        <img src="${character.image}" alt="${character.name}">
                    </div>
                    <div class="p-4">
                        <h3 class="text-xl font-bold mb-1">${character.name}</h3>
                        <p class="text-sm text-gray-400">${character.subtitle || ''}</p>
                    </div>
                `;
                container.appendChild(card);

                // Click para mostrar detalles
                card.addEventListener('click', () => {
                    loadCharacterDetails(character.id);
                    document.getElementById('character-detail').style.transform = 'translateX(0)';
                    document.body.classList.add('overflow-hidden');
                });
            });
        });

    // ======================
    // Variables de navegación
    // ======================
    const hamburgerMenu = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    const overlay = document.getElementById('overlay');
    const navCharacters = document.getElementById('nav-characters');
    const navVideos = document.getElementById('nav-videos');
    const navHome = document.getElementById('nav-home');

    // ======================
    // Variables de secciones
    // ======================
    const characterSection = document.getElementById('character-section');
    const videosSection = document.getElementById('videos-section');
    const characterDetail = document.getElementById('character-detail');
    const closeDetailButton = document.querySelector('.close-detail');

    // ======================
    // Funciones de navegación
    // ======================
    navHome?.addEventListener('click', () => {
        characterSection.style.display = 'none';
        videosSection.style.display = 'none';
        characterDetail.style.transform = 'translateX(100%)';
        document.body.classList.remove('overflow-hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    hamburgerMenu?.addEventListener('click', () => {
        hamburgerMenu.classList.toggle('open');
        mobileMenu.classList.toggle('open');
        overlay.classList.toggle('active');
        document.body.classList.toggle('overflow-hidden');
    });

    overlay?.addEventListener('click', closeMobileMenu);

    document.querySelectorAll('.mobile-nav-item').forEach(item => {
        item.addEventListener('click', function () {
            const target = this.getAttribute('data-target');
            toggleSection(target);
            closeMobileMenu();
        });
    });

    navCharacters?.addEventListener('click', () => toggleSection('characters'));
    navVideos?.addEventListener('click', () => toggleSection('videos'));

    // ======================
    // Mostrar detalles de personaje
    // ======================
    document.querySelectorAll('.character-card').forEach(card => {

        console.log('Tarjeta:', card.getAttribute('data-character'));
        console.log('Keys de characterData:', Object.keys(window.characterData));
        card.addEventListener('click', function () {
            const characterId = this.getAttribute('data-character');
            loadCharacterDetails(characterId);
            characterDetail.style.transform = 'translateX(0)';
            document.body.classList.add('overflow-hidden');
        });
    });

    closeDetailButton?.addEventListener('click', () => {
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
        const character = window.characterData?.[characterId];
        if (!character) {
            alert('Personaje no encontrado');
            return;
        }

        // Datos principales
        document.querySelector('.character-name').textContent = character.name;
        document.querySelector('.character-age').textContent = character.age;
        document.querySelector('.character-type').textContent = character.type;
        document.querySelector('.character-grade').textContent = character.grade;
        document.querySelector('.character-affiliation').textContent = character.affiliation;
        document.querySelector('.character-technique').textContent = character.technique;
        const imgEl = document.querySelector('.character-detail-img');
        imgEl.src = character.image_detail;
        imgEl.alt = character.name;

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



document.addEventListener("DOMContentLoaded", () => {
    const authBtn = document.getElementById("authBtn");
    const authModal = document.getElementById("authModal");
    const closeModal = document.getElementById("closeModal");

    const loginTab = document.getElementById("loginTab");
    const registerTab = document.getElementById("registerTab");
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    // Mostrar modal
    authBtn.addEventListener("click", () => {
        authModal.classList.remove("hidden");
        authModal.classList.add("flex");
    });

    // Cerrar modal
    closeModal.addEventListener("click", () => {
        authModal.classList.add("hidden");
        authModal.classList.remove("flex");
    });

    // Cambiar entre pestañas
    loginTab.addEventListener("click", () => {
        loginForm.classList.remove("hidden");
        registerForm.classList.add("hidden");
        loginTab.classList.add("active-tab");
        registerTab.classList.remove("active-tab");
    });

    registerTab.addEventListener("click", () => {
        registerForm.classList.remove("hidden");
        loginForm.classList.add("hidden");
        registerTab.classList.add("active-tab");
        loginTab.classList.remove("active-tab");
    });
});
// Script para manejar el modal de login/registro