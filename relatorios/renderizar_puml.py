"""Renderiza arquivos PlantUML (.puml) para PNG usando o serviço oficial do PlantUML.

Uso:
    python relatorios/renderizar_puml.py AppsUFG
    python relatorios/renderizar_puml.py Seguranca
    python relatorios/renderizar_puml.py Locais
    python relatorios/renderizar_puml.py --tudo
"""
import sys
import zlib
import urllib.request
from pathlib import Path

def encode_plantuml(text: str) -> str:
    """Codifica o texto PlantUML no formato aceito pela URL do servidor oficial."""
    z = zlib.compress(text.encode("utf-8"))[2:-4]
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    res = []
    for i in range(0, len(z), 3):
        b1 = z[i]
        b2 = z[i + 1] if i + 1 < len(z) else 0
        b3 = z[i + 2] if i + 2 < len(z) else 0
        res.append(alphabet[b1 >> 2])
        res.append(alphabet[((b1 & 0x3) << 4) | (b2 >> 4)])
        if i + 1 < len(z):
            res.append(alphabet[((b2 & 0xF) << 2) | (b3 >> 6)])
        if i + 2 < len(z):
            res.append(alphabet[b3 & 0x3F])
    return "".join(res)

def renderizar_arquivo(caminho_puml: Path) -> bool:
    """Renderiza um único arquivo .puml gerando o .png ao lado."""
    caminho_png = caminho_puml.with_suffix(".png")
    try:
        texto = caminho_puml.read_text(encoding="utf-8")
        url = "http://www.plantuml.com/plantuml/png/" + encode_plantuml(texto)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            caminho_png.write_bytes(resp.read())
        print(f"[OK] {caminho_puml.name} -> {caminho_png.name}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao renderizar {caminho_puml.name}: {e}")
        return False

def main():
    raiz = Path(__file__).resolve().parent.parent
    if len(sys.argv) < 2 or sys.argv[1] == "--tudo":
        alvos = [p for p in raiz.glob("*/*.puml")]
    else:
        arg = Path(sys.argv[1])
        caminho = arg if arg.is_absolute() else raiz / arg
        if caminho.is_file() and caminho.suffix == ".puml":
            alvos = [caminho]
        elif caminho.is_dir():
            alvos = list(caminho.glob("*.puml"))
        else:
            print(f"Caminho não encontrado: {caminho}")
            return

    print(f"Renderizando {len(alvos)} diagrama(s)...")
    sucessos = sum(1 for p in alvos if renderizar_arquivo(p))
    print(f"Concluído: {sucessos}/{len(alvos)} diagramas renderizados com sucesso.")

if __name__ == "__main__":
    main()

