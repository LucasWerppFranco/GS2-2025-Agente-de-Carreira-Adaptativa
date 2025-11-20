#!/usr/bin/env python3
import os
import sys
from typing import List, Dict, Any

try:
    from google import genai
except Exception:
    print("Erro ao importar google.genai. Instale com: pip install google-genai")
    sys.exit(1)

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("Erro: defina a variável de ambiente GEMINI_API_KEY com sua chave do Gemini.")
    sys.exit(1)

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
Você é o Agente de Carreira Adaptativa (ACA). Sua função é orientar o usuário sobre:
- Risco de automação
- Habilidades críticas
- Upskilling
- Reskilling
- Simulação e avaliação de entrevista
Responda sempre de maneira organizada, clara e objetiva.
"""

def call_gemini(prompt: str) -> str:
    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )
    except Exception as e:
        return f"Erro ao chamar Gemini: {str(e)}"

    try:
        return resp.text
    except Exception:
        pass

    try:
        return resp.candidates[0].content.parts[0].text
    except Exception:
        return str(resp)

def analyze_profile(profession: str, tasks: str) -> Dict[str, Any]:
    prompt = f"""
{SYSTEM_PROMPT}

Tarefa: Analise o seguinte perfil:
Profissão: {profession}
Tarefas principais: {tasks}

Entregue:
- Risco de automação (baixo/médio/alto) + justificativa
- 5 habilidades críticas (soft e hard)
- 2 ações rápidas para esta semana
"""
    return {"raw": call_gemini(prompt)}

def upskilling_plan(profession: str, skills: List[str]) -> Dict[str, Any]:
    skills_txt = "\n".join(f"- {s}" for s in skills)
    prompt = f"""
{SYSTEM_PROMPT}

Gerar plano de Upskilling para: {profession}

Skills críticas informadas:
{skills_txt}

Para cada skill, indique 3–5 áreas de aprimoramento com 1 recurso recomendado.
"""
    return {"raw": call_gemini(prompt)}

def reskilling_path(current: str, target: str, transferable: str) -> Dict[str, Any]:
    prompt = f"""
{SYSTEM_PROMPT}

Planejar transição de carreira.
Profissão atual: {current}
Profissão alvo: {target}
Habilidades transferíveis: {transferable}

Entregue:
- 3–5 novas habilidades necessárias
- descrição + nível + recurso prático
- plano de 3 meses
"""
    return {"raw": call_gemini(prompt)}

def simulate_interview(role: str) -> Dict[str, Any]:
    prompt = f"""
{SYSTEM_PROMPT}
Gerar 3 perguntas de entrevista para o cargo: {role}

Inclua critérios de avaliação:
- Clareza
- Relevância
- Profundidade
(com notas de 1 a 5)
"""
    return {"raw": call_gemini(prompt)}

def evaluate_answer(question: str, answer: str) -> Dict[str, Any]:
    prompt = f"""
{SYSTEM_PROMPT}
Avalie a resposta do candidato usando:
- clareza
- relevância
- profundidade

Pergunta: {question}
Resposta: {answer}

Retorne em JSON.
"""
    return {"raw": call_gemini(prompt)}

def prompt_input(msg: str) -> str:
    print()
    return input(msg + "\n> ")

def main():
    print("\n=== Agente de Carreira Adaptativa (ACA) ===\n")

    while True:
        print("Escolha uma ação:")
        print("1) Análise de Perfil e Risco de Automação")
        print("2) Plano de Upskilling")
        print("3) Caminho de Reskilling")
        print("4) Simulação de Entrevista")
        print("5) Sair")

        choice = input("\nEscolha (1-5): ")

        if choice == "1":
            prof = prompt_input("Profissão atual:")
            tasks = prompt_input("Principais tarefas:")
            print("\n--- Resultado ---\n")
            print(analyze_profile(prof, tasks)["raw"])

        elif choice == "2":
            prof = prompt_input("Profissão alvo do upskilling:")
            skills_raw = prompt_input("Skills críticas (separadas por vírgula):")
            skills = [s.strip() for s in skills_raw.split(",")]
            print("\n--- Plano ---\n")
            print(upskilling_plan(prof, skills)["raw"])

        elif choice == "3":
            current = prompt_input("Profissão atual:")
            target = prompt_input("Profissão alvo:")
            transferable = prompt_input("Habilidades transferíveis (opcional):")
            print("\n--- Reskilling ---\n")
            print(reskilling_path(current, target, transferable)["raw"])

        elif choice == "4":
            role = prompt_input("Cargo para entrevista simulada:")
            sim = simulate_interview(role)
            print("\n--- Perguntas ---\n")
            print(sim["raw"])

            question = prompt_input("Digite a pergunta que quer responder:")
            answer = prompt_input("Sua resposta:")
            print("\n--- Avaliação ---\n")
            print(evaluate_answer(question, answer)["raw"])

        elif choice == "5":
            print("Saindo... Boa sorte na sua carreira!")
            break

        else:
            print("Escolha inválida.\n")

if __name__ == "__main__":
    main()

