# main.py
"""
Arquivo principal da aplicação PsicoIA Pro
Integra todos os componentes e gerencia o fluxo principal do sistema
"""

import streamlit as st
import logging
from langchain_openai import ChatOpenAI
import os
from datetime import datetime

# Importação dos módulos personalizados
from constants import (
    REPORT_TYPES, TONE_DESCRIPTIONS, ABORDAGENS_TERAPEUTICAS,
    GENEROS, THEME_COLORS, COMPANY_INFO
)
from styles import load_css
from utils import (
    check_login, convert_markdown_to_docx, create_prompt,
    format_date, generate_filename, validate_patient_data
)
from components import (
    render_login_page, render_sidebar, render_patient_form,
    render_report_config, render_about_page
)

# Configuração inicial do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração inicial da página
st.set_page_config(
    page_title="PsicoIA Pro - Relatórios Psicológicos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carrega os estilos CSS personalizados
st.markdown(load_css(), unsafe_allow_html=True)

def initialize_session_state():
    """Inicializa as variáveis de estado da sessão"""
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'login'
    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = None

def handle_login(username, password):
    """Gerencia o processo de login"""
    success, user_name = check_login(username, password)
    if success:
        st.session_state['logged_in'] = True
        st.session_state['user_data'] = {'name': user_name, 'username': username}
        st.success(f"Bem-vindo(a), {user_name}!")
        st.rerun()
    else:
        st.error("Email ou senha incorretos!")

def generate_report(patient_data, report_type, tone, specific_fields):
    """Gera o relatório usando o modelo de IA"""
    try:
        # Configuração do modelo de IA
        api_key = st.secrets["OPENAI_API_KEY"]
        os.environ['OPENAI_API_KEY'] = api_key
        
        model = ChatOpenAI(
            model_name='gpt-3.5-turbo',
            temperature=0.7
        )
        
        # Criação do prompt
        prompt = create_prompt(report_type, tone, patient_data, specific_fields)
        
        # Geração do relatório
        with st.spinner("Gerando relatório..."):
            response = model.invoke(prompt)
            docx_file = convert_markdown_to_docx(response.content)
            
            return response.content, docx_file
            
    except Exception as e:
        logger.error(f"Erro ao gerar relatório: {str(e)}")
        raise

def render_report_generation_page():
    """Renderiza a página de geração de relatórios"""
    st.markdown("""
    <div class="header">
        <h1>Gerador de Relatórios Psicológicos</h1>
        <p>Crie relatórios profissionais com facilidade e precisão</p>
    </div>
    """, unsafe_allow_html=True)

    # Configuração do relatório
    report_type, tone = render_report_config()

    # Abas para organizar o conteúdo
    tab1, tab2, tab3 = st.tabs([
        "📋 Dados do Paciente",
        "📝 Informações Específicas",
        "✨ Gerar Relatório"
    ])

    with tab1:
        patient_data = render_patient_form()

    with tab2:
        specific_fields = get_specific_fields(REPORT_TYPES[report_type])

    with tab3:
        if st.button("Gerar Relatório", key="generate_report"):
            try:
                # Validação dos dados
                valid, error_msg = validate_patient_data(patient_data)
                if not valid:
                    st.error(error_msg)
                    return

                # Geração do relatório
                report_content, docx_file = generate_report(
                    patient_data, report_type, tone, specific_fields
                )

                # Exibição do resultado
                st.success("Relatório gerado com sucesso!")
                st.markdown(report_content)

                # Botão de download
                filename = generate_filename(REPORT_TYPES[report_type])
                st.download_button(
                    "📥 Download Relatório (DOCX)",
                    docx_file,
                    filename,
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

            except Exception as e:
                st.error(f"Erro ao gerar relatório: {str(e)}")
                logger.error(f"Erro ao gerar relatório: {str(e)}")

def render_settings_page():
    """Renderiza a página de configurações"""
    st.markdown("""
    <div class="header">
        <h1>Configurações</h1>
        <p>Personalize sua experiência</p>
    </div>
    
    <div class="card">
        <h3>🚧 Em Desenvolvimento</h3>
        <p>Novas funcionalidades em breve!</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Função principal que controla o fluxo da aplicação"""
    initialize_session_state()

    # Verifica o estado do login
    if not st.session_state['logged_in']:
        username, password = render_login_page()
        if username and password:
            handle_login(username, password)
        return

    # Menu lateral
    menu_selection = render_sidebar()

    # Navegação principal
    if menu_selection == "📝 Gerar Relatório":
        render_report_generation_page()
    elif menu_selection == "⚙️ Configurações":
        render_settings_page()
    elif menu_selection == "ℹ️ Sobre":
        render_about_page()

def get_specific_fields(report_type):
    """
    Obtém os campos específicos para cada tipo de relatório
    
    Args:
        report_type (str): Tipo do relatório
    
    Returns:
        dict: Campos específicos do relatório
    """
    fields = {}
    
    if report_type == "devolutiva":
        fields.update({
            "resultados_avaliacao": st.text_area("Resultados da Avaliação:", height=150),
            "interpretacao": st.text_area("Interpretação dos Resultados:", height=150),
            "recomendacoes": st.text_area("Recomendações:", height=150),
            "recursos_utilizados": st.text_area("Recursos e Testes Utilizados:", height=100)
        })
    
    elif report_type == "evolucao":
        fields.update({
            "periodo_avaliado": st.text_input("Período Avaliado:"),
            "objetivos_terapeuticos": st.text_area("Objetivos Terapêuticos:", height=150),
            "progresso": st.text_area("Progresso Observado:", height=150),
            "desafios": st.text_area("Desafios Encontrados:", height=150),
            "estrategias": st.text_area("Estratégias Utilizadas:", height=150)
        })
    
    elif report_type == "anamnese":
        fields.update({
            "queixa_principal": st.text_area("Queixa Principal:", height=150),
            "historico_sintomas": st.text_area("Histórico dos Sintomas:", height=150),
            "historico_familiar": st.text_area("Histórico Familiar:", height=150),
            "historico_medico": st.text_area("Histórico Médico:", height=150),
            "desenvolvimento": st.text_area("História do Desenvolvimento:", height=150)
        })
    
    elif report_type == "avaliacao_inicial":
        fields.update({
            "demanda": st.text_area("Demanda Inicial:", height=150),
            "sintomas_atuais": st.text_area("Sintomas Atuais:", height=150),
            "historico_tratamentos": st.text_area("Histórico de Tratamentos:", height=150),
            "suporte_social": st.text_area("Rede de Suporte Social:", height=150)
        })
    
    elif report_type == "alta":
        fields.update({
            "motivo_alta": st.text_area("Motivo da Alta:", height=150),
            "objetivos_alcancados": st.text_area("Objetivos Alcançados:", height=150),
            "progresso_final": st.text_area("Progresso Final:", height=150),
            "recomendacoes_futuras": st.text_area("Recomendações Futuras:", height=150)
        })
    
    elif report_type == "personalidade":
        fields.update({
            "instrumentos_utilizados": st.text_area("Instrumentos de Avaliação Utilizados:", height=150),
            "resultados_personalidade": st.text_area("Resultados da Avaliação de Personalidade:", height=150),
            "perfil_psicologico": st.text_area("Perfil Psicológico:", height=150),
            "implicacoes_praticas": st.text_area("Implicações Práticas:", height=150)
        })
    
    elif report_type == "neuropsicologica":
        fields.update({
            "funcoes_avaliadas": st.text_area("Funções Cognitivas Avaliadas:", height=150),
            "instrumentos_neuropsicologicos": st.text_area("Instrumentos Neuropsicológicos Utilizados:", height=150),
            "resultados_cognitivos": st.text_area("Resultados por Função Cognitiva:", height=150),
            "conclusao_diagnostica": st.text_area("Conclusão Diagnóstica:", height=150),
            "recomendacoes_reabilitacao": st.text_area("Recomendações para Reabilitação:", height=150)
        })
    
    elif report_type == "acompanhamento":
        fields.update({
            "periodo_acompanhamento": st.text_input("Período de Acompanhamento:"),
            "objetivos_alcancados": st.text_area("Objetivos Alcançados:", height=150),
            "evolucao_observada": st.text_area("Evolução Observada:", height=150),
            "aspectos_relevantes": st.text_area("Aspectos Relevantes:", height=150),
            "proximos_passos": st.text_area("Próximos Passos:", height=150)
        })
    
    elif report_type == "intervencao":
        fields.update({
            "comportamentos_alvo": st.text_area("Comportamentos-Alvo:", height=150),
            "estrategias_intervencao": st.text_area("Estratégias de Intervenção:", height=150),
            "resultados_obtidos": st.text_area("Resultados Obtidos:", height=150),
            "ajustes_necessarios": st.text_area("Ajustes Necessários:", height=150)
        })
    
    elif report_type == "diagnostico":
        fields.update({
            "sintomas_apresentados": st.text_area("Sintomas Apresentados:", height=150),
            "criterios_diagnosticos": st.text_area("Critérios Diagnósticos:", height=150),
            "diagnostico_diferencial": st.text_area("Diagnóstico Diferencial:", height=150),
            "conclusao_diagnostica": st.text_area("Conclusão Diagnóstica:", height=150),
            "plano_tratamento": st.text_area("Plano de Tratamento:", height=150)
        })
    
    elif report_type == "emocional":
        fields.update({
            "estado_emocional": st.text_area("Estado Emocional Atual:", height=150),
            "fatores_estresse": st.text_area("Fatores de Estresse:", height=150),
            "recursos_enfrentamento": st.text_area("Recursos de Enfrentamento:", height=150),
            "suporte_social": st.text_area("Suporte Social:", height=150),
            "recomendacoes": st.text_area("Recomendações:", height=150)
        })
    
    elif report_type == "escolar":
        fields.update({
            "desempenho_academico": st.text_area("Desempenho Acadêmico:", height=150),
            "comportamento_escolar": st.text_area("Comportamento em Ambiente Escolar:", height=150),
            "relacoes_interpessoais": st.text_area("Relações Interpessoais:", height=150),
            "necessidades_especificas": st.text_area("Necessidades Específicas:", height=150),
            "recomendacoes_escola": st.text_area("Recomendações para a Escola:", height=150)
        })
    
    elif report_type == "infantil":
        fields.update({
            "desenvolvimento_atual": st.text_area("Desenvolvimento Atual:", height=150),
            "comportamento_observado": st.text_area("Comportamento Observado:", height=150),
            "interacao_social": st.text_area("Interação Social:", height=150),
            "aspectos_familiares": st.text_area("Aspectos Familiares:", height=150),
            "recomendacoes_pais": st.text_area("Recomendações aos Pais:", height=150)
        })
    
    elif report_type == "profissional":
        fields.update({
            "interesses_profissionais": st.text_area("Interesses Profissionais:", height=150),
            "habilidades_identificadas": st.text_area("Habilidades Identificadas:", height=150),
            "valores_trabalho": st.text_area("Valores Relacionados ao Trabalho:", height=150),
            "areas_recomendadas": st.text_area("Áreas Recomendadas:", height=150),
            "plano_desenvolvimento": st.text_area("Plano de Desenvolvimento:", height=150)
        })
    
    elif report_type == "familiar":
        fields.update({
            "dinamica_familiar": st.text_area("Dinâmica Familiar:", height=150),
            "padroes_relacionamento": st.text_area("Padrões de Relacionamento:", height=150),
            "conflitos_identificados": st.text_area("Conflitos Identificados:", height=150),
            "recursos_familiares": st.text_area("Recursos Familiares:", height=150),
            "recomendacoes_familia": st.text_area("Recomendações para a Família:", height=150)
        })
    
    elif report_type == "sessao":
        fields.update({
            "temas_abordados": st.text_area("Temas Abordados:", height=150),
            "tecnicas_utilizadas": st.text_area("Técnicas Utilizadas:", height=150),
            "respostas_paciente": st.text_area("Respostas do Paciente:", height=150),
            "insights_obtidos": st.text_area("Insights Obtidos:", height=150),
            "planejamento_proxima": st.text_area("Planejamento para Próxima Sessão:", height=150)
        })
    
    elif report_type == "feedback":
        fields.update({
            "progresso_observado": st.text_area("Progresso Observado:", height=150),
            "pontos_positivos": st.text_area("Pontos Positivos:", height=150),
            "areas_desenvolvimento": st.text_area("Áreas para Desenvolvimento:", height=150),
            "orientacoes_praticas": st.text_area("Orientações Práticas:", height=150),
            "proximos_objetivos": st.text_area("Próximos Objetivos:", height=150)
        })
    
    return fields

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Erro na aplicação: {str(e)}")
        st.error("Ocorreu um erro inesperado. Por favor, tente novamente.")
