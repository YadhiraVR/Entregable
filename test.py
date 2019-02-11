from cliente import listar

if __name__ == '__main__':
    base_url = "http://localhost:4000/"
    rpta = listar(base_url)
    print(rpta)