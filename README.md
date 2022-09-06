# paper-selector

## How to use

### To add new paperlist:
1. create txt file in 'raws' directory
2. copy paperlist from conference webpage
3. paste 2. to 1.
4. rename the file into format 'cccc-yyyy-raw.txt' e.g.) cvpr-2022-raw.txt
5. Edit run_parser.sh
6. $./run_parser.sh

### To signin as new user
1. Edit run_signin.sh as below 

--user "yourname"
--targets "your" "paperlist" "as many as you want"

2. $./run_signin.sh

### To select papers from paperlist
1. Edit run_selector.sh as below
--user "yourname"
2. $./run_selector.sh
3. Follow instruction on shell prompt
* Press ENTER to pass the paper
* Put in 'exit' to save and exit
