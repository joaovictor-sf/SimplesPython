from pytube import YouTube

while True:
    link = input("Digite o link do vídeo ou 'done' para finalizar o código: ")
    if link == 'done':
            quit()
    try:
        yt = YouTube(link)
    except:
        print("link invalido")
        continue

    print(("Titulo: ", yt.title))
    print("Autor: ", yt.author)
    print("Se deseja realizar o download digite 'y', ")
    print("Se deseja encerrar o codigo digite 'done'")
    print("Se deseja escolher outro link aperte Enter")
    escolha = input()
    if escolha == 'y':
        print("Downloading...")
        yd = yt.streams.get_highest_resolution()
        yd.download('./ytDownloads')
    elif escolha == 'done':
        quit()
