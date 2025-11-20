#!/usr/bin/env python3
"""Agente de Carreira Adaptativa (ACA)
Rodando no terminal. Usa a biblioteca `google-genai` (Gemini API) para raciocínio.


Configuração: defina a variável de ambiente GEMINI_API_KEY com sua chave do Gemini.
Opcionalmente defina GEMINI_MODEL (ex: "gemini-2.5-flash" ou "gemini-2.5-pro")


Uso: python aca_agent.py
"""
import os
import sys
import textwrap
from typing import List, Dict, Any


try:
from google import genai
except Exception as e:
print("Erro ao importar google.genai. Verifique se 'google-genai' está instalado.")
raise


# Cliente Gemini
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
print("Erro: defina a variável de ambiente GEMINI_API_KEY com sua chave do Gemini.")
sys.exit(1)


MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
client = genai.Client(api_key=API_KEY)


# Prompt base (também fornecido em prompt.txt)
SYSTEM_PROMPT = """
Você é o Agente de Carreira Adaptativa (ACA). Você ajuda um profissional (perfil fictício)
identificando risco de automação, habilidades críticas, planos de upskilling e caminhos de
reskilling, e também simula entrevistas curtas avaliando respostas com critérios.
Responda de maneira clara, estruturada, acionável e curta quando for necessário.
"""


# Helpers
def call_gemini(prompt: str, max_output_tokens: int = 800) -> str:
"""Chama o modelo Gemini e retorna o texto gerado."""
resp = client.models.generate_content(
model=MODEL,
contents=prompt,
max_output_tokens=max_output_tokens,
)
# A API pode retornar objetos com .text ou .result ou .candidates; tratamos de forma simples
try:
return resp.text
except Exception:
# Tentativa alternativa
try:
return resp.content[0].text
except Exception:
return str(resp)


# Funções do ACA


def analyze_profile(profession: str, tasks: str) -> Dict[str, Any]:
main()
