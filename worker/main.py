#####################################################################################
# GENERAL NOTES
#####################################################################################



#####################################################################################
# Imports and External Refs
#####################################################################################
import sys
import admin
import student



#####################################################################################
# Main
#####################################################################################
def main():
    # get arguments to main call starting after script name
    for arg in sys.argv[1:]:
        if arg == "admin":
            # run the admin gen script 
            admin.main()
        elif arg == "student":
            # run the student gen script
            student.main()
        else:
            print "Error: Invalid arg"
            break

main()
