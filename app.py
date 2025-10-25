import streamlit as st
import datetime

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
# "wide" soluciona el problema de que se vea "estrecho"
st.set_page_config(
    page_title="Chingon Cocteles",
    page_icon="💀",
    layout="wide", # <-- MÁS GRANDE
    initial_sidebar_state="collapsed"
)

# --- 2. URLs DE LOGOS ---
LOGO_URL = "https://github.com/GIUSEPPESAN21/Chingon-Logo/blob/main/Captura%20de%20pantalla%202025-10-20%20080734.png?raw=true"
SAVA_LOGO_URL = "https://github.com/GIUSEPPESAN21/LOGO-SAVA/blob/main/logo_sava.png?raw=true"

# --- 3. DATOS DEL MENÚ (Sin cambios) ---
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
EXTRAS_SIN_ALCOHOL = [
    {"type": "card", "name": "GRANIZADO SIN ALCOHOL", "desc": "Preguntar Disponibilidad", "prices": [("", "$14.000")]},
    {"type": "simple", "name": "SHOTS MOLECULAR", "price": "$3.000"},
    {"type": "simple", "name": "BOTELLA AGUARDIENTE", "price": "$70.000"},
    {"type": "card", "name": "JERINGAS DE VENENO", "desc": "", "prices": [("Pequeña", "$3.000"), ("Grande", "$5.000")]},
    {"type": "simple", "name": "CANECA AGUARDIENTE", "price": "$40.000"},
    {"type": "card", "name": "GOMAS ENCHILADAS", "desc": "", "prices": [("Tamaño S", "$10.000"), ("Tamaño M", "$15.000"), ("Tamaño L", "$19.000")]}
]
PA_PICAR = [
    {"name": "ALITAS", "desc": "5 Alitas, Porcion De Papas, Jugo Hit En Caja", "price": "$16.000"},
    {"name": "NUGGETS", "desc": "8 Nuggets, Porcion De Papas, Jugo Hit En Caja", "price": "$16.000"},
    {"name": "SALCHIPAPA", "desc": "Porción De Papa, Salchicha, Salsas Al Gusto, Queso Derretido y 2 Jugos Hit", "price": "$16.000"}
]
PA_COMPARTIR = [
    {"name": "NEVECON DE CHELA", "desc": "", "prices": [("Pequeño (3 a 4 Personas)", "$45.000"), ("Grande (7 a 8 Personas)", "$70.000")]},
    {"name": "NEVECON CHINGON", "desc": "", "prices": [("", "$60.000")]},
    {"name": "NEVECON CHINGON GRANDE", "desc": "", "prices": [("", "$90.000")]},
    {"name": "NEVECON PUPPY", "desc": "Granizado Con Gomitas Rojas o Varias Presentaciones, Perlas Explosivas, Bombombum y 2 JP", "prices": [("", "$100.000")]},
    {"name": "LA PECERA", "desc": "Granizado Azul, Fresa, Naranja, Gomitas, Perlas Explosivas y Cerveza Coronita (2 a 4 Personas)", "prices": [("", "$50.000")]},
    {"name": "CUATAZO", "desc": "Bebida Michelada con Tajín Gomitas bañadas en Chamoy, Tajín y Manzana verde (Mamoncillo) o Guayaba Manzana", "prices": [("", "$24.000")]}
]
COCTELES = [
    {"name": "EXPLOSION DE FRESAS", "desc": "Smirnoff Con Fresas y Leche Condensada", "price": "$25.000"},
    {"name": "CHINGON", "desc": "Tequila, Limon, Sirope Cosmico, etc. Servido En Botella Exclusiva Con Gajos De Limon (2 Personas)", "price": "$50.000"},
    {"name": "MARGARITA", "desc": "", "price": "$20.000"}
]
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

# --- 4. FUNCIONES DE RENDERIZADO NATIVAS ---

def render_native_header():
    """Dibuja el logo principal centrado"""
    _, col_img, _ = st.columns([1, 1, 1])
    with col_img:
        st.image(LOGO_URL, use_column_width='always')

def render_native_footer():
    """Dibuja el pie de página nativo"""
    st.divider()
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem;">
        <b>¡Siguenos en Nuestras Redes!</b>
        <br>
        <a href="https://www.instagram.com/CHINGON_COCTELES" target="_blank">@CHINGON_COCTELES</a> (Instagram)
        <br>
        <a href="https://www.tiktok.com/@CHINGON.CCTELES" target="_blank">@CHINGON.CCTELES</a> (TikTok)
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    with st.container(border=True):
        st.subheader("Desarrollado Por")
        cols_sava = st.columns([1, 3])
        with cols_sava[0]:
            st.image(SAVA_LOGO_URL)
        with cols_sava[1]:
            st.write("#### Joseph Javier Sánchez Acuña")
            st.caption("CEO - SAVA SOFTWARE FOR ENGINEERING")
            st.write("Líder visionario con una profunda experiencia en inteligencia artificial y desarrollo de software. Joseph es el cerebro detrás de la arquitectura de OSIRIS, impulsando la innovación y asegurando que nuestra tecnología se mantenga a la vanguardia.")
            
    current_year = datetime.date.today().year
    st.caption(f"© {current_year} Chingon Cocteles. Todos los derechos reservados.")

# --- 5. FUNCIÓN PRINCIPAL DE LA APP ---
def main():
    # 1. Dibujar el logo
    render_native_header()

    # 2. Definir las pestañas
    tab_list = [
        "💀 Granizados", 
        "🔥 Pa' Picar/Compartir", 
        "🍹 Cocteles y Micheladas", 
        "🍜 Ramen", 
        "🥤 Bebidas", 
        "🍬 Dulces", 
        "🎉 Promos"
    ]
    tabs = st.tabs(tab_list)

    # 3. Renderizar cada pestaña con COMPONENTES NATIVOS

    # --- PESTAÑA 1: GRANIZADOS ---
    with tabs[0]:
        st.header("Granizados", divider="green")
        cols_granizados = st.columns(2)
        for i, item in enumerate(GRANIZADOS_PRINCIPALES):
            with cols_granizados[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.caption(item['desc'])
                    for p_label, p_price in PRECIOS_GRANIZADOS:
                        st.write(f"{p_label}: **:green[{p_price}]**")
        
        st.header("Granizados Cremosos", divider="cyan")
        cols_cremosos = st.columns(2)
        for i, item in enumerate(GRANIZADOS_CREMOSOS):
            with cols_cremosos[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")
                    
        st.header("Extras y Sin Alcohol", divider="cyan")
        cols_extras = st.columns(2)
        for i, item in enumerate(EXTRAS_SIN_ALCOHOL):
            with cols_extras[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    if item.get('desc'):
                        st.caption(item['desc'])
                    
                    if item["type"] == "card":
                        for p_label, p_price in item['prices']:
                            st.write(f"{p_label}: **:green[{p_price}]**")
                    elif item["type"] == "simple":
                        st.write(f"**:green[{item['price']}]**")

    # --- PESTAÑA 2: PA' PICAR / COMPARTIR ---
    with tabs[1]:
        st.header("Pa' Picar", divider="green")
        cols_picar = st.columns(2)
        for i, item in enumerate(PA_PICAR):
            with cols_picar[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.caption(item['desc'])
                    st.write(f"**:green[{item['price']}]**")

        st.header("Pa' Compartir", divider="cyan")
        cols_compartir = st.columns(2)
        for i, item in enumerate(PA_COMPARTIR):
            with cols_compartir[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    if item.get('desc'):
                        st.caption(item['desc'])
                    for p_label, p_price in item['prices']:
                        st.write(f"{p_label}: **:green[{p_price}]**")

    # --- PESTAÑA 3: COCTELES Y MICHELADAS ---
    with tabs[2]:
        st.header("Cocteles", divider="pink")
        cols_cocteles = st.columns(2)
        for i, item in enumerate(COCTELES):
            with cols_cocteles[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    if item.get('desc'):
                        st.caption(item['desc'])
                    st.write(f"**:green[{item['price']}]**")

        st.header("Micheladas y Mas", divider="pink")
        cols_micheladas = st.columns(2) # 2 columnas para más espacio
        for i, item in enumerate(MICHELADAS):
            with cols_micheladas[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    if item.get('desc'):
                        st.caption(item['desc'])
                    st.write(f"**:green[{item['price']}]**")

    # --- PESTAÑA 4: RAMEN ---
    with tabs[3]:
        st.header("Ramen", divider="yellow")
        cols_ramen = st.columns(2) # 2 columnas para más espacio
        for i, item in enumerate(RAMEN_LIST):
            with cols_ramen[i % 2]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    if item.get('note'):
                        st.caption(item['note'])
                    st.write(f"**:green[{item['price']}]**")

    # --- PESTAÑA 5: BEBIDAS ---
    with tabs[4]:
        st.header("Otras Bebidas", divider="yellow")
        cols_bebidas = st.columns(2) # 2 columnas para más espacio
        split_idx = len(OTRAS_BEBIDAS) // 2 + (len(OTRAS_BEBIDAS) % 2)
        
        with cols_bebidas[0]:
            for item in OTRAS_BEBIDAS[:split_idx]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")
        with cols_bebidas[1]:
            for item in OTRAS_BEBIDAS[split_idx:]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")

        st.header("Bebidas Importados", divider="cyan")
        cols_importadas = st.columns(2) # 2 columnas para más espacio
        split_idx = len(BEBIDAS_IMPORTADAS) // 2 + (len(BEBIDAS_IMPORTADAS) % 2)

        with cols_importadas[0]:
             for item in BEBIDAS_IMPORTADAS[:split_idx]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")
        with cols_importadas[1]:
            for item in BEBIDAS_IMPORTADAS[split_idx:]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")

    # --- PESTAÑA 6: DULCES ---
    with tabs[5]:
        st.header("Dulces Importados", divider="yellow")
        cols_dulces = st.columns(2) # 2 columnas para más espacio
        split_idx = len(DULCES) // 2 + (len(DULCES) % 2)
        
        with cols_dulces[0]:
            for item in DULCES[:split_idx]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")
        with cols_dulces[1]:
            for item in DULCES[split_idx:]:
                with st.container(border=True):
                    st.subheader(item['name'])
                    st.write(f"**:green[{item['price']}]**")

    # --- PESTAÑA 7: PROMOS ---
    with tabs[6]:
        st.header("Promos e Info", divider="yellow")
        
        st.info("¡DULCERIA! ¡En Chingon Cocteles contamos con dulceria mexicana y oriental!", icon="🍬")
        st.success("¡SOMOS ARTE! Podrás tambien pintar mientras disfrutas de un granizado (Pintura en Ceramica + Pincel + Vinilo)", icon="🎨")
        st.warning("LUNES DE AMIGOS: ¡Compra 2 Granizados y llevas el 3 GRATIS!", icon="🎉")
        st.success("MARTES DE VENENO: ¡Jeringa GRATIS para todos los granizados!", icon="💉")
        st.info("YA DISPONIBLE TERMOS", icon="🥤")


    # 5. Dibujar el pie de página
    render_native_footer()

if __name__ == "__main__":
    main()

