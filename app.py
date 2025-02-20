import streamlit as st
from PIL import Image

# Carregamos a imagem local, supondo que esteja na mesma pasta do app.py
CR7_IMAGE_FILE = "images.jpeg"

def aplicar_estilos():
    """
    Injeta um CSS para deixar o fundo gradiente e alguns elementos coloridos.
    """
    st.markdown(
        """
        <style>
        /* Deixa o fundo da aplicação em um gradiente suave */
        .stApp {
            background: linear-gradient(to bottom right, #ffffff, #f2f2f2);
        }

        /* Muda a cor dos títulos */
        h1, h2, h3, h4, h5, h6 {
            color: #B22222; /* FireBrick */
        }

        /* Botões com cor de fundo e texto branco */
        .stButton>button {
            background-color: #DC143C; /* Crimson */
            color: white;
            border-radius: 8px;
            font-size: 16px;
            height: 3em;
            width: 15em;
        }

        /* Alguns ajustes de fonte nos inputs */
        input {
            font-size: 1.1rem !important;
            color: #00008B; /* Navy */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def exibir_cartao_frente(dados):
    st.markdown("<h2 style='color:#2F4F4F;'>Frente do Cartão </h2>", unsafe_allow_html=True)

    try:
        # Carrega a imagem local
        img_cr7 = Image.open(CR7_IMAGE_FILE)
        st.image(img_cr7, width=250, caption="CR7 ")
    except Exception as e:
        st.warning("Não foi possível carregar a imagem local 'images.jpeg'.")

    st.markdown(f"""
    <div style='font-size:18px; color:#4B0082; margin-top:10px;'>
        <p><strong>Nome do Titular:</strong> {dados['titular']}</p>
        <p><strong>Número do Cartão:</strong> {dados['numero']}</p>
        <p><strong>Validade:</strong> {dados['validade']}</p>
    </div>
    """, unsafe_allow_html=True)

def exibir_cartao_verso(dados):
    st.markdown("<h2 style='color:#2F4F4F;'>Verso do Cartão (CR7 Theme)</h2>", unsafe_allow_html=True)

    try:
        # Podemos usar a mesma imagem ou outra
        img_cr7 = Image.open(CR7_IMAGE_FILE)
        st.image(img_cr7, width=250, caption="CR7 - Verso")
    except Exception as e:
        st.warning("Não foi possível carregar a imagem local 'images.jpeg'.")

    st.markdown(f"""
    <div style='font-size:18px; color:#4B0082; margin-top:10px;'>
        <p><strong>CVV (Código de Segurança):</strong> {dados['cvv']}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Aplica os estilos/CSS personalizados
    aplicar_estilos()

    st.title("Quer ver qual jogador você é? Coloque os dados do seu cartão aqui!")
    st.write("Preencha os campos abaixo e descubra que você sempre será o CR7! 🏆⚽")

    # Campos de entrada
    titular = st.text_input("Nome do Titular (Ex: Bruno Souza)")
    numero = st.text_input("Número do Cartão (Ex: 1234 5678 9012 3456)")
    validade = st.text_input("Data de Validade (Ex: 12/28)")
    cvv = st.text_input("CVV (Ex: 123)", type="password")  # Oculta o CVV no input

    # Dicionário com dados do cartão
    dados_cartao = {
        "titular": titular,
        "numero": numero,
        "validade": validade,
        "cvv": cvv,
    }

    # Botão de ação
    if st.button("Descobrir qual jogador eu sou!"):
        st.success("Parabéns, você é o CR7! 🏆")
        st.write("---")
        exibir_cartao_frente(dados_cartao)
        st.write("---")
        exibir_cartao_verso(dados_cartao)

if __name__ == "__main__":
    main()
