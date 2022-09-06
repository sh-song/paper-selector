import argparse
import os
import shutil

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

user_dir = 'users/' + args.user_name
if os.path.isdir(user_dir) == False:
    os.mkdir(user_dir)
    print(f"User directory '{args.user_name}' is created.")
else:
    print(f"User directory '{args.user_name}' already exists.")

for item in args.targets:
    filename = item + '.csv'
    if not os.path.exists(user_dir + '/' + filename):
        try:
            shutil.copy('csvs/' +  filename, user_dir)
            print(f"{filename} copied to {user_dir}")
        except FileNotFoundError as e:
            print(e)
    else:
        print(f"{user_dir + '/' + filename} already exists.")