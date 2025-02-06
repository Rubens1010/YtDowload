from pytube import YouTube

def baixar_video(url):
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)  # Usa autenticação OAuth se necessário
        stream = yt.streams.get_highest_resolution()
        print(f"Baixando: {yt.title}")
        stream.download()
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    url = input("Digite o link do vídeo do YouTube: ")
    baixar_video(url)
