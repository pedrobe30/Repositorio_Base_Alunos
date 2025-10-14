document.addEventListener('DOMContentLoaded', () => {
    // =================================
    // CONFIGURAÇÃO DA API
    // =================================
    const API_BASE_URL = 'http://127.0.0.1:5000';

    // =================================
    // SELETORES GLOBAIS
    // =================================
    const paginaLanding = document.getElementById('pagina-landing');
    const paginaAutenticacao = document.getElementById('pagina-autenticacao');
    const paginaHome = document.getElementById('pagina-home');
    const paginaMinhaConta = document.getElementById('pagina-minha-conta');

    // --- Autenticação ---
    const authWrapper = document.getElementById('auth-wrapper');
    const formLogin = document.getElementById('form-login');
    const formCadastro = document.getElementById('form-cadastro');
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');

    // --- Home Page ---
    const userNameDisplay = document.getElementById('user-name-display');
    const cursosContainer = document.getElementById('cursos-container');
    const polosContainer = document.getElementById('polos-container');
    const buscaCursoInput = document.getElementById('busca-curso');
    const filtroAreaSelect = document.getElementById('filtro-area');

    // --- Minha Conta ---
    const perfilNome = document.getElementById('perfil-nome');
    const perfilEmail = document.getElementById('perfil-email');
    const meusCursosContainer = document.getElementById('meus-cursos-container');

    // --- Modais ---
    const modalDetalhesCurso = document.getElementById('modal-detalhes-curso');
    const modalConfirmacaoExclusao = document.getElementById('modal-confirmacao-exclusao');
    
    // =================================
    // ESTADO DA APLICAÇÃO
    // =================================
    let currentUser = null;
    let todosCursos = [];
    let todosPolos = [];

    // =================================
    // FUNÇÕES DE NAVEGAÇÃO
    // =================================
    function navegarPara(pagina) {
        paginaLanding.classList.add('hidden');
        paginaAutenticacao.classList.add('hidden');
        paginaHome.classList.add('hidden');
        paginaMinhaConta.classList.add('hidden');

        if (pagina === 'autenticacao') {
            paginaAutenticacao.classList.remove('hidden');
        } else if (pagina === 'home') {
            paginaHome.classList.remove('hidden');
            carregarDadosHome();
        } else if (pagina === 'minha-conta') {
            paginaMinhaConta.classList.remove('hidden');
            carregarDadosMinhaConta();
        } else { // 'landing'
            paginaLanding.classList.remove('hidden');
        }
    }

    // =================================
    // FUNÇÕES DE VALIDAÇÃO
    // =================================
    function mostrarErro(input, mensagem) {
        const formGrupo = input.closest('.form-grupo');
        const errorDiv = formGrupo.querySelector('.error-message');
        errorDiv.textContent = mensagem;
        errorDiv.style.display = 'block';
    }

    function limparTodosErros(form) {
        form.querySelectorAll('.error-message').forEach(el => el.style.display = 'none');
    }
    
    function validarFormulario(form) {
        let ehValido = true;
        limparTodosErros(form);
        const inputs = form.querySelectorAll('input[required]');

        inputs.forEach(input => {
            if (!input.value.trim()) {
                mostrarErro(input, `Campo obrigatório.`);
                ehValido = false;
            }
        });
        
        if (form.id === 'form-cadastro') {
            const senha = form.querySelector('#senha');
            const confirmarSenha = form.querySelector('#confirmar-senha');
            if (senha.value !== confirmarSenha.value) {
                mostrarErro(confirmarSenha, 'As senhas não coincidem.');
                ehValido = false;
            }
        }
        return ehValido;
    }

    // =================================
    // FUNÇÕES DE API
    // =================================
    const fetchAPI = async (endpoint, options = {}) => {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                ...options,
                headers: { 'Content-Type': 'application/json', ...options.headers },
                credentials: 'include'
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || 'Ocorreu um erro na requisição.');
            }
            return data;
        } catch (error) {
            console.error(`Erro na API (${endpoint}):`, error);
            throw error;
        }
    };

    async function realizarLogin(e) {
        e.preventDefault();
        if (!validarFormulario(formLogin)) return;

        const formData = new FormData(formLogin);
        const body = Object.fromEntries(formData);

        try {
            const data = await fetchAPI('/login', {
                method: 'POST',
                body: JSON.stringify(body)
            });
            currentUser = data;
            localStorage.setItem('currentUserFaculdadeNew', JSON.stringify(currentUser));
            navegarPara('home');
        } catch (error) {
            const generalError = formLogin.querySelector('.general-error');
            generalError.textContent = error.message;
            generalError.style.display = 'block';
        }
    }

    async function cadastrarUsuario(e) {
        e.preventDefault();
        if (!validarFormulario(formCadastro)) return;
        
        const formData = new FormData(formCadastro);
        const body = {
            nome: formData.get('nome'),
            sobrenome: formData.get('sobrenome'),
            email: formData.get('email'),
            senha: formData.get('senha'),
            endereco: {
                rua: formData.get('rua'),
                numero: formData.get('numero'),
                cep: formData.get('cep')
            }
        };

        try {
            await fetchAPI('/usuarios', {
                method: 'POST',
                body: JSON.stringify(body)
            });
            alert('Cadastro realizado com sucesso! Por favor, faça o login.');
            signInButton.click();
        } catch (error) {
            mostrarErro(formCadastro.querySelector('#email'), error.message);
        }
    }

    async function realizarMatricula(cursoId) {
        try {
            const data = await fetchAPI('/matriculas', {
                method: 'POST',
                body: JSON.stringify({ id_curso: cursoId })
            });
            alert(`Matrícula no curso ${data.curso.nome} realizada com sucesso!`);
            controlarModal('#modal-detalhes-curso', false);
        } catch (error) {
            alert(`Erro ao matricular: ${error.message}`);
             if (error.message.toLowerCase().includes('logado')) {
                fazerLogout();
            }
        }
    }

    async function deletarConta() {
        if (!currentUser) return;

        try {
            const resultado = await fetchAPI(`/deletar/${currentUser.id}`, {
                method: 'DELETE'
            });
            alert(resultado.mensagem);
            fazerLogout();
        } catch (error) {
            alert(`Erro ao excluir conta: ${error.message}`);
        }
    }

    async function carregarDadosHome() {
        if (!currentUser) {
            navegarPara('landing');
            return;
        };
        userNameDisplay.textContent = `Olá, ${currentUser.nome}!`;

        try {
            [todosCursos, todosPolos] = await Promise.all([
                fetchAPI('/lista_cursos'),
                fetchAPI('/list_polos')
            ]);
            renderizarCursos();
            renderizarPolos();
        } catch (error) {
            if (error.message.toLowerCase().includes('logado')) {
                fazerLogout();
            } else {
                cursosContainer.innerHTML = `<p>Erro ao carregar cursos.</p>`;
                polosContainer.innerHTML = `<p>Erro ao carregar polos.</p>`;
            }
        }
    }

    async function carregarDadosMinhaConta() {
        if (!currentUser) {
            navegarPara('landing');
            return;
        }
        perfilNome.textContent = `${currentUser.nome} ${currentUser.sobrenome}`;
        perfilEmail.textContent = currentUser.email;

        try {
            const matriculas = await fetchAPI('/matricula_usuario');
            renderizarMeusCursos(matriculas);
        } catch (error) {
            meusCursosContainer.innerHTML = `<p class="error-message" style="display:block;">Não foi possível carregar seus cursos.</p>`
        }
    }

    // =================================
    // FUNÇÕES DE RENDERIZAÇÃO
    // =================================
    function renderizarCursos() {
        const termoBusca = buscaCursoInput.value.toLowerCase();
        const areaFiltro = filtroAreaSelect.value;
        
        const cursosFiltrados = todosCursos.filter(curso => {
            const matchBusca = curso.nome.toLowerCase().includes(termoBusca);
            const matchArea = !areaFiltro || curso.area === areaFiltro;
            return matchBusca && matchArea;
        });

        cursosContainer.innerHTML = cursosFiltrados.map(curso => `
            <div class="card card-curso" data-curso-id="${curso.id}">
                <h3>${curso.nome}</h3>
                <p><strong>Área:</strong> ${curso.area}</p>
                <p><strong>Modalidade:</strong> ${curso.modalidade}</p>
            </div>
        `).join('') || '<p>Nenhum curso encontrado.</p>';
    }

    function renderizarPolos() {
        polosContainer.innerHTML = todosPolos.map(polo => `
            <div class="card">
                <h3>${polo.nome}</h3>
                <p>${polo.endereco.rua}, ${polo.endereco.numero}</p>
                <p>${polo.endereco.cidade} - ${polo.endereco.estado}</p>
            </div>
        `).join('') || '<p>Nenhum polo encontrado.</p>';
    }

    function renderizarDetalhesCurso(cursoId) {
        const curso = todosCursos.find(c => c.id === cursoId);
        if (!curso) return;

        document.getElementById('modal-curso-nome').textContent = curso.nome;
        
        const body = document.getElementById('modal-curso-body');
        body.innerHTML = `
            <p><strong>Carga Horária:</strong> ${curso.carga_horaria} horas</p>
            <p><strong>Modalidade:</strong> ${curso.modalidade}</p>
            <p><strong>Área:</strong> ${curso.area}</p>
            <h4>Polos Disponíveis</h4>
            <ul>
                ${curso.polos.map(p => `<li>${p.nome}</li>`).join('') || '<li>Curso 100% online</li>'}
            </ul>
        `;
        
        const footer = document.getElementById('modal-curso-footer');
        footer.innerHTML = `
            <button class="btn btn-secundario btn-fechar-modal" data-target-modal="#modal-detalhes-curso">Fechar</button>
            <button class="btn btn-primario" id="btn-matricular" data-curso-id="${curso.id}">Matricular-se</button>
        `;
    }

    function renderizarMeusCursos(matriculas) {
        if (!matriculas || matriculas.length === 0) {
            meusCursosContainer.innerHTML = '<p>Você ainda não se matriculou em nenhum curso.</p>';
            return;
        }

        meusCursosContainer.innerHTML = matriculas.map(matricula => {
            const data = new Date(matricula.data_matricula).toLocaleDateString('pt-BR');
            return `
            <div class="card">
                <h3>${matricula.curso.nome}</h3>
                <p><strong>Status:</strong> <span class="status-${matricula.status}">${matricula.status}</span></p>
                <p><strong>Data de Matrícula:</strong> ${data}</p>
            </div>
        `}).join('');
    }

    // =================================
    // FUNÇÕES DE MODAL E ESTADO
    // =================================
    function controlarModal(modalSeletor, abrir = true) {
        const modal = document.querySelector(modalSeletor);
        if (abrir) {
            modal.classList.add('ativo');
        } else {
            modal.classList.remove('ativo');
        }
    }

    async function fazerLogout() {
        try {
            await fetchAPI('/logout'); // Chama a rota de logout no backend
        } catch (error) {
            console.error("Erro ao fazer logout no backend (pode já ter expirado):", error.message);
        } finally {
            currentUser = null;
            localStorage.removeItem('currentUserFaculdadeNew');
            navegarPara('landing');
        }
    }

    // =================================
    // FUNÇÃO DE INICIALIZAÇÃO
    // =================================
    async function checarLoginPersistente() {
        try {
            const sessaoAtiva = await fetchAPI('/verificar-session');
            const usuarioSalvo = JSON.parse(localStorage.getItem('currentUserFaculdadeNew'));

            if (usuarioSalvo && sessaoAtiva.user_id === usuarioSalvo.id) {
                currentUser = usuarioSalvo;
                navegarPara('home');
            } else {
                fazerLogout();
            }
        } catch (error) {
            fazerLogout();
        }
    }

    // =================================
    // EVENT LISTENERS
    // =================================
    // --- Navegação ---
    document.getElementById('btn-landing-login').addEventListener('click', () => navegarPara('autenticacao'));
    document.getElementById('btn-landing-cadastro').addEventListener('click', () => {
        navegarPara('autenticacao');
        authWrapper.classList.add('right-panel-active');
    });
    document.getElementById('btn-hero-cadastro').addEventListener('click', () => {
        navegarPara('autenticacao');
        authWrapper.classList.add('right-panel-active');
    });
    document.getElementById('btn-minha-conta').addEventListener('click', () => navegarPara('minha-conta'));
    document.getElementById('btn-voltar-home').addEventListener('click', () => navegarPara('home'));

    // --- Autenticação ---
    signUpButton.addEventListener('click', () => authWrapper.classList.add('right-panel-active'));
    signInButton.addEventListener('click', () => authWrapper.classList.remove('right-panel-active'));
    formLogin.addEventListener('submit', realizarLogin);
    formCadastro.addEventListener('submit', cadastrarUsuario);
    document.getElementById('btn-logout').addEventListener('click', fazerLogout);

    // --- Home Page ---
    buscaCursoInput.addEventListener('input', renderizarCursos);
    filtroAreaSelect.addEventListener('change', renderizarCursos);
    cursosContainer.addEventListener('click', (e) => {
        const card = e.target.closest('.card-curso');
        if (card) {
            const cursoId = parseInt(card.dataset.cursoId);
            renderizarDetalhesCurso(cursoId);
            controlarModal('#modal-detalhes-curso', true);
        }
    });
    
    // --- Minha Conta ---
    document.getElementById('btn-excluir-conta').addEventListener('click', () => {
        controlarModal('#modal-confirmacao-exclusao', true);
    });
    document.getElementById('btn-confirmar-exclusao').addEventListener('click', () => {
        deletarConta();
        controlarModal('#modal-confirmacao-exclusao', false);
    });
    document.getElementById('btn-cancelar-exclusao').addEventListener('click', () => {
        controlarModal('#modal-confirmacao-exclusao', false);
    });

    // --- Modais ---
    document.addEventListener('click', (e) => {
        if (e.target.matches('.btn-fechar-modal') || e.target.matches('.modal')) {
            const modalId = e.target.dataset.targetModal || (e.target.closest('.modal') ? `#${e.target.closest('.modal').id}`: null);
            if(modalId) controlarModal(modalId, false);
        }
        if (e.target.id === 'btn-matricular') {
            const cursoId = parseInt(e.target.dataset.cursoId);
            realizarMatricula(cursoId);
        }
    });
    
    // =================================
    // INICIALIZAÇÃO DA APLICAÇÃO
    // =================================
    checarLoginPersistente();
});

