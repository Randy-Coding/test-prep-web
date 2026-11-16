from pathlib import Path
import xml.etree.ElementTree as E
import zipfile,re,pprint
ROOT=Path.cwd()
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
def text(el):
 return '\n'.join(''.join(t.text or '' for t in p.findall('.//a:t',ns)) for p in el.findall('.//a:p',ns)).strip()
def parts(root):
 out=[]
 for el in root.find('p:cSld/p:spTree',ns):
  if el.tag.endswith('}sp'):
   s=text(el)
   if s: out.append(s)
  elif el.tag.endswith('}graphicFrame'):
   for tbl in el.findall('.//a:tbl',ns):
    rows=[[text(c).replace('\n',' ') for c in row.findall('a:tc',ns)] for row in tbl.findall('a:tr',ns)]
    widths=[max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    out.append('```text\n'+'\n'.join('  '.join(c.ljust(widths[i]) for i,c in enumerate(row)).rstrip() for row in rows)+'\n```')
 return out
def fmt(s):
 if s.startswith('```'): return s
 if re.match(r'(?:int\s+|pid_t\s+|volatile sig_atomic_t\s+|void h\(|while \(head|printf\(|I\.\s+free\()',s):
  return '```c\n'+s+'\n```'
 return s.replace('\n',' ')
def topic(n):
 for end,name in [(6,'processes'),(11,'signals'),(21,'virtual memory'),(29,'heap memory'),(39,'general concepts'),(44,'HW3 [Compiler]'),(49,'HW4 [Pages]'),(54,'HW5 [Shell]')]:
  if n<=end:return name+' review session'
slides={}
with zipfile.ZipFile(ROOT/'cse320/midterm-2/CSE 320 MT2 Review Session.pptx') as z:
 for name in z.namelist():
  m=re.fullmatch(r'ppt/slides/slide(\d+)\.xml',name)
  if m: slides[int(m[1])]=parts(E.fromstring(z.read(name)))
groups={}
for i,ps in sorted(slides.items()):
 m=re.match(r'(Question|Answer) (\d+)',ps[0])
 if m:groups.setdefault(int(m[2]),{'Question':[],'Answer':[]})[m[1]].append((i,ps))
assert set(groups)==set(range(1,55))
bank={}
for n,g in groups.items():
 qparts=[];seen=set();choices={}
 for i,ps in g['Question']:
  for s in ps[1:]:
   if s in seen:continue
   seen.add(s)
   m=re.match(r'^([ABC])\.\s+(.*)',s,re.S)
   if m:choices[m[1]]=m[2].replace('\n',' ');continue
   if s.startswith('Bottom tables 0'):continue
   qparts.append(fmt(s))
 assert set(choices)==set('ABC'),n
 # Preserve the source's three choices inline: the app's structured MCQ format
 # requires four choices, so use its existing open-response/reveal format.
 title=re.sub(r'Question \d+(?: \(\d+/\d+\))?:\s*','',g['Question'][0][1][0])
 prompt=f'Question {n}: {title}\n\n'+'\n\n'.join(qparts)+'\n\n'+'\n'.join(f'{k}. {v}' for k,v in choices.items())
 correct={re.search(r'Correct: ([ABC])',ps[0])[1] for i,ps in g['Answer']}
 assert len(correct)==1
 letter=correct.pop()
 explanation='\n\n'.join('\n\n'.join(fmt(s) for s in ps[1:]) for i,ps in g['Answer']).strip()
 record={'id':f'RS{n:02}','subcategory':title,'answer':f'{letter}. {choices[letter]}','sources':[f'CSE 320 MT2 Review Session.pptx, slides '+', '.join(str(i) for i,ps in g['Question']+g['Answer'])], 'review_question':n, 'question_slides':[i for i,ps in g['Question']], 'answer_slides':[i for i,ps in g['Answer']]}
 if explanation:record['explanation']=explanation
 bank.setdefault(topic(n),{})[prompt]=record
path=ROOT/'question_banks/CSE320_MT2.py'
original=path.read_bytes()
(ROOT/'tmp/mt2_before_review.py').write_bytes(original)
assert b'# Review session questions (RS01-RS54)' not in original
with path.open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n\n# Review session questions (RS01-RS54). Each numbered question appears once.\n# Multi-slide prompts and answers are consolidated; page tables remain embedded.\n# Three source choices are kept inline for the existing answer-reveal format.\nquestions.update('+pprint.pformat(bank,width=110,sort_dicts=False)+')\n')
print({k:len(v) for k,v in bank.items()})
