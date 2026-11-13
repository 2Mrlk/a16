import os
from PIL import Image, ImageDraw, ImageFont

def create_mockups():
    os.makedirs("docs", exist_ok=True)
    
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"

    font_phone_title = ImageFont.truetype(font_bold_path, 26)
    font_phone_sub = ImageFont.truetype(font_reg_path, 16)
    font_label = ImageFont.truetype(font_bold_path, 14)
    font_sm = ImageFont.truetype(font_reg_path, 13)
    font_xs = ImageFont.truetype(font_reg_path, 11)
    font_lg_bold = ImageFont.truetype(font_bold_path, 20)

    # -------------------------------------------------------------
    # 1. MOCKUP: TELA INICIAL DO APP (DASHBOARD & CARDS)
    # -------------------------------------------------------------
    w, h = 900, 1100
    canvas = Image.new("RGB", (w, h), (18, 22, 28))
    draw = ImageDraw.Draw(canvas)

    # Moldura do Celular
    phone_w, phone_h = 420, 840
    px = (w - phone_w) // 2
    py = 130

    # Sombra do Celular
    draw.rounded_rectangle([px - 8, py - 4, px + phone_w + 8, py + phone_h + 16], radius=44, fill=(10, 12, 16))

    # Corpo do Smartphone (Borda escura metálica)
    draw.rounded_rectangle([px, py, px + phone_w, py + phone_h], radius=40, fill=(28, 34, 40), outline=(50, 60, 70), width=4)

    # Tela do Smartphone (Screen)
    sx = px + 10
    sy = py + 10
    sw = phone_w - 20
    sh = phone_h - 20
    draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=32, fill=(13, 31, 24))

    # Câmera Frontal (Punch-hole notch)
    draw.ellipse([sx + sw//2 - 7, sy + 8, sx + sw//2 + 7, sy + 22], fill=(10, 10, 10))

    # Barra de Status do Android
    draw.text((sx + 24, sy + 10), "10:30", fill=(200, 200, 200), font=font_xs)
    draw.text((sx + sw - 60, sy + 10), "100% 📶", fill=(200, 200, 200), font=font_xs)

    # Header FloraCare
    hy = sy + 38
    draw.rounded_rectangle([sx + 16, hy, sx + 52, hy + 36], radius=10, fill=(16, 185, 129))
    draw.text((sx + 24, hy + 6), "🌿", font=font_phone_sub)
    draw.text((sx + 62, hy + 2), "FloraCare", fill=(248, 250, 252), font=font_phone_title)
    draw.text((sx + 62, hy + 28), "Lembrete Inteligente de Rega", fill=(148, 163, 184), font=font_xs)

    # Botão + no header
    draw.ellipse([sx + sw - 52, hy + 4, sx + sw - 16, hy + 40], fill=(16, 185, 129))
    draw.text((sx + sw - 39, hy + 10), "+", fill=(255, 255, 255), font=font_phone_title)

    # Stats Row
    sty = hy + 54
    card_w = (sw - 48) // 3
    # Card 1: Rega
    draw.rounded_rectangle([sx + 16, sty, sx + 16 + card_w, sty + 64], radius=10, fill=(20, 42, 34), outline=(14, 165, 233), width=1)
    draw.text((sx + 24, sty + 8), "💧 2", fill=(56, 189, 248), font=font_label)
    draw.text((sx + 24, sty + 36), "Regar Hoje", fill=(148, 163, 184), font=font_xs)

    # Card 2: Adubo
    draw.rounded_rectangle([sx + 24 + card_w, sty, sx + 24 + card_w*2, sty + 64], radius=10, fill=(20, 42, 34), outline=(245, 158, 11), width=1)
    draw.text((sx + 32 + card_w, sty + 8), "🌱 1", fill=(251, 191, 36), font=font_label)
    draw.text((sx + 32 + card_w, sty + 36), "Adubar", fill=(148, 163, 184), font=font_xs)

    # Card 3: Total
    draw.rounded_rectangle([sx + 32 + card_w*2, sty, sx + sw - 16, sty + 64], radius=10, fill=(20, 42, 34), outline=(16, 185, 129), width=1)
    draw.text((sx + 40 + card_w*2, sty + 8), "✨ 5", fill=(52, 211, 153), font=font_label)
    draw.text((sx + 40 + card_w*2, sty + 36), "Plantas", fill=(148, 163, 184), font=font_xs)

    # Planta 1: Costela-de-Adão
    p1_y = sty + 78
    draw.rounded_rectangle([sx + 16, p1_y, sx + sw - 16, p1_y + 175], radius=14, fill=(20, 42, 34), outline=(36, 75, 60), width=1)
    draw.rounded_rectangle([sx + 26, p1_y + 12, sx + 70, p1_y + 56], radius=10, fill=(27, 56, 45))
    draw.text((sx + 36, p1_y + 20), "🌿", font=font_phone_title)

    draw.text((sx + 80, p1_y + 14), "Costela-de-Adão", fill=(255, 255, 255), font=font_label)
    draw.text((sx + 80, p1_y + 34), "Monstera Deliciosa • Sala de Estar", fill=(148, 163, 184), font=font_xs)

    # Badge de status regar hoje
    draw.rounded_rectangle([sx + sw - 110, p1_y + 14, sx + sw - 26, p1_y + 36], radius=8, fill=(239, 68, 68))
    draw.text((sx + sw - 102, p1_y + 17), "⚠️ Regar Hoje!", fill=(255, 255, 255), font=font_xs)

    # Barra rega
    draw.text((sx + 26, p1_y + 66), "Umidade do Solo (0%)", fill=(148, 163, 184), font=font_xs)
    draw.rounded_rectangle([sx + 26, p1_y + 86, sx + sw - 26, p1_y + 92], radius=3, fill=(16, 36, 28))
    draw.rounded_rectangle([sx + 26, p1_y + 86, sx + 50, p1_y + 92], radius=3, fill=(239, 68, 68))

    # Barra adubo
    draw.text((sx + 26, p1_y + 100), "Nutrientes (50% - em 15 dias)", fill=(148, 163, 184), font=font_xs)
    draw.rounded_rectangle([sx + 26, p1_y + 118, sx + sw - 26, p1_y + 124], radius=3, fill=(16, 36, 28))
    draw.rounded_rectangle([sx + 26, p1_y + 118, sx + 200, p1_y + 124], radius=3, fill=(245, 158, 11))

    # Botões
    btn_w = (sw - 60) // 2
    draw.rounded_rectangle([sx + 26, p1_y + 134, sx + 26 + btn_w, p1_y + 164], radius=8, fill=(2, 132, 199))
    draw.text((sx + 50, p1_y + 141), "💧 Regar Agora", fill=(255, 255, 255), font=font_xs)

    draw.rounded_rectangle([sx + 36 + btn_w, p1_y + 134, sx + sw - 26, p1_y + 164], radius=8, fill=(27, 56, 45))
    draw.text((sx + 66 + btn_w, p1_y + 141), "🌱 Adubar", fill=(251, 191, 36), font=font_xs)

    # Planta 2: Jiboia Dourada
    p2_y = p1_y + 190
    draw.rounded_rectangle([sx + 16, p2_y, sx + sw - 16, p2_y + 175], radius=14, fill=(20, 42, 34), outline=(36, 75, 60), width=1)
    draw.rounded_rectangle([sx + 26, p2_y + 12, sx + 70, p2_y + 56], radius=10, fill=(27, 56, 45))
    draw.text((sx + 36, p2_y + 20), "🌱", font=font_phone_title)

    draw.text((sx + 80, p2_y + 14), "Jiboia Dourada", fill=(255, 255, 255), font=font_label)
    draw.text((sx + 80, p2_y + 34), "Epipremnum aureum • Quarto", fill=(148, 163, 184), font=font_xs)

    draw.rounded_rectangle([sx + sw - 105, p2_y + 14, sx + sw - 26, p2_y + 36], radius=8, fill=(245, 158, 11))
    draw.text((sx + sw - 98, p2_y + 17), "🌱 Adubar Hoje!", fill=(255, 255, 255), font=font_xs)

    draw.text((sx + 26, p2_y + 66), "Umidade do Solo (60% - em 3 dias)", fill=(148, 163, 184), font=font_xs)
    draw.rounded_rectangle([sx + 26, p2_y + 86, sx + sw - 26, p2_y + 92], radius=3, fill=(16, 36, 28))
    draw.rounded_rectangle([sx + 26, p2_y + 86, sx + 230, p2_y + 92], radius=3, fill=(14, 165, 233))

    draw.text((sx + 26, p2_y + 100), "Nutrientes (0% - Esgotado)", fill=(148, 163, 184), font=font_xs)
    draw.rounded_rectangle([sx + 26, p2_y + 118, sx + sw - 26, p2_y + 124], radius=3, fill=(16, 36, 28))
    draw.rounded_rectangle([sx + 26, p2_y + 118, sx + 50, p2_y + 124], radius=3, fill=(245, 158, 11))

    draw.rounded_rectangle([sx + 26, p2_y + 134, sx + 26 + btn_w, p2_y + 164], radius=8, fill=(2, 132, 199))
    draw.text((sx + 50, p2_y + 141), "💧 Regar Agora", fill=(255, 255, 255), font=font_xs)

    draw.rounded_rectangle([sx + 36 + btn_w, p2_y + 134, sx + sw - 26, p2_y + 164], radius=8, fill=(245, 158, 11))
    draw.text((sx + 58 + btn_w, p2_y + 141), "🌱 Adubar Agora", fill=(255, 255, 255), font=font_xs)

    # Barra de Navegação Inferior Android (Pill de navegação)
    draw.rounded_rectangle([sx + sw//2 - 40, sy + sh - 10, sx + sw//2 + 40, sy + sh - 6], radius=2, fill=(200, 200, 200))

    # Título do Mockup fora do celular
    draw.text((w//2 - 200, 35), "TELA INICIAL DO APLICATIVO", fill=(16, 185, 129), font=font_phone_title)
    draw.text((w//2 - 250, 75), "FloraCare: Monitoramento Inteligente em Execução", fill=(148, 163, 184), font=font_phone_sub)

    canvas.save("docs/mockup_app_screen.png", format="PNG")
    print("✓ docs/mockup_app_screen.png gerado com sucesso!")


    # -------------------------------------------------------------
    # 2. MOCKUP: GRADE DE APLICATIVOS (APP DRAWER / HOME SCREEN)
    # -------------------------------------------------------------
    canvas_drawer = Image.new("RGB", (w, h), (18, 22, 28))
    draw_d = ImageDraw.Draw(canvas_drawer)

    # Sombra e Corpo
    draw_d.rounded_rectangle([px - 8, py - 4, px + phone_w + 8, py + phone_h + 16], radius=44, fill=(10, 12, 16))
    draw_d.rounded_rectangle([px, py, px + phone_w, py + phone_h], radius=40, fill=(28, 34, 40), outline=(50, 60, 70), width=4)

    # Tela com papel de parede Android bonito
    draw_d.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=32, fill=(23, 30, 42))

    # Câmera e Status bar
    draw_d.ellipse([sx + sw//2 - 7, sy + 8, sx + sw//2 + 7, sy + 22], fill=(10, 10, 10))
    draw_d.text((sx + 24, sy + 10), "10:30", fill=(255, 255, 255), font=font_xs)
    draw_d.text((sx + sw - 60, sy + 10), "100% 📶", fill=(255, 255, 255), font=font_xs)

    # Widget de Relógio do Android
    wy = sy + 40
    draw_d.text((sx + sw//2 - 80, wy), "10:30", fill=(255, 255, 255), font=ImageFont.truetype(font_bold_path, 54))
    draw_d.text((sx + sw//2 - 95, wy + 64), "Quinta-feira, 13 de Novembro", fill=(200, 210, 225), font=font_xs)

    # Barra de Pesquisa Google
    g_y = wy + 110
    draw_d.rounded_rectangle([sx + 20, g_y, sx + sw - 20, g_y + 44], radius=22, fill=(255, 255, 255, 30), outline=(255, 255, 255, 50))
    draw_d.text((sx + 40, g_y + 12), "🔍  Pesquisar no smartphone...", fill=(180, 195, 215), font=font_xs)

    # Ícone oficial FloraCare redimensionado para caber no grid
    icon_flora = Image.open("assets/icon.png").resize((64, 64), Image.Resampling.LANCZOS)
    # Criar máscara circular para ícone adaptativo Android
    mask = Image.new("L", (64, 64), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, 64, 64], fill=255)

    # Grade de Aplicativos 4 colunas x 4 linhas
    cols = 4
    col_w = sw // cols
    grid_start_y = g_y + 90

    app_list = [
        ("FloraCare", icon_flora, True),
        ("Chrome", None, False, (66, 133, 244), "🌐"),
        ("Fotos", None, False, (234, 67, 53), "🖼️"),
        ("Câmera", None, False, (52, 168, 83), "📷"),
        ("Gmail", None, False, (234, 67, 53), "✉️"),
        ("Mapas", None, False, (66, 133, 244), "🗺️"),
        ("Play Store", None, False, (15, 157, 88), "▶️"),
        ("YouTube", None, False, (255, 0, 0), "▶"),
        ("Relógio", None, False, (40, 50, 70), "⏰"),
        ("Calculadora", None, False, (70, 80, 95), "🧮"),
        ("Configurações", None, False, (90, 100, 115), "⚙️"),
        ("Arquivos", None, False, (66, 133, 244), "📁"),
    ]

    for idx, item in enumerate(app_list):
        r = idx // cols
        c = idx % cols
        ix = sx + c * col_w + (col_w - 64) // 2
        iy = grid_start_y + r * 94

        name = item[0]
        if item[2]: # FloraCare
            # Efeito de Destaque / Dardo na Grade
            draw_d.ellipse([ix - 6, iy - 6, ix + 70, iy + 70], outline=(16, 185, 129), width=3)
            canvas_drawer.paste(item[1], (ix, iy), mask)
            draw_d.text((ix - 2, iy + 68), name, fill=(52, 211, 153), font=font_label)
        else:
            color = item[3]
            emoji = item[4]
            draw_d.ellipse([ix, iy, ix + 64, iy + 64], fill=color)
            draw_d.text((ix + 18, iy + 16), emoji, font=font_phone_title)
            t_w = draw_d.textbbox((0, 0), name, font=font_xs)[2]
            draw_d.text((ix + 32 - t_w//2, iy + 68), name, fill=(230, 235, 245), font=font_xs)

    # Dock Inferior (4 apps principais)
    dock_y = sy + sh - 95
    draw_d.rounded_rectangle([sx + 14, dock_y - 10, sx + sw - 14, dock_y + 75], radius=26, fill=(255, 255, 255, 20))
    dock_apps = [("Telefone", (52, 168, 83), "📞"), ("Mensagens", (66, 133, 244), "💬"), ("WhatsApp", (37, 211, 102), "🟢"), ("Config.", (100, 110, 120), "⚙️")]
    for idx, (dname, dcolor, demoji) in enumerate(dock_apps):
        d_ix = sx + idx * col_w + (col_w - 56) // 2
        draw_d.ellipse([d_ix, dock_y, d_ix + 56, dock_y + 56], fill=dcolor)
        draw_d.text((d_ix + 16, dock_y + 14), demoji, font=font_phone_sub)

    # Barra Home Android
    draw_d.rounded_rectangle([sx + sw//2 - 40, sy + sh - 10, sx + sw//2 + 40, sy + sh - 6], radius=2, fill=(255, 255, 255))

    # Título do Mockup fora do celular
    draw_d.text((w//2 - 250, 35), "GRADE DE APLICATIVOS (ANDROID)", fill=(16, 185, 129), font=font_phone_title)
    draw_d.text((w//2 - 275, 75), "Ícone Adaptativo com Roupa de Gala Instalado no Sistema", fill=(148, 163, 184), font=font_phone_sub)

    canvas_drawer.save("docs/mockup_app_drawer.png", format="PNG")
    print("✓ docs/mockup_app_drawer.png gerado com sucesso!")


    # -------------------------------------------------------------
    # 3. MOCKUP: TELA DE ABERTURA / SPLASH SCREEN NATIVA
    # -------------------------------------------------------------
    canvas_splash = Image.new("RGB", (w, h), (18, 22, 28))
    draw_s = ImageDraw.Draw(canvas_splash)

    draw_s.rounded_rectangle([px - 8, py - 4, px + phone_w + 8, py + phone_h + 16], radius=44, fill=(10, 12, 16))
    draw_s.rounded_rectangle([px, py, px + phone_w, py + phone_h], radius=40, fill=(28, 34, 40), outline=(50, 60, 70), width=4)

    # Abertura nativa (Splash) com recorte proporcional do splash.png
    splash_full = Image.open("assets/splash.png")
    # Recorte central 1080 x 2160
    splash_cropped = splash_full.crop((1366 - 450, 1366 - 900, 1366 + 450, 1366 + 900)).resize((sw, sh), Image.Resampling.LANCZOS)
    canvas_splash.paste(splash_cropped, (sx, sy))

    # Câmera e Status bar
    draw_s.ellipse([sx + sw//2 - 7, sy + 8, sx + sw//2 + 7, sy + 22], fill=(10, 10, 10))
    draw_s.rounded_rectangle([sx + sw//2 - 40, sy + sh - 10, sx + sw//2 + 40, sy + sh - 6], radius=2, fill=(200, 200, 200))

    # Título do Mockup fora do celular
    draw_s.text((w//2 - 240, 35), "TELA DE ABERTURA (SPLASH SCREEN)", fill=(16, 185, 129), font=font_phone_title)
    draw_s.text((w//2 - 260, 75), "Transição Nativa Fluida com Respeito à Safe Zone", fill=(148, 163, 184), font=font_phone_sub)

    canvas_splash.save("docs/mockup_splash_screen.png", format="PNG")
    print("✓ docs/mockup_splash_screen.png gerado com sucesso!")


if __name__ == "__main__":
    create_mockups()
