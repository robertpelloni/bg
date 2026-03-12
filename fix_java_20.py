import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = []
    in_enum = False
    
    for line in lines:
        stripped = line.strip()
        
        # Remove forward declarations
        if re.match(r'^public\s+class\s+[A-Za-z0-9_]+;$', stripped): continue
        
        # Fix enum class
        if 'enum AnimationState' in line:
            line = line.replace('enum AnimationState', 'enum AnimationState {')
            in_enum = True
        
        if in_enum:
            line = line.replace('public ', '')
            if '};' in line:
                line = line.replace('};', '}')
                in_enum = False
        
        # Remove artifacts
        if 'this->' in line: continue
        if 'return _stopThread' in line: continue
        if stripped == '};' or stripped == '};': continue
        if 'public };' in line: continue
        if 'public template' in line: continue
        if 'public typedef' in line: continue
        if 'public mutex' in line: continue
        if 'public condition_variable' in line: continue
        if 'public thread' in line: continue
        if 'public return ' in line: continue
        if 'boost::' in line: continue
        
        # Fix pointers
        line = re.sub(r'([A-Za-z0-9_]+)\s*\*\s*([a-zA-Z_])', r'\1 \2', line)
        line = line.replace('*', '')
        
        # Fix repeated public
        line = line.replace('public public', 'public')
        
        # Fix const
        line = line.replace('public const ', 'public ')
        
        # Fix nullptr
        line = line.replace('nullptr', 'null')
        
        out.append(line)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write("".join(out))

for filename in os.listdir(base_path):
    if filename.endswith('.java'):
        clean_file(os.path.join(base_path, filename))

print("Cleaned all puzzle files")
