import streamlit as st
import datetime

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Chingon Cocteles",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- URLs DE LOGOS ---
LOGO_URL = "https://github.com/GIUSEPPESAN21/Chingon-Logo/blob/main/Captura%20de%20pantalla%202025-10-20%20080734.png?raw=true"
SAVA_LOGO_URL = "https://github.com/GIUSEPPESAN21/LOGO-SAVA/blob/main/logo_sava.png?raw=true"

# --- CSS PERSONALIZADO (MEJORADO) ---
CUSTOM_CSS = """
<style>
/* 1. Carga de Fuentes */
@import url('https://fonts.googleapis.com/css2?family=Bungee&family=Teko:wght@400;600&display=swap');

/* 2. Estilos Globales (MEJORA: Fondo de calavera) */
body {
    font-family: 'Teko', sans-serif;
    /* Imagen de fondo de la calavera de tus menús */
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="50" font-size="90" fill="rgba(255,255,255,0.03)" dominant-baseline="central" text-anchor="middle">💀</text></svg>');
}

/* 3. Logo Principal (MEJORA: Sombra Neón) */
.main-logo {
    filter: drop-shadow(0 0 15px rgba(236, 72, 153, 0.6)); /* Sombra rosa neón */
}

/* 4. Estilos de fuentes */
.font-bungee { 
    font-family: 'Bungee', cursive; 
}
.font-teko { 
    font-family: 'Teko', sans-serif; 
}

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

/* 6. Estilo de Pestañas de Streamlit */
[data-baseweb="tab-list"] button {
    font-family: 'Bungee', cursive !important;
    font-size: 1.1rem !important;
    color: #9ca3af !important; /* gris */
    border-bottom: 2px solid transparent !important;
    transition: all 0.3s ease !important;
}
[data-baseweb="tab-list"] button:hover {
    color: #fefce8 !important;
}
[data-baseweb="tab-list"] button[aria-selected="true"] {
    color: #fefce8 !important; /* amarillo */
    border-bottom-color: #eab308 !important;
    text-shadow: 0 0 5px #eab308 !important;
}

/* 7. Estilo para los items del menú (el fondo oscuro) */
.menu-item-box {
    background-color: #111827; /* bg-gray-900 */
    border: 1px solid #374151; /* border-gray-700 */
    padding: 1.25rem; /* p-5 */
    border-radius: 0.5rem; /* rounded-lg */
    margin-bottom: 1rem;
    height: 100%; /* Para que las columnas tengan la misma altura */
    transition: all 0.3s ease;
}
.menu-item-box:hover {
    border-color: #ec4899; /* Borde rosa al pasar el mouse */
    box-shadow: 0 0 10px #ec4899;
}

.menu-item-box h3 {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem; /* text-3xl */
    font-weight: 600;
    color: white;
}
.menu-item-box p {
    font-family: 'Teko', sans-serif;
    font-size: 1.25rem; /* text-xl */
    color: #9ca3af; /* text-gray-400 */
    margin-bottom: 0.5rem;
}
.menu-item-box .price-item {
    display: flex;
    justify-content: space-between;
    font-family: 'Teko', sans-serif;
    font-size: 1.5rem; /* text-2xl */
}
.menu-item-box .price-item span:first-child {
    color: #d1d5db; /* text-gray-300 */
}
.menu-item-box .price-item span:last-child {
    font-weight: 700;
}

/* Estilo para items simples (Ramen, Bebidas, Dulces) */
.menu-item-list {
    background-color: #111827; /* bg-gray-900 */
    border: 1px solid #374151; /* border-gray-700 */
    padding: 0.75rem 1.25rem;
    border-radius: 0.5rem;
    margin-bottom: 0.75rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}
.menu-item-list:hover {
    border-color: #eab308; /* Borde amarillo al pasar el mouse */
    box-shadow: 0 0 8px #eab308;
}

.menu-item-list h3 {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem; /* text-3xl */
    color: white;
    margin: 0;
}
.menu-item-list span {
    font-family: 'Teko', sans-serif;
    font-size: 1.875rem; /* text-3xl */
    font-weight: 700;
}
.menu-item-list p {
    font-size: 1.1rem;
    color: #9ca3af; /* text-gray-400 */
    margin: 0;
    margin-left: 10px;
}

/* Estilo para Promos */
.promo-box {
    padding: 1.5rem;
    background-color: #111827; /* bg-gray-900 */
    border-radius: 0.5rem; /* rounded-lg */
    text-align: center;
    border-width: 2px;
}
.promo-pink {
    border-color: #ec4899; 
    box-shadow: 0 0 10px #ec4899;
}
.promo-green {
    border-color: #22c55e; 
    box-shadow: 0 0 10px #22c55e;
}
.promo-cyan {
    border-color: #06b6d4; 
    box-shadow: 0 0 10px #06b6d4;
}

</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- DATOS DEL MENÚ (Funciones Helper) ---
#
# ¡¡¡CORRECCIÓN APLICADA AQUÍ!!!
# Ahora el st.markdown está DENTRO de la función.
#

def format_item(name, desc, prices):
    """Formatea un item con descripción y múltiples precios."""
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

def format_item_simple(name, price):
    """Formatea un item con solo nombre y precio (para cremosos, etc.)."""
    html = f"""
    <div class="menu-item-box">
        <div class="price-item">
            <h3>{name}</h3>
            <span class="neon-green-text">{price}</span>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    
def format_item_list(name, price, note=""):
    """Formatea un item para lista simple (Ramen, Bebidas)."""
    note_html = f"<p>{note}</p>" if note else ""
    html = f"""
    <div class="menu-item-list">
        <div style="display: flex; align-items: center;">
            <h3>{name}</h3>
            {note_html}
        </div>
        <span class="neon-green-text">{price}</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# --- INICIO DE LA APP ---

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
    
    # Datos de Granizados
    granizados_principales = [
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
    precios_granizados = [("14 Oz", "$14.000"), ("16 Oz", "$19.000"), ("24 Oz", "$24.000")]
    
    cols = st.columns(2)
    for i, item in enumerate(granizados_principales):
        with cols[i % 2]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item(item["name"], item["desc"], precios_granizados)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Granizados Cremosos</h3>", unsafe_allow_html=True)
    
    granizados_cremosos = [
        {"name": "CREMA DE COCO", "price": "$14.000"},
        {"name": "CREMA DE FRESA", "price": "$14.000"},
        {"name": "CREMA DE COFFEE", "price": "$14.000"},
        {"name": "CREMA DE BAYLEYS", "price": "$14.000"},
        {"name": "CREMA DE PIÑA", "price": "$14.000"}
    ]
    
    cols = st.columns(2)
    for i, item in enumerate(granizados_cremosos):
        with cols[i % 2]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item_simple(item["name"], item["price"])
            
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Extras y Sin Alcohol</h3>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("GRANIZADO SIN ALCOHOL", "Preguntar Disponibilidad", [("", "$14.000")])
        format_item_simple("SHOTS MOLECULAR", "$3.000")
        format_item_simple("BOTELLA AGUARDIENTE", "$70.000")
    with cols[1]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("JERINGAS DE VENENO", "", [("Pequeña", "$3.000"), ("Grande", "$5.000")])
        format_item_simple("CANECA AGUARDIENTE", "$40.000")
        format_item("GOMAS ENCHILADAS", "", [("Tamaño S", "$10.000"), ("Tamaño M", "$15.000"), ("Tamaño L", "$19.000")])

# --- PESTAÑA 2: PA' PICAR / COMPARTIR ---
with tab_compartir:
    st.markdown("<h2 class='font-bungee neon-green-text' style='text-align: center;'>Pa' Picar y Compartir</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Pa' Picar</h3>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("ALITAS", "5 Alitas, Porcion De Papas, Jugo Hit En Caja", [("", "$16.000")])
    with cols[1]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("NUGGETS", "8 Nuggets, Porcion De Papas, Jugo Hit En Caja", [("", "$16.000")])
    # CORRECCIÓN: st.markdown() ya no es necesario aquí
    format_item("SALCHIPAPA", "Porción De Papa, Salchicha, Salsas Al Gusto, Queso Derretido y 2 Jugos Hit", [("", "$16.000")])
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Pa' Compartir</h3>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("NEVECON DE CHELA", "", [("Pequeño (3 a 4 Personas)", "$45.000"), ("Grande (7 a 8 Personas)", "$70.000")])
        format_item_simple("NEVECON CHINGON GRANDE", "$90.000")
        format_item("LA PECERA", "Granizado Azul, Fresa, Naranja, Gomitas, Perlas Explosivas y Cerveza Coronita (2 a 4 Personas)", [("", "$50.000")])
    with cols[1]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item_simple("NEVECON CHINGON", "$60.000")
        format_item("NEVECON PUPPY", "Granizado Con Gomitas Rojas o Varias Presentaciones, Perlas Explosivas, Bombombum y 2 JP", [("", "$100.000")])
        format_item("CUATAZO", "Bebida Michelada con Tajín Gomitas bañadas en Chamoy, Tajín y Manzana verde (Mamoncillo) o Guayaba Manzana", [("", "$24.000")])

# --- PESTAÑA 3: COCTELES Y MICHELADAS ---
with tab_cocteles:
    st.markdown("<h2 class='font-bungee neon-pink-text' style='text-align: center;'>Cocteles y Micheladas</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Cocteles</h3>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("EXPLOSION DE FRESAS", "Smirnoff Con Fresas y Leche Condensada", [("", "$25.000")])
    with cols[1]:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item("CHINGON", "Tequila, Limon, Sirope Cosmico, etc. Servido En Botella Exclusiva Con Gajos De Limon (2 Personas)", [("", "$50.000")])
    # CORRECCIÓN: st.markdown() ya no es necesario aquí
    format_item_simple("MARGARITA", "$20.000")
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Micheladas y Mas</h3>", unsafe_allow_html=True)

    micheladas = [
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
    
    cols = st.columns(2)
    for i, item in enumerate(micheladas):
        with cols[i % 2]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item(item["name"], item["desc"], [("", item["price"])])

# --- PESTAÑA 4: RAMEN ---
with tab_ramen:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Ramen</h2>", unsafe_allow_html=True)
    
    ramen_list = [
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
    
    st.markdown("<div class='menu-item-box'>", unsafe_allow_html=True) # Contenedor oscuro
    for item in ramen_list:
        # CORRECCIÓN: st.markdown() ya no es necesario aquí
        format_item_list(item["name"], item["price"], item["note"])
    st.markdown("</div>", unsafe_allow_html=True)


# --- PESTAÑA 5: BEBIDAS ---
with tab_bebidas:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Bebidas</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Otras Bebidas</h3>", unsafe_allow_html=True)
    
    otras_bebidas = [
        {"name": "CORONITA", "price": "$8.000"}, {"name": "AGUILA", "price": "$8.000"},
        {"name": "GATORADE", "price": "$6.000"}, {"name": "GASEOSA", "price": "$4.000"},
        {"name": "AGUA", "price": "$4.000"}, {"name": "SODAS", "price": "$4.000"},
        {"name": "SODA ITALIANA", "price": "$14.000"}, {"name": "SMIRNOFF", "price": "$16.000"},
        {"name": "FOUR LOKO", "price": "$24.000"}, {"name": "JP", "price": "$16.000"},
        {"name": "CORONA", "price": "$12.000"}, {"name": "MONSTER", "price": "$14.000"},
        {"name": "SPEED MAX", "price": "$5.000"}, {"name": "ELECTROLIT", "price": "$12.000"}
    ]
    
    st.markdown("<div class='menu-item-box'>", unsafe_allow_html=True) # Contenedor oscuro
    cols = st.columns(3)
    for i, item in enumerate(otras_bebidas):
        with cols[i % 3]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item_list(item["name"], item["price"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h3 class='font-bungee neon-cyan-text' style='text-align: center; margin-top: 2rem;'>Bebidas Importados</h3>", unsafe_allow_html=True)
    
    bebidas_importadas = [
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
    
    st.markdown("<div class='menu-item-box'>", unsafe_allow_html=True) # Contenedor oscuro
    cols = st.columns(3)
    for i, item in enumerate(bebidas_importadas):
        with cols[i % 3]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item_list(item["name"], item["price"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- PESTAÑA 6: DULCES ---
with tab_dulces:
    st.markdown("<h2 class='font-bungee neon-yellow-text' style='text-align: center;'>Dulces Importados</h2>", unsafe_allow_html=True)
    
    dulces = [
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
    
    st.markdown("<div class='menu-item-box'>", unsafe_allow_html=True) # Contenedor oscuro
    cols = st.columns(3)
    for i, item in enumerate(dulces):
        with cols[i % 3]:
            # CORRECCIÓN: st.markdown() ya no es necesario aquí
            format_item_list(item["name"], item["price"])
    st.markdown("</div>", unsafe_allow_html=True)

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

# --- PIE DE PÁGINA ---
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

# Sección SAVA (Arreglado el KeyError)
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

