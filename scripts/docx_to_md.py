#!/usr/bin/env python3
"""导出DOCX文字供Git比较；不替代Word文档，不反向生成DOCX。"""
import sys,zipfile
from pathlib import Path
from xml.etree import ElementTree as E
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
src=Path(sys.argv[1]);out=Path(sys.argv[2])
with zipfile.ZipFile(src) as z: root=E.fromstring(z.read('word/document.xml'))
paragraphs=[''.join(p.itertext()) for p in []]
paragraphs=[''.join(t.text or '' for t in p.findall('.//w:t',ns)) for p in root.findall('.//w:p',ns)]
out.write_text('\n\n'.join(p for p in paragraphs if p)+'\n',encoding='utf-8')
