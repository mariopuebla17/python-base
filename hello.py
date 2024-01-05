"""Hello World Multi Línguas

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

DICAS:
- Escrever comentários até a coluna 79
- Usar as regras do site pep8.org para estilização
"""

__version__ = "0.0.1"
__author__ = "Mario Puebla"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)