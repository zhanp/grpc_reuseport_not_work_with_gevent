import multiprocessing


def run():
    import greeter_server
    greeter_server.serve()


if __name__ == '__main__':
    for i in range(2):
        p = multiprocessing.Process(target=run)
        p.start()
