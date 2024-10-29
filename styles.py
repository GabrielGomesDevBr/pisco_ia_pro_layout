# styles.py
"""
Arquivo de estilos da aplicação
Contém todas as definições de CSS e estilos visuais
"""

def load_css():
    return """
    <style>
    /* Variáveis do tema */
    :root {
        --primary-color: #4A90E2;
        --secondary-color: #2ECC71;
        --accent-color: #FF6B6B;
        --background-color: #F8F9FA;
        --text-color: #2C3E50;
    }

    /* Reset e estilos globais */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Inter', sans-serif;
        color: var(--text-color);
        background-color: var(--background-color);
    }

    /* Container principal */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    /* Cabeçalhos */
    .header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }

    .header h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    /* Cards */
    .card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
    }

    /* Botões */
    .stButton > button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    /* Campos de entrada */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #E0E0E0;
        padding: 1rem;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
    }

    /* Seleções */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid #E0E0E0;
    }

    /* Abas */
    .stTabs {
        background: white;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: #f0f2f5;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: var(--primary-color);
        color: white;
    }

    /* Login Form */
    .login-container {
        max-width: 400px;
        margin: 4rem auto;
        padding: 2rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .login-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .login-header img {
        width: 120px;
        margin-bottom: 1rem;
    }

    /* Features Grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        padding: 2rem 0;
    }

    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: var(--primary-color);
    }

    /* Sidebar personalizada */
    .sidebar {
        background: white;
        padding: 2rem;
        border-right: 1px solid #E0E0E0;
    }

    .sidebar-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .sidebar-menu {
        list-style: none;
        padding: 0;
    }

    .sidebar-menu-item {
        padding: 1rem;
        margin-bottom: 0.5rem;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    .sidebar-menu-item:hover {
        background: var(--background-color);
    }

    /* Alertas e mensagens */
    .success-message {
        background: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .error-message {
        background: #F8D7DA;
        color: #721C24;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    /* Responsividade */
    @media (max-width: 768px) {
        .header {
            padding: 1.5rem;
        }

        .header h1 {
            font-size: 2rem;
        }

        .features-grid {
            grid-template-columns: 1fr;
        }

        .login-container {
            margin: 2rem;
        }
    }
    </style>
    """
