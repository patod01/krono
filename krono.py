import os

WOKRDIR = os.getcwd()

if not os.path.isfile('info.csv'):
     with open('info.csv', 'w') as csv:
          csv.write('123456,passwd,pepa\n')

if not os.path.isdir('built'):
     os.mkdir('built')
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

with open('tpl/lili.tab') as lili:
     jobs = [
          job % WOKRDIR for job in lili.readlines() if job.count('check') > 0
     ]

with open('built/lili.tab', 'w') as lili: lili.writelines(jobs)

os.system('crontab -l > built/join.tab')
os.system('printf "#\n#^# OLD CRONTAB JOBS #^#\n" >> built/join.tab')
os.system('printf "### NEW CRONTAB JOBS ###\n#\n" >> built/join.tab')
os.system('cat built/lili.tab >> built/join.tab')
os.system('crontab -T built/join.tab')

print('-> `join.tab` content:\n')
os.system('cat built/join.tab')
print('\n-> You can edit this file at `built` prior to input the following answer.')
print('-> Do you wish to implement into `crontab`? [y/N] ')
if input('<: ') == 'y':
     os.system('crontab built/join.tab')
     print('-> `crontab` updated!')
else:
     print('-> Old `crontab` preserved.')
