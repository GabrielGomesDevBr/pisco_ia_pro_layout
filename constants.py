# constants.py
"""
Arquivo de constantes e configurações do sistema
Contém todas as definições estáticas usadas na aplicação
"""

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
    'tester10': {'password': 'Psy10#Ts', 'name': 'Tester 10'},
    'tester11': {'password': 'T11st@Psy', 'name': 'Tester 11'},
    'tester12': {'password': 'Psy12#Tst', 'name': 'Tester 12'},
    'tester13': {'password': 'T13st@Psy', 'name': 'Tester 13'},
    'tester14': {'password': 'Psy14#Tst', 'name': 'Tester 14'},
    'tester15': {'password': 'T15st@Psy', 'name': 'Tester 15'},
    'tester16': {'password': 'Psy16#Tst', 'name': 'Tester 16'},
    'tester17': {'password': 'T17st@Psy', 'name': 'Tester 17'},
    'tester18': {'password': 'Psy18#Tst', 'name': 'Tester 18'},
    'tester19': {'password': 'T19st@Psy', 'name': 'Tester 19'},
    'tester20': {'password': 'Psy20#Tst', 'name': 'Tester 20'},
    'tester21': {'password': 'T21st@Psy', 'name': 'Tester 21'},
    'tester22': {'password': 'Psy22#Tst', 'name': 'Tester 22'},
    'tester23': {'password': 'T23st@Psy', 'name': 'Tester 23'},
    'tester24': {'password': 'Psy24#Tst', 'name': 'Tester 24'},
    'tester25': {'password': 'T25st@Psy', 'name': 'Tester 25'},
    'tester26': {'password': 'Psy26#Tst', 'name': 'Tester 26'},
    'tester27': {'password': 'T27st@Psy', 'name': 'Tester 27'},
    'tester28': {'password': 'Psy28#Tst', 'name': 'Tester 28'},
    'tester29': {'password': 'T29st@Psy', 'name': 'Tester 29'},
    'tester30': {'password': 'Psy30#Tst', 'name': 'Tester 30'},
    'tester31': {'password': 'T31st@Psy', 'name': 'Tester 31'},
    'tester32': {'password': 'Psy32#Tst', 'name': 'Tester 32'},
    'tester33': {'password': 'T33st@Psy', 'name': 'Tester 33'},
    'tester34': {'password': 'Psy34#Tst', 'name': 'Tester 34'},
    'tester35': {'password': 'T35st@Psy', 'name': 'Tester 35'},
    'tester36': {'password': 'Psy36#Tst', 'name': 'Tester 36'},
    'tester37': {'password': 'T37st@Psy', 'name': 'Tester 37'},
    'tester38': {'password': 'Psy38#Tst', 'name': 'Tester 38'},
    'tester39': {'password': 'T39st@Psy', 'name': 'Tester 39'},
    'tester40': {'password': 'Psy40#Tst', 'name': 'Tester 40'},
    'tester41': {'password': 'T41st@Psy', 'name': 'Tester 41'},
    'tester42': {'password': 'Psy42#Tst', 'name': 'Tester 42'},
    'tester43': {'password': 'T43st@Psy', 'name': 'Tester 43'},
    'tester44': {'password': 'Psy44#Tst', 'name': 'Tester 44'},
    'tester45': {'password': 'T45st@Psy', 'name': 'Tester 45'},
    'tester46': {'password': 'Psy46#Tst', 'name': 'Tester 46'},
    'tester47': {'password': 'T47st@Psy', 'name': 'Tester 47'},
    'tester48': {'password': 'Psy48#Tst', 'name': 'Tester 48'},
    'tester49': {'password': 'T49st@Psy', 'name': 'Tester 49'},
    'tester50': {'password': 'Psy50#Tst', 'name': 'Tester 50'}
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
