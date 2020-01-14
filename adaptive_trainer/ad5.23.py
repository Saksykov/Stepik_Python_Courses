# Annoying input
def get_int(start_message, error_message, end_message):
    cnt = 0
    while True:
        if cnt == 0:
            print(start_message)
            cnt = 1
        try:
            b = int(input())
            print(end_message)
            return b
        except ValueError:
            print(error_message)