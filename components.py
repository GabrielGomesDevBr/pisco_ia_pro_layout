# components.py
"""
Componentes da interface do usuário
Contém funções para renderizar diferentes partes da interface
"""

import streamlit as st
from constants import REPORT_TYPES, TONE_DESCRIPTIONS, ABORDAGENS_TERAPEUTICAS, GENEROS, COMPANY_INFO

def render_login_page():
    """Renderiza a página de login com elementos visuais aprimorados"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="header">
            <h1>PsicoIA Pro</h1>
            <p>A evolução na elaboração de relatórios psicológicos</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Precisão Técnica</h3>
                <p>Relatórios com alto padrão profissional e rigor técnico</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Agilidade</h3>
                <p>Economia de até 70% do tempo na elaboração de documentos</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3>Segurança</h3>
                <p>Dados protegidos com os mais altos padrões de segurança</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("""
        <div class="login-header">
            <h2>Acesso ao Sistema</h2>
            <p>Entre com suas credenciais</p>
        </div>
        """, unsafe_allow_html=True)
        
        username = st.text_input("Email ou Usuário")
        password = st.text_input("Senha", type="password")
        
        if st.button("Entrar", key="login_button"):
            return username, password
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        return None, None

def render_sidebar():
    """Renderiza a barra lateral com informações da empresa"""
    st.sidebar.markdown("""
    <div class="sidebar-header">
        <h2>🧠 PsicoIA Pro</h2>
        <p>{}</p>
    </div>
    """.format(COMPANY_INFO['slogan']), unsafe_allow_html=True)
    
    st.sidebar.markdown("### 📱 Contatos")
    st.sidebar.markdown(f"""
    - 🌐 [{COMPANY_INFO['website']}]({COMPANY_INFO['website']})
    - 📱 WhatsApp: {COMPANY_INFO['whatsapp']}
    - 📧 [{COMPANY_INFO['email']}](mailto:{COMPANY_INFO['email']})
    """)
    
    menu_selection = st.sidebar.radio(
        "Menu Principal",
        ["📝 Gerar Relatório", "⚙️ Configurações", "ℹ️ Sobre"]
    )
    
    if st.sidebar.button("📤 Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
        
    return menu_selection

def render_patient_form():
    """Renderiza o formulário de dados do paciente"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome = st.text_input("Nome completo do paciente")
        idade = st.number_input("Idade", min_value=0, max_value=120)
        genero = st.selectbox("Gênero", GENEROS)
        
    with col2:
        data_avaliacao = st.date_input("Data da avaliação")
        abordagem = st.selectbox(
            "Abordagem terapêutica",
            ABORDAGENS_TERAPEUTICAS
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return {
        'nome': nome,
        'idade': idade,
        'genero': genero,
        'data_avaliacao': data_avaliacao,
        'abordagem_terapeutica': abordagem
    }

def render_report_config():
    """Renderiza a configuração do relatório"""
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox(
            "Tipo de Relatório",
            list(REPORT_TYPES.keys())
        )
    
    with col2:
        tone = st.selectbox(
            "Tom do Relatório",
            list(TONE_DESCRIPTIONS.keys())
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    return report_type, tone

def render_about_page():
    """Renderiza a página Sobre"""
    st.markdown("""
    <div class="header">
        <h1>Sobre o PsicoIA Pro</h1>
        <p>Tecnologia e Psicologia em harmonia</p>
    </div>
    
    <div class="card">
        <h3>Nossa Missão</h3>
        <p>Revolucionar a forma como relatórios psicológicos são criados, 
        combinando expertise profissional com inteligência artificial de ponta.</p>
    </div>
    
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>17 Tipos de Relatórios</h3>
            <p>Modelos especializados para cada necessidade</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>IA Avançada</h3>
            <p>Tecnologia de ponta para resultados precisos</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <h3>Personalização</h3>
            <p>Adaptável ao seu estilo profissional</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
