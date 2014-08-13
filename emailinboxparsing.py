
##step 1 [in theory somewhat complete], download all e-mails from particular inbox (label)

import sys
import imaplib
import getpass
 
 ##If you'd like to try this, modify the variables with your personal information, i'd recommend setting up a throwaway account.
 ##On a personal gmail account you have to go into settings and enable "Access for less secure apps" in your account permissions

IMAP_SERVER = 'imap.gmail.com'
EMAIL_ACCOUNT = 'gregce.junk@gmail.com'
EMAIL_FOLDER = 'Personal'
OUTPUT_DIRECTORY = '/Users/ceccarelli/email'


PASSWORD = getpass.getpass()
 
def process_mailbox(M):
   #Dump all emails in the folder to files in output directory.
   #
 
    rv, data = M.search(None, 'ALL')
    if rv != 'OK':
        print "No messages found!"
        return
 
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print 'ERROR getting message', num
            return
        print 'Writing message ', num
        f = open('%s/%s.eml' %(OUTPUT_DIRECTORY, num), 'wb')
        f.write(data[0][1])
        f.close()
 
def main():
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print 'Processing mailbox: ', EMAIL_FOLDER
        process_mailbox(M)
        M.close()
    else:
        print 'ERROR: Unable to open mailbox ', rv
    M.logout()
 
if __name__ == '__main__':
    #Run Program
    main()
    
    
##step 2, parse e-mails in directory (or in memory) for specific details job name, etc

##step 3, Create mini report based on comparing consolidation from step 2 to dictionary of known jobs 

##step 4, Send all jobs clear (or not) e-mail to distribution, cleanup downloaded files
