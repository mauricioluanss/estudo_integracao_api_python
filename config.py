from dotenv import load_dotenv #essa lib serve pra carregar o arquivo .env no meu código. Aí eu vou poder importar os endpoints salvos lá.
import os
load_dotenv()
CHAMADA_PAGAMENTO = os.getenv('CHAMADA_PAGAMENTO')
CHAMADA_CONSULTA = os.getenv('CHAMADA_CONSULTA')