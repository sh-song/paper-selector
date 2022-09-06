import os, json
import argparse
import pandas as pd
class Selector:
    def __init__(self, config):
        self.user_name = config['user_name']
        self.user_dir = config['user_dir']
        self.file_list = config['file_list']
        self.paperlist_name = ''
        self.paperlist = None
        self.current_point = -1
    def select_paperlist(self):
        for i, filename in enumerate(self.file_list):
            print(f"{i}. {filename}")
            
        userinput = input('select paperlist: ')
        self.paperlist_name = self.file_list[int(userinput)] 
        print(f"{self.paperlist_name} is selected.")

    def load_paperlist(self):
        paperlist_dir = self.user_dir + '/' + self.paperlist_name
        self.paperlist = pd.read_csv(paperlist_dir)

    def check_startpoint(self):
        paperlist_size = self.paperlist.shape[0] -1 #except tags
        for i in range(paperlist_size):
            checked = self.paperlist.loc[i, 'checked']
            if checked == 0:
                self.current_point = i
                break

    def select_paper(self):
        papername = self.paperlist.loc[self.current_point, 'name']
        YELLOW = '\033[33m'
        COLORRESET = '\033[0m' 
        papername_with_color = YELLOW + papername + COLORRESET
        userinput = input(papername_with_color + '\n')

        if userinput== '':
            print('pass\n')
        elif userinput == 'exit':
            print('exit\n')
            return False
        else:
            self.paperlist.loc[self.current_point, 'selected'] = 1
            print('select\n')

        self.paperlist.loc[self.current_point, 'checked'] = 1
        self.current_point +=1        
        
        return True
    def save_csv(self):
        self.paperlist.to_csv(self.user_dir + '/' + self.paperlist_name, index=False)
        print(f"{self.user_dir + '/' + self.paperlist_name} saved.")

    def run(self):
        self.select_paperlist()
        self.load_paperlist()
        self.check_startpoint()

        is_on = True
        while is_on:
            is_on = self.select_paper()

        self.save_csv()        
if __name__ == "__main__":

    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        '--user',
        default='user',
        help='user name'
    )
    args = argparser.parse_args()

    
    path = 'users/' + args.user
    print('path: ', path)
    with open(os.path.join(path,("config.json")),'r') as fp :
        config = json.load(fp)

    ss = Selector(config)
    ss.run()