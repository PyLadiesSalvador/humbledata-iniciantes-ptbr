# Humble Data Workshop

[![Humble Data Workshop](./media/humble-data-logo-transparent.png)](https://humbledata.org)

## ℹ️ Se você gostaria de saber mais sobre esse workshop, por favor, nos envie um [email](mailto:contact@humbledata.org).

---
## Tabela de Conteúdos
* [Acessando os materiais pelo navegador](#accessing-the-materials-in-browser)
* [Preparando o ambiente local](#local-environment-setup)
	+ [Instalação do UV](#uv-installation)
	+ [Instalação do Miniconda](#installing-miniconda)
 		- [Windows](#windows)
 		- [Unix (Linux/macOS)](#unix-linuxmacos)
+ [Criando e Ativando o Ambiente](#creating-and-activating-the-environment)

* [Licença](#license)
---

### Acessando os materiais pelo navegador

Ao longo do workshop, nós fornecemos os materiais para iniciantes usando um servidor JupyterLite. Os materiais estão disponíveis atualmente em [Inglês](https://humbledata.org/online-workshop/lab/index.html), [Espanhol](https://humbledata.org/online_workshop_spanish/lab/index.html), [Italiano](https://humbledata.org/online-workshop-italian-v2/lab/index.html) e [Português Brasileiro](https://humbledata.org/online_workshop_ptbr/lab/index.html). Por favor, nos contate se você gostaria de contribuir com o projeto traduzindo os materiais para outros idiomas!
**O jeito mais fácil de acessar os materiais para iniciantes é usando nosso servidor [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/).** Selecione um idioma abaixo para iniciar:

Os materiais também podem ser clonados do nosso [repositório no GitHub](https://github.com/HumbleData/beginners-data-workshop). Se você quiser usar os materiais desse jeito, será preciso instalá-los localmente. As instruções de como fazer isso estão disponíveis abaixo. Não se preocupe se você nunca fez isso antes - essas instruções foram pensadas para completos iniciantes e vão te guiar por cada passo do workshop.
- [Inglês](https://humbledata.org/online-workshop/lab/index.html)
- [Espanhol](https://humbledata.org/online_workshop_spanish/lab/index.html)
- [Italiano](https://humbledata.org/online-workshop-italian-v2/lab/index.html)
- [Português Brasileiro](https://humbledata.org/online_workshop_ptbr/lab/index.html).

Por favor, nos contate se você gostaria de contribuir com o projeto traduzindo os materiais para outros idiomas!

### Instalando os materiais localmente

Se você estiver interessado em aprender como gerenciar o seu próprio ambiente Python, será preciso instalar os materiais localmente. As instruções de como fazer isso estão disponíveis abaixo. Não se preocupe se você nunca fez isso antes - essas instruções foram pensadas para completos iniciantes e vão te guiar por cada passo do workshop.

Para rodar esses notebooks na sua máquina, você deve preparar um *ambiente Python*. Esse documento contém instruções de como rodar o workshop usando o `uv` ou `conda` (Miniconda) como gerenciador de pacotes.

Comece cloonando o repositório e entrando no diretório `beginners-data-workshop`:
```bash
git clone https://github.com/HumbleData/beginners-data-workshop.git
cd beginners-data-workshop
```
Então siga as instruções "Instação do UV" ou "Instação do Miniconda" abaixo.

### Instação do UV
Para rodar localmente esse worshop usando `uv`, primeiro você vai precisar [instalar o uv](https://docs.astral.sh/uv/getting-started/installation/) no seu computador.

Assim que esteja instalado, siga as instruções abaixo:

1. Crie um ambiente virtual python na versão 3.10+
	* `uv venv humble-data-workshop --python 3.10`
2. Ative o ambiente virtual.
	* `source humble-data-workshop/bin/activate`
3. Instale as dependências
	* `uv pip install -r requirements.txt`

### Instação do Miniconda

#### Windows
1. Faça o download do instalador do Miniconda para Windows do [site oficial](https://docs.conda.io/en/latest/miniconda.html)
2. Clique duas vezes no arquivo `.exe` baixado
3. Siga os comandos de instalação:
   - Clique em "Next" (Próximo)
   - Aceite os termos de licença
   - Selecione "Just me" (Apenas eu) para o escopo da instalação
   - Escolha o diretório para instalação (o diretório padrão é recomendado)
   - Em "Advanced Options" (Opções Avançadas), clique em "Adicionar Miniconda3 a minha variável de ambiente PATH"
   - Clique em "Instalar"

#### Unix (Linux/macOS)
1. Faça o download do instalador do Miniconda installer para o seu sistema do [site oficial](https://docs.conda.io/en/latest/miniconda.html)
2. Abra o Terminal
3. Navegue até o diretório que contém o arquivo baixado
4. Torne o instalador executável:
   ```bash
   chmod +x Miniconda3-latest-*-x86_64.sh
   ```
5. Rode o instalado:
   ```bash
   ./Miniconda3-latest-*-x86_64.sh
   ```
6. Siga os comandos:
   - Pressione Enter para revisar o acordo da licença 
   - Digite "yes" para aceitar os termos da licença  
   - Confirme o local da instalação (default é recomendado) 
   - Digite "yes" para inicializar o Miniconda3

#### Criando e Ativando o Ambiente

1. Abra um novo terminal (Windows: Anaconda Prompt, Unix: Terminal)
2. Crie um novo ambiente chamado 'humble-data':
   ```bash
   conda create -n humble-data python=3.8
   ```
3. Ative o ambiente:
   - Windows:
     ```bash
     conda activate humble-data
     ```
   - Unix:
     ```bash
     conda activate humble-data
     ```
4. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicialize o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
   Esse comando abrirá o Jupyter Notebook no seu navegador padrão. Agora vocẽ pode navegar por ou abrir qualquer um dos notebooks do workshopo.

## Contribuindo

1. Crie um fork desse repositório
2. Clone seu fork localmente
3. Crie uma branch para suas alterações:
```git checkout -b improve-notebook-x```

4. Realize suas alterações:

- Mnatenha as explicações simples e fáceis para iniciantes 
- Teste os  notebooks tanto no Google Colab quanto em ambientes locais
- Siga os estilos existentes de código e formatação


5. Faça o commit com uma mensagem clara:
```git commit -m "Fix typo in data visualization notebook"```

6. Faça o push da sua branch e crie um pull request:
```git push -u origin improve-notebook-x```
---

## Licença

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Este projeto está sob uma <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licença Internacional Creative Commons 4.0 que permite uso com crédito, proíbe fins comerciais e exige que obras derivadas a usem</a>.
