import streamlit as st
import math
import pandas as pd
import plotly.express as px
from io import BytesIO
from fpdf import FPDF

# ============================
# Configuración de la Página
# ============================
st.set_page_config(
    page_title="🚀 Simulador de Inversión en CETES 🚀",
    layout="wide",
    page_icon="💹"
)

# Función para generar PDF usando fpdf
def generar_pdf(resultados: dict) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Simulación de Inversión en CETES", ln=True, align="C")
    pdf.ln(8)
    pdf.set_font("Arial", "", 12)
    # Recorremos cada resultado y lo agregamos al PDF en dos columnas
    for key, value in resultados.items():
        pdf.cell(60, 10, f"{key}:", border=1)
        pdf.cell(0, 10, f"{value}", border=1, ln=True)
    # Retornamos el PDF como bytes
    return pdf.output(dest="S").encode("latin1")

# ============================
# Pestañas Principales
# ============================
tabs = st.tabs(["📚 Mini Curso de CETES", "💰 Simulador de Inversión"])

# ====================================================
# Pestaña 1: Curso de CETES – Explicación Integral
# ====================================================
with tabs[0]:
    st.title("Curso de CETES: Explicación Integral 📚")
    st.markdown("---")
    
    # 1. ¿Qué es un CETE?
    st.header("1. ¿Qué es un CETE? 🤔")
    st.markdown(
        "Los **CETES** (Certificados de la Tesorería de la Federación) son instrumentos de deuda a corto plazo emitidos por el gobierno mexicano para financiar sus operaciones. "
        "Se emiten con vencimientos de **28, 91, 182 o 364 días** y tienen un valor nominal de **$10 MXN** por título. "
        "Este instrumento permite a los inversionistas obtener rendimientos en un plazo determinado, siendo una alternativa segura y respaldada por el gobierno."
    )
    st.markdown("---")
    
    # 2. Valor Nominal
    st.header("2. Valor Nominal 💵")
    st.markdown("**Concepto:** Es el valor que se recibirá al vencimiento del título.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Valor Nominal} = 10 \text{ MXN}")
    st.markdown("---")
    
    # 3. Precio de Compra
    st.header("3. Precio de Compra 🛒")
    st.markdown("**Concepto:** Precio al que se adquiere el CETE, obtenido al descontar el valor nominal mediante la tasa de descuento aplicada durante el plazo de la inversión.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio de Compra} = \text{Valor Nominal} \times \left(1 - \frac{\text{Tasa de Descuento}}{360} \times \text{Días}\right)")
    with st.expander("Ejemplo de Precio de Compra"):
        st.markdown("Con un valor nominal de **$10 MXN**, una tasa de descuento de **9.02%** y un plazo de **28 días**:")
        st.latex(r"\text{Precio de Compra} = 10 \times \left(1 - \frac{0.0902}{360} \times 28\right) \approx 9.92984 \text{ MXN}")
    st.markdown("---")
    
    # 4. Remanente
    st.header("4. Remanente 💰")
    st.markdown("**Concepto:** Capital no utilizado en la compra de títulos enteros, que se devuelve al inversor.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Remanente} = \text{Monto a Invertir} - \left(\text{Número de Títulos} \times \text{Precio de Compra}\right)")
    st.markdown("---")
    
    # 5. Interés Bruto
    st.header("5. Interés Bruto 📈")
    st.markdown("**Concepto:** Ganancia total sin deducción de impuestos, calculada como la diferencia entre el valor nominal y el precio de compra, multiplicada por el número de títulos adquiridos.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Bruto} = \text{Número de Títulos} \times \left(\text{Valor Nominal} - \text{Precio de Compra}\right)")
    st.markdown("---")
    
    # 6. ISR (Impuesto Sobre la Renta)
    st.header("6. ISR (Impuesto Sobre la Renta) 💸")
    st.markdown("**Concepto:** Porcentaje que se retiene sobre el interés bruto como impuesto, reduciendo la ganancia final del inversor.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{ISR} = \text{Interés Bruto} \times \frac{\text{Tasa de ISR}}{100}")
    st.markdown("---")
    
    # 7. Interés Neto
    st.header("7. Interés Neto 💵➡️💰")
    st.markdown("**Concepto:** Ganancia final después de deducir el ISR del interés bruto.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Neto} = \text{Interés Bruto} - \text{ISR}")
    st.markdown("---")
    
    # 8. Rendimientos del periodo
    st.header("8. Rendimiento al Final del Periodo del Certificado del CETE 📆")
    st.markdown("**Concepto:** Indicador que mide la rentabilidad de la inversión durante el plazo del certificado.")
    
    st.markdown("**Rendimiento Nominal$_{\text{(Periodo)}}$:** Es el rendimiento bruto obtenido al finalizar el CETE.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Nominal}_{\text{(Periodo)}} = \left(\frac{\text{Valor Nominal}}{\text{Precio de Compra}} - 1\right) \times 100")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Nominal"):
        st.markdown("Proyección del rendimiento a un año (base 360 días):")
        st.latex(r"\text{Rendimiento Nominal}_{\text{(Anualizado)}} = \left[\left(1 + \frac{\text{Rendimiento Nominal}_{\text{(Periodo)}}}{100}\right)^{\frac{360}{\text{Días}}} - 1\right] \times 100")
    
    st.markdown("**Rendimiento Neto$_{\text{(Periodo)}}$:** Es el rendimiento nominal ajustado por el ISR.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Neto}_{\text{(Periodo)}} = \text{Rendimiento Nominal}_{\text{(Periodo)}} \times \left(1 - \frac{\text{Tasa de ISR}}{100}\right)")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Neto"):
        st.markdown("Anualizando el rendimiento neto:")
        st.latex(r"\text{Rendimiento Neto}_{\text{(Anualizado)}} = \text{Rendimiento Nominal}_{\text{(Anualizado)}} \times \left(1 - \frac{\text{Tasa de ISR}}{100}\right)")
    
    st.markdown("**Rendimiento Real$_{\text{(Periodo)}}$:** Es el rendimiento neto ajustado por la inflación.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Real}_{\text{(Periodo)}} = \frac{1 + \frac{\text{Rendimiento Neto}_{\text{(Periodo)}}}{100}}{1 + \frac{\text{Tasa de Inflación}}{100}} - 1")
    st.markdown("---")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Real"):
        st.markdown("Anualizando el rendimiento real:")
        st.latex(r"\text{Rendimiento Real}_{\text{(Anualizado)}} = \frac{1 + \frac{\text{Rendimiento Neto}_{\text{(Anualizado)}}}{100}}{1 + \frac{\text{Tasa de Inflación}}{100}} - 1")
    
    # 9. Utilidades Totales
    st.header("9. Utilidades Totales al Final del Periodo de Vencimiento del CETE 🏦")
    st.markdown("**Utilidad Bruta:** Ganancia total obtenida, que incluye el capital invertido y el interés bruto.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Utilidad Bruta} = \text{Monto Invertido} + \text{Interés Bruto}")
    
    st.markdown("**Utilidad Real:** Ganancia total obtenida, que incluye el capital invertido y el interés bruto, después de descontar el ISR.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Utilidad Real (Principal)} = \text{Utilidad Bruta} - \text{ISR} - \text{Monto Invertido}")
    
    # 10. Rendimientos cuando se vende el CETE antes de su plazo de vencimiento
    st.header("10. Caso de Venta Anticipada del CETE (Cuando se Vende Antes de su Plazo de Vencimiento) ⏳")
    
    st.markdown("**Precio de Venta del CETE a Tasa de Descuento Actual:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Precio de Venta} = \text{Valor Nominal} \times \left(1 - \frac{\text{Tasa de Descuento Actual}}{360} \times \text{Días Restantes}\right)")
    with st.expander("Ejemplo de Precio de Venta en Venta Anticipada"):
        st.markdown("Si restan **20 días** para el vencimiento y se utiliza la tasa de descuento actual para calcular el precio de venta, se obtiene el valor de mercado del título.")
    
    st.markdown("**Ganancia de la Venta Anticipada por CETE:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Ganancia de Venta} = \text{Precio de Venta} - \text{Precio de Compra}")
    
    st.markdown("**Interés Bruto en Venta Anticipada:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Bruto}_{\text{(Anticipado)}} = \text{Número de Títulos} \times \text{Ganancia de Venta}")
    
    st.markdown("**ISR:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{ISR} = \text{Interés Bruto}_{\text{(Anticipado)}} \times \frac{\text{Tasa de ISR}}{100}")
    
    st.markdown("**Interés Neto:** Ganancia final después de deducir el ISR del interés bruto.")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Interés Neto}_{\text{(Anticipado)}} = \text{Interés Bruto}_{\text{(Anticipado)}} - \text{ISR}")
    
    st.markdown("**Rendimientos en Venta Anticipada:**")
    st.markdown("**Rendimiento Nominal$_{\text{(Periodo)}}$:**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Rendimiento Nominal}_{\text{(Periodo)}} = \frac{\text{Ganancia de Venta}}{\text{Precio de Compra}} \times 100")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Nominal"):
        st.latex(r"\text{Rendimiento Nominal}_{\text{(Anualizado)}} = \left[\left(1 + \frac{\text{Rendimiento Nominal}_{\text{(Periodo)}}}{100}\right)^{\frac{360}{\text{Días}}} - 1\right] \times 100")
    
    st.latex(r"\text{Rendimiento Neto}_{\text{(Periodo)}} = \text{Rendimiento Nominal}_{\text{(Periodo)}} \times \left(1 - \frac{\text{Tasa de ISR}}{100}\right)")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Neto"):
        st.markdown("Anualizando el rendimiento neto:")
        st.latex(r"\text{Rendimiento Neto}_{\text{(Anualizado)}} = \text{Rendimiento Nominal}_{\text{(Anualizado)}} \times \left(1 - \frac{\text{Tasa de ISR}}{100}\right)")
    
    st.latex(r"\text{Rendimiento Real}_{\text{(Periodo)}} = \frac{1 + \frac{\text{Rendimiento Neto}_{\text{(Periodo)}}}{100}}{1 + \frac{\text{Tasa de Inflación}}{100}} - 1")
    
    with st.expander("Fórmula $_{\text{(Anualizado)}}$ para Rendimiento Real"):
        st.latex(r"\text{Rendimiento Real}_{\text{(Anualizado)}} = \frac{1 + \frac{\text{Rendimiento Neto}_{\text{(Anualizado)}}}{100}}{1 + \frac{\text{Tasa de Inflación}}{100}} - 1")
    
    # Utilidades Totales en Venta Anticipada
    st.markdown("**Utilidades Totales de la Venta Anticipada de los CETES**")
    
    st.markdown("**Utilidad Bruta (Anticipada):**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Utilidad Bruta} = \text{Monto Invertido} + \text{Interés Bruto}_{\text{(Anticipado)}}")
    
    st.markdown("**Utilidad Real (Anticipada):**")
    st.markdown("**Fórmula:**")
    st.latex(r"\text{Utilidad Real (Principal)} = \text{Utilidad Bruta} - \text{ISR} - \text{Monto Invertido}")
    
    # ====================================================
    # Resolución de Ejercicios
    # ====================================================
    st.header("Resolución de Ejercicios")
    st.markdown("---")
    
    st.subheader("Ejercicio 1")
    st.markdown(
        """
        **Enunciado:**
        El señor Juan desea comprar CETES que tienen **139 días por vencer** y una **tasa de descuento del 4.25%**. 
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
        st.markdown("1. Calcular el factor de descuento:")
        st.latex(r"\text{Factor} = \frac{0.0425}{360} \times 139 \approx 0.0163069")
        st.markdown("2. Calcular el precio de compra:")
        st.latex(r"\text{Precio} = 10 \times \left(1 - 0.0163069\right) \approx 10 \times 0.9836931 \approx 9.8369")
        st.markdown("**Resultado:** El precio de cada CETE es aproximadamente **$9.8369 MXN**.")
    
    st.markdown("---")
    
    st.subheader("Ejercicio 2")
    st.markdown(
        """
        **Enunciado:**
        La señora Carmen compró pagarés con rendimiento liquidable al vencimiento (PRLV) que tienen **49 días por vencer**, un valor nominal de **$1.00 MXN** y pagó **$0.984513 MXN** por cada uno. 
        Calcular la tasa de descuento.
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{TdD} = \left(1 - \frac{\text{Precio}}{VN}\right) \times \frac{360}{\text{días}} \times 100\%")
    st.markdown("**Datos:**")
    st.markdown("- VN = $1.00 MXN")
    st.markdown("- Precio = $0.984513 MXN")
    st.markdown("- Días = 49")
    with st.expander("Solución Ejercicio 2 - Procedimiento Detallado"):
        st.markdown("1. **Descuento Unitario:**")
        st.latex(r"\text{Descuento Unitario} = 1 - \frac{0.984513}{1.00} = 0.015487")
        st.markdown("2. **Factor de Anualización:** Se usa la base de 360 días, por lo que el factor es:")
        st.latex(r"\frac{360}{49} \approx 7.3469")
        st.markdown("3. **Tasa de Descuento Anualizada:**")
        st.latex(r"\text{TdD} = 0.015487 \times 7.3469 \times 100\% \approx 11.36\%")
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
    st.markdown("- VN = $10 MXN")
    st.markdown("- TdD = 4.15% = 0.0415")
    st.markdown("- Días = 87")
    with st.expander("Solución Ejercicio 3"):
        st.markdown("1. Calcular el factor de descuento:")
        st.latex(r"\frac{0.0415}{360} \times 87 \approx 0.0100479")
        st.markdown("2. Calcular el precio de compra:")
        st.latex(r"\text{Precio} = 10 \times \left(1 - 0.0100479\right) \approx 10 \times 0.9899521 \approx 9.8995")
        st.markdown("**Resultado:** El precio por cada CETE es aproximadamente **$9.8995 MXN**.")
    
    st.markdown("---")
    
    st.subheader("Ejercicio 4")
    st.markdown(
        """
        **Enunciado:**
        Un inversionista compró aceptaciones bancarias con un **valor nominal de $100 MXN**, **221 días por vencer**, pagando **$96.930556 MXN** por cada una. 
        Calcular la tasa de descuento aplicada.
        """
    )
    st.markdown("**Fórmula:**")
    st.latex(r"\text{TdD} = \left(1 - \frac{\text{Precio}}{VN}\right) \times \frac{360}{\text{días}} \times 100\%")
    st.markdown("**Datos:**")
    st.markdown("- VN = $100 MXN")
    st.markdown("- Precio = $96.930556 MXN")
    st.markdown("- Días = 221")
    with st.expander("Solución Ejercicio 4 - Procedimiento Detallado"):
        st.markdown("1. **Descuento Unitario:**")
        st.latex(r"\text{Descuento Unitario} = 1 - \frac{96.930556}{100} = 0.03069444")
        st.markdown("2. **Factor de Anualización:**")
        st.latex(r"\frac{360}{221} \approx 1.6294")
        st.markdown("3. **Tasa de Descuento Anualizada:**")
        st.latex(r"\text{TdD} = 0.03069444 \times 1.6294 \times 100\% \approx 5.00\%")
        st.markdown("**Resultado:** La tasa de descuento es aproximadamente **5.00% anual**.")
    
    st.markdown("---")
    st.markdown("**Comentarios Finales:**")
    st.markdown("- En los Ejercicios 1 y 3 se aplicó correctamente la fórmula de precio, considerando un valor nominal de $10 MXN y una base de 360 días.")
    st.markdown("- En los Ejercicios 2 y 4 se despejó la tasa de descuento de forma precisa, destacando que el valor nominal varía según el instrumento.")
    st.markdown("- La base de 360 días es el estándar en cálculos financieros para estos instrumentos.")


# ====================================================
# Pestaña 2: Simulador de Inversión en CETES
# ====================================================
with tabs[1]:
    st.title("💰 Simulador de Inversión en CETES 💰")
    st.markdown("🚀 Ajusta los parámetros a continuación y observa los resultados de tu inversión en CETES. ¡Diviértete y aprende! 😎")
    st.markdown("---")
    
    st.header("📊 Parámetros de la Inversión 📊")
    
    # MONTO A INVERTIR
    monto_total = st.number_input(
        "Monto Total a Invertir (MXN) 💵",
        min_value=1000.0, value=40000.0, step=500.0,
        help="Ingresa el monto total que deseas invertir en CETES."
    )
    
    # Precio Nominal del CETE (slider para seleccionar de 1 a 200)
    VN_CETES = st.slider(
        "Precio Nominal del CETE (MXN) 💲",
        min_value=1.0, max_value=200.0, value=10.0, step=1.0,
        help="Selecciona el valor nominal de cada CETE."
    )
    
    # PLAZO
    monto_cetes = monto_total
    dias = st.slider(
        "Plazo de Inversión (días) ⏱️",
        min_value=28,
        max_value=365,
        value=28,  # Valor inicial
        step=1,
        help="Selecciona el plazo de tu inversión entre 28 y 365 días."
    )
    
    # TASA DE DESCUENTO
    tdd_percent = st.number_input(
        "Tasa de Descuento (%) 📉",
        min_value=0.1, max_value=15.0, value=9.2015, step=0.00000001, format="%.8f",
        help="Ingresa la tasa anualizada de descuento para CETES con máxima precisión."
    )
    tdd = tdd_percent / 100.0
    
    # ISR E INFLACIÓN
    st.subheader("🔹 Parámetros Fiscales y Económicos 🔹")
    inflacion = st.number_input(
        "Tasa de Inflación (%) 📈",
        min_value=0.0, max_value=20.0, value=3.77, step=0.00000001, format="%.8f",
        help="Ejemplo: 3.77% medido el 28/03/2025"
    )
    
    isr_percent = st.number_input(
        "Tasa de ISR Aplicada (%) 💸",
        min_value=0.0, max_value=16.0, value=5.0, step=0.00000001, format="%.8f",
        help="Ingresa la tasa de retención del ISR que se aplicará sobre el rendimiento obtenido."
    )
    
    # --- Parámetros para Venta Anticipada ---
    venta_anticipada = st.checkbox(
        "Simular Venta Anticipada (Antes del Vencimiento) ⏳",
        help="Activa esta opción para simular la venta del CETE antes de su vencimiento."
    )
    
    if venta_anticipada:
        dias_transcurridos = st.number_input(
            "Días Transcurridos (antes de la venta) 🕒",
            min_value=1, max_value=dias-1, value=35, step=1,
            help="Ingresa el número de días transcurridos antes de realizar la venta anticipada."
        )
        dias_restantes = dias - dias_transcurridos
        tdd_actual_percent = st.number_input(
            "Tasa de CETES Actual para Venta (%) 🔄",
            min_value=0.1, max_value=30.0, value=9.002000, step=0.00000001, format="%.8f",
            help="Ingresa la tasa de descuento vigente para el CETE en el momento de la venta."
        )
        tdd_actual = tdd_actual_percent / 100.0
    else:
        dias_transcurridos = None
        dias_restantes = None
        tdd_actual = None
    
    # --- CÁLCULOS DE RENDIMIENTOS, TASAS E INTERESES ---
    st.markdown("---")
    st.header("💰 Resultados de la Inversión 💰")
    
    # Precio de compra calculado con la tasa de descuento original
    precio_cetes = VN_CETES * (1 - (tdd / 360) * dias)
    
    # Número de títulos comprados (solo se adquieren títulos enteros)
    titulos_cetes = math.floor(monto_cetes / precio_cetes)
    inversion_cetes = titulos_cetes * precio_cetes
    remanente_cetes = monto_cetes - inversion_cetes
    
    # Interés Bruto del periodo completo
    interes_bruto_cetes = titulos_cetes * (VN_CETES - precio_cetes)
    isr_cetes = interes_bruto_cetes * (isr_percent / 100.0)
    interes_neto_cetes = interes_bruto_cetes - isr_cetes
    
    # Rendimientos del CETE (Periodo Completo)
    rendimiento_nominal_cetes = ((VN_CETES / precio_cetes) - 1) * 100 if inversion_cetes > 0 else 0
    rendimiento_neto_cetes = rendimiento_nominal_cetes * (1 - isr_percent / 100.0) if inversion_cetes > 0 else 0
    rendimiento_real_cetes = ((1 + rendimiento_neto_cetes/100) / (1 + inflacion/100) - 1) * 100
    
    # Rendimientos Anualizados
    rendimiento_nominal_cetes_anual = ((1 + (rendimiento_nominal_cetes / 100)) ** (360 / dias) - 1) * 100 if inversion_cetes > 0 else 0
    rendimiento_neto_cetes_anual = rendimiento_nominal_cetes_anual * (1 - isr_percent / 100.0) if inversion_cetes > 0 else 0
    rendimiento_real_cetes_anual = ((1 + rendimiento_neto_cetes_anual/100) / (1 + inflacion/100) - 1) * 100
    
    # Utilidades Totales
    utilidad_bruta = monto_cetes + interes_bruto_cetes
    principal = utilidad_bruta - isr_cetes
    utilidad_neta = principal - monto_cetes
    
    # --- Cálculos para Venta Anticipada ---
    if venta_anticipada:
        precio_venta_cetes = VN_CETES * (1 - (tdd_actual / 360) * dias_restantes)
        ganancia_venta_cetes = precio_venta_cetes - precio_cetes
        interes_bruto_cetes_anticipado = titulos_cetes * ganancia_venta_cetes
        isr_cetes_anticipado = interes_bruto_cetes_anticipado * (isr_percent / 100.0)
        interes_neto_cetes_anticipado = interes_bruto_cetes_anticipado - isr_cetes_anticipado
        
        # Rendimiento del periodo en venta anticipada
        tasa_rendimiento_venta_periodo = (ganancia_venta_cetes / precio_cetes) * 100
        tasa_rendimiento_neta_periodo = tasa_rendimiento_venta_periodo * (1 - isr_percent / 100.0)
        tasa_rendimiento_real_periodo = ((1 + tasa_rendimiento_neta_periodo/100) / (1 + inflacion/100) - 1) * 100
        
        # Rendimiento anualizado en venta anticipada (usando días transcurridos)
        tasa_rendimiento_venta = (ganancia_venta_cetes * 360 / (precio_cetes * dias_transcurridos)) * 100
        tasa_rendimiento_neta = tasa_rendimiento_venta * (1 - isr_percent / 100.0)
        tasa_rendimiento_real = ((1 + tasa_rendimiento_neta/100) / (1 + inflacion/100) - 1) * 100
        
        utilidad_bruta_anticipado = monto_cetes + interes_bruto_cetes_anticipado
        principal_anticipado = utilidad_bruta_anticipado - isr_cetes_anticipado
        utilidad_neta_anticipado = principal_anticipado - monto_cetes
    
    # --- MOSTRAR RESULTADOS ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Venta al Vencimiento")
        st.metric("Capital Disponible", f"${monto_cetes:,.0f} MXN", help="Monto total destinado a la inversión en CETES.")
        st.metric("Precio de Compra", f"${precio_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento original.")
        st.metric("Capital Invertido", f"${inversion_cetes:,.2f} MXN", help="Monto utilizado en la compra de CETES.")
        st.metric("Títulos Comprados", f"{titulos_cetes:,d}", help="Cantidad de títulos adquiridos (títulos enteros).")
        st.metric("Remanente", f"${remanente_cetes:,.2f} MXN", help="Capital no invertido en títulos.")
    
        st.markdown("**Rendimientos Anualizados:**")
        st.metric("Rendimiento Nominal", f"{rendimiento_nominal_cetes_anual:.8f}%", help="Rendimiento anualizado sin aplicar ISR.")
        st.metric("Rendimiento Neto", f"{rendimiento_neto_cetes_anual:.8f}%", help="Rendimiento anualizado después de ISR.")
        st.metric("Rendimiento Real", f"{rendimiento_real_cetes_anual:.8f}%", help="Rendimiento anualizado ajustado por ISR e inflación.")
    
        st.markdown("**Rendimientos del Periodo:**")
        st.metric("Rendimiento Nominal", f"{rendimiento_nominal_cetes:.8f}%", help="Rendimiento obtenido durante el periodo sin impuestos.")
        st.metric("Rendimiento Neto", f"{rendimiento_neto_cetes:.8f}%", help="Rendimiento obtenido durante el periodo después de ISR.")
        st.metric("Rendimiento Real", f"{rendimiento_real_cetes:.8f}%", help="Rendimiento obtenido durante el periodo ajustado por inflación.")
    
        st.markdown("**Interés y Utilidad:**")
        st.metric("Interés Bruto", f"${interes_bruto_cetes:,.2f} MXN", help="Ganancia total sin ISR.")
        st.metric("ISR", f"${isr_cetes:,.2f} MXN", help="Impuesto aplicado al interés bruto.")
        st.metric("Interés Neto", f"${interes_neto_cetes:,.2f} MXN", help="Ganancia después de ISR.")
        st.metric("Utilidad Bruta", f"${utilidad_bruta:,.8f} MXN", help="Suma del capital invertido y el interés bruto.")
        st.metric("Utilidad Real (Principal)", f"${principal:,.8f} MXN", help="Utilidad bruta menos ISR y el capital invertido.")
    
    with col2:
        if venta_anticipada:
            st.markdown("#### Venta Anticipada")
            st.metric("Capital Disponible", f"${monto_cetes:,.0f} MXN", help="Monto destinado a la inversión.")
            st.metric("Precio de Compra", f"${precio_cetes:,.8f} MXN", help="Precio de compra con la tasa original.")
            st.metric("Capital Invertido", f"${inversion_cetes:,.2f} MXN", help="Monto invertido en CETES.")
            st.metric("Títulos Comprados", f"{titulos_cetes:,d}", help="Número de títulos adquiridos.")
            st.metric("Remanente", f"${remanente_cetes:,.2f} MXN", help="Capital no invertido en títulos.")
    
            st.markdown("**Rendimientos Anualizados (Venta Anticipada):**")
            st.metric("Rendimiento Nominal", f"{tasa_rendimiento_venta:.8f}%", help="Rendimiento anualizado sin ISR ni inflación.")
            st.metric("Rendimiento Neto", f"{tasa_rendimiento_neta:.8f}%", help="Rendimiento anualizado después de ISR.")
            st.metric("Rendimiento Real", f"{tasa_rendimiento_real:.8f}%", help="Rendimiento anualizado ajustado por ISR e inflación.")
    
            st.markdown("**Rendimientos del Periodo (Venta Anticipada):**")
            st.metric("Rendimiento Nominal", f"{tasa_rendimiento_venta_periodo:.8f}%", help="Rendimiento del periodo sin ISR.")
            st.metric("Rendimiento Neto", f"{tasa_rendimiento_neta_periodo:.8f}%", help="Rendimiento del periodo después de ISR.")
            st.metric("Rendimiento Real", f"{tasa_rendimiento_real_periodo:.8f}%", help="Rendimiento del periodo ajustado por inflación.")
    
            st.markdown("**Interés y Utilidad (Venta Anticipada):**")
            st.metric("Interés Bruto", f"${interes_bruto_cetes_anticipado:,.2f} MXN", help="Ganancia total en venta anticipada sin ISR.")
            st.metric("ISR", f"${isr_cetes_anticipado:,.2f} MXN", help="Impuesto aplicado en venta anticipada.")
            st.metric("Interés Neto", f"${interes_neto_cetes_anticipado:,.2f} MXN", help="Ganancia en venta anticipada después de ISR.")
            st.metric("Utilidad Bruta", f"${utilidad_bruta_anticipado:,.8f} MXN", help="Capital invertido más el interés bruto en venta anticipada.")
            st.metric("Utilidad Real (Principal)", f"${principal_anticipado:,.8f} MXN", help="Utilidad bruta menos ISR y el capital invertido en venta anticipada.")
        else:
            st.info("Activa la opción de **'Venta Anticipada'** para ver estos resultados. 🤓")
    
    with col3:
        if venta_anticipada:
            st.markdown("#### Ajuste por Venta Anticipada")
            st.metric("Precio de Compra (Tasa Original)", f"${precio_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento original.")
            st.metric("Precio de Venta (Tasa Actual)", f"${precio_venta_cetes:,.8f} MXN", help="Precio calculado con la tasa de descuento actual.")
            st.metric("Ganancia por Venta", f"${ganancia_venta_cetes:,.8f} MXN", help="Diferencia entre el precio de venta y el de compra.")
    
    st.markdown("---")


    st.markdown("---")
    st.header("Exportar Resultados 📄")
    # Crear diccionario con los principales resultados a exportar
    resultados_dict = {
        "CETES": "Simulación",
        "Monto Invertido": f"${monto_cetes:,.8f}",
        "Plazo": f"{dias} días",
        "Tasa de Desc. Original": f"{tdd_percent}%",
        "ISR": f"{isr_percent}%",
        "Inflación": f"{inflacion}%",
        "Precio de Compra": f"${precio_cetes:,.8f}",
        "Títulos Comprados": f"{titulos_cetes:,d}",
        "Remanente": f"${remanente_cetes:,.8f}",
        "Rend. Nominal (Anual)": f"{rendimiento_nominal_cetes_anual:.8f}%",
        "Rend. Neto (Anual)": f"{rendimiento_neto_cetes_anual:.8f}%",
        "Rend. Real (Anual)": f"{rendimiento_real_cetes_anual:.8f}%",
        "Rend. Nominal (Periodo)": f"{rendimiento_nominal_cetes:.8f}%",
        "Rend. Neto (Periodo)": f"{rendimiento_neto_cetes:.8f}%",
        "Rend. Real (Periodo)": f"{rendimiento_real_cetes:.8f}%",
        "Interés Bruto": f"${interes_bruto_cetes:,.8f}",
        "ISR (Interés)": f"${isr_cetes:,.8f}",
        "Interés Neto": f"${interes_neto_cetes:,.8f}",
        "Utilidad Bruta": f"${utilidad_bruta:,.8f}",
        "Utilidad Real": f"${principal:,.8f}",
    }
    
    if venta_anticipada:
        resultados_dict.update({
            "Precio de Venta": f"${precio_venta_cetes:,.8f}",
            "Ganancia de Venta": f"${ganancia_venta_cetes:,.8f}",
            "Interés Bruto (Anticipado)": f"${interes_bruto_cetes_anticipado:,.8f}",
            "ISR (Anticipado)": f"${isr_cetes_anticipado:,.8f}",
            "Interés Neto (Anticipado)": f"${interes_neto_cetes_anticipado:,.8f}",
            "Utilidad Bruta (Anticipada)": f"${utilidad_bruta_anticipado:,.8f}",
            "Utilidad Real (Anticipada)": f"${principal_anticipado:,.8f}"
        })
    
    pdf_bytes = generar_pdf(resultados_dict)
    st.download_button(
        label="Descargar PDF con Resultados 📥",
        data=pdf_bytes,
        file_name="simulacion_inversion.pdf",
        mime="application/pdf"
    )




# ================================
# Pie de Página
# ================================
st.markdown("---")
st.markdown("""
🎓 **SEMINARIO DE INVERSIÓN Y MERCADOS FINANCIEROS - IPN**  
🧑💻 Realizado por **J. Cruz Gómez** • 📧 josluigomez@gmail.com  
🔮 *"Los datos son como el acero: en bruto no valen, procesados son invencibles"*
""")
