# Luiz Machado · Soluções digitais

Portfólio de Luiz Machado: sites, sistemas completos, dashboards Power BI, automações e motion design.

**No ar:** https://luiz-machado.vercel.app

## Stack
- HTML, CSS e JavaScript puro (sem framework, sem build de bundler)
- [GSAP 3.12.5](https://gsap.com) + ScrollTrigger para animações ligadas à rolagem
- [Lenis 1.1.13](https://lenis.darkroom.engineering) para rolagem suave
- Fontes: Archivo, Geist e Geist Mono (Google Fonts)
- Hospedagem estática na Vercel

## Estrutura
```
portfolio-luiz.html   código-fonte do site (um arquivo)
assets/               imagens usadas no site (.webp)
cv/                   currículos em PDF
scripts/build_site.py monta a pasta site/ para publicação
site/                 versão publicada (index.html, favicon, vercel.json)
```

## Atualizar o site
```bash
python scripts/build_site.py .
```
Depois faça commit e push: a Vercel publica a pasta `site/` automaticamente.
