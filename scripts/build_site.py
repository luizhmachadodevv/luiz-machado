import os, shutil, sys
root = sys.argv[1]
src = os.path.join(root, 'portfolio-luiz.html')
out = os.path.join(root, 'site')
os.makedirs(out, exist_ok=True)
for name in ('assets', 'cv', 'index.html', 'favicon.svg', 'vercel.json'):
    t = os.path.join(out, name)
    if os.path.isdir(t):
        shutil.rmtree(t)
    elif os.path.exists(t):
        os.remove(t)
for d in ('assets', 'cv'):
    os.makedirs(os.path.join(out, d))
for f in ('luiz-terno.webp', 'luiz-terno-cyber.webp'):
    shutil.copy(os.path.join(root, 'assets', f), os.path.join(out, 'assets', f))
for f in os.listdir(os.path.join(root, 'cv')):
    shutil.copy(os.path.join(root, 'cv', f), os.path.join(out, 'cv', f))

body = open(src, encoding='utf-8').read()
# split the head-ish part (metas, title, links, style) from the body markup
cut = body.index('</style>') + len('</style>')
head_part, body_part = body[:cut], body[cut:]
for tag in ('<meta charset="utf-8">\n', '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'):
    head_part = head_part.replace(tag, '')
head_part = head_part.replace('<title>Luiz Machado Portfolio</title>', '<title>Luiz Machado · Soluções digitais</title>')

favicon = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120"><rect width="120" height="120" rx="24" fill="#0A0B08"/>'
           '<g fill="#D4FF3A" stroke="#0A0B08" stroke-width="2.6" paint-order="stroke">'
           '<path d="M22 58 H40 V94 H52 V112 H22 Z"/><path d="M46 58 H57 L68 76 L79 58 H98 V112 H82 V84 L68 102 L56 84 V88 H46 Z"/></g>'
           '<g fill="#D4FF3A">' + ''.join(
               f'<circle cx="{28+i*8}" cy="{48-abs(4-i)*-2 - (8 - abs(4-i)*2)}" r="5"/>' for i in range(9)) +
           '</g></svg>')
open(os.path.join(out, 'favicon.svg'), 'w', encoding='utf-8').write(favicon)

desc = 'Luiz Machado: sites, sistemas completos, dashboards Power BI, automações e motion design. Do briefing ao deploy, em Curitiba.'
html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A0B08">
<meta property="og:type" content="website">
<meta property="og:title" content="Luiz Machado · Soluções digitais">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/luiz-terno.webp">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" as="image" href="assets/luiz-terno.webp">
<link rel="preload" as="image" href="assets/luiz-terno-cyber.webp">
{head_part}
<style>html,body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{body_part}
</body>
</html>
'''
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(html)
open(os.path.join(out, 'vercel.json'), 'w', encoding='utf-8').write('{\n  "cleanUrls": true,\n  "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}]\n}\n')
print('built', sorted(os.listdir(out)))
