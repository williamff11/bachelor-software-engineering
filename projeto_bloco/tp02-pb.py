import psutil
import pygame
import cpuinfo

# Iniciando a janela principal
largura_tela = 1240
altura_tela = 760
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Painel")
pygame.display.init()

azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

pygame.font.init()
font = pygame.font.Font(None, 32)


def show_use_memory():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


def show_use_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    info = cpuinfo.get_cpu_info()
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, azul, (20, 250, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(tela, vermelho, (20, 250, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    labels = "Número de núcleos: " + \
        str(info['count']) + ", bits: " + str(info['bits'])
    brand_raw = font.render(
        info['brand_raw'] + " Detalhes: " + str(labels), 1, branco)
    tela.blit(text, (20, 210))
    tela.blit(brand_raw, (20, 330))


def show_use_disk():
    disk = psutil.disk_usage('.')
    total = round(disk.total/(1024*1024*1024))
    used = round(disk.used/(1024*1024*1024))
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, azul, (20, 450, larg, 70))
    larg = larg*disk.percent/100
    pygame.draw.rect(tela, vermelho, (20, 450, larg, 70))
    text = font.render("Uso do Disco Atual (Total: " +
                       str(total) + "GB / Usado: " +
                       str(used) + "GB):" + str(disk.percent) + "%", 1, branco)
    tela.blit(text, (20, 410))


def show_addrs_ip():
    addrs = psutil.net_if_addrs()
    ip = addrs['Ethernet'][1].address
    text = font.render("IP: " + str(ip), 1, branco)
    tela.blit(text, (largura_tela/2 - 80, 560))


    # Cria relógio
clock = pygame.time.Clock()

cont = 60

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        show_use_memory()
        show_use_cpu()
        show_use_disk()
        show_addrs_ip()
        cont = 0

    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(500)
    cont = cont + 1

# Finaliza a janela
pygame.display.quit()
