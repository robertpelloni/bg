import sys

filepath = 'bobsgameweb/src/shared/Config.ts'

with open(filepath, 'r') as f:
    content = f.read()

search = 'export const APP_VERSION = "3.0.10";'
replace = 'export const APP_VERSION = "2.1.100";'

content = content.replace(search, replace)

with open(filepath, 'w') as f:
    f.write(content)
print("done")
