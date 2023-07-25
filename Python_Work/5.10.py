current_users = ['kloosman', 'yunus', 'sas', 'ar12', 'yoyoman']
new_users = ['mcbeast', 'yoyoman', 'bucksfan', 'AR12', 'fib']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry username {new_user} is unavailable.")