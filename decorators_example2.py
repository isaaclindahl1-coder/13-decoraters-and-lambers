is_admin = False

def admin_required(func):
    def wrapper(*args, **kwargs):
        if is_admin:
            return func(*args,**kwargs)
        else:
            print("Access denied. Admin privileges required")
    return wrapper


@admin_required
def delet_user(username):
    print(f"{username} deleted")

if __name__ == "__main__":
    is_admin = True
    delet_user("jKlins")