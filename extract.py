import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', '\n', text)
text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)

print(text.strip())
