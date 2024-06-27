from bs4 import BeautifulSoup
import requests

trabajosInfo = []
nombresTrabajos = []

for i in range(66):
    url_base = "https://empleos.educacionit.com/index.php?pageID="+str(i)
    pedido = requests.get(url_base)
    htmlObtenido = pedido.text
    soup = BeautifulSoup(htmlObtenido, "html.parser")
    trabajos = soup.find_all("p", class_="fs12 lh13 mt10 mb10")
    nombres = soup.find_all("a", class_="fw600")
    for parrafo in trabajos:
        trabajo = "https://empleos.educacionit.com/" + parrafo.a["href"]
        trabajosInfo.append(trabajo)

    for nombre in nombres:
        titulo = nombre.get_text()
        nombresTrabajos.append(titulo)

for i, trabajo in enumerate(trabajosInfo):
    print(f"Se encontro el trabajo {nombresTrabajos[i]} el link es: {trabajo}")