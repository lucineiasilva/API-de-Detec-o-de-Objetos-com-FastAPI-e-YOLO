# Projeto API de Detecção de Objetos com FastAPI e YOLO**🚀
## Descrição
A API foi solicitada como atividade da disciplina "Inteligência Artificial", como nota parcial para conclusão da referida disciplina.

## Configuração do ambiente de execução
* Editor de código-fonte utilizado para esta atividade: [VSCODE](https://code.visualstudio.com/Download)
* Linguagem de programação utlizada: [Python](https://www.python.org/downloads/)
* Necessãrio instalação das bibliotecas: _fastapi, uvicorn, opencv-python, pillow, numpy e ultralytics_
  ### Para instalação via terminal, considerando que já tenha instalado o editor de código e o python
     * 1. Abra o terminal do linux, com o comando:```ctrl+alt+t``` ou no terminal do vscode: ```crtl+j```
     * 2. Ative o ambiente virtual (venv):  ```python -m venv venv``` ou ```python3 -m venv venv``` e   ```source venv/bin/activate```
     * 3. Instale as bibliotecas: ```pip install fastapi uvicorn opencv-python pillow numpy ultralytics``
        * Observação: Eu tive dificuldade em instalar direto, precisei utilizar o sudo. Nesse caso basta utilizar sudo apt install e o nome da biblioteca.
### Para rodar o servidor, digite o comando:
```uvicorn main:app --host 0.0.0.0 --port 8000 --reload```
  ### Para testar a API, digite o comando:
```http://127.0.0.1:8000/```
Irá aparecer a mensagem ->  _{"message":"Esta página faz parte da última Atividade da Disciplina de IA - Docente: José Lucas Brandão e Discente: Lucineia Pacheco "}._
  ### Testar a documentação Swagger (documentação automática):
```http://127.0.0.1:8000/docs```


        
    
