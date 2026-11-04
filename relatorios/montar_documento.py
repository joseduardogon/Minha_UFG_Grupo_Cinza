"""Monta o documento final INF0290-APS-Cinza.pdf a partir dos itens do repositório.

Uso (na raiz do repositório):
    python relatorios/montar_documento.py

Estrutura (regra 4 e Apêndices B e D do enunciado):
    capa e sumário; 1 Projeto estrutural; 2 Projeto comportamental; Referências;
    Apêndice I (registros de uso de IA), II (comunicações) e III (rastreabilidade).

Tratamentos feitos só na saída (os arquivos do repositório não são alterados):
    - a ficha do item mostra autor, revisor e "rastreia para" (sem a linha Status);
    - o "Registro de revisão" e a linha "Fonte: ...puml" são omitidos;
    - figuras e tabelas recebem numeração contínua; tabelas sem legenda ganham uma;
    - os DD por pacote ficam de fora (consolidados no DD-Geral-01);
    - o marcador "Questão: Apêndice <X>, Seção <X.1>" das referências de IA é
      substituído pela seção do Apêndice I que traz o registro correspondente;
    - os códigos de itens citados viram links internos.

Requisitos: pip install markdown pymupdf; Google Chrome ou Edge instalado.
O PDF é gravado em relatorios/INF0290-APS-Cinza.pdf.
"""
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
import pymupdf

PASTA = Path(__file__).resolve().parent
RAIZ = PASTA.parent
SAIDA = PASTA / "INF0290-APS-Cinza.pdf"
CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]
ROTULO = "INF 0290 - Projeto de Software - 2026/2 | APS - Equipe Cinza"

AUTORES = [
    "José Eduardo Gontijo de Carvalho",
    "Maicon Brendo da Silva",
    "Phablo Tavares Paixão",
]

# (pasta, nome exibido) na ordem do documento
PACOTES = [
    ("Comum", "Comum"),
    ("Inicio", "Início"),
    ("Seguranca", "Segurança"),
    ("Locais", "Locais"),
    ("AppsUFG", "Apps UFG"),
    ("Eventos", "Eventos"),
    ("RU", "RU"),
    ("Noticias", "Notícias"),
    ("Radio", "Rádio"),
    ("Guia", "Guia Estudantil"),
    ("AvalRegistrar", "Avaliação – Registrar"),
    ("AvalConsultar", "Avaliação – Consultar notas"),
]
ESTRUTURAIS = ["DCmp", "DCla"]
COMPORTAMENTAIS = ["DCdu", "DAtv", "DSeq", "DIhc", "DEst", "Contrato", "ECA"]

# figuras que vão numa página em paisagem
PAISAGEM = {
    "RU/DCla-RU-01",
    "AvalRegistrar/DCla-AvalRegistrar-01",
    "AvalRegistrar/DAtv-AvalRegistrar-03",
    "AvalConsultar/DCla-AvalConsultar-01",
    "Eventos/DCla-Eventos-01",
    "AvalRegistrar/DSeq-AvalRegistrar-05",
    "Noticias/DCla-Noticias-01",
}

# registros de IA: arquivo, título da seção no Apêndice I
REGISTROS = [
    ("IA/registro-B.md", "Registro de Maicon Brendo da Silva"),
    ("IA/registro-C.md", "Registro de José Eduardo Gontijo de Carvalho"),
    ("IA/registro-D.md", "Registro de Phablo Tavares Paixão"),
]


def secao_ia(ref):
    """Seção do Apêndice I que traz o registro citado por uma referência de IA."""
    if ref.startswith("GOOGLE."):
        return "I.1.1"
    if "claude.ai/code" in ref:
        return "I.2.1"
    if "claude.com/claude-code" in ref:
        return "I.3.2"
    if "Disponível em: claude.ai." in ref:
        return "I.3.1"
    raise ValueError("Referência de IA não mapeada: " + ref)


def ajustar_ref(ref):
    ref = ref.strip()
    if not (ref.startswith("ANTHROPIC.") or ref.startswith("GOOGLE.")):
        return ref
    sec = secao_ia(ref)
    ref = re.sub(r"\s*Questão:.*$", "", ref).rstrip()
    ref = re.sub(r"\(resumo em `IA/registro-[A-D]\.md`\)", f"(resumo no Apêndice I, Seção {sec})", ref)
    if not ref.endswith("."):
        ref += "."
    return f"{ref} Questão: Apêndice I, Seção {sec}."


class Doc:
    contador = 0

    def __init__(self):
        self.partes = []
        self.titulos = []  # (nível, id, texto)
        self.nfig = 0
        self.ntab = 0
        self.refs = []
        self.codigos = set()
        self.usados = set()

    def titulo(self, nivel, texto, ident=None):
        Doc.contador += 1
        ident = ident or f"s{Doc.contador}"
        self.titulos.append((nivel, ident, texto))
        self.partes.append(f'<h{nivel} id="{ident}">{html.escape(texto)}</h{nivel}>')

    def html(self, trecho):
        self.partes.append(trecho)

    # ---------- markdown ----------
    def links(self, md):
        def troca(m):
            texto, alvo = m.group(1), m.group(2)
            cod = Path(alvo.split("#")[0]).stem
            if alvo.endswith(".md") and cod in self.codigos:
                return f"[{texto}](#{cod})"
            return texto
        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", troca, md)

    def tabelas(self, md, contexto):
        """Numera as tabelas em sequência e cria legenda para as que não têm."""
        linhas = md.split("\n")
        # rótulo "Tabela n" sem tabela em seguida (ex.: enumerações): o rótulo sai
        for i, l in enumerate(linhas):
            if re.match(r"\*\*Tabela \d+ [–-] ", l):
                j = i + 1
                while j < len(linhas) and not linhas[j].strip():
                    j += 1
                if j >= len(linhas) or not linhas[j].startswith("|"):
                    linhas[i] = re.sub(r"^\*\*Tabela \d+ [–-] ", "**", l)
        mapa, saida, legendas = {}, [], set()
        titulo_atual = contexto
        for i, l in enumerate(linhas):
            mh = re.match(r"#+\s+(.*)", l)
            if mh:
                titulo_atual = mh.group(1).strip()
            ini_tab = l.startswith("|") and (i == 0 or not linhas[i - 1].startswith("|"))
            if ini_tab:
                k = len(saida) - 1
                while k >= 0 and not saida[k].strip():
                    k -= 1
                self.ntab += 1
                ant = saida[k] if k >= 0 else ""
                m = re.match(r"\*\*Tabela (\d+) [–-] (.*)\*\*\s*$", ant)
                m2 = re.match(r"\*\*Tabela (\d+)\b", ant)
                if m:
                    # legenda própria, sozinha na linha
                    mapa[m.group(1)] = str(self.ntab)
                    saida[k] = f"@@LEG@@@@T{self.ntab}@@ – {m.group(2)}"
                elif m2:
                    # legenda no início de um parágrafo descritivo
                    mapa[m2.group(1)] = str(self.ntab)
                    saida[k] = re.sub(r"^\*\*Tabela \d+", f"**@@T{self.ntab}@@", ant)
                else:
                    if titulo_atual in ("Descrição", contexto):
                        leg = contexto
                    else:
                        leg = f"{contexto}: {titulo_atual}"
                    saida.append(f"@@LEG@@@@T{self.ntab}@@ – {leg}")
                    saida.append("")
            saida.append(l)
        texto = "\n".join(saida)
        if mapa:
            texto = re.sub(
                r"\bTabela (\d+)\b",
                lambda m: "Tabela " + mapa.get(m.group(1), m.group(1)),
                texto,
            )
        return re.sub(r"@@T(\d+)@@", r"Tabela \1", texto)

    def md_html(self, md, contexto, desloc=2):
        md = self.links(md)
        md = self.tabelas(md, contexto)
        # desloca os títulos internos (## -> h4, ### -> h5)
        md = re.sub(r"^(#{2,4}) ", lambda m: "#" * min(len(m.group(1)) + desloc, 6) + " ", md, flags=re.M)
        corpo = markdown.markdown(md, extensions=["tables", "md_in_html", "sane_lists"])
        corpo = re.sub(r"<p>@@LEG@@(.*?)</p>", r'<p class="leg-tab">\1</p>', corpo, flags=re.S)
        corpo = re.sub(
            r"<table>(.*?)</table>",
            lambda m: ('<table class="curta">' if m.group(1).count("<tr>") <= 10 else "<table>")
            + m.group(1) + "</table>",
            corpo,
            flags=re.S,
        )
        return corpo

    # ---------- itens ----------
    def item(self, caminho, numero):
        pasta = caminho.parent.name
        texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
        texto = texto.split("\n## Registro de revisão")[0]
        texto = re.sub(r"\n---\s*$", "", texto.rstrip())
        m = re.match(r"# (.+?)\n", texto)
        titulo_h1 = m.group(1).strip()
        cod = caminho.stem
        titulo_item = re.sub(r"^" + re.escape(cod) + r"\s*[–-]\s*", "", titulo_h1)
        self.usados.add(caminho)

        # ficha
        ficha = {}
        for l in texto.split("\n## ")[0].splitlines():
            mf = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|$", l)
            if mf:
                ficha[mf.group(1)] = mf.group(2)
        for campo in ("Autor(a)", "Revisor(a)", "Rastreia para"):
            if not ficha.get(campo):
                raise SystemExit(f"{cod}: campo {campo} vazio")
        rastreia = re.sub(
            r"`([A-Za-z]+-[A-Za-z]+-\d\d)`",
            lambda mm: f'<a href="#{mm.group(1)}"><code>{mm.group(1)}</code></a>'
            if mm.group(1) in self.codigos else f"<code>{mm.group(1)}</code>",
            html.escape(ficha["Rastreia para"], quote=False),
        )
        self.titulo(3, f"{numero} {cod} – {titulo_item}", ident=cod)
        self.html(
            '<table class="ficha">'
            f'<tr><th>Autor(a)</th><td>{html.escape(ficha["Autor(a)"])}</td></tr>'
            f'<tr><th>Revisor(a)</th><td>{html.escape(ficha["Revisor(a)"])}</td></tr>'
            f"<tr><th>Rastreia para</th><td>{rastreia}</td></tr></table>"
        )

        # seções
        secoes = re.split(r"\n## ", "\n## " + texto.split("\n## ", 1)[1]) if "\n## " in texto else []
        for sec in secoes:
            if not sec.strip():
                continue
            nome, _, corpo = sec.partition("\n")
            nome = nome.strip()
            if nome == "Diagrama":
                self.figura(pasta, cod, titulo_item)
            elif nome == "Referências":
                refs = [ajustar_ref(l) for l in corpo.splitlines() if l.strip() and l.strip() != "---"]
                if refs:
                    self.html('<h4>Referências</h4><div class="refs">')
                    for r in refs:
                        self.refs.append(r)
                        self.html(markdown.markdown(r))
                    self.html("</div>")
            else:
                self.html(f"<h4>{html.escape(nome)}</h4>")
                self.html(self.md_html(corpo, cod))

    def figura(self, pasta, cod, titulo_item):
        png = RAIZ / pasta / f"{cod}.png"
        if not png.exists():
            raise SystemExit(f"Figura ausente: {png}")
        self.nfig += 1
        n = self.nfig
        self.html(f"<p>A Figura {n} apresenta o diagrama <code>{cod}</code>.</p>")
        fig = (
            f'<div class="figura"><img src="{png.as_uri()}" alt="{cod}">'
            f'<div class="leg">Figura {n} – {html.escape(cod)}: {html.escape(titulo_item)}</div></div>'
        )
        if f"{pasta}/{cod}" in PAISAGEM:
            fig = f'<div class="paisagem">{fig}</div>'
        self.html(fig)


def itens_do_pacote(pasta, tipos):
    def chave(p):
        tipo = p.stem.split("-")[0]
        return (tipos.index(tipo), p.stem)
    return sorted(
        (p for p in (RAIZ / pasta).glob("*-*.md") if p.stem.split("-")[0] in tipos),
        key=chave,
    )


def capa():
    autores = "<br>".join(AUTORES)
    return f"""
<div class="capa">
  <div class="inst">Universidade Federal de Goiás<br>Instituto de Informática<br>
  Bacharelado em Engenharia de Software<br><br>
  <b>INF 0290 – Projeto de Software – semestre 2026/2</b><br>
  Atividades Práticas Supervisionadas (APS)</div>
  <div>
    <div class="titulo">Projeto de Software do aplicativo Minha UFG v3.1.1</div>
    <div class="sub">Projeto estrutural e comportamental, com a evolução<br>
    “Avaliação de qualidade de Unidades Acadêmicas”</div>
  </div>
  <div>
    <div class="equipe">Equipe Cinza</div>
    <div class="autores">{autores}</div>
  </div>
  <div class="local">Goiânia<br>2026</div>
</div>"""


def registro_ia(doc, idx, arquivo, titulo):
    texto = (RAIZ / arquivo).read_text(encoding="utf-8").replace("\r\n", "\n")
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    doc.titulo(2, f"I.{idx} {titulo}")
    partes = re.split(r"\n## ", texto)
    intro = re.sub(r"^# .*\n", "", partes[0]).strip()
    doc.html(doc.md_html(intro, titulo))
    for j, entrada in enumerate(partes[1:], start=1):
        nome, _, corpo = entrada.partition("\n")
        doc.titulo(3, f"I.{idx}.{j} {nome.strip()}")
        corpo = "\n".join(ajustar_ref(l) if l.startswith(("ANTHROPIC.", "GOOGLE.")) else l for l in corpo.splitlines())
        doc.html(doc.md_html(corpo, nome.strip(), desloc=1))
        for l in corpo.splitlines():
            if l.startswith(("ANTHROPIC.", "GOOGLE.")):
                doc.refs.append(l)


def montar():
    doc = Doc()
    todos = [p for d, _ in PACOTES for p in (RAIZ / d).glob("*-*.md")] + list((RAIZ / "Geral").glob("*-*.md"))
    doc.codigos = {p.stem for p in todos if not (p.stem.startswith("DD-") and p.parent.name != "Geral")}

    # 1 Projeto estrutural
    doc.titulo(1, "1 Projeto estrutural")
    doc.html(
        "<p>Esta seção reúne o modelo conceitual de dados, a estrutura externa (implantação) "
        "e a estrutura interna do software: o diagrama de pacotes e, para cada pacote, "
        "os diagramas de componentes e de classes.</p>"
    )
    doc.titulo(2, "1.1 Modelo conceitual de dados")
    doc.item(RAIZ / "Geral/DDados-Geral-01.md", "1.1.1")
    doc.item(RAIZ / "Geral/DD-Geral-01.md", "1.1.2")
    doc.titulo(2, "1.2 Estrutura externa")
    doc.item(RAIZ / "Geral/DImp-Geral-01.md", "1.2.1")
    doc.titulo(2, "1.3 Estrutura interna")
    doc.item(RAIZ / "Geral/DPac-Geral-01.md", "1.3.1")
    sec = 4
    for pasta, nome in PACOTES:
        itens = itens_do_pacote(pasta, ESTRUTURAIS)
        if not itens:
            continue
        doc.titulo(2, f"1.{sec} Pacote {nome}")
        for k, p in enumerate(itens, start=1):
            doc.item(p, f"1.{sec}.{k}")
        sec += 1

    # 2 Projeto comportamental
    doc.titulo(1, "2 Projeto comportamental")
    doc.html(
        "<p>Esta seção traz o diagrama de casos de uso geral e, para cada funcionalidade, "
        "os casos de uso detalhados, as atividades, as sequências, os protótipos de IHC, "
        "os diagramas de estados, os contratos das operações e as regras E-C-A.</p>"
    )
    doc.titulo(2, "2.1 Casos de uso gerais")
    doc.item(RAIZ / "Geral/DCdu-Geral-01.md", "2.1.1")
    sec = 2
    for pasta, nome in PACOTES:
        itens = itens_do_pacote(pasta, COMPORTAMENTAIS)
        if not itens:
            continue
        doc.titulo(2, f"2.{sec} {nome}")
        for k, p in enumerate(itens, start=1):
            doc.item(p, f"2.{sec}.{k}")
        sec += 1

    # conferência: todo item (menos os DD por pacote) entrou
    faltam = [p for p in todos if p.stem in doc.codigos and p not in doc.usados]
    if faltam:
        raise SystemExit("Itens fora do documento: " + ", ".join(p.stem for p in faltam))

    # Apêndices (montados antes para coletar as referências dos registros de IA)
    ap = Doc()
    ap.nfig, ap.ntab, ap.codigos = doc.nfig, doc.ntab, doc.codigos
    ap.titulos = []
    ap.titulo(1, "Apêndice I – Registros de uso de IA")
    ap.html(
        "<p>Registros de uso de inteligência artificial de cada integrante (regra 6 do enunciado). "
        "As referências de IA citadas nos itens remetem às seções deste apêndice.</p>"
    )
    for idx, (arq, tit) in enumerate(REGISTROS, start=1):
        registro_ia(ap, idx, arq, tit)

    ap.titulo(1, "Apêndice II – Registro de comunicações da equipe")
    com = (RAIZ / "Atas/comunicacoes.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    com = re.sub(r"^# .*\n", "", com)
    blocos = re.split(r"\n## ", com)
    ap.html(ap.md_html(blocos[0].strip(), "Comunicações"))
    for j, b in enumerate(blocos[1:], start=1):
        nome, _, corpo = b.partition("\n")
        ap.titulo(2, f"II.{j} {nome.strip()}")
        ap.html(ap.md_html(corpo, "Registro cronológico das comunicações", desloc=1))

    ap.titulo(1, "Apêndice III – Matriz de rastreabilidade")
    ap.html(
        "<p>Matriz gerada a partir do campo “Rastreia para” de cada item de informação "
        "(critério 5.2). A coluna “Rastreado por” lista os itens que apontam para o item.</p>"
    )
    rast = (RAIZ / "Integracao/rastreabilidade.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    matriz = rast.split("\n## 3. Matriz", 1)[1].split("\n", 1)[1]
    blocos = re.split(r"\n### ", "\n" + matriz)
    for j, b in enumerate([b for b in blocos if b.strip()], start=1):
        nome, _, corpo = b.partition("\n")
        if not corpo.strip().startswith("|"):
            # texto introdutório antes do primeiro pacote
            ap.html(ap.md_html(b.strip(), "Matriz"))
            continue
        pac = re.sub(r"\s*\(dono:.*\)", "", nome.strip())
        ap.titulo(2, f"III.{j} Pacote {pac}")
        ap.html(ap.md_html(corpo, f"Rastreabilidade do pacote {pac}"))

    # Referências gerais (antes dos apêndices)
    vistas, refs = set(), []
    for r in doc.refs + ap.refs:
        chave = re.sub(r"\s+", " ", r.strip())
        if chave not in vistas:
            vistas.add(chave)
            refs.append(chave)
    refs.sort(key=lambda r: re.sub(r"[*_`]", "", r).upper())
    doc.titulo(1, "Referências")
    doc.html('<div class="refs-gerais">' + "".join(markdown.markdown(r) for r in refs) + "</div>")

    return doc.partes + ap.partes, doc.titulos + ap.titulos, doc, ap


def montar_toc(titulos, paginas):
    itens = []
    for nivel, ident, texto in titulos:
        num = paginas.get(ident, "")
        itens.append(
            f'<li class="l{nivel}"><a href="#{ident}"><span class="t">{html.escape(texto)}</span>'
            f'<span class="d"></span><span class="n">{num}</span></a></li>'
        )
    return '<div class="sumario"><h1 id="sumario">Sumário</h1><ul class="toc">' + "".join(itens) + "</ul></div>"


def html_final(partes, toc, css):
    return (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        "<title>INF0290-APS-Cinza</title>"
        f"<style>{css}</style></head><body>" + capa() + toc + "".join(partes) + "</body></html>"
    )


def achar_chrome():
    for c in CHROME:
        if os.path.exists(c):
            return c
    sys.exit("Chrome/Edge não encontrado.")


def imprimir(texto_html, destino):
    with tempfile.TemporaryDirectory() as perfil:
        arq = PASTA / "_documento_tmp.html"
        arq.write_text(texto_html, encoding="utf-8")
        try:
            subprocess.run(
                [achar_chrome(), "--headless=new", "--disable-gpu", f"--user-data-dir={perfil}",
                 "--no-pdf-header-footer", f"--print-to-pdf={destino}", arq.as_uri()],
                check=True, timeout=600, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        finally:
            arq.unlink(missing_ok=True)


def paginas_dos_titulos(pdf, titulos):
    """Página de cada título, lida dos destinos internos dos links do sumário."""
    d = pymupdf.open(pdf)
    paginas = {}
    for i, pg in enumerate(d):
        if i > 40:
            break
        for ln in pg.get_links():
            nome = ln.get("nameddest")
            if nome and ln.get("page", -1) >= 0 and nome not in paginas:
                paginas[nome] = str(ln["page"] + 1)
    d.close()
    return paginas


def finalizar(entrada, saida, titulos, paginas):
    d = pymupdf.open(entrada)
    total = len(d)
    for i, pg in enumerate(d):
        if i == 0:
            continue
        w, h = pg.rect.width, pg.rect.height
        cinza = (0.35, 0.35, 0.35)
        pg.insert_text((45, 30), ROTULO, fontsize=7.5, fontname="helv", color=cinza)
        pg.draw_line((45, 35), (w - 45, 35), color=(0.75, 0.78, 0.82), width=0.4)
        y = h - 24
        pg.draw_line((45, y - 9), (w - 45, y - 9), color=(0.75, 0.78, 0.82), width=0.4)
        pg.insert_text((45, y), "INF0290-APS-Cinza", fontsize=7.5, fontname="helv", color=cinza)
        txt = f"Página {i + 1} de {total}"
        larg = pymupdf.get_text_length(txt, fontname="helv", fontsize=7.5)
        pg.insert_text((w - 45 - larg, y), txt, fontsize=7.5, fontname="helv", color=cinza)
    marcadores = [[1, "Sumário", 2]]
    for nivel, ident, texto in titulos:
        if ident in paginas:
            marcadores.append([nivel, texto, int(paginas[ident])])
    d.set_toc(marcadores)
    d.set_metadata({"title": "INF0290-APS-Cinza – Projeto de Software do aplicativo Minha UFG",
                    "author": "; ".join(AUTORES), "subject": "INF 0290 – Projeto de Software – APS"})
    d.save(saida, garbage=3, deflate=True)
    d.close()


def main():
    partes, titulos, doc, ap = montar()
    css = (PASTA / "documento.css").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        p1 = os.path.join(tmp, "p1.pdf")
        imprimir(html_final(partes, montar_toc(titulos, {}), css), p1)
        paginas = paginas_dos_titulos(p1, titulos)
        p2 = os.path.join(tmp, "p2.pdf")
        imprimir(html_final(partes, montar_toc(titulos, paginas), css), p2)
        conf = paginas_dos_titulos(p2, titulos)
        if conf != paginas:
            paginas = conf
            imprimir(html_final(partes, montar_toc(titulos, paginas), css), p2)
        finalizar(p2, str(SAIDA), titulos, paginas)
    sem = [t for _, i, t in titulos if i not in paginas]
    print(f"Itens: {len(doc.usados)} | figuras: {doc.nfig} | tabelas: {ap.ntab} | títulos: {len(titulos)}")
    if sem:
        print("Atenção: títulos sem página:", sem[:10])
    print("PDF gerado:", SAIDA)


if __name__ == "__main__":
    main()
