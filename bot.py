import random

# Define patterns and responses
patterns = {
    #INTRO
    'hello': ['Hi!', 'Hello!', 'Hey there!'],
    'how are you': ['I\'m good, thanks!', 'I\'m doing well, how about you?'],
    'what is your name': ['I am sara.', 'You can call me nevia.'],
    'default': ['I\'m not sure how to respond to that.', 'Could you please rephrase that?'],
    'where are you from': ['I\'m from jaipur'],
    'age': ['I don\'t have an age. I\'m just a computer program.'],
    'who created you': ['I was created by Animo Tanixome & Ankit shukla.','My creator are the brilliant minds at cwc.'],
    'how can you help': ['I can assist with general information, answer questions, and more. Just ask!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Have a great day!'],
    'who are you': ['I\'m Sara'],
    # request methods
    'request method':['''
            * TYPES OF REQUEST METHODS *
    ~ GET          ==>      data transfer through url easily visible'],
    ~ HEAD         ==>      same as get but transfers the states link and headers section only'],
    ~ post         ==>      sends user information & file in body, to server using html forms'],
    ~ PUT          ==>      vulnarable method! Replaces all current representations of the target resource with the upload contant'],
    ~ DELETE       ==>      vulnarable method! Removes all current representations of the target resources with the given url'],
    ~ OPTIONS      ==>      describe the communication options for the target resource'],
    ~ TRACE        ==>      performs a massage loop-back test along the path to target resource'],
    ~ CONNECT      ==>      established a tunnel to the server identified given by the url'],
    '''],
    #file system
    'file system':['''
            * BASIC FILE SYSTEM OF LINUX *
            
    /bin          : basic programs (ls, cd, mv etc...),
    /sbin         : system programs (fdisks, systemctl, mkfs etc...),
    /etc          : configurations files,
    /temp         : temporary files,
    /usr/bin      : preinstalled applications (apt,nmap),
    /usr/share    : Application support files & data files,
    /home         : personal directory of user's
    /root         : home directory of super user ADMIN,
    /etc/host     : IP localhost,
    /var/www/html : HTML file (index.html) local host site's page,
    shell files   : /bin/sh   /bin/bash    /bin/zsh,
    /var/lib/tor/hidden_services/hostname : tor's .onion site link   
    '''],
    #PROTOCOLS
    'types of protocol':['''
              * TYPES OF PROTOCOLS *
       
    TCP/IP MODEL        ~       INTERNET PROTOCOL SUITE
    
    ~ APPLICATION     ==>      telnet,SMTP,POP3,FTP,NTP,HTTP,SNMP,DNS,SSH
    ~ TRANSPORT       ==>      TCP, UDP
    ~ INTERNET        ==>      IP,ICMP,ARP,DHCP
    ~ NETWORK         ==>      ETHERNET,PPP,ADSL    
    '''],
    #FLAGS
    'flags':['''
                 * FLAGS      <==>        WORKING *
         
      ~ URG : URGENT           ==>     the contained in the packet should be process immedetly
      ~ SYN : SYNCHRONIZE      ==>     initiates a connections between host
      ~ ACK : ACKNOWLEDGEMENT  ==>     acknowledges the receipt of a packet
      ~ RST : RESET            ==>     reset a connections
      ~ FIN : FINISH           ==>     there will be no further transmission
      ~ PSH : PUSH             ==>     sends all buffer data immediatly
    
    '''],
    '4 layers':['''
           * OSI     vs     TCP/IP MODEL  ( 4 LAYERS) *     

    ~ APPLICATION-----\\n
    ~ PRESENTATIONS    }---> APPLICATION LAYER
    ~ SESSION---------/
    
    ~ TRANSPORT-----------}> TRANSPORT LAYER
    
    ~ NETWORK-------------}> INTERNET LAYER
    
    ~ DATA LINK-------\\n
                       }---> NETWORK ACCESS LAYER
    ~ PHYSICAL--------/
    '''],
}


def respond(user_input):
    user_input = user_input.lower()

    for pattern, responses in patterns.items():
        if pattern in user_input:
            return random.choice(responses)

    return random.choice(patterns['default'])


# Main interaction loop
print("Sara: Hi! I'm your friendly Sara. How can I help you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Sara: Goodbye! Have a great day!")
        break

    response = respond(user_input)
    print(f"Sara: {response}")


