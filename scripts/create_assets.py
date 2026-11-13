import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_plant_emblem(draw, cx, cy, scale=1.0, is_foreground_only=False):
    """
    Desenha o emblema botânico com vaso, folhas estilizadas,
    gota d'água de rega e partículas de adubo (nutrientes).
    """
    # Escalas e tamanhos
    r_pot = int(90 * scale)
    pot_h = int(100 * scale)
    pot_y = cy + int(70 * scale)
    
    # 1. Base / Vaso Cerâmico Minimalista Moderno
    # Formato trapezoidal moderno com borda arredondada
    pot_top_w = int(140 * scale)
    pot_bot_w = int(100 * scale)
    pot_points = [
        (cx - pot_top_w, pot_y),
        (cx + pot_top_w, pot_y),
        (cx + pot_bot_w, pot_y + pot_h),
        (cx - pot_bot_w, pot_y + pot_h),
    ]
    draw.polygon(pot_points, fill=(35, 75, 58))
    
    # Borda do vaso
    draw.rounded_rectangle(
        [cx - pot_top_w - int(10 * scale), pot_y - int(16 * scale),
         cx + pot_top_w + int(10 * scale), pot_y],
        radius=int(8 * scale),
        fill=(46, 95, 75)
    )

    # 2. Folhas da Planta (Curvas de Bezier aproximadas por polígonos suaves)
    # Folha Esquerda (Grande, curvada)
    leaf_pts_left = []
    for t in [i / 50.0 for i in range(51)]:
        # Curva de subida
        x = (1-t)**2 * cx + 2*(1-t)*t * (cx - 260*scale) + t**2 * (cx - 160*scale)
        y = (1-t)**2 * pot_y + 2*(1-t)*t * (pot_y - 120*scale) + t**2 * (pot_y - 280*scale)
        leaf_pts_left.append((x, y))
    for t in [i / 50.0 for i in range(51)]:
        # Curva de volta ao centro
        x = (1-t)**2 * (cx - 160*scale) + 2*(1-t)*t * (cx - 40*scale) + t**2 * cx
        y = (1-t)**2 * (pot_y - 280*scale) + 2*(1-t)*t * (pot_y - 150*scale) + t**2 * pot_y
        leaf_pts_left.append((x, y))
    draw.polygon(leaf_pts_left, fill=(16, 185, 129)) # Emerald Green

    # Nervura central da folha esquerda
    draw.line([
        (cx, pot_y),
        (cx - 90*scale, pot_y - 130*scale),
        (cx - 160*scale, pot_y - 280*scale)
    ], fill=(52, 211, 153), width=max(2, int(4 * scale)))

    # Folha Direita (Ainda maior e exuberante)
    leaf_pts_right = []
    for t in [i / 50.0 for i in range(51)]:
        x = (1-t)**2 * cx + 2*(1-t)*t * (cx + 280*scale) + t**2 * (cx + 170*scale)
        y = (1-t)**2 * pot_y + 2*(1-t)*t * (pot_y - 140*scale) + t**2 * (pot_y - 320*scale)
        leaf_pts_right.append((x, y))
    for t in [i / 50.0 for i in range(51)]:
        x = (1-t)**2 * (cx + 170*scale) + 2*(1-t)*t * (cx + 30*scale) + t**2 * cx
        y = (1-t)**2 * (pot_y - 320*scale) + 2*(1-t)*t * (pot_y - 170*scale) + t**2 * pot_y
        leaf_pts_right.append((x, y))
    draw.polygon(leaf_pts_right, fill=(5, 150, 105)) # Deep Leaf Green

    # Nervura central folha direita
    draw.line([
        (cx, pot_y),
        (cx + 100*scale, pot_y - 150*scale),
        (cx + 170*scale, pot_y - 320*scale)
    ], fill=(52, 211, 153), width=max(2, int(4 * scale)))

    # Broto Central Novo (Folha central jovem)
    sprout_pts = []
    for t in [i / 40.0 for i in range(41)]:
        x = (1-t)**2 * cx + 2*(1-t)*t * (cx - 40*scale) + t**2 * cx
        y = (1-t)**2 * pot_y + 2*(1-t)*t * (pot_y - 120*scale) + t**2 * (pot_y - 210*scale)
        sprout_pts.append((x, y))
    for t in [i / 40.0 for i in range(41)]:
        x = (1-t)**2 * cx + 2*(1-t)*t * (cx + 40*scale) + t**2 * cx
        y = (1-t)**2 * (pot_y - 210*scale) + 2*(1-t)*t * (pot_y - 120*scale) + t**2 * pot_y
        sprout_pts.append((x, y))
    draw.polygon(sprout_pts, fill=(52, 211, 153))

    # 3. Gota de Água Inteligente (Representando a Rega)
    # Gota caindo no centro acima do broto
    drop_x = cx
    drop_y = cy - int(240 * scale)
    drop_r = int(28 * scale)
    drop_pts = [
        (drop_x, drop_y - int(35 * scale)), # ponta superior
        (drop_x + int(24 * scale), drop_y + int(10 * scale)),
        (drop_x + int(18 * scale), drop_y + int(28 * scale)),
        (drop_x, drop_y + int(36 * scale)),
        (drop_x - int(18 * scale), drop_y + int(28 * scale)),
        (drop_x - int(24 * scale), drop_y + int(10 * scale)),
    ]
    draw.polygon(drop_pts, fill=(14, 165, 233)) # Sky Blue Water
    # Brilho na gota de água
    draw.ellipse([
        drop_x - int(10 * scale), drop_y - int(5 * scale),
        drop_x - int(2 * scale), drop_y + int(12 * scale)
    ], fill=(186, 230, 253))

    # 4. Partículas Douradas de Adubo / Nutrientes Bio (Sparkles)
    def draw_sparkle(sx, sy, sz):
        s_pts = [
            (sx, sy - sz),
            (sx + sz//3, sy - sz//3),
            (sx + sz, sy),
            (sx + sz//3, sy + sz//3),
            (sx, sy + sz),
            (sx - sz//3, sy + sz//3),
            (sx - sz, sy),
            (sx - sz//3, sy - sz//3)
        ]
        draw.polygon(s_pts, fill=(245, 158, 11)) # Amber Gold
        draw.ellipse([sx - sz//4, sy - sz//4, sx + sz//4, sy + sz//4], fill=(254, 240, 138))

    draw_sparkle(cx + int(190 * scale), cy - int(190 * scale), int(22 * scale))
    draw_sparkle(cx - int(180 * scale), cy - int(140 * scale), int(16 * scale))
    draw_sparkle(cx + int(130 * scale), cy + int(40 * scale), int(14 * scale))


def create_icon():
    """Gera o icon.png (1024x1024) com super-amostragem (2048x2048 -> 1024x1024)"""
    size_2x = 2048
    img = Image.new("RGBA", (size_2x, size_2x), (13, 31, 24, 255)) # #0d1f18 Fundo Sólido Opaco
    draw = ImageDraw.Draw(img)

    cx, cy = size_2x // 2, size_2x // 2

    # Círculo sutil de iluminação de fundo (respeitando a Safe Zone central de 66%)
    glow_r = int(580 * 2) # raio 580 no canvas de 2048 (equivale a 580 de diâmetro em 1024)
    draw.ellipse(
        [cx - glow_r//2, cy - glow_r//2, cx + glow_r//2, cy + glow_r//2],
        fill=(20, 48, 37, 255),
        outline=(26, 62, 48, 255),
        width=int(6 * 2)
    )

    # Anel externo bem suave na safe zone
    ring_r = int(640 * 2)
    draw.ellipse(
        [cx - ring_r//2, cy - ring_r//2, cx + ring_r//2, cy + ring_r//2],
        outline=(16, 185, 129, 60),
        width=int(3 * 2)
    )

    # Desenhar o emblema na safe zone
    draw_plant_emblem(draw, cx, cy, scale=2.1)

    # Redimensionar para 1024x1024 com LANCZOS
    icon = img.resize((1024, 1024), Image.Resampling.LANCZOS)
    icon_rgb = icon.convert("RGB") # Garante sem canal alpha conforme especificação nativa Android
    icon_rgb.save("assets/icon.png", format="PNG")
    icon_rgb.save("assets/icon-only.png", format="PNG")
    print("✓ assets/icon.png (1024x1024) gerado com sucesso!")


def create_foreground_and_background():
    """Gera icon-foreground.png (transparente) e icon-background.png para ícones adaptativos do Android"""
    # Background sólido
    bg = Image.new("RGB", (1024, 1024), (13, 31, 24))
    bg.save("assets/icon-background.png", format="PNG")

    # Foreground com transparência
    fg_2x = Image.new("RGBA", (2048, 2048), (0, 0, 0, 0))
    draw_fg = ImageDraw.Draw(fg_2x)
    cx, cy = 1024, 1024
    draw_plant_emblem(draw_fg, cx, cy, scale=1.9, is_foreground_only=True)
    fg = fg_2x.resize((1024, 1024), Image.Resampling.LANCZOS)
    fg.save("assets/icon-foreground.png", format="PNG")
    print("✓ assets/icon-background.png e icon-foreground.png gerados!")


def create_splash():
    """Gera o splash.png (2732x2732) com logotipo centralizado na Safe Zone (~1200px)"""
    w, h = 2732, 2732
    img = Image.new("RGB", (w, h), (13, 31, 24)) # #0d1f18 Fundo Sólido Opaco
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # Circulo de brilho suave ao fundo da logo (Safe Zone)
    glow_r = 750
    draw.ellipse(
        [cx - glow_r, cy - glow_r - 120, cx + glow_r, cy + glow_r - 120],
        fill=(19, 44, 34),
        outline=(27, 65, 50),
        width=6
    )

    # Desenha o emblema da planta centralizado na parte superior da safe zone
    emblem_cy = cy - 200
    draw_plant_emblem(draw, cx, emblem_cy, scale=2.8)

    # Carregar fontes para Tipografia Oficial
    font_title_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_sub_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_title_path):
        font_title_path = "C:/Windows/Fonts/arialbd.ttf"
        font_sub_path = "C:/Windows/Fonts/arial.ttf"

    font_title = ImageFont.truetype(font_title_path, 150)
    font_sub = ImageFont.truetype(font_sub_path, 54)
    font_badge = ImageFont.truetype(font_title_path, 42)

    # Título Principal "FloraCare"
    title_text = "FloraCare"
    t_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    t_w = t_bbox[2] - t_bbox[0]
    title_y = cy + 260
    draw.text((cx - t_w // 2, title_y), title_text, fill=(248, 250, 252), font=font_title)

    # Ponto de destaque verde no título "FloraCare •"
    draw.ellipse([cx + t_w // 2 + 15, title_y + 90, cx + t_w // 2 + 35, title_y + 110], fill=(16, 185, 129))

    # Subtítulo Oficial
    sub_text = "Lembrete Inteligente de Rega e Adubação"
    s_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
    s_w = s_bbox[2] - s_bbox[0]
    sub_y = title_y + 180
    draw.text((cx - s_w // 2, sub_y), sub_text, fill=(148, 163, 184), font=font_sub)

    # Badge Decorativo "CUIDADO BOTÂNICO NATIVO"
    badge_text = "🌿 CUIDADO BOTÂNICO NATIVO 🌿"
    b_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    b_w = b_bbox[2] - b_bbox[0]
    b_h = b_bbox[3] - b_bbox[1]
    badge_y = sub_y + 100
    pad_x = 40
    pad_y = 16
    draw.rounded_rectangle(
        [cx - b_w // 2 - pad_x, badge_y - pad_y, cx + b_w // 2 + pad_x, badge_y + b_h + pad_y],
        radius=25,
        fill=(22, 54, 42),
        outline=(16, 185, 129),
        width=3
    )
    draw.text((cx - b_w // 2, badge_y), badge_text, fill=(52, 211, 153), font=font_badge)

    img.save("assets/splash.png", format="PNG")
    img.save("assets/splash-dark.png", format="PNG")
    print("✓ assets/splash.png (2732x2732) gerado com sucesso!")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    create_icon()
    create_foreground_and_background()
    create_splash()
    print("Todos os assets foram gerados com perfeição!")
