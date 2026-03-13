import re
for f in ['index.html', 'en/index.html']:
    with open(f) as fh: html = fh.read()
    fixed = re.sub(
        r'<a href="/cdn-cgi/l/email-protection[^"]*" class="ct-val">.*?</a>',
        '<a href="mailto:enrique@azlyc.com" class="ct-val">enrique@azlyc.com</a>',
        html, flags=re.DOTALL
    )
    with open(f, 'w') as fh: fh.write(fixed)
    print(f, 'ok')
