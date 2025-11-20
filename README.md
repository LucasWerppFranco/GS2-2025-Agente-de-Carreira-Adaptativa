# GS2-2025-Agente-de-Carreira-Adaptativa

## Iniciando o programa

Criar e ativar uma virtual environment

- Linux / macOS

```
python3 -m venv venv
source venv/bin/activate
```

- Windows (PowerShell)

```
python -m venv venv
venv\Scripts\Activate.ps1
```

Atualizar pip

```
pip install --upgrade pip
```

Instalar dependências do projeto

```
pip install -r requirements.txt
```

Definir a chave de API do Gemini

- Linux / macOS (bash/zsh)

```
export GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

- Windows (PowerShell)

```
setx GEMINI_API_KEY "SUA_CHAVE_AQUI"

```

(Opcional) Definir modelo padrão

```
export GEMINI_MODEL="gemini-2.5-flash"
```

Rodando o Programa

```
python aca_agent.py
```
