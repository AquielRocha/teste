import streamlit as st
from PIL import Image

CR7_IMAGE_FILE = "images.jpeg"

def aplicar_estilos(tema_escolhido: str):
    """
    Injeta CSS para tema claro ou escuro e algumas animações.
    """
    # Defina estilos para tema claro
    css_claro = """
    <style>
    /* Fundo gradiente claro */
    .stApp {
        background: linear-gradient(to bottom right, #ffffff, #0000FF);
        transition: background 0.5s ease;
    }

    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #B22222; /* FireBrick */
        transition: color 0.5s ease;
    }

    /* Botões */
    .stButton>button {
        background-color: #DC143C; /* Crimson */
        color: white;
        border-radius: 8px;
        font-size: 16px;
        height: 3em;
        width: 15em;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #A52A2A; /* Brown, para hover */
    }

    /* Inputs */
    input {
        font-size: 1.1rem !important;
        color: #00008B; /* Navy */
        transition: color 0.5s ease;
    }

    /* Imagens "pulsando" no hover */
    img:hover {
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.03); }
      100% { transform: scale(1); }
    }
    </style>
    """

    # Defina estilos para tema escuro
    css_escuro = """
    <style>
    /* Fundo gradiente escuro */
    .stApp {
        background: linear-gradient(to bottom right, #2f2f2f, #696969);
        transition: background 0.5s ease;
    }

    /* Títulos com cor mais clara */
    h1, h2, h3, h4, h5, h6 {
        color: #FFA07A; /* Light Salmon */
        transition: color 0.5s ease;
    }

    /* Botões */
    .stButton>button {
        background-color: #FF6347; /* Tomato */
        color: white;
        border-radius: 8px;
        font-size: 16px;
        height: 3em;
        width: 15em;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #CD5C5C; /* IndianRed, para hover */
    }

    /* Inputs com texto amarelado */
    input {
        font-size: 1.1rem !important;
        color: #FFE4B5; /* Moccasin */
        transition: color 0.5s ease;
    }

    /* Imagens "pulsando" no hover */
    img:hover {
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.03); }
      100% { transform: scale(1); }
    }
    </style>
    """

    # Injeta o CSS de acordo com o tema
    if tema_escolhido == "Claro":
        st.markdown(css_claro, unsafe_allow_html=True)
    else:
        st.markdown(css_escuro, unsafe_allow_html=True)

def exibir_cartao_frente(dados, tema):
    st.markdown("<h2 style='margin-top:0;'>Frente do Cartão</h2>", unsafe_allow_html=True)

    try:
        # Carrega a imagem local
        img_cr7 = Image.open(CR7_IMAGE_FILE)
        st.image(img_cr7, width=250, caption="CR7 - Frente")
    except Exception as e:
        st.warning("Não foi possível carregar a imagem local 'images.jpeg'.")

    # Se quiser ajustar cores do texto, podemos usar HTML inline
    cor_texto = "#4B0082" if tema == "Claro" else "#FFE4B5"
    st.markdown(f"""
    <div style='font-size:18px; color:{cor_texto}; margin-top:10px;'>
        <p><strong>Nome do Titular:</strong> {dados['titular']}</p>
        <p><strong>Número do Cartão:</strong> {dados['numero']}</p>
        <p><strong>Validade:</strong> {dados['validade']}</p>
    </div>
    """, unsafe_allow_html=True)

def exibir_cartao_verso(dados, tema):
    st.markdown("<h2 style='margin-top:0;'>Verso do Cartão (CR7 Theme)</h2>", unsafe_allow_html=True)

    try:
        # Reutiliza a mesma imagem
        img_cr7 = Image.open(CR7_IMAGE_FILE)
        st.image(img_cr7, width=250, caption="CR7 - Verso")
    except Exception as e:
        st.warning("Não foi possível carregar a imagem local 'images.jpeg'.")

    cor_texto = "#4B0082" if tema == "Claro" else "#FFE4B5"
    st.markdown(f"""
    <div style='font-size:18px; color:{cor_texto}; margin-top:10px;'>
        <p><strong>CVV (Código de Segurança):</strong> {dados['cvv']}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Adiciona um selectbox para escolher o tema
    tema_escolhido = st.sidebar.selectbox("Selecione o tema", ["Claro", "Escuro"])

    # Aplica o CSS personalizado baseado no tema
    aplicar_estilos(tema_escolhido)

    # Título e descrição
    st.title("Quer ver qual jogador você é? Coloque os dados do seu cartão aqui!")
    st.write("Preencha os campos abaixo e descubra que você sempre será o CR7! 🏆⚽")

    # Campos de entrada
    titular = st.text_input("Nome do Titular (Ex: Isaac Pereira, Rudson )")
    numero = st.text_input("Número do Cartão (Ex: 1234 5678 9012 3456)")
    validade = st.text_input("Data de Validade (Ex: 12/28)")
    cvv = st.text_input("CVV (Ex: 123)", type="password")

    # Dicionário com dados do cartão
    dados_cartao = {
        "titular": titular,
        "numero": numero,
        "validade": validade,
        "cvv": cvv,
    }

    # Botão para revelar que é CR7
    if st.button("Descobrir qual jogador eu sou!"):
        st.success("Parabéns, você é o CR7! 🏆")
        st.write("---")
        exibir_cartao_frente(dados_cartao, tema_escolhido)
        st.write("---")
        exibir_cartao_verso(dados_cartao, tema_escolhido)

if __name__ == "__main__":
    main()
