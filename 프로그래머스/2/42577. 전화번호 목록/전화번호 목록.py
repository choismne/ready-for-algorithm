def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if hash(phone_book[i]) == hash(phone_book[i+1][:length]):
            return False
    return True
            