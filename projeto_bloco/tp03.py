import platform
import re
import sys
import cpuinfo
from urllib.request import urlopen

import psutil
import pygame
from pygame.locals import *


# INICIALIZAÇÃO
pygame.init()
CLOCK = pygame.time.Clock()
HZ = 60

# CONFIGURAÇÃO JANELA PRINCIPAL
LARGURA_TELA = 600
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Painel De Recursos")

# CORES
VERMELHO = (242, 27, 63)
WINE = (97, 3, 69)
PASTEL = (241, 233, 219)
AZUL_PISCINA = (93, 183, 222)
SALMAO = (239, 111, 108)

# FONTES
pygame.font.init()
TITLE_FONT = pygame.font.SysFont("roboto-mono", 60)
INFO_FONT = pygame.font.SysFont("roboto", 18)
INFO_BOLD_FONT = pygame.font.SysFont("roboto-mono", 26)
SUBINFO_BOLD_FONT = pygame.font.SysFont("roboto-mono", 20)
PERCENT_FONT = pygame.font.SysFont("noto-serif", 26)
PERCENT_PROC_FONT = pygame.font.SysFont("noto-serif", 20)

TAM_TELA = (LARGURA_TELA, 500)
TAM_SETA = (LARGURA_TELA, 100)

THICKNESS = 10

info_cpu = cpuinfo.get_cpu_info()


def show_cpu():
    info_cpu = cpuinfo.get_cpu_info()
    uso_cpu = psutil.cpu_percent(percpu=True)
    tela_02 = pygame.Surface(TAM_TELA)
    tela_02.fill(PASTEL)

    titulo = TITLE_FONT.render("Processador", True, WINE)
    tela_02.blit(titulo, (40, 20))
    # Informações
    marca = "{}".format(info_cpu['brand_raw'])
    more_infos = "Clock: {} GHz | bits: {} bits | Arch: {}".format(
        psutil.cpu_freq().current/1000, info_cpu['bits'], info_cpu['arch'])
    system_operation = "SO: {} ({})".format(
        platform.system(), platform.platform())
    freq = "Frequência: {}Mhz / {}Mhz".format(
        psutil.cpu_freq().current, psutil.cpu_freq().max)
    more_infos_render = INFO_FONT.render(more_infos, True, WINE)
    system_operation_render = INFO_FONT.render(system_operation, True, WINE)
    marca_render = INFO_FONT.render(marca, True, WINE)
    numero_nucleos = "Threads e Núcleos: {} threads e {} núcleos".format(
        psutil.cpu_count(),  psutil.cpu_count(logical=False))
    freq_obj = INFO_FONT.render(freq, True, WINE)
    numero_nucleos_render = INFO_FONT.render(numero_nucleos, True, WINE)
    tela_02.blit(marca_render, (310, 70))
    tela_02.blit(more_infos_render, (310, 95))
    tela_02.blit(system_operation_render, (310, 120))
    tela_02.blit(freq_obj, (310, 142))
    tela_02.blit(numero_nucleos_render, (310, 165))

    bar = 0
    end_bar = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    for i in uso_cpu:
        percentage = "{}%".format(i)
        percentagem_uso = PERCENT_PROC_FONT.render(percentage, True, WINE)
        tela_02.blit(percentagem_uso, (15, 200 + bar))

        pygame.draw.rect(tela_02, SALMAO, (60, 200 + bar,
                                           end_bar, THICKNESS))
        end_bar_uso = end_bar * (i / 100)
        pygame.draw.rect(tela_02, VERMELHO, (60, 200 +
                                             bar, end_bar_uso, THICKNESS))
        bar += 25
    TELA.blit(tela_02, (0, 0))


def show_use_memory():
    memoria = psutil.virtual_memory()
    tela_01 = pygame.Surface(TAM_TELA)
    tela_01.fill(PASTEL)
    # Posições em pixels
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(tela_01, SALMAO, (70, pos_altura_barra,
                                       pos_final_barra, THICKNESS))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (memoria.percent / 100)
    pygame.draw.rect(tela_01, VERMELHO, (70, pos_altura_barra,
                                         pos_final_barra_uso, THICKNESS))

    # Início Textos
    perc_texto = "{}%".format(memoria.percent)

    titulo = INFO_BOLD_FONT.render(
        f"Uso de Memória (Total: {round(memoria.total / (1024.0 ** 3), 0)}) GB", True, WINE)
    percentagem_uso = PERCENT_FONT.render(perc_texto, True, WINE)
    tela_01.blit(titulo, (40, 20))
    tela_01.blit(percentagem_uso, (15, pos_altura_barra))

    # Memoria Física total
    free_memory = "Memória em uso: {:.2f} GB | Memória livre: {:.2f} GB".format(memoria.used / (1024.0 ** 3),
                                                                                memoria.free / (1024.0 ** 3))
    free_memory_render = INFO_FONT.render(free_memory, True, WINE)
    tela_01.blit(free_memory_render,
                 (LARGURA_TELA // 5, pos_altura_barra + 20))
    TELA.blit(tela_01, (0, 0))


# Disco
def show_use_disk():
    disk = verifica_discos()
    tela_03 = pygame.Surface(TAM_TELA)
    tela_03.fill(PASTEL)
    # Posições em pixels
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(tela_03, SALMAO, (70, 110,
                                       pos_final_barra, THICKNESS))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (disk[5] / 100)
    pygame.draw.rect(tela_03, VERMELHO, (70, 110,
                                         pos_final_barra_uso, THICKNESS))

    # Início Textos
    perc_texto = "{}%".format(disk[5])

    titulo = TITLE_FONT.render("Espaço Total em Disco", True, WINE)
    percentagem_uso = PERCENT_FONT.render(perc_texto, True, WINE)
    tela_03.blit(titulo, (40, 20))
    tela_03.blit(percentagem_uso, (15, 110))

    # Espaço total

    qnt = "Quantidade de discos: {:g}".format(round(disk[0]))
    qnt_render = INFO_FONT.render(qnt, True, WINE)
    disks = "Esses foram os discos encontrados: {}".format(disk[1])
    disks_render = INFO_FONT.render(disks, True, WINE)
    tela_03.blit(
        qnt_render, (pos_final_barra - 160, 130))
    tela_03.blit(
        disks_render, (pos_final_barra - 160, 150))

    # Espaço livre/ocupado no hd
    free = "Espaço livre: {:.2f} GB".format(disk[4] / (1024.0 ** 3))
    fill = "Espaço usado: {:.2f} GB".format(disk[3] / (1024.0 ** 3))
    free_render = INFO_FONT.render(free, True, WINE)
    fill_render = INFO_FONT.render(fill, True, WINE)
    tela_03.blit(free_render, (70, 130))
    tela_03.blit(fill_render, (70, 150))
    TELA.blit(tela_03, (0, 0))


# Rede
def show_addrs_ip():
    # Interface de rede terá que ser colocada manualmente, variação muito grande.
    INTERFACE_REDE = "Wi-Fi"

    dic_interfaces = psutil.net_if_addrs()
    ip_rede = dic_interfaces[INTERFACE_REDE][1].address
    net_mask = dic_interfaces[INTERFACE_REDE][1].netmask
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_netmask = "Máscara de Sub-rede: {}".format(net_mask)
    ip_local_render = TITLE_FONT.render(ip_local, True, WINE)
    ip_netmask_render = SUBINFO_BOLD_FONT.render(ip_netmask, True, WINE)
    tela_04 = pygame.Surface(TAM_TELA)
    tela_04.fill(PASTEL)
    titulo = TITLE_FONT.render("Rede", True, WINE)
    tela_04.blit(titulo, (40, 20))
    tela_04.blit(ip_local_render, (20, 200))
    tela_04.blit(ip_netmask_render, (20, 290))

    TELA.blit(tela_04, (0, 0))


def resumo():
    tela_05 = pygame.Surface(TAM_TELA)
    tela_05.fill(PASTEL)

    # Título
    titulo = TITLE_FONT.render("Resumo", True, WINE)
    tela_05.blit(titulo, (40, 20))

    # memoria
    memoria = psutil.virtual_memory()
    perc_memory_texto = "Memória em uso: {}%".format(memoria.percent)

    percentagem_uso = PERCENT_FONT.render(perc_memory_texto, True, WINE)
    tela_05.blit(percentagem_uso, (40, 95))

    # cpu
    uso_cpu = psutil.cpu_percent(interval=0)

    perc_cpu_texto = "CPU em uso: {}%".format(uso_cpu)
    cpu_use = PERCENT_FONT.render(perc_cpu_texto, True, WINE)

    tela_05.blit(cpu_use, (380, 95))

    # disco
    disk = verifica_discos()
    perc_texto = "Disco em uso: {}%".format(disk[5])
    percentagem_uso = PERCENT_FONT.render(perc_texto, True, WINE)
    tela_05.blit(percentagem_uso, (40, 140))

    # address
    INTERFACE_REDE = "Wi-Fi"
    dic_interfaces = psutil.net_if_addrs()
    ip_rede = dic_interfaces[INTERFACE_REDE][1].address
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_local_render = PERCENT_FONT.render(ip_local, True, WINE)
    tela_05.blit(ip_local_render, (380, 140))

    TELA.blit(tela_05, (0, 0))


def verifica_discos():
    # verifica a quantidade de discos
    qtd_discos = len(psutil.disk_partitions())
    discos = []
    espaco_total = 0
    espaco_usado = 0
    espaco_livre = 0

    # Faz a iteração sobre os retornos do disk_partitions e disk_usage.
    for partition in psutil.disk_partitions():
        discos.append(partition[1])
        espaco_total += psutil.disk_usage(partition[1])[0]
        espaco_usado += psutil.disk_usage(partition[1])[1]
        espaco_livre += psutil.disk_usage(partition[1])[2]

    string_discos = ""
    for i in range(len(discos)):
        string_discos += discos[i]+" "

    # Calcula a porcentagem do uso total.
    percent_usado = round(espaco_usado / espaco_total * 100, 1)
    return qtd_discos, string_discos, espaco_total, espaco_usado, espaco_livre, percent_usado


def controle_setas():
    tela_seta = pygame.Surface(TAM_TELA)
    tela_seta.fill(PASTEL)
    image = pygame.image.load(r'resources/seta-direita.png')
    imagered = pygame.transform.smoothscale(image, (70, 70))
    tela_seta.blit(imagered, (340, 10))
    tela_seta.blit(pygame.transform.rotate(imagered, 180), (180, 10))
    TELA.blit(tela_seta, (0, 500))


def colisao_setas(mouse):
    # Posições das setas esquerda e direita
    # Posição no eixo x
    if 510 <= mouse[1] <= 580:
        if 180 <= mouse[0] <= 240:
            return 1
        if 350 <= mouse[0] <= 405:
            return 2


# Verifica o IP público que acessou a página do dyndns.
def ip_publico():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)


# Variável inicializada vazia (IP_Externo)
ip_net = ""


def main():
    controle = 60
    pagina = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if colisao_setas(pos) == 1:
                    if pagina > 0:
                        pagina -= 1
                if colisao_setas(pos) == 2:
                    if pagina < 4:
                        pagina += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if pagina > 0:
                        pagina -= 1
                if event.key == pygame.K_RIGHT:
                    if pagina < 5:
                        pagina += 1
        if controle == 60:
            controle_setas()
            if pagina == 0:
                show_cpu()
            if pagina == 1:
                show_use_memory()
            if pagina == 2:
                show_use_disk()
            if pagina == 3:
                show_addrs_ip()
            if pagina == 4:
                resumo()
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
