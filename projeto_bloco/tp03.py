import cpuinfo
import platform
import psutil
import pygame


# INICIALIZAÇÃO
pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60

LARGURA_TELA = 800
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Painel De Recursos")

VERMELHO = (242, 27, 63)
WINE = (97, 3, 69)
PASTEL = (241, 233, 219)
AZUL_PISCINA = (93, 183, 222)
SALMAO = (239, 111, 108)

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

    marca = "Marca: {}".format(info_cpu['brand_raw'])
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
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    pygame.draw.rect(tela_01, SALMAO, (70, pos_altura_barra,
                                       pos_final_barra, THICKNESS))
    pos_final_barra_uso = pos_final_barra * (memoria.percent / 100)
    pygame.draw.rect(tela_01, VERMELHO, (70, pos_altura_barra,
                                         pos_final_barra_uso, THICKNESS))

    perc_texto = "{}%".format(memoria.percent)

    titulo = INFO_BOLD_FONT.render(
        f"Uso de Memória (Total: {round(memoria.total / (1024.0 ** 3), 0)}) GB", True, WINE)
    percentagem_uso = PERCENT_FONT.render(perc_texto, True, WINE)
    tela_01.blit(titulo, (40, 20))
    tela_01.blit(percentagem_uso, (15, pos_altura_barra))

    free_memory = "Memória em uso: {:.2f} GB | Memória livre: {:.2f} GB".format(memoria.used / (1024.0 ** 3),
                                                                                memoria.free / (1024.0 ** 3))
    free_memory_render = INFO_FONT.render(free_memory, True, WINE)
    tela_01.blit(free_memory_render,
                 (LARGURA_TELA // 5, pos_altura_barra + 20))
    TELA.blit(tela_01, (0, 0))


def show_use_disk():
    disk = verifica_discos()
    tela_03 = pygame.Surface(TAM_TELA)
    tela_03.fill(PASTEL)
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    pygame.draw.rect(tela_03, SALMAO, (70, 110,
                                       pos_final_barra, THICKNESS))
    pos_final_barra_uso = pos_final_barra * (disk[5] / 100)
    pygame.draw.rect(tela_03, VERMELHO, (70, 110,
                                         pos_final_barra_uso, THICKNESS))

    perc_texto = "{}%".format(disk[5])

    titulo = TITLE_FONT.render("Espaço Total em Disco", True, WINE)
    percentagem_uso = PERCENT_FONT.render(perc_texto, True, WINE)
    tela_03.blit(titulo, (40, 20))
    tela_03.blit(percentagem_uso, (15, 110))

    qnt = "Quantidade de discos: {:g}".format(round(disk[0]))
    qnt_render = INFO_FONT.render(qnt, True, WINE)
    disks = "Esses foram os discos encontrados: {}".format(disk[1])
    disks_render = INFO_FONT.render(disks, True, WINE)
    tela_03.blit(
        qnt_render, (pos_final_barra - 160, 130))
    tela_03.blit(
        disks_render, (pos_final_barra - 160, 150))

    free = "Espaço livre: {:.2f} GB".format(disk[4] / (1024.0 ** 3))
    used = "Espaço usado: {:.2f} GB".format(disk[3] / (1024.0 ** 3))
    free_render = INFO_FONT.render(free, True, WINE)
    used_render = INFO_FONT.render(used, True, WINE)
    tela_03.blit(free_render, (70, 130))
    tela_03.blit(used_render, (70, 150))
    TELA.blit(tela_03, (0, 0))


def show_addrs_ip():
    dic_interfaces = psutil.net_if_addrs()
    ip_rede = dic_interfaces["Wi-Fi"][1].address
    net_mask = dic_interfaces["Wi-Fi"][1].netmask
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
    dic_interfaces = psutil.net_if_addrs()
    ip_rede = dic_interfaces["Wi-Fi"][1].address
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_local_render = PERCENT_FONT.render(ip_local, True, WINE)
    tela_05.blit(ip_local_render, (380, 140))

    TELA.blit(tela_05, (0, 0))


def show_message(current_page):
    message_surface = pygame.Surface(TAM_TELA)
    message_surface.fill(PASTEL)
    if not current_page == 4:
        perc_texto = "Pressione espaço para ver o resumo ou seta para ir à direita ou esquerda"
        percentagem_uso = PERCENT_FONT.render(perc_texto, True, AZUL_PISCINA)
        message_surface.blit(percentagem_uso, (100, 10))
    TELA.blit(message_surface, (0, 500))


def verifica_discos():
    partitions = psutil.disk_partitions()
    qtd_discos = len(partitions)
    disks = []
    all_space = 0
    used_space = 0
    free_space = 0

    for partition in partitions:
        disks.append(partition[1])
        all_space += psutil.disk_usage(partition[1])[0]
        used_space += psutil.disk_usage(partition[1])[1]
        free_space += psutil.disk_usage(partition[1])[2]

    label_disks = ""
    for i in range(len(disks)):
        label_disks += disks[i]+" "

    percent = round(used_space / all_space * 100, 1)
    return qtd_discos, label_disks, all_space, used_space, free_space, percent


def main():
    conta_clocks = 60
    page = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if page > 0:
                        page -= 1
                if event.key == pygame.K_RIGHT:
                    if page <= 2:
                        page += 1
                if event.key == pygame.K_SPACE:
                    page = 4

        if conta_clocks == 60:
            if page == 0:
                show_cpu()
            if page == 1:
                show_use_memory()
            if page == 2:
                show_use_disk()
            if page == 3:
                show_addrs_ip()
            if page == 4:
                resumo()
            conta_clocks = 0
        show_message(page)
        pygame.display.update()
        conta_clocks += 1
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
