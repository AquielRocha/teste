import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# URL de uma imagem do Cristiano Ronaldo
CR7_IMAGE_URL = "https://raw.githubusercontent.com/leugimkm/Images/main/cr7.jpg"

def carregar_imagem(url):
    """
    Tenta carregar a imagem a partir da URL.
    Se falhar, retorna None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except Exception:
        return None

def exibir_cartao_frente(dados):
    st.markdown("## Frente do Cartão (CR7 Theme)")

    # Tenta carregar imagem online do CR7
    img_cr7 = carregar_imagem(CR7_IMAGE_URL)
    if img_cr7:
        st.image(img_cr7, width=250, caption="CR7 - Frente")
    else:
        st.warning("Não foi possível carregar a imagem do CR7. (Use uma imagem local ou outra URL.)")

    # Exibe as informações do cartão na frente
    st.write(f"**Nome do Titular:** {dados['titular']}")
    st.write(f"**Número do Cartão:** {dados['numero']}")
    st.write(f"**Validade:** {dados['validade']}")

def exibir_cartao_verso(dados):
    st.markdown("## Verso do Cartão (CR7 Theme)")

    # Podemos repetir ou usar outra imagem
    img_cr7 = carregar_imagem(CR7_IMAGE_URL)
    if img_cr7:
        st.image(img_cr7, width=250, caption="CR7 - Verso")
    else:
        st.warning("Não foi possível carregar a imagem do CR7 no verso.")

    # Exibe o CVV (código de segurança)
    st.write(f"**CVV (Código de Segurança):** {dados['cvv']}")

def main():
    st.title("Quer ver qual jogador você é? Coloque os dados do cartão aqui!")
    st.write("Preencha os campos abaixo e descubra o resultado. (Spoiler: Você é o CR7!)")

    # Campos de entrada do usuário
    titular = st.text_input("Nome do Titular (Ex: Bruno Souza)")
    numero = st.text_input("Número do Cartão (Ex: 1234 5678 9012 3456)")
    validade = st.text_input("Data de Validade (Ex: 12/28)")
    cvv = st.text_input("CVV (Ex: 123)", type="password")  # type="password" oculta o CVV no input

    # Dicionário com dados do cartão
    dados_cartao = {
        "titular": titular,
        "numero": numero,
        "validade": validade,
        "cvv": cvv,
    }

    if st.button("Descobrir qual jogador eu sou"):
        st.success("Parabéns, você é o CR7!")
        st.write("---")
        exibir_cartao_frente(dados_cartao)
        st.write("---")
        exibir_cartao_verso(dados_cartao)

if __name__ == "__main__":
    main()
