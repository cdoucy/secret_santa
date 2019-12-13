from json import load
from sys import exit, stderr
from random import shuffle
from argparse import ArgumentParser
from mail import Mail

def main(argv):
    args = get_args()
    data, addr_list = get_mail_addresses(args.input)
    mail = Mail(args.address, args.port, args.login, args.password)
    secret_santa(addr_list, data, mail)
    del mail
    return 0

def get_args():
    parser = ArgumentParser(description="Secret Santa script. Send an email to each participant with the name of the person to whom he must offer a gift. Hide output if you are participant !")

    parser.add_argument("-i", "--input", required=True, help="Input json file path with email addresses and names.")
    parser.add_argument("-a", "--address", required=True, help="Adress of SMTP server")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port of SMTP server")
    parser.add_argument("-l", "--login", required=True, help="Login of mail account")
    parser.add_argument("-pw", "--password", required=True, help="Password of mail account")

    args = parser.parse_args()
    return args

def get_mail_addresses(path):
    addr_list = []

    try:
        fd = open(path, 'r')
    except:
        print("Error: file not found.", file=stderr)
        exit(2)
    try:
        data = load(fd)
    except:
        print("Error: input file must be in JSON format.", file=stderr)
        fd.close()
        exit(2)
    fd.close()
    for key in [*data]:
        addr_list.append(key)
    return data, addr_list

def secret_santa(addr_list, data, mail):
    size = len(addr_list)

    shuffle(addr_list)
    for i in range(size - 1):
        send_mail(addr_list[i], data[addr_list[i + 1]], i + 1, size, mail)
    send_mail(addr_list[size - 1], data[addr_list[0]], size, size, mail)

def send_mail(addr, name, count, size, mail):
    print("{}/{}".format(count, size))
    print("Sending mail to", addr)
    msg = "Tu dois offrir un cadeau à {} !".format(name)
    mail.send(addr, "Secret Santa", msg)
    print("Mail sended.")