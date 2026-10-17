"""Gera o PDF de um relatório de evolução a partir do arquivo Markdown.

Uso (na raiz do repositório ou em relatorios/):
    python gerar_pdf.py Relatorio-Evolucao-01_2026-10-16.md
    python gerar_pdf.py Relatorio-Evolucao-01_2026-10-16_resumo.md --compacto

--compacto: versão resumida, sem capa nem sumário, com estilo adensado
(relatorio-compacto.css) e rodapé em todas as páginas.

O PDF é gravado ao lado do .md, com o mesmo nome. Requisitos:
    pip install markdown pymupdf
    Google Chrome instalado (usado em modo headless para imprimir o HTML).

O bloco "## Sumário" do Markdown é substituído por um índice com números de
página, e cada página (exceto a capa) recebe rodapé com a numeração.
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
CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]


def achar_chrome():
    for caminho in CHROME:
        if os.path.exists(caminho):
            return caminho
    sys.exit("Chrome/Edge não encontrado; ajuste a lista CHROME em gerar_pdf.py.")


def texto_puro(trecho_html):
    return html.unescape(re.sub(r"<[^>]+>", "", trecho_html)).strip()


def converter(md_texto):
    """Markdown -> (corpo HTML com ids nos títulos, lista de (nível, id, texto))."""
    md_texto = re.sub(
        r"(## Sumário\n).*?(?=<div class=\"quebra\"></div>)",
        r"\1\n<!--TOC-->\n\n",
        md_texto,
        count=1,
        flags=re.S,
    )
    corpo = markdown.markdown(
        md_texto, extensions=["tables", "md_in_html", "sane_lists"]
    )
    # tabelas curtas (até 9 linhas de corpo) não são partidas entre páginas
    corpo = re.sub(
        r"<table>(.*?)</table>",
        lambda m: ('<table class="curta">' if m.group(1).count("<tr>") <= 10 else "<table>")
        + m.group(1)
        + "</table>",
        corpo,
        flags=re.S,
    )
    titulos = []

    def marcar(m):
        nivel, conteudo = int(m.group(1)), m.group(2)
        texto = texto_puro(conteudo)
        if texto == "Sumário":
            return m.group(0)
        ident = f"s{len(titulos) + 1}"
        titulos.append((nivel, ident, texto))
        return f'<h{nivel} id="{ident}">{conteudo}</h{nivel}>'

    corpo = re.sub(r"<h([23])>(.*?)</h\1>", marcar, corpo, flags=re.S)
    return corpo, titulos


def montar_toc(titulos, paginas):
    itens = []
    for nivel, ident, texto in titulos:
        num = paginas.get(ident, "00")
        itens.append(
            f'<li class="l{nivel}"><a href="#{ident}"><span class="t">{html.escape(texto)}</span>'
            f'<span class="d"></span><span class="n">{num}</span></a></li>'
        )
    return '<ul class="toc">' + "".join(itens) + "</ul>"


def montar_html(corpo, toc, css):
    return (
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        "<title>Relatório de Evolução do Projeto – Equipe Cinza</title>"
        f"<style>{css}</style></head><body>"
        + corpo.replace("<!--TOC-->", toc)
        + "</body></html>"
    )


def imprimir(html_texto, destino):
    chrome = achar_chrome()
    with tempfile.TemporaryDirectory() as perfil:
        arq = PASTA / "_relatorio_tmp.html"
        arq.write_text(html_texto, encoding="utf-8")
        try:
            subprocess.run(
                [
                    chrome,
                    "--headless=new",
                    "--disable-gpu",
                    f"--user-data-dir={perfil}",
                    "--no-pdf-header-footer",
                    f"--print-to-pdf={destino}",
                    arq.as_uri(),
                ],
                check=True,
                timeout=120,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        finally:
            arq.unlink(missing_ok=True)


def paginas_dos_titulos(pdf, titulos):
    """Primeira página (1-based, após o sumário) em que cada título aparece."""
    doc = pymupdf.open(pdf)
    inicio = next(
        (i for i, p in enumerate(doc) if "Sumário" in p.get_text()), 1
    ) + 1
    # pula as páginas do próprio sumário
    while inicio < len(doc) and "Sumário" in doc[inicio].get_text()[:80]:
        inicio += 1
    paginas, cursor = {}, inicio
    for _, ident, texto in titulos:
        chave = re.sub(r"\s+", " ", texto)
        for i in range(cursor, len(doc)):
            blocos = [re.sub(r"\s+", " ", b[4]).strip() for b in doc[i].get_text("blocks")]
            if any(b.startswith(chave) for b in blocos):
                paginas[ident] = str(i + 1)
                cursor = i
                break
    doc.close()
    return paginas


def rodape(pdf_entrada, pdf_saida, rotulo, pular_capa=True):
    doc = pymupdf.open(pdf_entrada)
    total = len(doc)
    for i, pagina in enumerate(doc):
        if i == 0 and pular_capa:
            continue
        y = pagina.rect.height - 28
        pagina.draw_line((57, y - 8), (pagina.rect.width - 57, y - 8), color=(0.7, 0.75, 0.8), width=0.5)
        pagina.insert_text((57, y), rotulo, fontsize=8, fontname="helv", color=(0.35, 0.35, 0.35))
        txt = f"Página {i + 1} de {total}"
        larg = pymupdf.get_text_length(txt, fontname="helv", fontsize=8)
        pagina.insert_text(
            (pagina.rect.width - 57 - larg, y), txt, fontsize=8, fontname="helv", color=(0.35, 0.35, 0.35)
        )
    doc.save(pdf_saida, garbage=3, deflate=True)
    doc.close()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    compacto = "--compacto" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    md = Path(args[0]).resolve() if Path(args[0]).exists() else (PASTA / args[0]).resolve()
    saida = md.with_suffix(".pdf")
    css = (PASTA / "relatorio.css").read_text(encoding="utf-8")
    if compacto:
        css += (PASTA / "relatorio-compacto.css").read_text(encoding="utf-8")
    corpo, titulos = converter(md.read_text(encoding="utf-8"))
    rotulo = "Relatório de Evolução nº 01 | Equipe Cinza | INF 0290 - Projeto de Software | 16/10/2026"

    with tempfile.TemporaryDirectory() as tmp:
        passo1 = os.path.join(tmp, "p1.pdf")
        if compacto:
            imprimir(montar_html(corpo, "", css), passo1)
            rodape(passo1, str(saida), rotulo, pular_capa=False)
            print("PDF gerado:", saida)
            return
        imprimir(montar_html(corpo, montar_toc(titulos, {}), css), passo1)
        paginas = paginas_dos_titulos(passo1, titulos)
        passo2 = os.path.join(tmp, "p2.pdf")
        imprimir(montar_html(corpo, montar_toc(titulos, paginas), css), passo2)
        rodape(passo2, str(saida), rotulo)
    faltando = [t for _, i, t in titulos if i not in paginas]
    if faltando:
        print("Atenção: títulos sem página no sumário:", faltando)
    print("PDF gerado:", saida)


if __name__ == "__main__":
    main()
