# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue o padrão do [Mantenha um Changelog](http://keepachangelog.com/en/1.0.0/)
e este projeto adota [Versionamento Semântico](http://semver.org/spec/v2.0.0.html).

<!-- TOWNCRIER -->

## [2.0.0] - 2025-02-01

- Simplificado o processo de configuração e as instruções do projeto
- Estrutura reorganizada, movendo todos os notebooks para o diretório raiz, facilitando o uso no Colab
- Uso de `!cat` em vez de *load magic* para carregar soluções, já que *load magics* não são implementados em alguns ambientes

## [1.1.0] - 2022-07-10

- Diversas melhorias ([#40](https://github.com/HumbleData/beginners-data-workshop/pull/40))
- **Bastidores**
  - Atualização do Python para a versão 3.9.13
  - Atualização de todas as dependências para as versões mais recentes, com NumPy, pandas, Matplotlib e scikit-learn compatíveis com o CoCalc
  - Migração de `pip-tools` para Poetry (configuração em `pyproject.toml`)
  - Atualização das instruções de setup de desenvolvimento no `README.md`
  - Integração e configuração do flake8, pylint, black e outros linters
  - Adicionada configuração de pre-commit
  - Atualização do arquivo `settings.json` do VS Code
  - Adicionado `linestripper.py` para evitar novas linhas no EOF (End Of File, Fim do arquivo) nos códigos das soluções (melhor experiência para participantes), mantendo conformidade com o black
  - Adicionado o `CHANGELOG.md` e início do versionamento de releases
- **Materiais do workshop**
  - Revisão de todos os materiais para remover itens obsoletos
  - Substituição de aspas simples por aspas duplas nas soluções, em conformidade com o black
  - Adicionadas novas linhas EOF nos datasets
  - Outras alterações menores: remoção de espaços em branco finais, vírgulas finais e organização de imports conforme o isort

## [1.0.0] - 2021-07-23

Versão final utilizada nos workshops do Humble Data em 2021.
