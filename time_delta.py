import datetime
import time

time_now = datetime.datetime.now().timestamp()
hour_ago = (datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp()
print(hour_ago > time_now)
print(time_now - hour_ago)


# # remove To be Processed from categories csv conditionally
# hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
# if (not email_assignment_bot_active) and (email.ReceivedTime.timestamp() < hour_ago.timestamp()):
#         email.Categories = mod_csv(category, "To be Processed")
#         log_output(log_file_path,f"Removed category 'To be Processed' from email from {email_from} with subject {subject} and message ID {message_id} and categories {category}")
# # SAVE Email
# email.save()