import subprocess

urls = ["https://firefly.adobe.com", "https://poe.com", "https://bard.google.com", "https://notion.so", "https://ai.com"]

command = ['open', '-na', 'Google Chrome', '--args']

for url in urls:
    command.append('--new-tab')
    command.append(url)

subprocess.run(command)

print("🎉 任务已执行")