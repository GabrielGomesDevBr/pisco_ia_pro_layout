# constants.py
"""
Arquivo de constantes e configurações do sistema
Contém todas as definições estáticas usadas na aplicação
"""

# Banco de dados de usuários (simulado)
USERS_DB = {
    'gabriel@aperdata.com': {'password': 'gabriel123', 'name': 'Gabriel'},
    'tester01': {'password': 'Tst1@Psy', 'name': 'Tester 01'},
    'tester02': {'password': 'Psy2#Tst', 'name': 'Tester 02'},
    'tester03': {'password': 'T3st@Psy', 'name': 'Tester 03'},
    'tester04': {'password': 'Psy4#Tst', 'name': 'Tester 04'},
    'tester05': {'password': 'T5st@Psy', 'name': 'Tester 05'},
    'tester06': {'password': 'Psy6#Tst', 'name': 'Tester 06'},
    'tester07': {'password': 'T7st@Psy', 'name': 'Tester 07'},
    'tester08': {'password': 'Psy8#Tst', 'name': 'Tester 08'},
    'tester09': {'password': 'T9st@Psy', 'name': 'Tester 09'},
    'tester10': {'password': 'Psy10#Ts', 'name': 'Tester 10'}
}

# Tipos de relatórios disponíveis
REPORT_TYPES = {
    "Relatório de Devolutiva": "devolutiva",
    "Relatório de Evolução": "evolucao",
    "Relatório de Anamnese": "anamnese",
    "Relatório de Avaliação Psicológica Inicial": "avaliacao_inicial",
    "Relatório de Alta Terapêutica": "alta",
    "Relatório de Avaliação de Personalidade": "personalidade",
    "Relatório de Avaliação Neuropsicológica": "neuropsicologica",
    "Relatório de Acompanhamento Terapêutico": "acompanhamento",
    "Relatório de Intervenção Comportamental": "intervencao",
    "Relatório de Diagnóstico Psicológico": "diagnostico",
    "Relatório de Avaliação Emocional": "emocional",
    "Relatório para Escolas": "escolar",
    "Relatório de Avaliação Infantil": "infantil",
    "Relatório de Avaliação para Orientação Profissional": "profissional",
    "Relatório de Avaliação Familiar": "familiar",
    "Relatório de Sessão Terapêutica": "sessao",
    "Relatório de Feedback para o Paciente e Família": "feedback"
}

# Descrições dos tons de relatório
TONE_DESCRIPTIONS = {
    "Tom Formal e Técnico": "Use linguagem técnica e profissional, priorizando termos científicos e mantendo um tom objetivo e formal.",
    "Tom Acessível e Didático": "Use linguagem clara e acessível, explicando conceitos técnicos de forma didática e compreensível.",
    "Tom Colaborativo e Empático": "Use linguagem acolhedora e empática, mantendo o profissionalismo mas priorizando a conexão humana."
}

# Abordagens terapêuticas disponíveis
ABORDAGENS_TERAPEUTICAS = [
    'Terapia Cognitivo-Comportamental',
    'Psicanálise',
    'Terapia Humanista',
    'Terapia Sistêmica',
    'Terapia Integrativa',
    'Terapia ABA',
    'Gestalt-terapia',
    'Terapia Analítica',
    'Terapia Centrada na Pessoa',
    'Terapia Comportamental'
]

# Opções de gênero
GENEROS = [
    'Masculino',
    'Feminino',
    'Não-binário',
    'Prefiro não especificar'
]

# Cores do tema
THEME_COLORS = {
    'primary': '#4A90E2',
    'secondary': '#2ECC71',
    'accent': '#FF6B6B',
    'background': '#F8F9FA',
    'text': '#2C3E50'
}

# Configurações da empresa
COMPANY_INFO = {
    'name': 'AperData Solutions',
    'website': 'https://aperdata.com',
    'whatsapp': '11 98854-3437',
    'email': 'gabriel@aperdata.com',
    'slogan': 'Inovação em Psicologia'
}
