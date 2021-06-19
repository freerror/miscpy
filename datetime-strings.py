import datetime

# Make fstr a Thing(tm)
def fstr(template):
    return eval(f"f'{template}'")

summary_template = '{datetime.datetime.now().date().strftime("%d/%m/%Y")} - Request - Phone Profile - Delete user {email_subject.split("for ")[1].encode("ascii",errors="ignore").decode()}'

print(fstr(summary_template))



# x = datetime.datetime.now().date()

# email_subject = "Off-boarding request for Chris Hinchliffe"

# print(f'{datetime.datetime.now().date().strftime("%d/%m/%Y")} - Request - Phone Profile - Delete user {email_subject.split("for ")[1].encode("ascii",errors="ignore").decode()}')
# print(f'This is the date {datetime.datetime.now().date().strftime("%d/%m/%Y")}')

# email_subject = "Off-boarding request for Chris Hinchliffe"
# email_body = """
# CYBER SECURITY WARNING: This email is from an external source - be careful of attachments and links. Please follow the Cyber Code and report suspicious emails.
# On-boarding/off-boarding workflow notification 
# This is a system generated email. Please do not respond to this notification. 
# ________________________________________
# Please process the off-boarding request for Chris Hinchliffe and advise the status.
# Requestor details 
# Requestor name
# Tamara Horua
# Requestor email
# Tamara.Horua@mbie.govt.nz
# Requestor phone
# +6449018468
# Date requested
# 5/05/2021 9:55 a.m.
#  Person and role
# First name
# Chris
# Last name
# Hinchliffe
# User ID	hinchlc
# Job title
# Triage Advisor
# Type of employment
# Employee
# Group
# Managed Isolation and Quarantine
# Branch
# MIQ National Operations Services
# Unit
# """