![Criando interfaces gráficas com Python (PySide6) e Qt 6](./docs/images/readme/pyside6-cover-1600x840.webp "Criando interfaces gráficas com Python (PySide6) e Qt 6")

<br>

[![natorsc - gui-python-pyside6-qt6](https://img.shields.io/static/v1?label=natorsc&message=gui-python-pyside6-qt6&color=blue&logo=github)](https://github.com/natorsc/gui-python-pyside6-qt6 "Ir para o repositório.")
&emsp;
[![stars - gui-python-pyside6-qt6](https://img.shields.io/github/stars/natorsc/gui-python-pyside6-qt6?style=social)](https://github.com/natorsc/gui-python-pyside6-qt6)
&emsp;
[![forks - gui-python-pyside6-qt6](https://img.shields.io/github/forks/natorsc/gui-python-pyside6-qt6?style=social)](https://github.com/natorsc/gui-python-pyside6-qt6)

[![License MIT](https://img.shields.io/static/v1?label=License&message=MIT&color=blue)](https://github.com/natorsc/gui-python-pyside6-qt6)

# Criando interfaces gráficas com Python (PySide6) e Qt 6

## 📝 Descrição

Repositório criado para documentar e centralizar conteúdos, dicas, tutoriais e exemplos de código sobre a construção de interfaces com a linguagem de programação Python (PySide6) e o framework gráfico Qt 6

## 📚 Documentação

🚨 Importante!

Para facilitar a navegação e consulta dos conteúdos contidos neste repositório, a documentação foi criada com [Sphinx](https://www.sphinx-doc.org/en/master/) + [Furo](https://github.com/pradyunsg/furo).

Acesse [https://pyside6.justcode.com.br/](https://pyside6.justcode.com.br/) para poder ver ao conteúdo completo.

---

## 🛠 Tecnologias utilizadas

Até o presente momento as seguintes tecnologias estão sendo utilizadas na construção do projeto:

[![Python](https://img.shields.io/static/v1?label=&message=Python&color=blue&logoColor=white&logo=python)](https://www.python.org/ "Ir para o site.")
&emsp;
[![PySide6](https://img.shields.io/static/v1?label=&message=PySide6&color=blue&logoColor=white&logo=pypi)](https://pypi.org/project/PySide6/ "Ir para o PyPi.")
&emsp;
[![Qt](https://img.shields.io/static/v1?label=&message=Qt&nbsp;6&color=blue&logoColor=white&logo=qt)](https://www.qt.io/ "Ir para o site.")
&emsp;
[![KDE](https://img.shields.io/static/v1?label=&message=KDE&color=blue&logoColor=white&logo=kde)](https://kde.org/pt-br/ "Ir para o site.")
&emsp;
[![kirigami](https://img.shields.io/static/v1?label=&message=Kirigami&color=blue&logoColor=white&logo=kirigami)](https://develop.kde.org/frameworks/kirigami/ "Ir para o site.")

---

## 🤓 Autor

Feito com 💙 por [Renato Cruz](https://github.com/natorsc) 🤜🤛 Entre em contato!

[![E-mail](https://img.shields.io/static/v1?label=&message=E-mail&color=blueviolet&logoColor=white&logo=gmail)](mailto:zkpcvm6dz@mozmail.com "Enviar e-mail.")
&emsp;
[![LinkedIn](https://img.shields.io/static/v1?label=&message=LinkedIn&color=blue&logoColor=white&logo=LinkedIn)](https://www.linkedin.com/in/natorsc "Entre em contato.")

Uma das playlist que costumo ouvir quando estou estudando ou "codando" 😁:

[![Spotify](https://img.shields.io/static/v1?label=&message=Spotify&color=darkgreen&logoColor=white&logo=spotify)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Acessar playlist.")

Sempre que possível escrevo tutoriais no meu blog pessoal 🚀:

[![Blog](https://img.shields.io/static/v1?label=&message=Blog&color=gray&logoColor=blue&logo=hashnode)](https://blog.codigoninja.dev/ "Ir para o blog.")

---

## 💝 Doações

### Ko-Fi

[![Ko-Fi](https://img.shields.io/static/v1?label=&message=Ko-Fi&color=orange&logoColor=white&logo=ko-fi)](https://ko-fi.com/natorsc "Ajude com uma doação.")

### Pix

<img src="./docs/images/donation/pix-qr-code.jpg" alt="drawing" width="150"/>

**Chave**: `b1839493-2afe-484d-9272-82a3e402b36f`

---

## 💡 Extra

### Resources

Para gerar o arquivo de resources:

```bash
pyside6-rcc resources_rc.qrc -o resources_rc.py
```

> Posteriormente o arquivo deve ser importado no código.

### Tradução

Para gerar o arquivo de tradução:

```bash
pyside6-lupdate MainWindow.py -ts br.com.justcode.Example.ts
```

Para arquivos de interface:

```bash
pyside6-lupdate MainWindow.ui -ts br.com.justcode.Example.ts
```

Para gerar o arquivo binário da tradução `*.qm`:

```bash
pyside6-lrelease br.com.justcode.Example.ts -qm br.com.justcode.Example.qm
```

### Poetry

#### requirements.txt

Para gerar o arquivo de dependências `requirements.txt` através do [Poetry](https://python-poetry.org/) utilizar o comando:

```bash
poetry export \
--without-hashes \
-f requirements.txt \
-o requirements.txt
```

Para gerar o arquivo com as dependências de desenvolvimento (`requirements-dev.txt`):

```bash
poetry export \
--with dev \
--without-hashes \
-f requirements.txt \
-o requirements-dev.txt
```

Dependências da documentação (`docs/requirements.txt`)

```bash
poetry export \
--only docs \
--without-hashes \
-f requirements.txt \
-o docs/data/requirements-doc.txt
```

---

### Documentação.

Acessar a pasta da documentação:

```bash
cd docs
```

Criar a documentação:

```bash
make dirhtml
```

Executando um servidor local para a documentação:

```bash
python3 -m http.server -d build/dirhtml
```

---
