from pytube import YouTube

print("Bem vindo ao YoutuberDownloader")
print("Aqui voce pode baixar videos do youtube com facilidade")

while True:
    link = input("Digite o link do vídeo desejado ou 'done' para finalizar o código: ")
    if link == 'done':
            quit()
    try:
        yt = YouTube(link)
    except:
        print("link inválido")
        continue

    print(("Titulo: ", yt.title))
    print("Autor: ", yt.author)
    print("Se deseja realizar o download digite 'y'")
    print("Se deseja escolher outro link aperte Enter")
    escolha = input()
    if escolha == 'y':
        print("Downloading...")
        yd = yt.streams.get_highest_resolution()
        yd.download('/Users/User/Downloads')
        print("Downloaded")