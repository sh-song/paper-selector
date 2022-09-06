import argparse
import os
import shutil
import json

argparser = argparse.ArgumentParser()

argparser.add_argument(
    '--user_name',
    default='user',
    help='user name'
)
argparser.add_argument(
    '--targets',
    default='cvpr-2022',
    help='target conferences',
    type=str,
    nargs='+'
)

args = argparser.parse_args()
data = {}
data['user_name'] = args.user_name
data['user_dir'] ='users/' + args.user_name

if os.path.isdir(data['user_dir']) == False:
    os.mkdir(data['user_dir'])
    print(f"User directory '{data['user_name']}' is created.")
else:
    print(f"User directory '{data['user_name']}' already exists.")

data['file_list'] =[]
for item in args.targets:
    filename = item + '.csv'
    data['file_list'].append(filename)
    if not os.path.exists(data['user_dir'] + '/' + filename):
        try:
            shutil.copy('csvs/' +  filename, data['user_dir'])
            print(f"{filename} copied to {data['user_dir']}")
        except FileNotFoundError as e:
            print(e)
    else:
        print(f"{data['user_dir'] + '/' + filename} already exists.")

with open(data['user_dir'] + '/' + 'config.json', 'w') as fp:
    json.dump(data, fp)