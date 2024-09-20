import os

WOKRDIR = os.getcwd()

if not os.path.isfile('info.csv'):
     with open('info.csv', 'w') as csv:
          csv.write('123456,passwd,pepa\n')

if not os.path.isdir('built'):
     os.mkdir('built/tests')
else:
     os.system('rm -rf built/tests')
os.mkdir('built/tests')
assert os.path.isdir('built/tests')

os.system('cp tpl/test-0.py built/tests/test_0.py')

with open('info.csv') as csv:
     users = [_.split(',') for _ in csv.read().split()]

with open('tpl/test-user.py') as tpl_user:
     tpl_user = tpl_user.read()
with open('tpl/test-check.py') as tpl_check:
     tpl_check = tpl_check.read()

for user in users:
     with open(f'built/tests/test_user_{user[0]}.py', 'w') as test_user:
          test_user.write(tpl_user % (user[0], user[1]))
     with open(f'built/tests/test_check_{user[0]}.py', 'w') as test_check:
          test_check.write(tpl_check % (user[0], user[1]))

with open('tpl/slave.sh') as tpl_slave:
     with open('built/slave.sh', 'w') as new_slave:
          new_slave.write(tpl_slave.read() % WOKRDIR)

with open('tpl/lili.tab') as file:
     jobs = [
          job % WOKRDIR for job in file.readlines() if job.count('check') > 0
     ]

with open('built/lili.tab', 'w') as file: file.writelines(jobs)

os.system('crontab -l > built/join.tab')
os.system('cat built/lili.tab >> built/join.tab')
print('temp cron content:')
os.system('cat built/join.tab')
if input('do you wish to implement into `crontab`? [y/N] ') == 'y':
     os.system('crontab built/join.tab')
     print('`crontab` updated')
else:
     print('temp file in project directory for manual use.')
