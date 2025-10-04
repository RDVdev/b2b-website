document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('nav ul li a');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    sections.forEach(section => {
        section.classList.add('hidden');
        observer.observe(section);
    });

    // Active link switching
    const currentPage = window.location.pathname.split('/').pop();
    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href').split('/').pop();
        if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
            link.classList.add('active');
        }
    });

    // Hide header on scroll down
    let lastScrollTop = 0;
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > lastScrollTop) {
            header.style.top = '-80px';
        } else {
            header.style.top = '0';
        }
        lastScrollTop = scrollTop;
    });

    // Theme switcher
    const themeSwitcher = document.getElementById('theme-switcher');
    themeSwitcher.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        if (document.body.classList.contains('dark-mode')) {
            themeSwitcher.textContent = '☀️';
        } else {
            themeSwitcher.textContent = '🌙';
        }
    });

    // Chatbot functionality
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotWindow = document.getElementById('chatbot-window');
    const chatbotSend = document.getElementById('chatbot-send');
    const chatbotInput = document.getElementById('chatbot-input');
    const chatbotMessages = document.getElementById('chatbot-messages');
    const webhookUrl = 'https://rdt556.app.n8n.cloud/webhook-test/policy-questions';

    chatbotToggle.addEventListener('click', () => {
        chatbotWindow.classList.toggle('hidden');
    });

    const addMessage = (text, sender) => {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chatbot-message', `${sender}-message`);
        messageElement.textContent = text;
        chatbotMessages.appendChild(messageElement);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    };

    chatbotSend.addEventListener('click', async () => {
        const message = chatbotInput.value.trim();
        if (message) {
            addMessage(message, 'user');
            chatbotInput.value = '';

            try {
                const response = await fetch(webhookUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message }),
                });

                if (response.ok) {
                    const data = await response.json();
                    console.log(data);  // Log the entire response for debugging
                    if (data.answer_text) {
                        addMessage(data.answer_text, 'bot');  // ✅ Show Gemini's reply
                    } else {
                        addMessage("Got a response, but no answer_text field found.", 'bot');
                    }
                } else {
                    addMessage("Sorry, something went wrong. Please try again.", 'bot');
                }

            } catch (error) {
                addMessage("Sorry, something went wrong. Please try again.", 'bot');
            }
        }
    });

    chatbotInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            chatbotSend.click();
        }
    });
});
