# secret_santa

usage: secret_santa [-h] -i INPUT -a ADDRESS -p PORT -l LOGIN -pw PASSWORD

Secret Santa script. Send an email to each participant with the name of the
person to whom he must offer a gift. Hide output if you are participant !

optional arguments:

  -h, --help            show this help message and exit
  
  -i INPUT, --input INPUT
                        Input json file path with email addresses and names.
                        
  -a ADDRESS, --address ADDRESS
                        Adress of SMTP server
                        
  -p PORT, --port PORT  Port of SMTP server
  
  -l LOGIN, --login LOGIN
                        Login of mail account
                        
  -pw PASSWORD, --password PASSWORD
                        Password of mail account

Input json file must be like this:

{
    "player.one@mail.com": "Player One",
    "player.two@mail.com": Player Two",
    ...
}
