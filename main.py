import pandas as pd
df = pd.read_csv("filename.csv", index_col=0)
print(df)
logon_logoff=(len(df[df['Id'].map(lambda x: x == 4624 or x == 4634)]))
print("Total Logon/logoff events:")
print(logon_logoff)
failed_login=(len(df[df['Id'].map(lambda x: x == 4625)]))
print("Total failed login attempts:")
print(failed_login)
password_change=(len(df[df['Id'].map(lambda x: x == 4723 or x == 4724)]))
print("Total password changes")
print(password_change)
unsuccessful_access=(len(df[df['Id'].map(lambda x: x == 4656 or x == 4661 or x == 4662 or x == 4663 or x == 5136 or x == 5137 or x == 5139)]))
print("Total unsuccessful access to security relevant objects:")
print(unsuccessful_access)
log_clear=(len(df[df['Id'].map(lambda x: x == 104 or x == 1102)]))
print("Total logs cleared:")
print(log_clear)
tasks_created=(len(df[df['Id'].map(lambda x: x == 4698)]))
print("Total tasks created:")
print(tasks_created)