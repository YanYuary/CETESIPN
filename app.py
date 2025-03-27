import streamlit as st
import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# ============================
# Configuración de la página
# ============================
st.set_page_config(
    page_title="🚀 Simulador de CETES y BONDES",
    layout="wide",
    page_icon="💹"
)

# ============================
# Pestañas principales
# ============================
tabs = st.tabs(["📚 Curso de CETES y BONDES", "💰 Simulador de Inversión"])

# ====================================================
# Pestaña 1: Curso de CETES y BONDES
# ====================================================
with tabs[0]:
    st.title("Curso de CETES y BONDES: Explicación Integral")
    st.markdown("---")
    
    # 1. ¿Qué es un CETE?
    st.header("1. ¿Qué es un CETE? 🤔")
    st.markdown(
        "Los **CETES** (Certificados de la Tesorería de la Federación) son instrumentos de deuda a corto plazo emitidos por el gobierno mexicano para financiar sus operaciones. "
        "Se emiten con vencimientos de 28, 91, 182 o 364 días, tienen un valor nominal de **$10 MXN** por título y son considerados de bajo riesgo."
    )
    st.markdown("---")
    
    # 2. Valor Nominal, Comercial y Remanente
    st.header("2. Valor Nominal, Comercial y Remanente 💸")
    st.markdown(
        "**Valor Nominal (VN):** Es el monto que se recibirá al vencimiento del instrumento. " 
        "Para CETES, el VN es **$10 MXN** por título, y para BONDES, es **$100 MXN** por título."
    )
    st.markdown(
        "**Valor Comercial (Precio de Compra):** Es el precio al que se adquiere el título, " 
        "obtenido al descontar el VN aplicando la tasa de descuento (TdD) durante el plazo de la inversión."
    )
    st.latex(r"Precio = VN \times \left(1 - \frac{TdD}{360} \times \text{días}\right)")
    with st.expander("Ejemplo de Cálculo de Precio (CETES y BONDES)"):
        st.markdown("**Ejemplo CETES:**")
        st.markdown("Para un CETE a 28 días con una Tasa de Descuento del 9.02%:")
        st.latex(r"Precio_{CETES} = 10 \times \left(1 - \frac{0.0902}{360} \times 28\right) \approx 9.92984")
        st.markdown("**Ejemplo BONDES:**")
        st.markdown("Para un BONDES a 91 días con una Tasa de Descuento del 7.50%:")
        st.latex(r"Precio_{BONDES} = 100 \times \left(1 - \frac{0.075}{360} \times 91\right)")
    st.markdown(
        "**Remanente:** Es la parte del monto invertido que sobra al comprar títulos enteros, " 
        "la cual se devuelve al inversor."
    )
    
    st.markdown("---")
    
    # 3. Rendimiento, Tasa Real y Venta Anticipada
    st.header("3. Rendimiento, Tasa Real y Venta Anticipada 📈")
    
    ## Interés Bruto
    st.markdown("**Interés Bruto:** Es la ganancia obtenida por la diferencia entre el VN y el Precio de Compra, " 
                "multiplicado por el número de títulos adquiridos.")
    st.latex(r"Interés\ Bruto = Títulos \times (VN - Precio)")
    with st.expander("Ejemplo de Cálculo de Interés Bruto"):
        st.markdown("Si compras 100 CETES a un precio de 9.93, el interés bruto se calcula como:")
        st.latex(r"Interés\ Bruto = 100 \times (10 - 9.93) = 100 \times 0.07 = 7 \text{ MXN}")
    
    ## Rendimiento Nominal (Tasa Bruta)
    st.markdown("**Rendimiento Nominal (Tasa Bruta):** Es el rendimiento anualizado que se obtendría si se mantuviera el título hasta el vencimiento, " 
                "calculado sobre la inversión realizada. Se expresa en porcentaje.")
    st.latex(r"Rendimiento\ Nominal = \left(\frac{Interés\ Bruto}{Inversión}\right) \times \frac{360}{días} \times 100")
    with st.expander("Ejemplo de Rendimiento Nominal"):
        st.markdown("Si la inversión es de 990 MXN y el interés bruto es de 7 MXN en 28 días:")
        st.latex(r"Rendimiento\ Nominal = \left(\frac{7}{990}\right) \times \frac{360}{28} \times 100 \approx 9.00\%")
    
    ## Tasa Neta (GAT Real)
    st.markdown("**Tasa Neta (GAT Real):** Es el rendimiento obtenido después de descontar el ISR. " 
                "Se puede aproximar restando la tasa del ISR a la Tasa Bruta (Rendimiento Nominal).")
    st.latex(r"Tasa\ Neta = Rendimiento\ Nominal - \text{Tasa ISR}")
    with st.expander("Ejemplo de Tasa Neta"):
        st.markdown("Si el Rendimiento Nominal es 9.00% y el ISR es 5.47%, entonces:")
        st.latex(r"Tasa\ Neta = 9.00\% - 5.47\% = 3.53\%")
    
    ## Utilidad Bruta y Utilidad Neta
    st.markdown("**Utilidad Bruta:** Es la ganancia en MXN obtenida (equivalente al Interés Bruto).")
    st.latex(r"Utilidad\ Bruta = Interés\ Bruto")
    with st.expander("Ejemplo de Utilidad Bruta"):
        st.markdown("Si el Interés Bruto es 7 MXN, la Utilidad Bruta es 7 MXN.")
    st.markdown("**Utilidad Neta:** Es la ganancia en MXN después de descontar el ISR del Interés Bruto.")
    st.latex(r"Utilidad\ Neta = Interés\ Bruto - ISR")
    with st.expander("Ejemplo de Utilidad Neta"):
        st.markdown("Si el Interés Bruto es 7 MXN y el ISR es 0.5 MXN, entonces:")
        st.latex(r"Utilidad\ Neta = 7 - 0.5 = 6.5 \text{ MXN}")
    
    ## Tasa Real
    st.markdown("**Tasa Real:** Es la tasa neta ajustada por la inflación, que refleja el rendimiento real en términos de poder adquisitivo. " 
                "Una forma de aproximarla es restando la tasa de inflación a la Tasa Neta.")
    st.latex(r"Tasa\ Real = Tasa\ Neta - Inflación")
    with st.expander("Ejemplo de Tasa Real"):
        st.markdown("Si la Tasa Neta es 3.53% y la inflación es 6%, entonces:")
        st.latex(r"Tasa\ Real = 3.53\% - 6\% = -2.47\%")
    
    ## Tasa de Rendimiento por Venta (Ganancia de Capital)
    st.markdown("**Tasa de Rendimiento por Venta (Ganancia de Capital):** Es la tasa que refleja la ganancia (o pérdida) obtenida al vender el título antes de su vencimiento, " 
                "anualizada según el periodo de tenencia.")
    st.latex(r"Tasa\ de\ Rendimiento\ Venta = \frac{(Precio_{Venta} - Precio_{Compra}) \times 360}{Precio_{Compra} \times \text{días de tenencia}} \times 100")
    with st.expander("Ejemplo de Tasa de Rendimiento por Venta"):
        st.markdown("Si se compró un CETE a 9.76 y se vende a 9.85 después de 35 días:")
        st.latex(r"Tasa\ de\ Rendimiento\ Venta = \frac{(9.85 - 9.76) \times 360}{9.76 \times 35} \times 100 \approx 9.48\%")
    
    ## Precio de Venta (Venta Anticipada)
    st.markdown("**Precio de Venta:** Es el precio obtenido al recalcular el valor del título si se vende antes de su vencimiento, " 
                "utilizando la tasa de descuento vigente (TdD actual) para los días restantes.")
    st.latex(r"Precio_{Venta} = VN \times \left(1 - \frac{TdD\ actual}{360} \times \text{días restantes}\right)")
    with st.expander("Ejemplo de Precio de Venta"):
        st.markdown("Si un CETE tiene VN = 10, se vende con una tasa actual del 4.25% y quedan 13 días:")
        st.latex(r"Precio_{Venta} = 10 \times \left(1 - \frac{0.0425}{360} \times 13\right)")
    st.markdown("*Para obtener el rendimiento real se comparan los precios de compra y venta, considerando también el ajuste por ISR y el remanente.*")
    
    st.markdown("---")
    
    # Resolución de Ejercicios
    st.header("Resolución de Ejercicios")
    st.markdown("---")
    
    st.subheader("Ejercicio 1")
    st.markdown(
        """
        **Enunciado:**  
        El señor Juan quiere comprar unos CETES que tienen **139 días por vencer** y una **tasa de descuento del 4.25%**.  
        Calcular el precio de los CETES.
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio} = VN \times \left(1 - \frac{\text{TdD}}{360} \times \text{días}\right)")
    st.markdown("**Datos:**")
    st.markdown("- VN = $10 MXN")
    st.markdown("- TdD = 4.25% = 0.0425")
    st.markdown("- Días = 139")
    with st.expander("Solución Ejercicio 1"):
        st.markdown("1. Calcular el descuento:")
        st.latex(r"\text{Descuento} = \frac{0.0425}{360} \times 139 \approx 0.0163069")
        st.markdown("2. Aplicar al valor nominal:")
        st.latex(r"\text{Precio} = 10 \times \left(1 - 0.0163069\right) \approx 10 \times 0.9836931 \approx 9.8369")
        st.markdown("**Resultado:** El precio de cada CETE es aproximadamente **$9.8369**.")
    
    st.markdown("---")
    
    st.subheader("Ejercicio 2")
    st.markdown(
        """
        **Enunciado:**  
        La señora Carmen compró unos pagarés con rendimiento liquidable al vencimiento (PRLV) que tienen **49 días por vencer**, un valor nominal de **$1.00** y pagó **$0.984513** por cada uno.  
        Calcular la tasa de descuento.
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{TdD} = \left(1 - \frac{\text{Precio}}{VN}\right) \times \frac{360}{\text{días}} \times 100\%")
    st.markdown("**Datos:**")
    st.markdown("- VN = $1.00")
    st.markdown("- Precio = $0.984513")
    st.markdown("- Días = 49")
    with st.expander("Solución Ejercicio 2"):
        st.markdown("1. Calcular el descuento unitario:")
        st.latex(r"1 - \frac{0.984513}{1.00} = 0.015487")
        st.markdown("2. Convertir a tasa anualizada:")
        st.latex(r"\text{TdD} = 0.015487 \times \frac{360}{49} \times 100\% \approx 11.36\%")
        st.markdown("**Resultado:** La tasa de descuento es aproximadamente **11.36% anual**.")
    
    st.markdown("---")
    
    st.subheader("Ejercicio 3")
    st.markdown(
        """
        **Enunciado:**  
        Juan compró CETES al banco con **87 días por vencer** y una **tasa de descuento del 4.15%**.  
        ¿Cuál es el precio que pagó Juan por cada título?
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio} = VN \times \left(1 - \frac{\text{TdD}}{360} \times \text{días}\right)")
    st.markdown("**Datos:**")
    st.markdown("- VN = $10")
    st.markdown("- TdD = 4.15% = 0.0415")
    st.markdown("- Días = 87")
    with st.expander("Solución Ejercicio 3"):
        st.markdown("1. Calcular el descuento:")
        st.latex(r"\text{Descuento} = \frac{0.0415}{360} \times 87 \approx 0.0100479")
        st.markdown("2. Aplicar al valor nominal:")
        st.latex(r"\text{Precio} = 10 \times (1 - 0.0100479) \approx 10 \times 0.9899521 \approx 9.8995")
        st.markdown("**Resultado:** El precio por cada CETE es aproximadamente **$9.8995**.")
    
    st.markdown("---")
    
    st.subheader("Ejercicio 4")
    st.markdown(
        """
        **Enunciado:**  
        Un inversionista compró aceptaciones bancarias con un **valor nominal de $100**, **221 días por vencer**, pagando **$96.930556** por cada una.  
        Calcular la tasa de descuento aplicada.
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{TdD} = \left(1 - \frac{\text{Precio}}{VN}\right) \times \frac{360}{\text{días}} \times 100\%")
    st.markdown("**Datos:**")
    st.markdown("- VN = $100")
    st.markdown("- Precio = $96.930556")
    st.markdown("- Días = 221")
    with st.expander("Solución Ejercicio 4"):
        st.markdown("1. Calcular el descuento unitario:")
        st.latex(r"1 - \frac{96.930556}{100} = 0.03069444")
        st.markdown("2. Convertir a tasa anualizada:")
        st.latex(r"\text{TdD} = 0.03069444 \times \frac{360}{221} \times 100\% \approx 5.00\%")
        st.markdown("**Resultado:** La tasa de descuento es aproximadamente **5.00% anual**.")
    
    st.markdown("---")
    st.markdown("**Comentarios Finales:**")
    st.markdown("- En los Ejercicios 1 y 3 se aplicó correctamente la fórmula de precio, considerando un VN de $10 y una base de 360 días. ")
    st.markdown("- En los Ejercicios 2 y 4 se despejó la tasa de descuento de forma precisa, destacando que el VN varía según el instrumento.")
    st.markdown("- La base de 360 días es el estándar en cálculos financieros para estos instrumentos.")
    
# ====================================================
# Pestaña 2: Simulador de Inversión Mejorado
# ====================================================
with tabs[1]:
    st.title("💰 Simulador de Inversión en CETES y BONDES")
    st.markdown("Ajusta los parámetros a continuación y observa los resultados de tu inversión. ¡Todo es interactivo y visual! 🚀")
    st.markdown("---")
    
    st.header("📊 Parámetros de la Inversión")
    
    # Selección de instrumento y distribución
    opcion_inversion = st.radio(
        "Selecciona el instrumento de inversión", 
        options=["CETES", "BONDES", "Ambos"],
        horizontal=True, 
        help="Elige si deseas invertir en CETES, en BONDES o en ambos"
    )
    
    monto_total = st.number_input(
        "Monto Total a Invertir (MXN)", 
        min_value=1000.0, value=100000.0, step=500.0,
        help="Monto total que deseas invertir."
    )
    
    if opcion_inversion == "Ambos":
        porc_cetes = st.number_input(
            "Porcentaje para CETES (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.01,
            help="Porcentaje del monto total a invertir en CETES. El resto se asigna a BONDES."
        )
        monto_cetes = monto_total * porc_cetes / 100
        monto_bondes = monto_total - monto_cetes
    elif opcion_inversion == "CETES":
        monto_cetes = monto_total
        monto_bondes = 0.0
    else:
        monto_bondes = monto_total
        monto_cetes = 0.0
    
    dias = st.number_input(
        "Plazo de Inversión (días)", 
        min_value=28, max_value=364, value=91, step=1,
        help="Número de días de la inversión (por ejemplo, 28, 91, 182, 364)."
    )
    
    # Parámetros para CETES
    if opcion_inversion in ["CETES", "Ambos"]:
        st.subheader("🔹 Parámetros para CETES")
        tdd_percent = st.number_input(
            "Tasa Bruta de CETES (%)", 
            min_value=0.1, max_value=15.0, value=9.2015, step=0.000001, format="%.6f",
            help="Tasa anualizada de descuento para CETES. Ingresa valores con precisión decimal."
        )
        tdd = tdd_percent / 100.0
    else:
        tdd = None
    
    # Parámetros para BONDES (valor nominal $100)
    if opcion_inversion in ["BONDES", "Ambos"]:
        st.subheader("🔹 Parámetros para BONDES")
        tasa_bondes_percent = st.number_input(
            "Tasa Bruta de BONDES (%)", 
            min_value=0.1, max_value=15.0, value=7.50, step=0.0001, format="%.4f",
            help="Tasa anualizada para BONDES. Ingresa valores con precisión decimal."
        )
        tasa_bondes = tasa_bondes_percent / 100.0
    else:
        tasa_bondes = None
    
    # Parámetros comunes
    inflacion_percent = st.number_input(
        "Tasa de Inflación (%)", 
        min_value=0.0, max_value=20.0, value=3.77, step=0.0001, format="%.4f",
        help="Tasa de inflación para calcular la tasa real. Ingresa valores con precisión decimal."
    )
    inflacion = inflacion_percent # / 100. -------------------------------------------------------------------------------0
    
    isr_percent = st.number_input(
        "Tasa de ISR Aplicada (%)", 
        min_value=0.0, max_value=16.0, value=5.0, step=0.0001, format="%.4f",
        help="Desde 2024, la tasa de retención anual del ISR para personas físicas en México es del 0.50% sobre el saldo promedio invertido. Este porcentaje se aplica automáticamente y funciona como un anticipo del impuesto que debes cubrir ante el SAT. Ejemplo incluir 5% este se aplicara sobre el rendimiento obtenido. Se calcula como (5%/100) * rendimiento obtendo"
    )
    
    # Opción de venta anticipada para CETES
    venta_anticipada = st.checkbox(
        "Simular Venta Anticipada (solo CETES)", 
        help="Activa esta opción para simular la venta antes del vencimiento de CETES."
    )
    if venta_anticipada and opcion_inversion in ["CETES", "Ambos"]:
        dias_transcurridos = st.number_input(
            "Días transcurridos antes de la venta", 
            min_value=1, max_value=dias-1, value=35, step=1,
            help="Días transcurridos antes de vender el título."
        )
        dias_restantes = dias - dias_transcurridos
        tdd_actual_percent = st.number_input(
            "Tasa de CETES actual para venta (%)", 
            min_value=0.1, max_value=30.0, value=tdd_percent, step=0.0001, format="%.4f",
            help="Tasa vigente para calcular el precio de venta en CETES. Si la tasa actual es mayor que la original, se recibe menos; si es menor, se recibe más."
        )
        tdd_actual = tdd_actual_percent / 100.0
    else:
        dias_transcurridos = None
        dias_restantes = None
        tdd_actual = None
    
    st.markdown("---")
    st.header("🔢 Cálculos")
    
    # Valores nominales para cada instrumento
    VN_CETES = 10.0
    VN_BONDES = 100.0
    
    # --- CÁLCULOS PARA CETES ---
    if opcion_inversion in ["CETES", "Ambos"]:
        # Precio de compra para CETES (con tasa original)
        precio_cetes = VN_CETES * (1 - (tdd / 360) * dias)
        titulos_cetes = math.floor(monto_cetes / precio_cetes)
        inversion_cetes = titulos_cetes * precio_cetes
        remanente_cetes = monto_cetes - inversion_cetes
        interes_bruto_cetes = titulos_cetes * (VN_CETES - precio_cetes)
        
        isr_cetes = interes_bruto_cetes * (isr_percent / 100.0)
       
        resultado_final_cetes = inversion_cetes + interes_bruto_cetes - isr_cetes + remanente_cetes
       
       
        rendimiento_nominal_cetes = (interes_bruto_cetes / inversion_cetes) * (360 / dias) * 100 if inversion_cetes > 0 else 0
        rendimiento_neto_cetes = ((interes_bruto_cetes - isr_cetes) / inversion_cetes) * (360 / dias) * 100 if inversion_cetes > 0 else 0
        # Para venta anticipada
        if venta_anticipada:
            precio_venta_cetes = VN_CETES * (1 - (tdd_actual / 360) * dias_restantes)
            ganancia_venta_cetes = precio_venta_cetes - precio_cetes
            # Tasa de Rendimiento por Venta (anualizada según días transcurridos)
            tasa_rendimiento_venta = (ganancia_venta_cetes * 360 / (precio_cetes * dias_transcurridos)) * 100
            resultado_final_cetes_anticipado = (titulos_cetes * precio_venta_cetes) + remanente_cetes - (ganancia_venta_cetes * (isr_percent / 100))

    # --- CÁLCULOS PARA BONDES ---
    if opcion_inversion in ["BONDES", "Ambos"]:
        precio_bondes = VN_BONDES * (1 - (tasa_bondes / 360) * dias)
        titulos_bondes = math.floor(monto_bondes / precio_bondes) if monto_bondes > 0 else 0
        inversion_bondes = titulos_bondes * precio_bondes
        remanente_bondes = monto_bondes - inversion_bondes
        interes_bruto_bondes = titulos_bondes * (VN_BONDES - precio_bondes)
        isr_bondes = interes_bruto_bondes * (isr_percent / 100.0)
        resultado_final_bondes = inversion_bondes + interes_bruto_bondes - isr_bondes + remanente_bondes
        rendimiento_nominal_bondes = (interes_bruto_bondes / inversion_bondes) * (360 / dias) * 100 if inversion_bondes > 0 else 0
        rendimiento_neto_bondes = ((interes_bruto_bondes - isr_bondes) / inversion_bondes) * (360 / dias) * 100 if inversion_bondes > 0 else 0
    
    # --- RESULTADOS: MOSTRAR LOS RESULTADOS PRINCIPALES ---
    st.subheader("Resultados Principales")
    col1, col2 = st.columns(2)
    with col1:
        if opcion_inversion in ["CETES", "Ambos"]:
            st.markdown("### CETES")
            st.metric("Monto Asignado a CETES", f"${monto_cetes:,.0f} MXN", help="Monto destinado a CETES")
            st.metric("Número de Títulos CETES", f"{titulos_cetes:,d}", help="Cantidad de títulos adquiridos")
            st.metric("Inversión en CETES", f"${inversion_cetes:,.2f} MXN", help="Monto invertido en la compra de títulos")
            st.metric("Remanente CETES", f"${remanente_cetes:,.2f} MXN", help="Monto sobrante que no se utiliza para comprar títulos")
            st.metric("Interés Bruto CETES", f"${interes_bruto_cetes:,.2f} MXN", help="Ganancia bruta antes de impuestos")
            st.metric("ISR CETES", f"${isr_cetes:,.2f} MXN", help="Impuesto sobre el rendimiento bruto")
            st.metric("Rendimiento Nominal CETES", f"{rendimiento_nominal_cetes:.2f}% anual", help="Rendimiento calculado sobre la inversión sin descontar ISR")
            st.metric("Rendimiento Neto CETES", f"{rendimiento_neto_cetes:.2f}% anual", help="Rendimiento después de aplicar ISR")
            
            st.markdown("**Tasa Neta (GAT Real):**")
            st.metric("Tasa Neta", f"{(rendimiento_nominal_cetes -  (isr_percent / 100.0)):.2f}%", help="Rendimiento Nominal menos la tasa de ISR")
            
            st.markdown("**Tasa Real (GAT Real):**")
            st.metric("Tasa Real", f"{((rendimiento_nominal_cetes -  (isr_percent / 100.0)) - inflacion):.2f}%", help="Tasa Neta menos Inflación (en puntos porcentuales)")
            
            st.markdown("**Utilidad:**")
            st.metric("Utilidad Bruta", f"${interes_bruto_cetes:,.2f} MXN", help="Equivalente al Interés Bruto")
            st.metric("Utilidad Neta", f"${interes_bruto_cetes - isr_cetes:,.2f} MXN", help="Utilidad Bruta menos ISR")
            st.metric("Utilidad Real", f"${interes_bruto_cetes - isr_cetes - inflacion:,.2f} MXN", help="Utilidad Bruta menos ISR")
            
            st.metric("Resultado Final CETES", f"${resultado_final_cetes:,.2f} MXN", help="Monto final ajustado, considerando inversion_cetes + utilidad real + remanente_cetes")

            if venta_anticipada:
                st.markdown("#### Venta Anticipada CETES")
                st.metric("Precio de Compra (Tasa Original)", f"${precio_cetes:,.6f} MXN", help="Precio de compra calculado con la tasa original")
                st.metric("Precio de Venta (Tasa Actual)", f"${precio_venta_cetes:,.6f} MXN", help="Precio de venta calculado con la tasa actual")
                st.metric("Ganancia por Venta", f"${ganancia_venta_cetes:,.6f} MXN", help="Diferencia entre precio de venta y precio de compra")
                st.metric("Tasa Bruta de Rendimiento por Venta", f"{tasa_rendimiento_venta:.6f}%", help="Ganancia de capital anualizada basada en la tenencia sin descontar ISR ni Inflación")
                st.metric("Tasa Neta de Rendimiento por Venta", f"{tasa_rendimiento_venta - (isr_percent / 100.0) :.6f}%", help="Ganancia de capital anualizada basada en la tenencia menos ISR")

                
                st.metric("Tasa Real de Rendimiento por Venta", f"{tasa_rendimiento_venta - (isr_percent / 100.0) - inflacion:.6f}%", help="Ganancia de capital anualizada basada en la tenencia menos ISR y menos Inflación")               
                st.metric("Resultado Final CETES Venta Anticipada", f"${resultado_final_cetes_anticipado:,.2f} MXN", help="Monto final al vender CETES antes de su vencimiento. Fórmula: (Títulos × Precio Venta) + Remanente - ISR. - Precio Venta = $10 × (1 - Tasa Actual × Días Restantes / 360)- ISR = (Precio Venta - Precio Compra) × Títulos × ISR%")
        else:
            st.info("No se invirtió en CETES.")
    with col2:
        if opcion_inversion in ["BONDES", "Ambos"]:
            st.markdown("### BONDES")
            st.metric("Monto Asignado a BONDES", f"${monto_bondes:,.2f} MXN", help="Monto destinado a BONDES")
            st.metric("Número de Títulos BONDES", f"{titulos_bondes:,d}", help="Cantidad de títulos adquiridos")
            st.metric("Inversión en BONDES", f"${inversion_bondes:,.2f} MXN", help="Monto invertido en la compra de títulos")
            st.metric("Remanente BONDES", f"${remanente_bondes:,.2f} MXN", help="Monto sobrante que no se utiliza para comprar títulos")
            st.metric("Interés Bruto BONDES", f"${interes_bruto_bondes:,.2f} MXN", help="Ganancia bruta antes de impuestos")
            st.metric("ISR BONDES", f"${isr_bondes:,.2f} MXN", help="Impuesto sobre el rendimiento bruto")
            st.metric("Rendimiento Nominal BONDES", f"{rendimiento_nominal_bondes:.2f}% anual", help="Rendimiento sin descontar impuestos")
            st.metric("Rendimiento Neto BONDES", f"{rendimiento_neto_bondes:.2f}% anual", help="Rendimiento después de aplicar ISR")
            st.metric("Tasa Real BONDES", f"{tasa_real_bondes*100:.2f}%", help="Rendimiento ajustado por inflación")
        else:
            st.info("No se invirtió en BONDES.")
    
    if opcion_inversion == "Ambos":
        st.markdown("### Totales Combinados")
        total_inversion = (inversion_cetes if opcion_inversion in ["CETES", "Ambos"] else 0) + \
                          (inversion_bondes if opcion_inversion in ["BONDES", "Ambos"] else 0)
        total_interes_bruto = (interes_bruto_cetes if opcion_inversion in ["CETES", "Ambos"] else 0) + \
                              (interes_bruto_bondes if opcion_inversion in ["BONDES", "Ambos"] else 0)
        total_isr = (isr_cetes if opcion_inversion in ["CETES", "Ambos"] else 0) + \
                    (isr_bondes if opcion_inversion in ["BONDES", "Ambos"] else 0)
        total_resultado_final = (resultado_final_cetes if opcion_inversion in ["CETES", "Ambos"] else 0) + \
                                (resultado_final_bondes if opcion_inversion in ["BONDES", "Ambos"] else 0)
        st.metric("Total Inversión", f"${total_inversion:,.2f} MXN")
        st.metric("Total Interés Bruto", f"${total_interes_bruto:,.2f} MXN")
        st.metric("Total ISR", f"${total_isr:,.2f} MXN")
        st.metric("Resultado Final Total", f"${total_resultado_final:,.2f} MXN")
    
    st.markdown("### Tabla de Resultados Detallada")
    data = []
    if opcion_inversion in ["CETES", "Ambos"]:
        data.append({
            "Concepto": "CETES",
            "Monto Invertido": f"${monto_cetes:,.2f}",
            "Interés Bruto": f"${interes_bruto_cetes:,.2f}",
            "ISR": f"${isr_cetes:,.2f}",
            "Resultado Final": f"${resultado_final_cetes:,.2f}",
            "Rendimiento Neto": f"{rendimiento_neto_cetes:.2f}%"
        })
    if opcion_inversion in ["BONDES", "Ambos"]:
        data.append({
            "Concepto": "BONDES",
            "Monto Invertido": f"${monto_bondes:,.2f}",
            "Interés Bruto": f"${interes_bruto_bondes:,.2f}",
            "ISR": f"${isr_bondes:,.2f}",
            "Resultado Final": f"${resultado_final_bondes:,.2f}",
            "Rendimiento Neto": f"{rendimiento_neto_bondes:.2f}%"
        })
    df_resultados = pd.DataFrame(data)
    st.table(df_resultados)
    
    st.markdown("### Gráficos Comparativos")
    distribucion = {}
    if opcion_inversion in ["CETES", "Ambos"]:
        distribucion["CETES"] = monto_cetes
    if opcion_inversion in ["BONDES", "Ambos"]:
        distribucion["BONDES"] = monto_bondes
    fig_pie = px.pie(
        names=list(distribucion.keys()), 
        values=list(distribucion.values()),
        title="Distribución del Monto Invertido"
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    categorias = []
    bruto = []
    neto = []
    if opcion_inversion in ["CETES", "Ambos"]:
        categorias.append("CETES")
        bruto.append(interes_bruto_cetes)
        neto.append(interes_bruto_cetes - isr_cetes)
    if opcion_inversion in ["BONDES", "Ambos"]:
        categorias.append("BONDES")
        bruto.append(interes_bruto_bondes)
        neto.append(interes_bruto_bondes - isr_bondes)
    df_bar = pd.DataFrame({
        "Instrumento": categorias,
        "Interés Bruto": bruto,
        "Interés Neto": neto
    })
    fig_bar = px.bar(
        df_bar, x="Instrumento", y=["Interés Bruto", "Interés Neto"],
        barmode="group", title="Comparación: Interés Bruto vs. Neto"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown("---")
    st.header("Exportar Resultados")
    pdf_str = "Simulación de Inversión\n\n" + df_resultados.to_string()
    buffer = BytesIO()
    buffer.write(pdf_str.encode())
    buffer.seek(0)
    st.download_button(
        label="Descargar PDF con Resultados",
        data=buffer,
        file_name="simulacion_inversion.pdf",
        mime="application/pdf"
    )
    
    

# ================================
# Pie de página
# ================================
st.markdown("---")
st.markdown("""
🎓 **SEMINARIO DE INVERSIÓN Y MERCADOS FINANCIEROS - IPN**  
🧑💻 Realizado por **J. Cruz Gómez** • 📧 josluigomez@gmail.com  
🔮 *"Los datos son como el acero: en bruto no valen, procesados son invencibles"*
""")
