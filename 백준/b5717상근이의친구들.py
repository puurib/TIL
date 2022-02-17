from zmq import EVENT_CLOSE_FAILED

while True:
    M, F = map(int, input().split())
    if M + F !=0:
        print(M + F)
    else:
        break