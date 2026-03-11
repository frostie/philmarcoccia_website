const fs = require('fs');

let text = fs.readFileSync('index.html', 'utf-8');
text = text.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
text = text.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
text = text.replace(/<!--[\s\S]*?-->/g, '');
text = text.replace(/<[^>]+>/g, '\n');
text = text.replace(/\n\s*\n\s*\n/g, '\n\n');

console.log(text.trim());
