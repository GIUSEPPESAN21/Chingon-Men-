import streamlit as st
import datetime

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
# Usamos "centered" para que no sea demasiado ancho en pantallas grandes
st.set_page_config(
    page_title="Chingon Cocteles",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. URLs DE LOGOS ---
LOGO_URL = "https://github.com/GIUSEPPESAN21/Chingon-Logo/blob/main/Captura%20de%20pantalla%202025-10-20%20080734.png?raw=true"
SAVA_LOGO_URL = "https://github.com/GIUSEPPESAN21/LOGO-SAVA/blob/main/logo_sava.png?raw=true"

# --- 3. ESTILOS CSS PERSONALIZADOS ---
# Inyectamos el CSS para dar el look "neón"
CUSTOM_CSS = """
<style>
/* 1. Carga de Fuentes */
@import url('https://fonts.googleapis.com/css2?family=Bungee&family=Teko:wght@400;600&display=swap');

/* 2. Estilos Globales (Fondo de calavera) */
body {
    font-family: 'Teko', sans-serif;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="50" font-size="90" fill="rgba(255,255,255,0.03)" dominant-baseline="central" text-anchor="middle">💀</text></svg>');
}

/* 3. Logo Principal (Sombra Neón) */
.main-logo {
    filter: drop-shadow(0 0 15px rgba(236, 72, 153, 0.6));
}

/* 4. Estilos de fuentes */
.font-bungee { font-family: 'Bungee', cursive; }
.font-teko { font-family: 'Teko', sans-serif; }

/* 5. Efectos Neón */
.neon-pink-text {
    color: #fce7f3;
    text-shadow: 0 0 5px #fce7f3, 0 0 10px #fce7f3, 0 0 15px #ec4899, 0 0 20px #ec4899;
}
.neon-green-text {
    color: #dcfce7;
    text-shadow: 0 0 5px #dcfce7, 0 0 10px #dcfce7, 0 0 15px #22c55e, 0 0 20px #22c55e;
}
.neon-yellow-text {
    color: #fefce8;
    text-shadow: 0 0 5px #fefce8, 0 0 10px #fefce8, 0 0 15px #eab308, 0 0 20px #eab308;
}
.neon-cyan-text {
    color: #cffafe;
    text-shadow: 0 0 5px #cffafe, 0 0 10px #cffafe, 0 0 15px #06b6d4, 0 0 20px #06b6d4;
}

/* 6. Estilo de Pestañas */
[data-baseweb="tab-list"] button {
    font-family: 'Bungee', cursive !important;
    font-size: 1.1rem !important;
    color: #9ca3af !important;
    border-bottom: 2px solid transparent !important;
    transition: all 0.3s ease !important;
}
[data-baseweb="tab-list"] button:hover {
    color: #fefce8 !important;
}
[data-baseweb="tab-list"] button[aria-selected="true"] {
    color: #fefce8 !important;
    border-bottom-color: #eab308 !important;
    text-shadow: 0 0 5px #eab308 !important;
}

/* 7. Estilo de Cajas de Menú (Items Grandes) */
.menu-item-box {
    background-color: #111827;
    border: 1px solid #374151;
    padding: 1.25rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    height: 100%;
    transition: all 0.3s ease;
}
.menu-item-box:hover {
    border-color: #ec4899;
    box-shadow: 0 0 10px #ec4899;
}
.menu-item-box h3 {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem;
    font-weight: 600;
    color: white;
}
.menu-item-box p {
    font-family: 'Teko', sans-serif;
    font-size: 1.25rem;
    color: #9ca3af;
    margin-bottom: 0.5rem;
}
.menu-item-box .price-item {
    display: flex;
    justify-content: space-between;
    font-family: 'Teko', sans-serif;
    font-size: 1.5rem;
}
.menu-item-box .price-item span:first-child {
    color: #d1d5db;
}
.menu-item-box .price-item span:last-child {
    font-weight: 700;
}

/* 8. Estilo de Listas (Items Pequeños) */
.menu-item-list-wrapper {
    background-color: #111827;
    border: 1px solid #374151;
    padding: 0.75rem 1.25rem;
    border-radius: 0.5rem;
}
.menu-item-list {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #374151;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}
.menu-item-list:last-child {
    border-bottom: none;
}
.menu-item-list h3 {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem;
    color: white;
    margin: 0;
}
.menu-item-list span {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem;
    font-weight: 700;
}
.menu-item-list p {
    font-size: 1.1rem;
    color: #9ca3af;
    margin: 0;
    margin-left: 10px;
}

/* 9. Estilo de Promos */
.promo-box {
    padding: 1.5rem;
    background-color: #111827;
    border-radius: 0.5rem;
    text-align: center;
    border-width: 2px;
}
.promo-pink { border-color: #ec4899; box-shadow: 0 0 10px #ec4899; }
.promo-green { border-color: #22c55e; box-shadow: 0 0 10px #22c55e; }
.promo-cyan { border-color: #06b6d4; box-shadow: 0 0 10px #06b6d4; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- 4. FUNCIONES HELPER (¡AQUÍ ESTÁ LA CORRECCIÓN!) ---
#
# Estas funciones AHORA imprimen el HTML directamente.
# Esto soluciona el error de ver texto HTML en crudo.
#

def render_item_card(name, desc, prices):
    """(Para Granizados, Micheladas) Dibuja una caja grande."""
    prices_html = ""
    for label, price in prices:
        prices_html += f"""
        <div class="price-item">
            <span>{label}</span>
            <span class="neon-green-text">{price}</span>
        </div>
        """
    html = f"""
    <div class="menu-item-box">
        <h3>{name}</h3>
        <p>{desc}</p>
        {prices_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_item_simple_card(name, price):
    """(Para Cremosos, Cocteles) Dibuja una caja grande simple."""
    html = f"""
    <div class="menu-item-box">
        <div class="price-item">
            <h3>{name}</h3>
            <span class="neon-green-text">{price}</span>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_item_list(items_list):
    """(Para Ramen, Bebidas, Dulces) Dibuja una lista dentro de una caja."""
    items_html = ""
    for item in items_list:
        note_html = f"<p>{item['note']}</p>" if 'note' in item and item['note'] else ""
        items_html += f"""
        <div class="menu-item-list">
            <div style="display: flex; align-items: center;">
                <h3>{item['name']}</h3>
                {note_html}
            </div>
            <span class="neon-green-text">{item['price']}</span>
        </div>
        """
    
    html = f"<div class='menu-item-list-wrapper'>{items_html}</div>"
    st.markdown(html, unsafe_allow_html=True)

# --- 5. DATOS DEL MENÚ (Más organizado) ---

# Datos Pestaña 1: Granizados
GRANIZADOS_PRINCIPALES = [
    {"name": "NO MAMES", "desc": "Jagermeister y Redbull Con Apariencia Color Caramelo"},
    {"name": "SINALOA", "desc": "Smirnoff De Lulo Con Apariencia Color Verde Selva"},
    {"name": "701", "desc": "Fourloko Sandia, Whisky y Tequila Con Apariencia Color Fucsia"},
    {"name": "TEQUILAZO", "desc": "Tequila y Mango Maduro Con Apariencia Color Naranja"},
    {"name": "TIJUANA", "desc": "Vodka y Algodón de Azúcar Con Apariencia Color Azul Baby"},
    {"name": "DIA DE LOS MUERTOS", "desc": "Champagne, Granadina, Vodka, Tequila y Kola Con Apariencia Color Rojo"},
    {"name": "WEY", "desc": "Mezcla Lista Para Granizar Con Sabor A Maracuyá y Lulo Con Viche, Tequila Apariencia Color Amarillo Naranja"},
    {"name": "CHIDO", "desc": "Cachaza, Maracuyá y Mago Maduro Con Apariencia Color Amarillo"},
    {"name": "CATRINA", "desc": "Vodka y Whisky Con sabor a Sandia y Fresa Apariencia Color Negro"},
    {"name": "QUE PEDO?", "desc": "Vodka Champagne y Cereza Con Apariencia Color Rojo"},
    {"name": "CARNAL", "desc": "Tequila y Mango Viche Con Apariencia Color Verde"},
    {"name": "CHUPETA", "desc": "Whisky y Fresa Con Apariencia Color Rojo Imperial"},
    {"name": "MORRAS", "desc": "Whisky, Melocotón y Sandia Con Apariencia Color Rojo Tenue"},
    {"name": "BELICO", "desc": "Fourloko Sabor a Limón, Lima, Naranja, Frambuesa, Notas De Banano y Melocotón Con Apariencia y Brillo Color Azul"},
    {"name": "NO MANCHES", "desc": "Ginebra y Manzana Con Apariencia Color Azul"},
    {"name": "LA PEDA", "desc": "Whisky y Tequila Con Apariencia y Brillo Color Dorado"},
    {"name": "QUE ONDA PERDIDA", "desc": "Whisky Con Apariencia Color Fucsia"}
]
PRECIOS_GRANIZADOS = [("14 Oz", "$14.000"), ("16 Oz", "$19.000"), ("24 Oz", "$24.000")]
GRANIZADOS_CREMOSOS = [
    {"name": "CREMA DE COCO", "price": "$14.000"},
    {"name": "CREMA DE FRESA", "price": "$14.000"},
    {"name": "CREMA DE COFFEE", "price": "$14.000"},
    {"name": "CREMA DE BAYLEYS", "price": "$14.000"},
    {"name": "CREMA DE PIÑA", "price": "$14.000"}
]

# Datos Pestaña 3: Micheladas
MICHELADAS = [
    {"name": "MICHELADA DE FRESA", "desc": "Vaso Con Cerveza Michelado Con Sal, Fresas, Zumo de Limón y Hielo", "price": "$15.000"},
    {"name": "MICHELADA ENCHILADA", "desc": "Vaso con Cerveza Michelado Con Sal Pimienta, Mango Biche Envuelto En Tajin, Zumo de Limón, Hielo y Takis", "price": "$19.000"},
    {"name": "MICHELADA DE MARACUMANGO", "desc": "Vaso con Cerveza Michelado Con Sal, Mango Biche Envuelto, Maracuyá y Zumo de Limón y Hielo", "price": "$15.000"},
    {"name": "MICHELADA SENCILLA", "desc": "", "price": "$8.000"},
    {"name": "MICHELADA LULI CHELA", "desc": "Vaso con Cerveza Michelado Con Sal Pimienta, Lulo, Sirope de Lulo con Zumo de Limón, Hielo y Chocolitos", "price": "$17.000"},
    {"name": "MICHELADA DE CEREZA", "desc": "Vaso Con Cerveza Michelado Con Sal, Cereza, Zumo de Limón y Hielo", "price": "$15.000"},
    {"name": "MICHELADA DE MANGO", "desc": "Vaso Con Cerveza Michelado Con Sal, Mango, Zumo de Limón y Hielo", "price": "$15.000"},
    {"name": "MICHELADA DE MARACUYA", "desc": "Vaso Con Cerveza Michelado Con Sal, Maracuya, Zumo de Limón y Hielo", "price": "$15.000"},
    {"name": "MILO OREO", "desc": "Milo Con Crema de Chocolate, Chantilli y Galletas Oreo", "price": "$13.000"},
    {"name": "MILO RAMITO", "desc": "Milo Con Crema de Chocolate, Chantilli y Cakes de Choco ramo", "price": "$13.000"}
]

# Datos Pestaña 4: Ramen
RAMEN_LIST = [
    {"name": "BULBACK EN BOLSA NEGRO", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$25.000"},
    {"name": "BULBACK CARBONA BOLSA", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$27.000"},
    {"name": "BULBACK BOLSA ROJO", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$26.000"},
    {"name": "CHAPAGUETTI BOLSA", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$25.000"},
    {"name": "RAMEN HELLO KITTY", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$28.000"},
    {"name": "RAMEN MARUCHAN", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$12.000"},
    {"name": "RAMEN NISSI", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$10.000"},
    {"name": "RAMEN AJINOMEN TARRO", "note": "", "price": "$12.000"},
    {"name": "RAMEN AJINOMEN BOLSA", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$10.000"},
    {"name": "RAMEN KIMCHI", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$17.000"},
    {"name": "RAMEN NUDELS", "note": "(Incluye Bowl y Palitos Chinos)", "price": "$14.000"}
]

# Datos Pestaña 5: Bebidas
OTRAS_BEBIDAS = [
    {"name": "CORONITA", "price": "$8.000"}, {"name": "AGUILA", "price": "$8.000"},
    {"name": "GATORADE", "price": "$6.000"}, {"name": "GASEOSA", "price": "$4.000"},
    {"name": "AGUA", "price": "$4.000"}, {"name": "SODAS", "price": "$4.000"},
    {"name": "SODA ITALIANA", "price": "$14.000"}, {"name": "SMIRNOFF", "price": "$16.000"},
    {"name": "FOUR LOKO", "price": "$24.000"}, {"name": "JP", "price": "$16.000"},
    {"name": "CORONA", "price": "$12.000"}, {"name": "MONSTER", "price": "$14.000"},
    {"name": "SPEED MAX", "price": "$5.000"}, {"name": "ELECTROLIT", "price": "$12.000"}
]
BEBIDAS_IMPORTADAS = [
    {"name": "SKITTLES SOUR", "price": "$35.000"}, {"name": "WARHEADS LATA", "price": "$25.000"},
    {"name": "STARBUCKS GRANDE", "price": "$40.000"}, {"name": "STARBUCKS PINK", "price": "$40.000"},
    {"name": "STARBUCKS ENERGY", "price": "$40.000"}, {"name": "STAR BUCKS PEQUEÑO", "price": "$25.000"},
    {"name": "DUNKIN", "price": "$35.000"}, {"name": "PACMAN LATA", "price": "$35.000"},
    {"name": "MONSTER ROSADO", "price": "$40.000"}, {"name": "MONSTER JAVA", "price": "$40.000"},
    {"name": "PRIME", "price": "$35.000"}, {"name": "ROCKSTAR", "price": "$35.000"},
    {"name": "MTN DEW", "price": "$24.000"}, {"name": "COFFI LATA", "price": "$12.000"},
    {"name": "SHOT CHIVAS", "price": "$24.000"}, {"name": "SHOT VODKA", "price": "$16.000"},
    {"name": "SHOT JAGERMEISTER", "price": "$18.000"}
]

# Datos Pestaña 6: Dulces
DULCES = [
    {"name": "CHOCOLATINA MR BETS", "price": "$22.000"}, {"name": "PALITOS POCKY", "price": "$25.000"},
    {"name": "NERDS CAJA GRANDE", "price": "$18.000"}, {"name": "NERDS BOLSA", "price": "$32.000"},
    {"name": "WARHEADS SUPER SOUR SPRAY", "price": "$10.000"}, {"name": "JUICY DROP", "price": "$28.000"},
    {"name": "SKITTLE BOLSA GRANDE", "price": "$35.000"}, {"name": "CAJA MOCHI ORIGINAL", "price": "$34.000"},
    {"name": "PALETA VERO PINTA AZUL", "price": "$14.000"}, {"name": "VERO PICA FRESA", "price": "$2.000"},
    {"name": "MARA PIÑA", "price": "$3.000"}, {"name": "TAKIS", "price": "$6.000"},
    {"name": "BOBBO HAMBURGUESA", "price": "$15.000"}, {"name": "ICE FRUNAS", "price": "$5.000"},
    {"name": "CHICLE EN POLVO", "price": "$15.000"}, {"name": "MENTOS", "price": "$13.000"},
    {"name": "SNICKERS", "price": "$8.000"}, {"name": "CHICLE METRO", "price": "$12.000"},
    {"name": "NERDS CAJITA PEQUEÑA", "price": "$4.000"}, {"name": "BOMBON SANDIA", "price": "$3.000"},
    {"name": "GOMITAS COLA PERRO CALIENTE", "price": "$3.000"}, {"name": "BURGUER", "price": "$3.000"},
    {"name": "GOMITA PIZZA", "price": "$4.000"}, {"name": "RING POP", "price": "$8.000"},
    {"name": "M&M", "price": "$10.000"}, {"name": "HERSHEY", "price": "$10.000"},
    {"name": "NUTELA", "price": "$4.000"}
]


# --- 6. RENDERIZADO DE LA APLICACIÓN ---

# --- Encabezado ---
st.markdown(f"""
<header style="text-align: center; margin-top: 2rem; margin-bottom: 2rem;">
    <img src="{LOGO_URL}" alt="Chingon Cocteles Logo" class="main-logo" style="width: auto; height: 12rem; margin: auto;">
</header>
""", unsafe_allow_html=True)

# --- Pestañas de Navegación ---
tab_list = [
    "Granizados", 
    "Pa' Picar/Compartir", 
    "Cocteles y Micheladas", 
    "Ramen", 
    "Bebidas", 
    "Dulces", 
    "Promos"
]
tab_granizados, tab_compartir, tab_cocteles, tab_ramen, tab_bebidas, tab_dulces, tab_promos = st.tabs(tab_list)

# --- PESTAÑA 1: GRANIZADOS ---
with tab_granizados:
    st.markdown("<h2 class='font-bungee neon-green-text' style='text-align: center;'>Granizados</h2>", unsafe_allow_html=True)
    
    # MEJORA: Se usa st.columns(1) para que no se vea "estrecho"
    with st.columns(1)[0]:
        for item in GRANIZADOS_PRINCIPALES:
            render_item_card(item["name"], item["desc"], PRECIOS_GRANIZADOS)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Granizados Cremosos</h3>", unsafe_allow_html=True)
    
    cols_cremosos = st.columns(2)
    for i, item in enumerate(GRANIZADOS_CREMOSOS):
        with cols_cremosos[i % 2]:
            render_item_simple_card(item["name"], item["price"])
            
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Extras y Sin Alcohol</h3>", unsafe_allow_html=True)
    
    cols_extras = st.columns(2)
    with cols_extras[0]:
        render_item_card("GRANIZADO SIN ALCOHOL", "Preguntar Disponibilidad", [("", "$14.000")])
        render_item_simple_card("SHOTS MOLECULAR", "$3.000")
        render_item_simple_card("BOTELLA AGUARDIENTE", "$70.000")
    with cols_extras[1]:
        render_item_card("JERINGAS DE VENENO", "", [("Pequeña", "$3.000"), ("Grande", "$5.000")])
        render_item_simple_card("CANECA AGUARDIENTE", "$40.000")
        render_item_card("GOMAS ENCHILADAS", "", [("Tamaño S", "$10.000"), ("Tamaño M", "$15.000"), ("Tamaño L", "$19.000")])

# --- PESTAÑA 2: PA' PICAR / COMPARTIR ---
with tab_compartir:
    st.markdown("<h2 class='font-bungee neon-green-text' style='text-align: center;'>Pa' Picar y Compartir</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Pa' Picar</h3>", unsafe_allow_html=True)
    
    cols_picar = st.columns(2)
    with cols_picar[0]:
        render_item_card("ALITAS", "5 Alitas, Porcion De Papas, Jugo Hit En Caja", [("", "$16.000")])
    with cols_picar[1]:
        render_item_card("NUGGETS", "8 Nuggets, Porcion De Papas, Jugo Hit En Caja", [("", "$16.000")])
    
    with st.columns(1)[0]:
        render_item_card("SALCHIPAPA", "Porción De Papa, Salchicha, Salsas Al Gusto, Queso Derretido y 2 Jugos Hit", [("", "$16.000")])
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Pa' Compartir</h3>", unsafe_allow_html=True)
    
    cols_compartir = st.columns(2)
    with cols_compartir[0]:
        render_item_card("NEVECON DE CHELA", "", [("Pequeño (3 a 4 Personas)", "$45.000"), ("Grande (7 a 8 Personas)", "$70.000")])
        render_item_simple_card("NEVECON CHINGON GRANDE", "$90.000")
        render_item_card("LA PECERA", "Granizado Azul, Fresa, Naranja, Gomitas, Perlas Explosivas y Cerveza Coronita (2 a 4 Personas)", [("", "$50.000")])
    with cols_compartir[1]:
        render_item_simple_card("NEVECON CHINGON", "$60.000")
        render_item_card("NEVECON PUPPY", "Granizado Con Gomitas Rojas o Varias Presentaciones, Perlas Explosivas, Bombombum y 2 JP", [("", "$100.000")])
        render_item_card("CUATAZO", "Bebida Michelada con Tajín Gomitas bañadas en Chamoy, Tajín y Manzana verde (Mamoncillo) o Guayaba Manzana", [("", "$24.000")])

# --- PESTAÑA 3: COCTELES Y MICHELADAS ---
with tab_cocteles:
    st.markdown("<h2 class='font-bungee neon-pink-text' style='text-align: center;'>Cocteles y Micheladas</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Cocteles</h3>", unsafe_allow_html=True)
    
    cols_cocteles = st.columns(2)
    with cols_cocteles[0]:
        render_item_card("EXPLOSION DE FRESAS", "Smirnoff Con Fresas y Leche Condensada", [("", "$25.000")])
    with cols_cocteles[1]:
        render_item_card("CHINGON", "Tequila, Limon, Sirope Cosmico, etc. Servido En Botella Exclusiva Con Gajos De Limon (2 Personas)", [("", "$50.000")])
    
    with st.columns(1)[0]:
        render_item_simple_card("MARGARITA", "$20.000")
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Micheladas y Mas</h3>", unsafe_allow_html=True)

    # MEJORA: Se usa st.columns(1) para que no se vea "estrecho"
    with st.columns(1)[0]:
        for item in MICHELADAS:
            render_item_card(item["name"], item["desc"], [("", item["price"])])

# --- PESTAÑA 4: RAMEN ---
with tab_ramen:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Ramen</h2>", unsafe_allow_html=True)
    
    with st.columns(1)[0]:
        render_item_list(RAMEN_LIST)

# --- PESTAÑA 5: BEBIDAS ---
with tab_bebidas:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Bebidas</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Otras Bebidas</h3>", unsafe_allow_html=True)
    
    # MEJORA: Se usa st.columns(2) en lugar de 3 para que no sea "estrecho"
    cols_otras = st.columns(2)
    split_idx = len(OTRAS_BEBIDAS) // 2 + 1
    with cols_otras[0]:
        render_item_list(OTRAS_BEBIDAS[:split_idx])
    with cols_otras[1]:
        render_item_list(OTRAS_BEBIDAS[split_idx:])

    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Bebidas Importados</h3>", unsafe_allow_html=True)
    
    # MEJORA: Se usa st.columns(2) en lugar de 3 para que no sea "estrecho"
    cols_importadas = st.columns(2)
    split_idx = len(BEBIDAS_IMPORTADAS) // 2 + 1
    with cols_importadas[0]:
        render_item_list(BEBIDAS_IMPORTADAS[:split_idx])
    with cols_importadas[1]:
        render_item_list(BEBIDAS_IMPORTADAS[split_idx:])

# --- PESTAÑA 6: DULCES ---
with tab_dulces:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Dulces Importados</h2>", unsafe_allow_html=True)
    
    # MEJORA: Se usa st.columns(2) en lugar de 3 para que no sea "estrecho"
    cols_dulces = st.columns(2)
    split_idx = len(DULCES) // 2 + 1
    with cols_dulces[0]:
        render_item_list(DULCES[:split_idx])
    with cols_dulces[1]:
        render_item_list(DULCES[split_idx:])

# --- PESTAÑA 7: PROMOS ---
with tab_promos:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Promos e Info</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="promo-box promo-pink" style="margin-top: 2rem;">
        <h3 class="font-bungee neon-pink-text" style="font-size: 2rem; margin-bottom: 0.5rem;">¡DULCERIA!</h3>
        <p style="font-size: 1.75rem;">¡En Chingon Cocteles contamos con dulceria mexicana y oriental!</p>
    </div>
    
    <div class="promo-box promo-cyan" style="margin-top: 2rem;">
        <h3 class="font-bungee neon-cyan-text" style="font-size: 2rem; margin-bottom: 0.5rem;">YA DISPONIBLE TERMOS</h3>
    </div>
    
    <div class="promo-box promo-green" style="margin-top: 2rem;">
        <h3 class="font-bungee neon-green-text" style="font-size: 2rem; margin-bottom: 0.5rem;">¡SOMOS ARTE!</h3>
        <p style="font-size: 1.75rem;">Podrás tambien pintar mientras disfrutas de un granizado</p>
        <p style="font-size: 1.25rem; color: #d1d5db;">(Pintura en Ceramica + Pincel + Vinilo)</p>
    </div>
    
    <div class="promo-box promo-pink" style="margin-top: 2rem;">
        <h3 class="font-bungee neon-pink-text" style="font-size: 2rem; margin-bottom: 0.5rem;">LUNES DE AMIGOS</h3>
        <p style="font-size: 1.75rem;">¡Compra 2 Granizados y llevas el 3 GRATIS!</p>
    </div>
    
    <div class="promo-box promo-green" style="margin-top: 2rem;">
        <h3 class="font-bungee neon-green-text" style="font-size: 2rem; margin-bottom: 0.5rem;">MARTES DE VENENO</h3>
        <p style="font-size: 1.75rem;">¡Jeringa GRATIS para todos los granizados!</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. PIE DE PÁGINA Y SECCIÓN SAVA ---
st.markdown("---")

st.markdown("""
<footer style="text-align: center; margin-top: 2rem;">
    <h3 class="font-bungee neon-pink-text" style="font-size: 1.5rem; margin-bottom: 1rem;">¡Siguenos en Nuestras Redes!</h3>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 1.5rem; font-size: 1.5rem; font-family: 'Teko';">
        <a href="https://www.instagram.com/CHINGON_COCTELES" target="_blank" style="color: #d1d5db; text-decoration: none; transition: all 0.3s ease;">
            @CHINGON_COCTELES
        </a>
        <a href="https://www.tiktok.com/@CHINGON.CCTELES" target="_blank" style="color: #d1d5db; text-decoration: none; transition: all 0.3s ease;">
            @CHINGON.CCTELES
        </a>
    </div>
</footer>
""", unsafe_allow_html=True)

# Sección SAVA (Corregido el KeyError)
sava_html = f"""
<div class="menu-item-box" style="margin-top: 2rem;">
    <h3 class="font-bungee neon-cyan-text" style="text-align: center; font-size: 1.5rem; margin-bottom: 1.5rem;">Desarrollado Por</h3>
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <img src="{SAVA_LOGO_URL}" alt="Logo SAVA" style="width: 8rem; height: 8rem; margin-bottom: 1rem;">
        <div>
            <h4 class="font-bungee" style="font-size: 1.5rem; color: white;">Joseph Javier Sánchez Acuña</h4>
            <p class="neon-cyan-text" style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem;">CEO - SAVA SOFTWARE FOR ENGINEERING</p>
            <p style="font-size: 1.25rem; color: #d1d5db;">
                Líder visionario con una profunda experiencia en inteligencia artificial y desarrollo de software. Joseph es el cerebro detrás de la arquitectura de OSIRIS, impulsando la innovación y asegurando que nuestra tecnología se mantenga a la vanguardia.
            </p>
        </div>
    </div>
</div>
"""
st.markdown(sava_html, unsafe_allow_html=True)


# Copyright
current_year = datetime.date.today().year
st.markdown(f"""
<p style="font-family: 'Teko'; font-size: 1.1rem; color: #6b7280; text-align: center; margin-top: 2rem;">
    &copy; {current_year} Chingon Cocteles. Todos los derechos reservados.
</p>
""", unsafe_allow_html=True)

