import sys
import subprocess

if(sys.argv[1] == "setup"):
    subprocess.call(['python3', 'setup.py', *sys.argv[2:]])
elif(sys.argv[1] == "send"):
    subprocess.call(['python3', 'send_message.py', *sys.argv[2:]])
elif(sys.argv[1] == "receive"):
    subprocess.call(['python3', 'receive_message.py'])
elif(sys.argv[1] == "help"):
    print("setup:")
    print("  chat setup [channel]")
    print("    Changes/sets the pusher channel you want to broadcast and receive messages to and from\n")
    print("  chat setup [channel] [username]")
    print("    Changes/sets both the pusher channel and username you want to use\n")
    print("  chat setup pusher [app id] [app key] [secret] [cluster]")
    print("    Sets up pusher\n")
    print("chat:")
    print("  chat send [message]")
    print("    Broadcasts a message to the pusher channel you've selected\n")
    print("  chat receive")
    print("    Run a listener to the pusher channel you've selected\n")
    print("Run 'chat receive' on a separate console")
else:
    print("Type 'chat help' for guidance")